# tmc-numerics — Numerical Toolkit for Temporal Micro Consensus

Numerical toolkit operationalising the *Consensus-Emergence of Classical Proper Time* framework's declared anchor measures — mutual information `I(C:M)`, quantum Fisher information `F[τ]`, and the temporal-redundancy functional `R_δ` — through master-equation simulation of clock-plus-carrier systems.

**Status: Phase 0–2 + Phase-3 Module 3a (Sorci protocol) implemented — 79 tests passing.** Module 3b (open temporal instrument, N≫2) is not yet started.

The authoritative scope, phase gates, locked architectural decisions, and the public-API contract live in the work plan: [`../workplans/toolkit-work-plan-v0.1.md`](../workplans/toolkit-work-plan-v0.1.md). This README is a scaffold and will grow with the API (the Phase 1 gate requires it to reflect committed function signatures).

## Layout

```
numerics/
├── pyproject.toml      authoritative build + dependency config (package: tmc-numerics)
├── requirements.txt    minimum-version manifest (work-plan §4)
├── src/tmc_numerics/   package source (src-layout)
├── tests/              pytest suite (smoke + Phase 1 core-layer tests)
├── examples/           reproducible example notebooks (Phase 3)
└── results/            committed numerical results + reproducibility metadata (Phase 3)
```

## Install (development)

```
python -m pip install -e ".[test]"
```

Run from this directory. Requires Python ≥ 3.10. Core dependencies: `qutip` ≥ 5.0, `numpy` ≥ 1.24, `scipy` ≥ 1.10. Optional extras: `viz` (matplotlib), `examples` (jupyter + matplotlib), `progress` (tqdm).

## Test

```
pytest
```

Continuous integration runs the suite on Python 3.10–3.12 on every push touching `numerics/` (`.github/workflows/numerics-ci.yml`). Failed tests block merges (work-plan §5).

## Phase 1 — core-layer API (accepted contract; implemented)

Accepted and implemented 2026-05-27 (37 tests passing, QuTiP 5.2). The signatures below are the **D6-locked** public surface (stable from v0.1; internal numerics free). Full contract with rationale, failure modes, and the implied test list: [`../workplans/toolkit-phase1-api-contract-v0.1.md`](../workplans/toolkit-phase1-api-contract-v0.1.md).

**Conventions.** `ℏ=1`; angular frequencies [rad/s], time [s], rates [s⁻¹]. Tensor order = `SystemLayout` subsystem order (Sorci: `clock ⊗ M₁ ⊗ … ⊗ M_N`). Quantum states are `qutip.Qobj` with layout-matching dims (the documented QuTiP boundary). **Backend scope:** this is the *full-Hilbert* QuTiP `mesolve` backend (Module 3a + small-N validation); the Module-3b factorised N≫2 backend is a separate Phase-3 component sharing these specs (D3). **Firewall:** no `R_δ` / pointer / `I(C:M)` / `F[τ]` symbol is part of Phase 1 — those are Phase 2.

### System and operators

```python
class SubsystemKind(Enum):
    TWO_LEVEL     # dim hard-validated == 2 (qudits → future FINITE_LEVEL)
    BOSONIC_MODE  # dim = Fock cutoff = n_max + 1

@dataclass(frozen=True)
class Subsystem:    label: str; kind: SubsystemKind; dim: int

@dataclass(frozen=True)
class SystemLayout:
    subsystems: tuple[Subsystem, ...]                 # tensor order = sequence order
    @classmethod
    def clock_and_modes(cls, n_modes, mode_cutoffs) -> "SystemLayout": ...   # clock(2) ⊗ M1 ⊗ …
    @classmethod
    def carriers(cls, n) -> "SystemLayout": ...                              # carrier_00 ⊗ …
    def index(self, label) -> int: ...
    def subsystem(self, label) -> Subsystem: ...
    def dims(self) -> list[int]: ...
    def validate_state(self, state: "Qobj") -> None: ...   # LayoutMismatchError on dims mismatch

class Op(Enum):
    IDENTITY; SIGMA_X; SIGMA_Y; SIGMA_Z; SIGMA_PLUS; SIGMA_MINUS   # two-level
    NUM; DESTROY; CREATE; X_QUAD; P_QUAD                            # bosonic

@dataclass(frozen=True)
class LocalOp:      op: Op | None = None; power: int = 1; qobj: "Qobj | None" = None  # exactly one of {op, qobj}

@dataclass(frozen=True)
class HamiltonianTerm:
    coefficient: float                 # rad·s⁻¹ (real); total H = Σ terms must be Hermitian
    operators: Mapping[str, LocalOp]   # subsystem-label -> local op; absent labels => identity
    label: str = ""
```

### Nuisance model (four layers; only the dynamical layer enters `evolve`)

initial-state → prep `prep_infidelity` · dynamical Lindblad → `LindbladChannel` · stochastic/drive → `DriveNoise` · readout/detection → `ReadoutModel` (declared; applied in Phase 2).

```python
class ChannelKind(Enum):                    # D[c]ρ = cρc† − ½{c†c, ρ}
    HEATING             # bosonic: ṅ·(D[a†]+D[a]);  d⟨n⟩/dt = +ṅ  (state-independent)
    THERMAL_RELAXATION  # bosonic: κ(n̄+1)D[a] + κn̄D[a†];  d⟨n⟩/dt = −κ(⟨n⟩−n̄)  (n̄=0 ⇒ cooling)
    MOTIONAL_DEPHASING  # bosonic: γ_φ·D[a†a]
    DEPHASING           # two-level: (γ_φ/2)·D[σ_z];  coherence ∝ e^{−γ_φ t}
    AMPLITUDE_DAMPING   # two-level: Γ·D[σ_−]

@dataclass(frozen=True)
class LindbladChannel:  target: str; kind: ChannelKind; rate: float; n_thermal: float | None = None; label: str = ""

class NoiseModel(Enum):  WHITE; CORRELATED          # CORRELATED deferred to v0.2

@dataclass(frozen=True)
class DriveNoise:       target: str; operator: LocalOp; model: NoiseModel; effective_rate: float; label: str = ""
    # effective_rate = COHERENCE-DECAY rate (matches DEPHASING). WHITE adds (effective_rate/2)·D[operator];
    # for σ_z this IS a DEPHASING channel at γ_φ=effective_rate (coherence ∝ e^{−effective_rate·t}).

@dataclass(frozen=True)
class ReadoutModel:     target: str; detection_infidelity: float = 0.0; correlated_with: str | None = None; label: str = ""
    # NOT consumed by evolve(); applied in Phase 2
```

### System and evolution

```python
class MasterEquationSystem:
    def __init__(self, layout, hamiltonian, channels=(), drive_noise=(), readout=()): ...
    @property
    def layout(self) -> SystemLayout: ...
    def hamiltonian_operator(self) -> "Qobj": ...      # Hermitian; raises otherwise
    def collapse_operators(self) -> list["Qobj"]: ...
    def evolve(self, state, times, *, e_ops=None, options=None, store_states=True) -> "EvolutionResult": ...

@dataclass(frozen=True)
class ObservableSpec:   operators: Mapping[str, LocalOp]; coefficient: float = 1.0   # like HamiltonianTerm.operators

@dataclass
class SolverOptions:
    solver: Literal["mesolve"] = "mesolve"      # v0.1: only mesolve; mcsolve deferred
    method: str = "adams"; atol: float = 1e-12; rtol: float = 1e-10; nsteps: int = 10_000
    fock_population_warn_threshold: float = 1e-6
    qutip_options: dict | None = None           # advanced pass-through (outside D6 stability)

@dataclass
class EvolutionDiagnostics:  max_fock_population: dict[str, float]; trace_drift: float; truncation_ok: bool

@dataclass
class EvolutionResult:
    times: "np.ndarray"; states: "list[Qobj] | None"; expect: dict[str, "np.ndarray"]
    final_state: "Qobj"; layout: SystemLayout; solver: str; converged: bool; diagnostics: EvolutionDiagnostics
# e_ops: Mapping[str, ObservableSpec | Qobj] | None
# typed failures: LayoutMismatchError, NonHermitianHamiltonianError, SolverConvergenceError
# truncation inadequacy is SOFT (diagnostics.truncation_ok=False), not an exception
```

### Preparation primitives

Local primitives return a **local** `Qobj` density matrix (infidelity is local); `product_state` tensors them into the full-space state on `layout`.

```python
def clock_superposition(*, relative_phase=0.0, prep_infidelity=0.0) -> "Qobj": ...     # (|0⟩+e^{iφ}|1⟩)/√2
def two_level_state(*, ket, prep_infidelity=0.0) -> "Qobj": ...
def squeezed_mode(*, dim, r, theta=0.0, n_thermal=0.0, prep_infidelity=0.0) -> "Qobj": ...  # ⟨n⟩=sinh²r
def coherent_mode(*, dim, alpha, prep_infidelity=0.0) -> "Qobj": ...
def thermal_mode(*, dim, n_thermal, prep_infidelity=0.0) -> "Qobj": ...
def fock_mode(*, dim, n, prep_infidelity=0.0) -> "Qobj": ...
def product_state(layout, parts: Mapping[str, "Qobj"]) -> "Qobj": ...   # tensors locals; absent => ground/vacuum
```

## Phase 2 — anchor-measure layer (`tmc_numerics.anchors`)

Accepted and implemented 2026-05-27 (D6-locked; the **D5 regression gate reproduces the MN v0.2 §2 analytic poles**). Imported explicitly, so the Phase-1 core stays import-clean:
`from tmc_numerics.anchors import mutual_information, quantum_fisher, temporal_redundancy`. Full contract: [`../workplans/toolkit-phase2-api-contract-v0.1.md`](../workplans/toolkit-phase2-api-contract-v0.1.md).

**Conventions.** Information in **bits** (`log2`); QFI is dimensionful (`[τ]⁻²`). Pointer basis fixed `"computational"` (binary) for v0.1.

```python
class InfoMode(Enum):
    PER_CARRIER   # classical MI of independent per-carrier outcomes (physical redundancy read-out; default)
    HOLEVO        # Holevo χ; the ideal global read-out (MN §2); = PER_CARRIER on the redundant pole

@dataclass(frozen=True)
class TemporalPointer:        dim: int = 2; prior: tuple[float, ...] | None = None   # default uniform

@dataclass(frozen=True)
class TemporalRecordEnsemble:
    pointer: TemporalPointer; n_carriers: int
    iid_carrier_states: Mapping[int, Qobj] | None = None   # T -> single-carrier ρ^{(T)} (i.i.d. of n; any n)
    joint_states: Mapping[int, Qobj] | None = None         # T -> full carrier-joint ρ^{(T)} (small n)
    joint_layout: SystemLayout | None = None
    readout: ReadoutModel | None = None                    # Phase-1 detection layer
    pointer_basis: str = "computational"
    @classmethod
    def iid(cls, conditional_carrier, n_carriers, pointer=None, *, readout=None) -> "TemporalRecordEnsemble": ...
    @classmethod
    def from_evolution(cls, results, joint_layout, pointer=None, *, readout=None) -> "TemporalRecordEnsemble": ...
        # results: {T: EvolutionResult | Qobj} — the composition point with Phase-1 evolve()

def partial_information(ensemble, fragment, *, mode=InfoMode.PER_CARRIER) -> float   # I(T:F) in bits
                                                # fragment: int count (iid) | carrier-index seq (joint)

def mutual_information(state, partition, *, layout=None, base="bits") -> float
                                                # quantum I(A:B); partition = (labels_or_idx_A, ..._B)
def quantum_fisher(state, generator) -> float   # QFI for ρ(τ)=e^{-iGτ}ρe^{+iGτ}; generator = Hermitian Qobj

@dataclass
class RedundancyResult:  R_delta: float | None; m_delta: int | None; deficit: float; H_T: float; info_curve: list; mode: str
                         # R_delta is None ("undefined") iff the threshold is never reached — distinct from R_delta == 1

def temporal_redundancy(ensemble, deficit, *, mode=InfoMode.PER_CARRIER, fragment_order=None) -> RedundancyResult
```

**D5 gate (`tests/test_d5_redundancy.py`).** Product (redundant) pole via the `iid` representation matches MN Appendix A to ≤1e-9 — `R_{0.10}=64/9≈7.1` at e=0.20, **undefined** at e≥0.40 — and never builds a 2⁶⁴ state. GHZ-shadow (anti-redundant) pole via the `joint` representation at small N gives `R_δ=1` under `HOLEVO`, with `test_ghz_per_carrier_reads_zero` as the negative confirmation (per-carrier read-out sees `I(N)=0`). Cross-anchor invariants (`tests/test_cross_anchor.py`) assert the resolution/classification split: `F[τ]` extensive (`N`) vs Heisenberg (`N²`), anti-correlated with `R_δ`.

## Phase 3 Module 3a — Sorci protocol (`tmc_numerics.modules.sorci`)

Implemented 2026-05-27 (D6-locked contract: [`../workplans/toolkit-module3a-sorci-contract-v0.1.md`](../workplans/toolkit-module3a-sorci-contract-v0.1.md)). The CL-2026-006 **D1** nuisance-budget decomposition for the squeezed-Ramsey two-carrier protocol.

Rotating frame w.r.t. the free clock (exact: σ_z commutes with the coupling). Two models: **secular dispersive** `H_sec = g_md σ_z n̂` (workhorse, any t — used for the ²⁷Al⁺ extrapolation) and **full** `ω n̂ + g_md σ_z P̂²` (scaled-parameter validation). `g_md = −ε_m ω_c/4` is **derived**; the baseline validates Sorci Eq. (12)'s coefficient (`(1−V)/(λ²sinh²2r) → 1/16` as `λ=ε_m ω_c t → 0`). Squeezing is the prepared initial state.

```python
@dataclass(frozen=True)
class SorciParams:
    omega_c; omega; cutoff; t; eps_m; r            # structural + signal
    n_dot=0; gamma_phi=0; eps_prep=0; drive_phase_rate=0; eps_det=0   # the four nuisance layers
    # .g_md = −eps_m*omega_c/4 ; .lam = eps_m*omega_c*t

def build_sorci_system(params, *, secular=True, include_nuisance=True) -> MasterEquationSystem
def sorci_initial_state(params) -> Qobj                          # clock |+> ⊗ squeezed(r)
def sorci_visibility(result) -> np.ndarray                       # LATENT V_state = 2|ρ01^clock| (read-out-invariant)
def sorci_observed_visibility(result, eps_det) -> np.ndarray     # OBSERVED V_obs = (1−2ε_det)·V_state
def clock_motion_mutual_information(result) -> np.ndarray        # LATENT I(C:M), bits
def baseline_visibility_check(params, *, lambdas=(.1,.05,.025)) -> dict   # (1−V)/(λ²sinh²2r) → 1/16
def rwa_error(params) -> float                                   # |V_full − V_secular| (→0 as ωt→∞)
def nuisance_budget(params, *, secular=True, sweep_ranges=None) -> NuisanceBudget
```

The budget splits **latent** (`I(C:M)`, `V_state` — read-out-invariant) from **observed** (`V_obs` — detection-degraded); the detection row's latent contributions are identically 0. Extraction = marginal-from-signal per channel + full + interaction residual (honest non-additivity). Validated against Sorci Eq. (12), full↔secular RWA agreement, and the ²⁷Al⁺ V≈0.93 extrapolation. (Benchmark-specific finding: motional dephasing is *secular-invisible* — the dispersive `σ_z n̂` coupling is insensitive to number-basis dephasing.)

## Licence

The toolkit is **MIT-licensed** (code, per the repository split licence; see the root [`LICENSE-MIT`](../LICENSE-MIT) and README §"Split licence"). This is distinct from the CC BY-SA 4.0 of the framework notes.

## Citing

Cite the toolkit per the appended code-citation section in the repository [`CITATION.cff`](../CITATION.cff); the repository as a whole is archived at [doi:10.5281/zenodo.20411120](https://doi.org/10.5281/zenodo.20411120).

## Phase 0 decisions (work plan §8)

- **Q1 (resolved):** code citation is an **appended section** in the root `CITATION.cff`, not a separate `numerics/CITATION.cff`.
- **Q2 (resolved):** GitHub Actions CI **enabled** for v0.1 (`.github/workflows/numerics-ci.yml`).
- **Q3 (resolved earlier):** Phase-3 results are **committed** to `results/` with reproducibility metadata, not generated on-demand.
- **Q5 (resolved):** reconciliation with CL-2026-005 (the Colla–Breuer–Gasbarri / "CBG" non-Markovian TCL pipeline, `oqs-cbg-pipeline`) — **reimplement in QuTiP** (per work-plan D3). CBG computes the coherent effective Hamiltonian `K(t)` (non-Markovian), not the Markovian-Lindblad nuisance/MI budget D1 needs, and carries a permanent trapped-ion stewardship-conflict flag. It is retained only as an *optional* non-Markovian validation backend (HEOM/pseudomode cross-checks, later) and a methodological template (benchmark-card / validity-envelope discipline). See work-plan §6/§8.
