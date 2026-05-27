# Toolkit Phase 1 — Core-Layer API Contract (proposal)

**Version:** v0.1 (proposal → **ACCEPTED + D6-LOCKED 2026-05-27**; two review passes — see §13)
**Status:** **ACCEPTED — D6-LOCKED.** Public signatures stable from v0.1. Mirrored to `numerics/README.md`; Phase 1 implementation proceeds against these signatures.
**Parent:** `workplans/toolkit-work-plan-v0.1.md` (Phase 1 deliverables; locked decisions D1–D6).
**Scope:** the public signatures and conventions of the Phase 1 *core layer* — `MasterEquationSystem`, `evolve`, and the preparation primitives. These are the **D6-locked contract** (public signatures stable from v0.1; internal numerics free).

---

## §0 — Principles for this pass

1. **Design-only.** Signatures, dataclass field lists, enums, prose contracts. **No function bodies.** `...` marks an unimplemented body.
2. **D6 surface.** Frozen by D6: the *native* dataclass/enum signatures and the *documented* quantum-state contract (QuTiP `Qobj` with layout-matching dims). Not frozen: QuTiP version internals, solver pass-throughs, the (extensible) operator registry, all numerics.
3. **`R_δ` does not leak into Phase 1.** Phase 1 prepares and evolves *clean dynamics* and returns states. The temporal pointer `T`, `P(T)`, per-carrier read-out POVMs, fragments, and the `R_δ`/`I(C:M)`/`F[τ]` post-processors are **Phase 2**. Phase 1 must not construct pointers or fragments. The *physical* detection layer (`ReadoutModel`, §5.4) is *declared* here for taxonomic completeness but is **applied** in Phase 2 — never by `evolve`.
4. **One core, two layouts, two backends (D2 + D3).** The spec dataclasses (`SystemLayout`, `HamiltonianTerm`, `LindbladChannel`, prep primitives) are shared. **Phase 1 ships exactly one backend: `MasterEquationSystem.evolve`, a full-Hilbert-space QuTiP `mesolve` engine.** It serves Module 3a (Sorci: clock + 1–2 modes) and small-N validation of Module 3b's regime. Module 3b at N≫2 **cannot** use a full-Hilbert backend (2^N is intractable — work-plan out-of-scope), so its **factorised product-state backend is a separate Phase-3 component** that *consumes the same specs* (layout, channels, prep) but evolves per-carrier, never building a 2^N `Qobj` (locked decision D3). The full-`Qobj` state currency (§9) is therefore the contract of the **Phase-1 full-Hilbert backend specifically**, not of the future factorised backend.

---

## §1 — Units and time convention

- `ℏ = 1`. Hamiltonian coefficients are **angular frequencies** in **rad·s⁻¹**.
- Time grids (`times`) are in **seconds**; rates in **s⁻¹** (meaning fixed per `ChannelKind`, §5.2).
- Dimensionless: squeezing `r`, the Sorci coupling `ε_m`, infidelities `ε_prep`/`ε_det`, relative phases.
- SI-with-`ℏ=1` is the contract default; nondimensionalisation by a reference frequency is a *caller* choice (O1, accepted). Sorci constants (`ω`, `mc²`, `ε_m`) enter only through the Module 3a Hamiltonian builder, never the core.

---

## §2 — `SystemLayout` (subsystems, tensor order, dims)

```python
class SubsystemKind(Enum):
    TWO_LEVEL    = "two_level"      # clock or carrier qubit; dim hard-validated == 2
    BOSONIC_MODE = "bosonic_mode"   # motional mode; dim = Fock cutoff = n_max + 1
    # (qudit clock/carriers are a FUTURE `FINITE_LEVEL` kind; v0.1 is TWO_LEVEL only.)

@dataclass(frozen=True)
class Subsystem:
    label: str                 # unique within a layout, e.g. "clock", "M1", "carrier_03"
    kind: SubsystemKind
    dim: int                   # TWO_LEVEL ⇒ must be 2; BOSONIC_MODE ⇒ Fock cutoff ≥ 2

@dataclass(frozen=True)
class SystemLayout:
    subsystems: tuple[Subsystem, ...]   # TENSOR ORDER = sequence order (leftmost = first factor)

    @classmethod
    def clock_and_modes(cls, n_modes: int, mode_cutoffs: int | Sequence[int]) -> "SystemLayout": ...
        # clock is TWO_LEVEL (dim 2); order: clock ⊗ M1 ⊗ … ⊗ M_n  (the Sorci convention)
    @classmethod
    def carriers(cls, n: int) -> "SystemLayout": ...
        # carriers are TWO_LEVEL (dim 2); order: carrier_00 ⊗ carrier_01 ⊗ …

    def index(self, label: str) -> int: ...
    def subsystem(self, label: str) -> Subsystem: ...
    def dims(self) -> list[int]: ...                       # Qobj-style dims, e.g. [2, 20, 20]
    def validate_state(self, state: "Qobj") -> None: ...   # raises LayoutMismatchError on dims mismatch
```

**Tensor-order convention (contract):** factors appear in `subsystems` order; Sorci is `clock ⊗ M₁ ⊗ … ⊗ M_N`. A state's `.dims[0]` must equal `layout.dims()`; validated on entry to `evolve` and post-processors. *(O2 accepted; clock/carrier `dim` args removed — `TWO_LEVEL` is always 2.)*

---

## §3 — Operator specifiers and the QuTiP boundary

```python
class Op(Enum):
    IDENTITY; SIGMA_X; SIGMA_Y; SIGMA_Z; SIGMA_PLUS; SIGMA_MINUS     # two-level
    NUM; DESTROY; CREATE; X_QUAD; P_QUAD                              # bosonic; X=(a+a†)/√2, P=(a−a†)/(i√2)

@dataclass(frozen=True)
class LocalOp:
    op: Op | None = None       # a registered local operator …
    power: int = 1             # … optionally raised to an integer power (e.g. P_QUAD**2 for Sorci)
    qobj: "Qobj | None" = None # … OR a raw QuTiP local operator (advanced escape hatch)
    # Exactly one of {op, qobj}. The `qobj` path is QuTiP-typed, outside the native-stability layer
    # of D6 (the documented Qobj contract still applies: it acts on the named subsystem's local space).
```

The native path (`Op` + `power`) is the D6-stable surface; the registry may *grow* across versions without breaking D6 (adding enum members is backward-compatible). The `qobj` escape hatch is an explicit power-user boundary.

---

## §4 — Hamiltonian terms

```python
@dataclass(frozen=True)
class HamiltonianTerm:
    coefficient: float                 # rad·s⁻¹ (real)
    operators: Mapping[str, LocalOp]   # subsystem-label -> local op; ABSENT labels => identity
    label: str = ""                    # human tag, e.g. "clock free", "mass-defect coupling"
    # Full-space term = coefficient · ⊗_{subsystems} (LocalOp or I). Total H = Σ terms and MUST be
    # Hermitian (validated on assembly); non-Hermitian single terms allowed only if they sum Hermitian.
```

*Sorci mass-defect coupling (clock + one mode), with `Ĥ_c = (ω_c/2)σ_z`:*
`HamiltonianTerm(coefficient=−(ω/2mc²)·(ω_c/2), operators={"clock": LocalOp(Op.SIGMA_Z), "M1": LocalOp(Op.P_QUAD, power=2)}, label="mass-defect coupling")`. The Module 3a builder emits such term lists; the core only assembles.

---

## §5 — Nuisance model: four layers, four code homes

Only **layer 2** enters `evolve`.

### §5.1 — Initial-state errors (preparation infidelity) → prep primitives
Applied to `ρ(0)`, **locally**, by the prep primitives (§8) via `prep_infidelity`. v0.1 model: symmetric depolarising toward the *local* maximally mixed state, `ρ' = (1−ε)ρ + ε·𝟙/d_sub` (O4 accepted). Mode-local errors such as squeezing-prep infidelity (Sorci D1 (iv)) live here as the squeezed mode's local `prep_infidelity`. *(Blocking-1 / O4 resolution: infidelity is per-primitive local; `product_state` does not re-apply it.)*

### §5.2 — Dynamical Lindblad channels → `MasterEquationSystem` (the only Liouvillian layer)
With `D[c]ρ = cρc† − ½{c†c, ρ}`:

```python
class ChannelKind(Enum):
    HEATING             # bosonic, constant-rate (trapped-ion anomalous-heating convention):
                        #   generator = ṅ·(D[a†] + D[a]);  d⟨n⟩/dt = +ṅ  (STATE-INDEPENDENT)
    THERMAL_RELAXATION  # bosonic, relaxation toward mean occupation n̄ = n_thermal at rate κ:
                        #   generator = κ(n̄+1)·D[a] + κ·n̄·D[a†];  d⟨n⟩/dt = −κ(⟨n⟩ − n̄)
                        #   (n̄ = 0 ⇒ pure cooling toward vacuum, ⟨n⟩(t) = ⟨n⟩₀ e^{−κt})
    MOTIONAL_DEPHASING  # bosonic: γ_φ · D[a†a]
    DEPHASING           # two-level: (γ_φ/2) · D[σ_z];  coherence decays as e^{−γ_φ t}
    AMPLITUDE_DAMPING   # two-level: Γ · D[σ_−]

@dataclass(frozen=True)
class LindbladChannel:
    target: str                      # subsystem label
    kind: ChannelKind
    rate: float                      # s⁻¹; meaning fixed by `kind`: ṅ (HEATING), κ (THERMAL_RELAXATION,
                                     #      AMPLITUDE_DAMPING as Γ), γ_φ (MOTIONAL_DEPHASING/DEPHASING)
    n_thermal: float | None = None   # used by THERMAL_RELAXATION only (n̄); ignored otherwise
    label: str = ""
```

The generator and the rate's meaning are pinned per `ChannelKind` (the comments above are part of the contract, so each closed-form test has a single right answer). *(Blocking-2 resolution: `HEATING` is now the symmetric pair giving constant `d⟨n⟩/dt = ṅ`; steady-state thermal behaviour moved to the explicit `THERMAL_RELAXATION` channel.)*

### §5.3 — Stochastic / drive noise → declared spec, handled by `evolve`
```python
class NoiseModel(Enum):
    WHITE       # spectrally flat → adds a Lindblad dissipator at `effective_rate` in evolve (v0.1)
    CORRELATED  # PSD/correlation-function noise → trajectory-ensemble averaging (DEFERRED, v0.2)

@dataclass(frozen=True)
class DriveNoise:
    target: str
    operator: LocalOp        # operator the noise couples to (e.g. Op.SIGMA_Z for drive-phase noise)
    model: NoiseModel
    effective_rate: float    # s⁻¹, the COHERENCE-DECAY rate (matches ChannelKind.DEPHASING).
                             # WHITE: adds (effective_rate/2)·D[operator] to the Liouvillian, so for
                             # operator=σ_z it is EXACTLY a DEPHASING channel at γ_φ=effective_rate
                             # (coherence ∝ e^{−effective_rate·t}). The /2 enforces consistency with
                             # ChannelKind.DEPHASING; no PSD-convention factor is hidden.
    label: str = ""
```
*(O5 / drive-noise-factor resolution: `effective_rate` is the **coherence-decay rate**, consistent with `ChannelKind.DEPHASING` — WHITE adds `(effective_rate/2)·D[operator]` (for σ_z, coherence ∝ e^{−effective_rate·t}). `CORRELATED` is named-and-deferred; its PSD spec lands in v0.2 without breaking this signature, per D6.)*

### §5.4 — Readout / detection model → declared here, **applied in Phase 2**
```python
@dataclass(frozen=True)
class ReadoutModel:
    target: str
    detection_infidelity: float = 0.0   # symmetric outcome bit-flip ε_det
    correlated_with: str | None = None  # e.g. motional-state-correlated detection (Sorci D1 (v))
    label: str = ""
    # NOT consumed by evolve(). Carried on the system as a declared spec; CONSUMED by Phase-2
    # post-processors / module observables. The Phase-2 TemporalRecordEnsemble COMPOSES the
    # pointer-defining POVM with this physical detection layer — that composition is Phase 2.
```

---

## §6 — `MasterEquationSystem` constructor

```python
class MasterEquationSystem:
    def __init__(
        self,
        layout: SystemLayout,
        hamiltonian: Sequence[HamiltonianTerm],
        channels: Sequence[LindbladChannel] = (),
        drive_noise: Sequence[DriveNoise] = (),
        readout: Sequence[ReadoutModel] = (),     # declared only; not used by evolve (§5.4, O7)
    ) -> None: ...

    @property
    def layout(self) -> SystemLayout: ...
    def hamiltonian_operator(self) -> "Qobj": ...     # assembled H (Hermitian; raises if not)
    def collapse_operators(self) -> list["Qobj"]: ... # c_ops from §5.2 + WHITE §5.3 reduction

    def evolve(self, state, times, *, e_ops=None, options=None,
               store_states=True) -> "EvolutionResult": ...   # §7

    # This is the Phase-1 FULL-HILBERT QuTiP backend (§0.4). The N≫2 factorised backend is a
    # separate Phase-3 component consuming the same specs; it does not subclass or override this.
```

Construction validates: labels unique/resolvable; `TWO_LEVEL` dim == 2; bosonic dims ≥ 2; channel/noise/readout `target`s exist; assembled `H` Hermitian. Failures raise typed errors (§7).

---

## §7 — `evolve(state, times)` contract

```python
@dataclass(frozen=True)
class ObservableSpec:                  # a full-space observable, built like HamiltonianTerm.operators
    operators: Mapping[str, LocalOp]   # product over named subsystems; ABSENT labels => identity
    coefficient: float = 1.0

@dataclass
class SolverOptions:
    solver: Literal["mesolve"] = "mesolve"   # v0.1: ONLY "mesolve" selectable; mcsolve deferred (O6)
    method: str = "adams"                     # ODE integrator (adams/bdf) — NOT solver selection
    atol: float = 1e-12
    rtol: float = 1e-10
    nsteps: int = 10_000
    fock_population_warn_threshold: float = 1e-6  # top-Fock pop above this ⇒ truncation_ok = False
    qutip_options: dict | None = None             # advanced pass-through (NOT covered by D6 stability)

@dataclass
class EvolutionDiagnostics:
    max_fock_population: dict[str, float]   # per bosonic subsystem: population in the top Fock level
    trace_drift: float                      # max |Tr ρ(t) − 1|
    truncation_ok: bool                     # max_fock_population below options.fock_population_warn_threshold

@dataclass
class EvolutionResult:
    times: "np.ndarray"
    states: "list[Qobj] | None"        # density matrices if store_states else None
    expect: dict[str, "np.ndarray"]    # keyed by e_op label; empty if no e_ops
    final_state: "Qobj"                # always present
    layout: SystemLayout
    solver: str                        # "mesolve" (v0.1)
    converged: bool
    diagnostics: EvolutionDiagnostics
```

**Accepted `state`:** a `Qobj` ket or density matrix with `.dims` matching `layout.dims()` (kets promoted internally), or the full-space `Qobj` returned by `product_state` (§8).
**`times`:** 1-D array-like of non-decreasing seconds.
**`e_ops`:** optional `Mapping[str, ObservableSpec | Qobj]` — named observables; results land in `expect`. *(Blocking-3 resolution: targets are carried by `ObservableSpec.operators` keys, mirroring `HamiltonianTerm`; a bare `LocalOp` — which has no target — is no longer accepted.)*
**Return:** always an `EvolutionResult` (native dataclass — this, not a raw QuTiP result, is the D6 boundary). `store_states=False` + `e_ops` ⇒ expectation-only mode; `store_states=True` (default) retains the trajectory.
**Failure modes (typed):** `LayoutMismatchError`, `NonHermitianHamiltonianError`, `SolverConvergenceError` (non-convergence / `nsteps` exhausted / trace drift beyond tolerance). Fock truncation inadequacy is a **soft** signal: `diagnostics.truncation_ok=False` (not an exception), so parameter sweeps don't abort — the caller decides.

---

## §8 — Preparation primitives

**Local** primitives return a **local** `Qobj` density matrix on their subsystem's space; `product_state` tensors locals into the full-space density matrix on `layout`. Preparation infidelity is **local** (carried by each primitive) — this is where mode-specific errors like squeezing-prep infidelity live; `product_state` does **not** re-apply it. *(Blocking-1 resolution.)*

```python
# local two-level states (return a 2×2 density matrix)
def clock_superposition(*, relative_phase=0.0, prep_infidelity=0.0) -> "Qobj": ...   # (|0⟩+e^{iφ}|1⟩)/√2
def two_level_state(*, ket, prep_infidelity=0.0) -> "Qobj": ...

# local bosonic-mode states (return a dim×dim density matrix; dim = the mode's Fock cutoff)
def squeezed_mode(*, dim, r, theta=0.0, n_thermal=0.0, prep_infidelity=0.0) -> "Qobj": ...  # ⟨n⟩=sinh²r at n_thermal=0
def coherent_mode(*, dim, alpha, prep_infidelity=0.0) -> "Qobj": ...
def thermal_mode(*, dim, n_thermal, prep_infidelity=0.0) -> "Qobj": ...
def fock_mode(*, dim, n, prep_infidelity=0.0) -> "Qobj": ...

# composition into the full-space product state
def product_state(layout, parts: Mapping[str, "Qobj"]) -> "Qobj": ...
    # Tensors the per-subsystem LOCAL states in layout order; each part's dims must match its
    # subsystem (validated). Unspecified subsystems default to ground (TWO_LEVEL |0⟩⟨0|) /
    # vacuum (BOSONIC_MODE |0⟩⟨0|). No prep_infidelity argument (it is applied locally above).
```

- **Module 3a (Sorci):** `product_state(layout, {"clock": clock_superposition(), "M1": squeezed_mode(dim=layout.subsystem("M1").dim, r=r, prep_infidelity=ε_prep)})`.
- **Module 3b (open temporal instrument):** `product_state(layout, {f"carrier_{k:02d}": clock_superposition() for k in range(N)})` — a *product of independent carriers* and nothing more. The temporal-pointer / read-out interpretation that turns these carriers into a redundancy count is **Phase 2**, not part of prep.

---

## §9 — Package boundary: native vs QuTiP

**Native (the D6-stable surface):** `SubsystemKind`, `Subsystem`, `SystemLayout`, `Op`, `LocalOp`, `HamiltonianTerm`, `ChannelKind`, `LindbladChannel`, `NoiseModel`, `DriveNoise`, `ReadoutModel`, `MasterEquationSystem`, `ObservableSpec`, `SolverOptions`, `EvolutionDiagnostics`, `EvolutionResult`, and all prep-primitive signatures.

**QuTiP-typed boundary (documented, deliberately not hidden):** (1) quantum states are `qutip.Qobj` (ket/dm) with layout-matching dims — the state currency in/out, validated against `SystemLayout`, not redundantly wrapped; (2) `LocalOp.qobj` escape hatch; (3) `SolverOptions.qutip_options` pass-through.

**Outside the contract (free to change):** Liouvillian/`c_ops` assembly, `qutip.mesolve` calls and option objects, the operator registry's construction, all numerics. **And — per §0.4 — the full-`Qobj` state currency is the contract of the Phase-1 full-Hilbert backend; the future Module-3b factorised backend will state its own state representation and is out of this contract's scope.** *(Blocking-4 resolution.)*

---

## §10 — Phase 1 tests implied by this contract

- **Layout/dims:** tensor order matches `subsystems` order; `dims()` correct; `validate_state` raises on mismatch; `TWO_LEVEL` with dim ≠ 2 rejected at construction.
- **Hamiltonian assembly:** registered ops on the right subsystems; identity-fill for absent labels; assembled `H` Hermitian; non-Hermitian total raises.
- **Closed-system limit** (no channels/noise): trace and purity preserved; qubit free-precession period; harmonic-mode phase.
- **Lindblad channels (closed-form):** `DEPHASING` → coherence `e^{−γ_φ t}`; **`HEATING` → `d⟨n⟩/dt = ṅ` (state-independent, the symmetric-pair generator)**; `THERMAL_RELAXATION` → `⟨n⟩(t) = n̄ + (⟨n⟩₀−n̄)e^{−κt}` (and pure cooling at n̄=0); damped-harmonic-oscillator closed form.
- **`evolve` contract:** trajectory vs expectation-only modes; `e_ops` via `ObservableSpec`; `EvolutionResult` fields populated; `LayoutMismatchError` on bad dims; `diagnostics.truncation_ok=False` when top-Fock population crosses `fock_population_warn_threshold`.
- **Prep primitives:** `squeezed_mode` (local) → ⟨n⟩=sinh²r and sub-vacuum quadrature variance; `clock_superposition` → unit-visibility coherence; `product_state` tensors in layout order and rejects dim-mismatched parts; local `prep_infidelity=ε` lowers purity by the declared amount.
- **Backend scope:** `MasterEquationSystem.evolve` is full-Hilbert (assert it builds the full `Qobj`); a documented note that the Module-3b factorised backend is **not** Phase 1.
- **Firewall (negative test):** no `R_δ`/pointer/fragment/`I(C:M)`/`F[τ]` symbol exists in the Phase-1 public namespace.

---

## §11 — Resolved decisions (steward calls, 2026-05-27)

O1 units: **SI, ℏ=1**, caller nondimensionalises. · O2 clock dim: **TWO_LEVEL=2 fixed**, constructor `dim` args removed, qudits → future `FINITE_LEVEL`. · O3 state currency: **bare `Qobj`** + `validate_state`, scoped to the full-Hilbert backend (§0.4). · O4 prep infidelity: **local symmetric depolarising** toward `𝟙/d_sub`. · O5 drive noise: **`WHITE`→explicit `effective_rate` Lindblad term**, `CORRELATED` deferred. · O6 solver: **`mesolve` only**, `solver` field pins it, `mcsolve` deferred. · O7 spec placement: **`drive_noise` + `readout` carried on `MasterEquationSystem`** as declared specs.

---

## §12 — Explicitly deferred to Phase 2 / Phase 3 (the firewall)

**Phase 2:** `TemporalRecordEnsemble`; pointer `T`, prior `P(T)`, dimension `d`, per-carrier POVMs, fragments, deficit `δ`; `mutual_information` (`I(C:M)`), `quantum_fisher` (`F[τ]`), `temporal_redundancy` (`R_δ`); cross-anchor invariants; the MN v0.2 §2 analytic-poles regression. **Phase 3:** the factorised product-state backend for Module 3b at N≫2 (§0.4). Phase 1 produces evolved full-Hilbert states and declares the readout layer; it constructs none of the above.

---

## §13 — Review resolution (rev. 2026-05-27)

Two reviews: one accepted the proposal as-is; the other found four Blocking + two High + two Medium items. **The blocking findings were correct on the merits and are resolved here** (notably the HEATING channel, which the accepting review mis-scored as non-blocking — `D[a†]` alone gives state-dependent `d⟨n⟩/dt = ṅ(⟨n⟩+1)`, not the constant `ṅ` the test asserts).

- **Blocking — prep contract:** local primitives now return *local* density matrices; `product_state` tensors them; `prep_infidelity` is local (§8, §5.1).
- **Blocking — HEATING generator:** redefined as `ṅ·(D[a†]+D[a])` for state-independent `d⟨n⟩/dt = ṅ`; steady-state thermal behaviour moved to a new `THERMAL_RELAXATION` channel (§5.2).
- **Blocking — `e_ops` ambiguity:** introduced `ObservableSpec` (`{label: LocalOp}` + coefficient); bare `LocalOp` (no target) no longer accepted (§7).
- **Blocking — full-Qobj vs N≫2:** §0.4 + §9 now state Phase 1 is the full-Hilbert QuTiP backend; the Module-3b factorised backend is a separate Phase-3 component sharing specs (D3).
- **High — constructor dim args:** `clock_dim`/`dim` removed from `clock_and_modes`/`carriers`; `TWO_LEVEL` hard-validated == 2; qudits → future `FINITE_LEVEL` (§2).
- **High — drive-noise rate:** `DriveNoise.effective_rate` is the **coherence-decay rate** matching `ChannelKind.DEPHASING`; WHITE adds `(effective_rate/2)·D[operator]` (§5.3). *(Second-pass fix: the first rev. wrote `effective_rate·D[σ_z]`, which decays as `e^{−2·effective_rate·t}` — inconsistent with `DEPHASING`'s `(γ_φ/2)·D[σ_z]`. The `/2` is now explicit, so a σ_z WHITE drive noise equals a `DEPHASING` channel at `γ_φ=effective_rate`.)*
- **Medium — truncation threshold:** `SolverOptions.fock_population_warn_threshold` added (§7).
- **Medium — solver vs integrator:** `SolverOptions.solver: Literal["mesolve"]` added, distinct from `method` (§7).

---

*End of Phase 1 API-contract proposal v0.1 (rev.). Awaiting steward acceptance; on acceptance the agreed signatures mirror into `numerics/README.md` and Phase 1 implementation begins.*
