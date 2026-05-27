# Toolkit Phase 2 — Anchor-Measure Layer: Contract Addendum (proposal)

**Version:** v0.1 (ACCEPTED + D6-LOCKED 2026-05-27)
**Status:** **ACCEPTED — D6-LOCKED.** Signatures mirrored to `numerics/README.md` and implemented in `tmc_numerics.anchors` (68 tests passing; the D5 gate reproduces the MN v0.2 §2 analytic poles).
**Parent:** `workplans/toolkit-work-plan-v0.1.md` (Phase 2; D5 gate) and `workplans/toolkit-phase1-api-contract-v0.1.md` (the locked core layer this builds on).
**Scope (lightweight):** specify only the two elements the Phase-1 contract left unspecced — the **D5 regression matrix** (§3) and the **`TemporalRecordEnsemble` API** (§1). The three post-processors are *typed*, not redesigned (§2). Cross-anchor invariants are *flagged, not blocking* (§5).

---

## §0 — Principles

1. **Builds on locked Phase 1.** Conditional carrier states come from Phase-1 `evolve` (`EvolutionResult.final_state`); the detection layer is the Phase-1 `ReadoutModel`. Nothing in Phase 1 changes.
2. **The N=64 scaling fact is load-bearing.** The MN v0.2 §2 poles live at N=64 → a 2⁶⁴ joint space. Phase 2 must **never build the full joint state** for the redundant pole. The redundant (product) record is i.i.d. across carriers, so `I(m)` is a *single-carrier-channel* computation (binomial, exactly MN Appendix A). The anti-redundant (GHZ) pole is verified at *small* N where the 2ᴺ state is constructible; its N=64 `R_δ=1` follows analytically (MN Appendix B). This dual nature drives the `TemporalRecordEnsemble` design — and the i.i.d. representation is also what keeps Phase-3 Module 3b (N≫2) tractable (locked decision D3).
3. **Firewall direction reversed.** Phase 2 *adds* the symbols Phase 1 forbids; the Phase-1 firewall test is updated to assert they now live in a `tmc_numerics.anchors` (or sibling) namespace, keeping the core layer import-clean.

---

## §1 — `TemporalRecordEnsemble` API

The object that composes the Phase-1 `ReadoutModel` + evolved states into the redundancy substrate. `R_δ` is `I(T : F_m)` between a classical pointer `T` and a fragment read-out — **not** a state-intrinsic quantity (this is why it could not be a Phase-1 state functional).

```python
@dataclass(frozen=True)
class TemporalPointer:
    dim: int = 2                              # d; binary clock = 2, H_T = log2(d) bits
    prior: tuple[float, ...] | None = None    # P(T); default uniform (1/dim each)


@dataclass(frozen=True)
class TemporalRecordEnsemble:
    pointer: TemporalPointer
    n_carriers: int
    # --- exactly ONE of the two representations is populated ---
    iid_carrier_states: Mapping[int, "qt.Qobj"] | None = None   # T -> SINGLE-carrier ρ^{(T)} (i.i.d. product of n)
    joint_states: Mapping[int, "qt.Qobj"] | None = None         # T -> FULL carrier-joint ρ^{(T)} (small n only)
    joint_layout: "SystemLayout | None" = None                  # carrier layout for joint_states (fragments via ptrace)
    readout: "ReadoutModel | None" = None                       # Phase-1 detection layer (per-carrier)
    pointer_basis: str = "computational"                        # assumed einselected per-carrier basis (binary: {|0>,|1>})

    @classmethod
    def iid(cls, conditional_carrier: Mapping[int, "qt.Qobj"], n_carriers, pointer=TemporalPointer(),
            *, readout=None) -> "TemporalRecordEnsemble": ...
        # n i.i.d. copies of a single-carrier conditional-state map. Scales to any n (no 2^n state).

    @classmethod
    def from_evolution(cls, results: Mapping[int, "EvolutionResult | qt.Qobj"], joint_layout, pointer=TemporalPointer(),
                       *, readout=None) -> "TemporalRecordEnsemble": ...
        # joint representation from Phase-1 evolutions: one evolve() per pointer value T -> final_state.
        # The composition point with Phase 1. Small-n only (dense joint state).
```

**Read-out modes** (how a fragment's conditional states become `I(T:F)`):

```python
class InfoMode(Enum):
    PER_CARRIER  # classical MI of INDEPENDENT per-carrier POVM outcomes (pointer-basis projective,
                 # composed with ReadoutModel.detection_infidelity). The physically meaningful
                 # redundancy read-out (MN §1.2 independence). Default.
    HOLEVO       # Holevo χ of {P(T), ρ_F^{(T)}}: χ = S(Σ P(T)ρ^{(T)}) − Σ P(T)S(ρ^{(T)}).
                 # = accessible information when the ensemble states commute (redundant pole) or are
                 # orthogonal (GHZ full set); the "ideal global read-out" of MN §2; an UPPER BOUND in general.
```

For the *redundant* (diagonal/commuting) pole, `PER_CARRIER == HOLEVO`. For the *anti-redundant* (GHZ) pole, only `HOLEVO` recovers `I(N)=H_T` (a per-carrier computational read-out cannot see the relative phase, so `PER_CARRIER` would read 0 even at m=N — see §3). This is exactly MN §2's "ideal global read-out" stipulation, made an explicit mode rather than a hidden assumption.

`partial_information` exploits the representation:
- **iid:** `I(m)` = MI of `m` i.i.d. uses of the single-carrier channel (binomial for binary `T`). Closed-form, any `n`, **no 2ᵐ state**.
- **joint:** `I(F)` for a fragment `F ⊆ carriers` via `ptrace` of the joint conditional states, then `PER_CARRIER`/`HOLEVO`. Small `n` only.

---

## §2 — The three post-processors (typed, not redesigned)

Stable typing against the `EvolutionResult` + `TemporalRecordEnsemble` boundary. All information quantities in **bits** (`log2`); QFI is dimensionful (`[τ]⁻²`).

```python
def mutual_information(state, partition, *, base: str = "bits") -> float: ...
    # quantum I(A:B) = S(ρ_A) + S(ρ_B) − S(ρ_AB) for a bipartition of layout subsystems.
    # state: qt.Qobj density matrix (or EvolutionResult -> .final_state).
    # partition: (labels_A, labels_B); disjoint; the complement is traced out. I(C:M) = ({"clock"}, {"M1"}).

def quantum_fisher(state, generator) -> float: ...
    # QFI for ρ(τ) = exp(−iGτ) ρ exp(+iGτ): F = 2 Σ_{i,j: λ_i+λ_j>0} (λ_i−λ_j)²/(λ_i+λ_j) |⟨i|G|j⟩|².
    # state: qt.Qobj density matrix (or EvolutionResult -> .final_state); generator: Hermitian qt.Qobj (full-space).
    # The RESOLUTION anchor — NOT a classifier (see §5).

@dataclass
class RedundancyResult:
    R_delta: float | None          # None == "undefined" (threshold never reached) — distinct from R_delta == 1
    m_delta: int | None
    deficit: float
    H_T: float                     # log2(dim) bits
    info_curve: list[tuple[int, float]]   # (m, I(m)) along the fragment ordering
    mode: str                      # "per_carrier" | "holevo"

def temporal_redundancy(ensemble, deficit, *, mode=InfoMode.PER_CARRIER,
                        fragment_order=None) -> RedundancyResult: ...
    # R_δ = n / m_δ, m_δ = min{ m : I(m) ≥ (1−δ)·H_T }; R_δ = None ("undefined") if never reached.
    # I(m) = partial_information over the first m carriers (default fragment_order = carrier index order;
    #        for i.i.d. records the ordering is immaterial).
```

---

## §3 — D5 regression matrix

The gate: reproduce the MN v0.2 §2 analytic poles. Two pole families; the harness builds the exact analytic states and checks `R_δ`.

### 3a — Redundant (product) pole — i.i.d. representation, any N

Single-carrier conditional states (binary `T`, flip probability `e ∈ (0, ½)`):
> `ρ_carrier^{(T)} = (1−e)·|T⟩⟨T| + e·|1−T⟩⟨1−T|`   (mixed, diagonal; `e` = finite per-carrier distinguishability)

Built as `TemporalRecordEnsemble.iid({0: ρ^{(0)}, 1: ρ^{(1)}}, n_carriers=64)`, `mode` either (they coincide here). `I(m)` = binomial-channel MI = MN Appendix A `I_product(m, e)`.

| Check (N=64, δ=0.10) | Expected | Tolerance |
|---|---|---|
| partial-info plot, e=0.20, m∈{1,2,4,8,16,32,48,64} | I = {0.2781, 0.4605, 0.6908, 0.8918, 0.9852, 0.9997, 1.0000, 1.0000} | `|ΔI| ≤ 1e-9` vs Appendix A |
| `R_δ` vs e: e=0.10 | m_δ=4, R_δ=16.0 | m_δ exact; R_δ exact rational |
| e=0.20 | m_δ=9, R_δ=64/9≈7.111 | as above |
| e=0.30 | m_δ=22, R_δ=64/22≈2.909 | as above |
| e=0.40 | **undefined** (I(64)=0.807 < 0.9) | m_δ=None, R_δ=None |
| e=0.45 | **undefined** (I(64)=0.354) | m_δ=None, R_δ=None |

*Construction note:* `e` is modelled as a **state** property (mixed diagonal conditional states), not a detector flip, so that even the optimal (`HOLEVO`) read-out sees it — `PER_CARRIER == HOLEVO` for these commuting states, and both reproduce Appendix A. (A separate, optional check encodes `e` instead via `ReadoutModel.detection_infidelity` on perfect `|T⟩` carriers — equivalent binomial channel — to exercise the detection-layer path.)

### 3b — Anti-redundant (GHZ-shadow) pole — joint representation, small N

> `|ψ_T⟩ = (|0⟩^{⊗N} + (−1)^T |1⟩^{⊗N})/√2`,  `ρ^{(T)} = |ψ_T⟩⟨ψ_T|`

Built via the **joint** representation at **small N (e.g. N=4 → 16-dim)**, where the cat is constructible. `mode=HOLEVO` (the ideal global read-out).

| Check (small N, δ=0.10) | Expected | Tolerance |
|---|---|---|
| proper fragments (m < N) | `I(m) = 0` (ρ_F^{(T)} is T-independent, MN Appendix B) | `≤ 1e-12` |
| full set (m = N) | `I(N) = H_T = 1` (ρ^{(0)} ⟂ ρ^{(1)}) | `≤ 1e-12` |
| redundancy | m_δ = N ⇒ `R_δ = N/N = 1` (**not** undefined) | exact |
| `PER_CARRIER` contrast | `I(N) = 0` under a per-carrier computational read-out (cannot see the phase) ⇒ confirms why `HOLEVO`/ideal-global is required | `≤ 1e-12` |

The N=64 `R_δ=1` claim is **analytic** (MN Appendix B: the I(m) step function gives m_δ=N at any N); the regression reproduces it *structurally* via the threshold logic, and verifies the underlying state behaviour at small N. The headline contrast — **same N carriers, `R_{0.10}=7.1` (product) vs `1` (GHZ)** — is asserted as a single test.

### 3c — Tolerance budget

The work-plan's suggested **1e-4** is the *outer* budget; the §2 poles are qubit-based and computed in closed form (binomial MI; von Neumann entropies of small states), so the regression achieves **~1e-9 or tighter**, and `m_δ`/`R_δ` are matched **exactly** (integers / rationals). The loose 1e-4 is reserved for later dynamical/bosonic cases (§4), not the analytic poles.

---

## §4 — Finite-cutoff note

The §2 poles are **two-level (qubit) carriers** — `dim = 2`, **no Fock truncation**, so the D5-core regression is cutoff-free and exact. "Finite-cutoff effects in the bosonic cases" do **not** arise for the canonical poles. Bosonic realisations (e.g. coherent-state phase carriers, where `dim` is a Fock cutoff) are a *separate, looser-tolerance class* whose truncation error must be declared via `EvolutionDiagnostics.truncation_ok`; they are **out of D5-core scope** and deferred (Phase 3 / a later regression tier).

---

## §5 — Cross-anchor invariants (flagged, not blocking)

Not implemented in this pass, but the test-file layout reserves `tests/test_cross_anchor.py` so the structure accounts for it. The invariants encode the **resolution/classification split** (work-plan §5; MN v0.2 §4): the two *classification* anchors `I(C:M)` and `R_δ` co-move; the *resolution* anchor `F[τ]` is **not** a classifier and must not be read as one (the named **CL-2026-007 v0.1 failure mode**). Reserved assertions:
- product pole → `R_δ ≫ 1`; GHZ pole → `R_δ = 1` with every proper-fragment `I(T:F)=0`;
- `F[τ]` **extensive** (additive over independent carriers, `F_τ(m)=m·F_1`) and **rises** toward the anti-redundant pole where `R_δ` falls — anti-correlated, non-substitutable;
- per-carrier nuisance (raise `e`) collapses the `R_δ` plateau with **no** change in entanglement structure (MN §2 second table, §5).

These ride along once the three post-processors exist (the user's steer); they are gated *after* the D5 primitives, not before.

---

## §6 — Open questions for steward review — ALL CONFIRMED (2026-05-27)

*Steward resolution: P1–P5 confirmed as recommended. Non-blocking observations honored — the GHZ negative test is named `test_ghz_per_carrier_reads_zero`; the cross-anchor anti-correlation (F[τ] rises where R_δ falls) is implemented in `tests/test_cross_anchor.py`.*


- **P1 — Default `InfoMode`.** `PER_CARRIER` as the default (physical redundancy read-out), `HOLEVO` opt-in for the anti-redundant pole / upper bound? (Recommended — and the D5 matrix names the mode per pole.)
- **P2 — Pointer basis.** v0.1 fixes `pointer_basis="computational"` (binary `{|0>,|1>}`); a general einselected-basis spec is deferred. (Recommended — the §2 poles need only computational.)
- **P3 — Namespace.** Put the anchor layer in a `tmc_numerics.anchors` submodule (keeping the Phase-1 core import-clean and the firewall test meaningful), vs flat in the top package? (Recommended: submodule.)
- **P4 — `mutual_information` log base.** Bits (`log2`) throughout for consistency with `H_T`? (Recommended.)
- **P5 — QFI input.** `quantum_fisher(state, generator)` with a Hermitian generator `G` (recommended), vs a finite-difference pair of states `(ρ(τ), ρ(τ+dτ))`? The generator form is exact and matches the Sorci elapsed-time encoding; the FD form is a convenience that could be added without breaking the signature.

---

## §7 — Deferred / firewall reaffirmation

Still Phase 3: the Module-3b factorised dynamical backend (the i.i.d. ensemble here is its post-processing substrate, but the *dynamical* `ε(γ_φ, ṅ, t)` derivation is Phase 3); bosonic-carrier regressions (§4). The Phase-1 core layer remains untouched; Phase 2 adds the anchor namespace and updates the firewall test to point at it.

---

*End of Phase 2 contract addendum v0.1 (proposal). Awaiting steward review; on acceptance the signatures mirror into `numerics/README.md` and Phase 2 implementation begins.*
