# Toolkit Module 3b — Open Temporal Instrument: Contract Addendum (proposal)

**Version:** v0.1 (ACCEPTED + D6-LOCKED 2026-05-27)
**Status:** **ACCEPTED — D6-LOCKED.** Mirrored to `numerics/README.md`; implemented in `tmc_numerics.modules.open_instrument`.
**Parent:** `workplans/toolkit-work-plan-v0.1.md` (Phase 3, Module 3b; Anti-Claim #6) + the Module 3a contract §8. Reuses the locked Phase-1 core, Phase-2 `iid` ensemble, and `temporal_redundancy`.

---

## §0 — Scope (short)

Module 3b is the **dynamical bridge** from a single-carrier master equation to the Phase-2 `iid` redundancy machinery. Almost everything already exists: Phase-1 `evolve` produces the single-carrier conditional state; Phase-2 `TemporalRecordEnsemble.iid` + `temporal_redundancy` produce `R_δ(N, ε)`. The only new content is (i) deriving `ε` from the dynamics (§1–§2) and (ii) sweeping it into `R_δ(N, γ_φ t)` curves (§3). The **einselection caveat (§4)** is load-bearing and verbatim-ready for Phase-4 feed-forward.

This is the **candidate worked exemplar for Anti-Claim #6** — *within the assumed regime* (§4). It does **not** resolve Anti-Claim #6.

---

## §1 — Single-carrier master equation

Two-level carriers (work-plan §0.4): `SystemLayout.carriers(1)` (one qubit). The carrier encodes the binary temporal pointer `T ∈ {0,1}` as a phase: conditioned on `T`, the carrier is `clock_superposition(relative_phase = π·T)` → `|+⟩` (T=0) or `|−⟩` (T=1) — orthogonal, perfectly distinguishable at t=0. Pure dephasing (the "reading" decoheres) degrades the distinguishability:

- Generator: `LindbladChannel("carrier_00", ChannelKind.DEPHASING, γ_φ)` → `(γ_φ/2)·D[σ_z]`, coherence `∝ e^{−γ_φ t}` (the Phase-1-validated convention). *(The dephasing's **physical** pointer basis is σ_z; the temporal-bin information lives in the orthogonal σ_x/phase quadrature — what is einselected for the temporal record is **assumed**, §4.)*
- Evolve `|+⟩` under it for time `t` (Phase-1 `evolve`); the conditional states are `ρ_carrier^{(T)}(t) = ½(I ± c·σ_x)` with `c = e^{−γ_φ t}` the surviving **phase-bin (σ_x) coherence**. The two values of `T` give the `±` (the phase flips; the coherence magnitude `c` is common). Both are obtained from a single dephasing evolve — `c = 2|ρ₀₁|` of the evolved `|+⟩`.
- *(Bosonic carriers / heating `ṅ` are out of scope for v0.1: the open-temporal-instrument carriers are two-level, so dephasing is the channel. Amplitude damping is an optional later addition.)*

---

## §2 — ε extraction (the distinguishability → flip probability)

The per-carrier flip probability `ε` (MN §2's `e`) is the **minimum-error discrimination** of the two conditional states under the assumed temporal read-out. For `ρ^{(T)} = ½(I ± c σ_x)` two equivalent measures give `ε`, and the Holevo information is consistent:

> `ε = (1 − c)/2`,  where `c = e^{−γ_φ t}`  ⟹  `ε(γ_φ, t) = (1 − e^{−γ_φ t})/2`.

- **trace distance / Helstrom:** `D(ρ^{(0)}, ρ^{(1)}) = c` ⟹ min-error `½(1 − D) = (1 − c)/2 = ε`.
- **phase-bin projective read-out** (`σ_x` measurement, the *assumed temporal readout basis* — **not** the dephasing's σ_z pointer): flip prob `(1 − c)/2 = ε` (optimal, since the states are `σ_x`-diagonal).
- **Holevo-consistent:** `χ = 1 − h₂(ε)` for equal priors — the classical MI of that optimal read-out (the iid ensemble's `I(1)` at this `ε`); **consistent with, not equal to, `ε`**.

This is the **dynamical increment over MN Appendix A**, which fixed `e` by hand: here `ε = ε(γ_φ, t)` is derived from the carrier's own decoherence. `ε ∈ (0, ½)`: `ε→0` at `t→0` (perfect), `ε→½` at `t→∞` (no information).

**Bridge to the `iid` ensemble.** Feed the **computational-basis** form (a Hadamard rotation of `½(I±cσ_x)`):
`ρ_iid^{(T)} = (1−ε)|T⟩⟨T| + ε|1−T⟩⟨1−T|` — exactly MN §2's product-pole conditional states, now with the *derived* `ε`. Then `TemporalRecordEnsemble.iid({0: ρ_iid^{(0)}, 1: ρ_iid^{(1)}}, n_carriers=N)` and `temporal_redundancy(ens, δ)` give `R_δ(N, ε)` (any N, no 2ᴺ state). *(The rotation is needed because the Phase-2 `iid` read-out is computational/binary, P2; the σ_x pointer basis maps to computational under Hadamard. Equivalent, and keeps the v0.1 fixed pointer basis.)*

---

## §3 — Parameter ranges and regime boundary

- **N sweep:** `N ∈ {4, 8, 16, 32, 64, 128}` (the `iid` representation scales freely; 128 is fine).
- **`γ_φ t` range:** `[0, ~2]` ⟹ `ε ∈ [0, ~0.43]` — spans the redundant plateau through its collapse.
- **deficit `δ`:** `0.10` (headline; the MN §2 value), optionally `0.05`.
- **Output:** `R_δ(N, γ_φ t)` curves — the first quantitative redundant-pole results for *temporal* records (the Module 3b deliverable). Cross-checks the MN §2 product pole at the matching `ε` (e.g. `γ_φ t = ln(1/(1−2·0.20)) = ln(5/3) ≈ 0.51` ⟹ `ε=0.20` ⟹ `R_{0.10}=64/9` at N=64).
- **Artifacts (Phase-3 gate):** the `R_δ(N, γ_φ t)` grid + the undefined-boundary data → `numerics/results/open_instrument_redundancy_<hash>.{json,md}` with reproducibility metadata; an example notebook → `numerics/examples/open_instrument.ipynb`.
- **Regime boundary (where the threshold stops being reached):** `R_δ` is *undefined* once even the full set fails `I(N) ≥ (1−δ)H_T`, i.e. `ε ≥ ε_crit(N, δ)`. `ε_crit` **rises with N** (more independent carriers tolerate more noise). For `δ=0.10, N=64`: undefined at `ε ≳ 0.40` ⟹ `γ_φ t ≳ ln5 ≈ 1.61`. The curves report the `(N, γ_φ t)` boundary explicitly — "a redundant temporal record destroyed by per-carrier nuisance alone, without any change in entanglement structure" (MN §5).

---

## §4 — Einselection caveat (VERBATIM for Phase-4 feed-forward)

> **Einselection caveat.** Module 3b computes `R_δ(N, γ_φ, t)` *conditional on the assumption that the temporal pointer `T` is einselected* (MN v0.2 §1.1). The existence of a dynamically-derived temporal-pointer basis — the temporal analogue of environment-induced superselection — is the hardest part of the Coastline's principal open problem (**Anti-Claim #6**) and is **not** addressed here: it is *assumed*, not derived. Module 3b is therefore a **candidate** worked exemplar of a *redundant temporal record* **within the assumed regime**, not a resolution of Anti-Claim #6, which **remains open**. Whether any such instance counts as *the* worked exemplar that converts Coastline Claim II from analogy to demonstration is a Coastline-level judgement reserved to the steward (Lock-Key).

This block propagates verbatim into MN v0.3, CL-2026-006 v0.5, and any publication derived from Module 3b results (work-plan Phase 4; Anti-Claims A3).

---

## §5 — Module API (`tmc_numerics.modules.open_instrument`)

```python
@dataclass(frozen=True)
class OpenInstrumentParams:
    gamma_phi: float; t: float; n_carriers: int; deficit: float = 0.10

def single_carrier_coherence(gamma_phi: float, t: float, *, cutoff_unused=None) -> float: ...
    # c = 2|ρ₀₁| of |+⟩ evolved under DEPHASING(γ_φ) for t (Phase-1 evolve) = e^{−γ_φ t}

def carrier_distinguishability(gamma_phi: float, t: float) -> float: ...
    # ε = (1 − c)/2  (trace-distance / Helstrom / pointer-projective; all coincide)

def carrier_conditional_states(eps: float) -> "dict[int, qt.Qobj]": ...
    # {0: (1-ε)|0><0|+ε|1><1|, 1: (1-ε)|1><1|+ε|0><0|}  (computational; feeds iid)

def redundancy_at(params: OpenInstrumentParams) -> "RedundancyResult": ...
    # ε = carrier_distinguishability(...); TemporalRecordEnsemble.iid(...); temporal_redundancy(...)

def redundancy_curve(*, gamma_phi: float, t_values, n_values, deficit=0.10) -> dict: ...
    # R_δ(N, γ_φ t) grid + the (N, γ_φ t) undefined boundary; committed to numerics/results/.
```

---

## §6 — Tests implied

- **Bridge consistency:** `single_carrier_coherence(γ_φ, t)` (from `evolve`) matches `e^{−γ_φ t}` to solver tolerance; `carrier_distinguishability` = `(1−e^{−γ_φ t})/2`.
- **D5 cross-link:** at `γ_φ t = ln(5/3)` (`ε=0.20`), `redundancy_at(N=64, δ=0.10).R_delta == 64/9` to the **D5 standard** (exact rational / ≤1e-9, not the looser outer budget) — the dynamical path lands on the validated analytic pole.
- **Monotonic collapse:** `R_δ(N, γ_φ t)` decreases in `γ_φ t` at fixed N; increases in N at fixed `γ_φ t`; the per-carrier-nuisance collapse occurs with **no** entanglement (the carriers are an unentangled product — MN §5).
- **Regime boundary:** `R_δ` is `None` for `ε ≥ ε_crit(N, δ)`; `ε_crit` rises with N.
- **Reproducibility:** committed curves regenerate from `OpenInstrumentParams` + seed.

---

## §7 — Resolved decisions (steward, 2026-05-27)

*B1, B2, B3 confirmed as recommended. Review fixes folded: the `σ_x` read-out is renamed the **assumed temporal / phase-bin readout basis** (not "einselected" — the dephasing's physical pointer is σ_z); Holevo `χ = 1 − h₂(ε)` (consistent with, not equal to, ε); single-carrier label `carrier_00`; artifacts → `numerics/results/` + an example notebook; D5 cross-link held to the ≤1e-9 D5 standard.*

- **B1 — Amplitude damping.** v0.1 = pure dephasing only (`ε` from `γ_φ`). Add carrier amplitude damping (so `ε = ε(γ_φ, Γ, t)`) now, or defer? *(rec: defer; dephasing is the MN §2 mechanism.)*
- **B2 — `δ` set.** Headline `δ=0.10` only, or also `0.05`? *(rec: 0.10 headline, 0.05 as a secondary curve.)*
- **B3 — Einselection-caveat wording.** §4 is verbatim-ready; confirm the wording is what you want propagated into v0.5 / MN v0.3 / publication, since it is the load-bearing honesty statement.

---

*End of Module 3b contract addendum v0.1 (proposal). Short by design — the dynamical bridge is the content; the rest is reused infrastructure. Awaiting steward review.*
