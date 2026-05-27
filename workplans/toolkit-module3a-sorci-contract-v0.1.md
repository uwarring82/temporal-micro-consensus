# Toolkit Module 3a — Sorci Protocol: Contract

**Version:** v0.1 (ACCEPTED + D6-LOCKED 2026-05-27; two review passes — see §9)
**Status:** **ACCEPTED — D6-LOCKED.** On acceptance: mirror to `numerics/README.md`, log, commit, implement (baseline cross-check first, then the budget).
**Parent:** `workplans/toolkit-work-plan-v0.1.md` (Phase 3, Module 3a; CL-2026-006 D1) on the locked Phase-1 core + Phase-2 anchor layer.

---

## §0 — Principles

1. **Builds on locked layers** (Phase-1 core; Phase-2 `mutual_information`, the declared I(C:M) anchor). Nothing in them changes.
2. **D1, not D1–D3.** Produces the *theoretical* per-channel decomposition CL-2026-006 **D1** names (one of three; D2/D3 experimental). Grounding for a CL-2026-006 v0.5 draft (Phase 4), not a verdict upgrade.
3. **D1-minimal scope (single mode); mode-mixing deferred.** v0.1 is `clock ⊗ M1`. The work plan's Module-3a sweep superset lists anomalous *mode-mixing* (a ≥2-mode effect); it is **deferred** to a later two-mode extension and is **not** in this contract. Flagged so the scope divergence is explicit.
4. **Latent vs observed (the review-1 split).** `I(C:M)` and `V_state = 2|ρ₀₁^clock|` are **state-intrinsic (latent)** — readout/detection cannot change them. Detection-correlated infidelity acts **only** on **observed** quantities through a terminal read-out channel (§3). The budget separates the two.
5. **Honest non-additivity.** Per-channel marginals + full model + interaction residual (A4).

---

## §1 — Hamiltonian builder

`Ĥ = Ĥ_c + ℏω(n̂+½) − (ℏω/2mc²) Ĥ_c P̂²`, `Ĥ_c = (ω_c/2)σ_z`, on `SystemLayout.clock_and_modes(1, cutoff)`.

### §1.1 — Terms → `HamiltonianTerm` (coefficients DERIVED, not fitted)
- **Free mode** `ω n̂` — `HamiltonianTerm(ω, {"M1": LocalOp(Op.NUM)})` (the `+½` c-number dropped).
- **Mass-defect coupling** `g_md σ_z P̂²`, with `g_md = −(ε_m ω_c)/4` **derived** from `Ĥ` and the Phase-1 `P_QUAD = (a−a†)/(i√2)` convention (`ε_m = ℏω/mc²`, dimensionless). `HamiltonianTerm(g_md, {"clock": LocalOp(Op.SIGMA_Z), "M1": LocalOp(Op.P_QUAD, power=2)}, "mass-defect coupling")`. The baseline test (§2, §6) **validates** that this derived coefficient reproduces Sorci Eq. (12) — it does **not** calibrate `g_md`.
- **Free clock** `(ω_c/2)σ_z` — **removed exactly by the rotating frame** (§1.3); `σ_z` commutes with the coupling, so there are no counter-rotating terms and the frame only strips the clock's global phase. Visibility (a coherence magnitude) is frame-invariant.

### §1.2 — Squeezing is a PREPARED STATE (M1)
Initial state `product_state(clock_superposition(prep_infidelity=…), squeezed_mode(dim=cutoff, r=r, prep_infidelity=ε_prep))`. The `sinh²(2r)` is the squeezed state's `P̂²`/number variance accrued through the coupling, not a drive. A dynamical squeezing-drive Hamiltonian is deferred to v0.2+.

### §1.3 — Tractability: rotating frame + two models + transfer conditions (M3)
The literal ²⁷Al⁺ point (ε_m=3.3×10⁻¹⁸, ω_c≈6.9×10¹⁵ rad/s, t≈1 s) is ~10¹⁵ oscillations — not integrable. Therefore:

- **Rotating frame w.r.t. the free clock — exact.** `σ_z` commutes with `g_md σ_z P̂²`; the frame removes the `e^{±iω_c t/2}` clock phase and leaves the coupling untouched.
- **Two models:**
  - **Secular/dispersive model = the experimental-column workhorse.** Time-averaging the `2ω` oscillation of `P̂²(t)` gives `P̂²(t) → n̂+½`, i.e. `H_sec = g_md σ_z (n̂+½)` — a dispersive dephasing whose strength tracks `Var(n̂)`. `n̂` is conserved, so `V_state(t) = |⟨e^{−2i g_md t n̂}⟩|` is exact for **any t** (no fast oscillation) → used for the ²⁷Al⁺ extrapolation. For squeezed vacuum `Var(n̂)=½sinh²(2r)` ⇒ `1−V = (ε_m ω_c t)² sinh²(2r)/16` analytically (the derived `g_md` is thus pinned, not fitted).
  - **Full `σ_z P̂²` model at scaled parameters = validation.** Confirms the `g_md` coefficient, the RWA/secular error, and the `sinh²(2r)` scaling, at a tractable trap frequency where `ωt` is O(10).
- **Transfer / validity conditions (must hold for scaled→experimental transfer).** Preserve the dimensionless controls `λ = ε_m ω_c t`, the squeezing `r`, and nuisance products `γ_φ t`, `ṅ t`, `drive_rate·t`; and the secular hierarchy `|g_md|/ω ≪ 1` and `ω t ≫ 1`. The module asserts these for any reported scaled→²⁷Al⁺ extrapolation; otherwise the scaled run would validate a different dynamical regime.

---

## §2 — Parameter sweep space

```python
@dataclass(frozen=True)
class SorciParams:
    omega_c: float; omega: float; cutoff: int; t: float        # fixed structural
    eps_m: float; r: float                                     # signal knobs
    n_dot: float = 0.0; gamma_phi: float = 0.0                 # dynamical-Lindblad (motional)
    eps_prep: float = 0.0                                      # initial-state (squeezing prep)
    drive_phase_rate: float = 0.0                              # stochastic-Hamiltonian (clock WHITE σ_z)
    eps_det: float = 0.0                                       # read-out (terminal; observed-only)
    # mode_mixing: deferred (≥2-mode extension; §0.3)
```

- **Baseline (zero-nuisance) cross-check:** recover Sorci Eq. (12) `1−V = (ε_m ω_c t)² sinh²(2r)/16` (secular, exact; full P̂² agrees within RWA error). Plus the N=2 **directional** R_δ reading (single transition, not a curve; §0).
- **Representative scaled headline point (M4):** `ω_c=10³`, `ω=10²`, `ε_m=10⁻³`, `t=0.1` (⇒ `λ=0.1`), `r=1.0` (`sinh²(2r)≈13.2`); `cutoff` grown until `EvolutionDiagnostics.truncation_ok` (not hand-fixed; ≈80 at r=1). Effects large enough to decompose cleanly.
- **Extrapolated ²⁷Al⁺ column (M4):** secular model at `r=2.26` and the experimental `λ = ε_m ω_c t ≈ 0.023` ⇒ `1−V ≈ 0.07`, `V≈0.93` (reproduces Sorci's headline); `cutoff` by `truncation_ok` (`⟨n⟩=sinh²r≈22.5` at r=2.26 ⇒ cutoff ~150–200).
- **Per-channel marginal sweeps:** vary one nuisance parameter over a declared range with the signal on (others zero).

---

## §3 — Nuisance-budget table (latent / observed split)

**Latent (state-intrinsic; from the evolved two-mode state):**
- `I(C:M) = mutual_information(state, ({"clock"}, {"M1"}))` (bits) — the declared classification anchor.
- `V_state = 2|ρ₀₁^clock|` (clock coherence; loss `L_state = 1 − V_state`).

**Observed (after the terminal read-out channel):**
- `V_obs` — `V_state` degraded by the `ReadoutModel` detection channel. For a symmetric clock-readout infidelity `ε_det`: `V_obs = (1−2ε_det)·V_state`; a *motion-correlated* detection error (D1 (v)) makes the flip depend on the motional read-out and is applied as a terminal channel on the joint read-out. **Detection touches only observed quantities.**

**Extraction = marginal-from-signal + full + residual:**
- *signal* row: all nuisance 0 → `L_state,sig`, `I_sig`.
- *channel k* row: `Δ = (with signal+k) − (signal)` for each of `{I(C:M), L_state, L_obs}`.
- *full* row and *interaction residual* row (`full − signal − Σ marginals`), reported for non-additivity.

| Layer | Channel | Parameter | `ΔI(C:M)` (latent) | `ΔL_state` (latent) | `ΔL_obs` (observed) |
|---|---|---|---|---|---|
| Hamiltonian (signal) | time-dilation | ε_m, r | `I_sig` | `L_state,sig` | `L_obs,sig` |
| dynamical-Lindblad | heating `ṅ` | … | … | … | … |
| dynamical-Lindblad | motional dephasing `γ_φ` | … | … | … | … |
| initial-state | prep infidelity `ε_prep` | … | … | … | … |
| stochastic-Hamiltonian | drive-phase `drive_phase_rate` | … | … | … | … |
| **read-out** | **detection `ε_det`** | … | **0** | **0** | **≠0** |
| — | full model | (all) | `I_full` | `L_state,full` | `L_obs,full` |
| — | interaction residual | — | residual | residual | residual |

The detection row's latent columns are **identically 0** (a read-out channel cannot change the quantum state) — the review-1 split made an executable invariant. Layers (ii)–(v) are CL-2026-006 D1's contributions; the layer column is the four Phase-1 nuisance layers + the Hamiltonian signal.

---

## §4 — Output artifacts

- **Budget table** → `numerics/results/sorci_nuisance_budget_<hash>.{json,md}` with full metadata (all `SorciParams`, seeds, code version, commit, cutoff, `truncation_ok`, the model used [secular/full], and the transfer-condition values `λ, |g_md|/ω, ωt`) — committed per Q3. Two budgets: the **scaled headline** and the **²⁷Al⁺ extrapolation** column.
- **Plots** (`viz` extra): `V(t)`/`I(C:M)(t)` per channel; the budget bar chart; the baseline cross-check (numerical `V` vs Sorci Eq. (12)).
- **Example notebook** → `numerics/examples/sorci_module.ipynb` (Phase-3 gate).
- **Feed-forward → CL-2026-006 v0.5** (Phase 4): a *theoretical* D1 decomposition under the declared channel set; verdict revisit + CBG-note softening remain steward/Lock-Key.

---

## §5 — Module API (`tmc_numerics.modules.sorci`)

```python
def build_sorci_system(params: SorciParams, *, secular: bool = True) -> MasterEquationSystem: ...
    # secular=True -> H_sec = ω·0 (clock removed) + g_md σ_z (n̂+½)  [workhorse; any t]
    # secular=False -> free mode ω n̂ + g_md σ_z P̂²                  [scaled-validation model]
    # plus nuisance channels (heating, dephasing), drive noise, and the ReadoutModel (declared).

def sorci_initial_state(params: SorciParams) -> "qt.Qobj": ...

def sorci_visibility(result: EvolutionResult) -> "np.ndarray": ...                 # V_state(t)
def sorci_observed_visibility(result: EvolutionResult, eps_det: float) -> "np.ndarray": ...  # V_obs(t)
def clock_motion_mutual_information(result: EvolutionResult) -> "np.ndarray": ...   # I(C:M)(t), bits

def baseline_visibility_check(params: SorciParams) -> dict: ...
    # numerical V vs Sorci Eq. (12); secular-vs-full agreement (RWA error); returns fit + max deviation.

@dataclass
class NuisanceBudget:
    rows: list; signal: tuple; full: tuple; interaction_residual: tuple
    params: SorciParams; model: str; transfer: dict; metadata: dict

def nuisance_budget(params: SorciParams, *,
                    sweep_ranges: "Mapping[str, Sequence[float]] | None" = None,
                    secular: bool = True) -> NuisanceBudget: ...
    # marginal-from-signal per channel (over sweep_ranges, or single op-point value from params) + full + residual.
```

---

## §6 — Tests implied

- **Baseline validation:** secular `1−V(t) = (ε_m ω_c t)² sinh²(2r)/16` (Sorci Eq. 12) to declared tolerance; full `σ_z P̂²` model agrees with secular within the RWA error at the scaled point (`ωt`≈10). This validates the **derived** `g_md` and the `P_QUAD` convention.
- **Latent invariance under read-out (review-1):** detection `ε_det` leaves `I(C:M)` and `V_state` **exactly** unchanged (`Δ=0`); only `V_obs` changes — an executable assertion, not a global monotonicity claim.
- **Sign diagnostics (benchmark-specific, NOT global invariants):** at the *specified operating point and ranges*, report and check the signs of `ΔI(C:M)`, `ΔL_state`, `ΔL_obs` per channel; do not assert universal monotonicity (heating can alter the signal dynamics; readout is latent-invariant).
- **Transfer conditions:** the module asserts `|g_md|/ω ≪ 1` and `ωt ≫ 1` (and records `λ`) before any scaled→²⁷Al⁺ extrapolation.
- **Budget bookkeeping:** marginals + residual reconstruct the full model; residual → 0 in the small-nuisance limit.
- **Cutoff:** `truncation_ok` holds across all sweep points (cutoff grown if not).
- **Reproducibility:** committed results regenerate from `SorciParams` + seed.

---

## §7 — Resolved decisions (steward, 2026-05-27)

M1 squeezing-as-prep: **confirmed**. M2 marginal+full+residual: **confirmed** (after the latent/observed split). M3: **confirmed + revised** — rotating frame (exact); secular dispersive model is the **experimental-column workhorse**; full `σ_z P̂²` scaled runs validate coefficient + RWA error + `sinh²(2r)`; explicit transfer conditions (§1.3). M4: **confirmed** — scaled headline (`ω_c=10³, ω=10², ε_m=10⁻³, t=0.1, r=1.0`) + extrapolated ²⁷Al⁺ column (`r=2.26`, experimental `λ`); cutoff by `truncation_ok`.

---

## §8 — Module 3b note (sketch; parallel/after)

A dynamical increment over the Phase-2 `iid` infrastructure: each carrier's `ρ_carrier^{(T)}` from a single-carrier pure-dephasing master equation (Phase-1 `evolve`), so `ε = ε(γ_φ, ṅ, t)` is *derived*, not posited; then `R_δ(N, ε)` via `TemporalRecordEnsemble.iid`. To write down before implementation: the parameter ranges (`N`, `γ_φ t`, `δ`) and the load-bearing **einselection caveat** — the temporal pointer is *assumed* einselected (MN §1.1), so 3b is a *candidate* exemplar within the assumed regime (Anti-Claim #6 stays open), propagated verbatim into any v0.5 / MN v0.3 / publication feed-forward. A short 3b addendum precedes its implementation.

---

## §9 — Review resolution (two passes)

One review accepted as-is; the other found 2 Blocking + 2 High + 1 Medium, all resolved here:
- **Blocking — readout/MI conflation:** §3 now splits latent (`I(C:M)`, `V_state`; readout-invariant) from observed (`V_obs`; detection-degraded); detection's latent columns are identically 0.
- **Blocking — M3 transfer under-specified:** §1.3 now states the dimensionless controls (`λ`, `r`, `γ_φ t`, `ṅ t`) and the secular hierarchy (`|g_md|/ω ≪ 1`, `ωt ≫ 1`) that must be preserved for scaled→experimental transfer.
- **High — circular `g_md`:** §1.1 now derives `g_md = −ε_m ω_c/4` from `Ĥ` + the `P_QUAD` convention; the baseline *validates*, not calibrates.
- **High — over-strong monotonicity:** §6 sign checks are benchmark-specific diagnostics; detection latent-invariance (`Δ=0`) is the only sign *assertion*.
- **Medium — mode-mixing:** §0.3 marks the contract D1-minimal (single mode); mode-mixing deferred to a ≥2-mode extension.
- **Minor — `sweeps` naming:** §5 renamed to `sweep_ranges: Mapping[str, Sequence[float]]` (per-channel marginal-sweep ranges).

---

*End of Module 3a contract v0.1 (ACCEPTED + D6-LOCKED). On acceptance the API mirrors into `numerics/README.md` and implementation begins.*
