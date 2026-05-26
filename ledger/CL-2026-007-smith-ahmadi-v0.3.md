# Breakwater Claim Analysis Ledger — Entry CL-2026-007

*Quantum Time Dilation as a Witness of Nonclassical Proper Time (Smith & Ahmadi 2020)*

| Field | Value |
| --- | --- |
| Ledger ID | CL-2026-007 |
| Date | 2026-05-26 |
| Author | U. Warring |
| Schema | Breakwater Claim Analysis Ledger v1.0-rc |
| Classification | **UNDERDETERMINED** |
| Framework reference | Consensus-Emergence of Classical Proper Time, Coastline **v0.4** |
| Declared evaluating measure | Fisher information about elapsed proper time, F[τ] = 4⟨(ΔH_clock)²⟩ (Claim IV anchor; registration role — see §Declared Evaluating Measure) |
| Source | A. R. H. Smith & M. Ahmadi, *Quantum clocks observe classical and quantum time dilation*, *Nat. Commun.* **11**, 5360 (2020), DOI 10.1038/s41467-020-18264-4 |
| Version | v0.3 |
| Predecessor | v0.2 (2026-05-26) |

---

## Endorsement Marker

This ledger entry is issued under Local Stewardship by U. Warring. It is a classification of an external scientific claim against a named Harbour framework. It does not assert that the external claim is correct or incorrect in the framework-independent sense; it asserts only how the claim sits relative to the framework's structural commitments, given the declared evaluating measure. Authority derives from explicit framework selection, declared measure, and stated discriminant conditions, not from institutional endorsement.

---

## The External Claim

Smith & Ahmadi (2020) extend the Page–Wootters conditional-probability formalism to relativistic particles carrying an internal clock. Proper time is encoded as a covariant POVM (not a self-adjoint operator); the clock mass `M_clock = m + H_clock/c²` is the self-adjoint observable, and a Helstrom–Holevo argument yields the time–energy/mass uncertainty relation `ΔM_clock · ΔT_clock ≥ 1/(2c²)`, with optimal covariant clocks saturating the quantum Cramér–Rao bound at Fisher information `F[τ] = 4⟨(ΔH_clock)²⟩` (their Eq. 12).

For a clock A whose centre-of-mass (COM) is prepared in a **coherent superposition** of two localized momentum wave packets, `|ψ_A^cm⟩ ∝ cosθ |p̄_A⟩ + e^{iφ} sinθ |p̄'_A⟩` (their Eq. 22), the average proper time read by A conditioned on a reference clock B reading τ_B is (their Eq. 23):

> ⟨T_A⟩ = (γ_C⁻¹ + γ_Q⁻¹) τ_B,

where (their Eqs. 24–25):
- **`γ_C⁻¹`** is *the time dilation of a clock in a classical **statistical mixture** of momenta p̄_A, p̄'_A with probabilities cos²θ, sin²θ* — the classical term, which includes the momentum-variance contributions; and
- **`γ_Q⁻¹`** is *the **quantum contribution***, which depends on the superposition phase φ (through cos φ sin 2θ) and **vanishes for a classical mixture** — explicitly, `γ_Q⁻¹ = 0` when θ ∈ {0, π/2} (no superposition) or p̄_A = p̄'_A.

The claim has two components, separated here for ledger purposes:

- **C1 (effect claim):** within the relativistic Page–Wootters formalism, a clock in a COM momentum *superposition* acquires the computable, coherence-dependent correction `γ_Q⁻¹` beyond the classical (statistical-mixture) value. A feasibility estimate is offered (⁸⁷Rb clocks, branch velocities ≈ 5 and 15 m/s, θ = 3π/4, φ = 0 → `γ_Q⁻¹ ≈ 10⁻¹⁵`; with 10⁻¹⁴ s clock resolution, a ~10 s coherence time of the momentum superposition is required, comparable to demonstrated atom-interferometer coherence).
- **C2 (interpretive claim):** this correction is a *genuinely quantum* time-dilation effect — distinct from classical time dilation and from a classical statistical mixture — characterising a regime in which a single classical proper-time value no longer describes the clock.

The Ledger evaluates **C2** against the Coastline. C1 is a derivation/feasibility statement reviewable on its own technical merits; it is not the object of this entry.

---

## Declared Evaluating Measure

Per the Claim IV measure-registration discipline (Coastline v0.4; carried forward from the Scout horizon signal on measure indeterminacy registered for CL-2026-006), this entry declares its evaluating measure upfront:

> **Fisher information about elapsed proper time, F[τ] = 4⟨(ΔH_clock)²⟩.**

Justification and scope of the choice: Fisher information is the quantity the authors themselves derive (Eq. 12) as the bound their optimal covariant clocks saturate, and it sets the temporal resolution required to resolve a correction as small as `γ_Q⁻¹ ≈ 10⁻¹⁵` — it is therefore the natural *registered* anchor for the feasibility/discriminability question this entry turns on. **A caveat, registered explicitly (cf. v0.2 revision):** F[τ] is a single-clock estimability bound and does *not* by itself isolate the coherence-dependent contribution `γ_Q⁻¹`, which is a two-clock (A-vs-B) cross-probe quantity. The active classification driver below is therefore the *experimental discriminability of `γ_Q⁻¹`* (Coastline Claim III), for which **cross-probe mismatch** (γ_Q⁻¹ itself) and **mutual information** `I(clock : COM)` (the measure declared for CL-2026-006) are the more direct anchors. Fisher information is retained as the registered measure because it governs the resolution budget; the choice is registered and may be revised in a subsequent entry.

---

## Classification Analysis

### Engagement with Coastline v0.4 Claim II (Redundancy, Stability, Compressibility)

**Redundancy.** The setting engages *two* temporal records: the clock's internal state (carrying phase through `H_clock`) and the COM momentum (modulating the clock's rate through the Lorentz factor). This is the minimum nontrivial bipartite case — two carriers, not many — and, in the v0.3 "many vs redundant" terminology, it is explicitly **not redundant**: a single clock and a single COM channel, no independent compatible copies. **Status under Claim II.1: minimally engaged; not redundant.**

**Stability.** In the momentum-localized (and in the classical-mixture) regime the inferred proper time is a stable, well-defined value. In the coherent-superposition regime the clock's reduced proper-time content carries the additional `γ_Q⁻¹` that no single classical value reproduces. **Status under Claim II.2: failing in the coherent-superposition regime — the framework's predicted failure mode.**

**Compressibility.** This is where the v0.1 analysis was *wrong* and is corrected here. The paper's own decomposition settles the superposition-vs-mixture question at the theoretical level: `γ_C⁻¹` (Eq. 24) is, by construction, the value of a classical statistical mixture — it is **compressible** to a shifted classical `τ_cl`. The quantum term `γ_Q⁻¹` (Eq. 25) is the part that a classical mixture does **not** reproduce; it is coherence-dependent (a function of the relative phase φ) and vanishes for a mixture or for no superposition. Therefore the coherent-superposition regime is **genuinely non-compressible** at the level of the theory: it cannot be organised by any single classical proper-time parameter. **Status under Claim II.3: the classical part is compressible; the quantum part `γ_Q⁻¹` is non-compressible — a genuine Claim II.3 failure in the coherent regime.**

### Verdict on the structural claim

Contrary to the v0.1 reading, the paper **does** establish the superposition-vs-mixture distinction theoretically: `γ_Q⁻¹` is constructed as the coherence-dependent contribution that vanishes for a classical mixture (Eqs. 24–25; Fig. 1). At the level of the formalism, C2's structural content — that the coherent-superposition regime is not describable by a single classical proper time — is therefore **framework-compatible**, exactly as the Hamiltonian-level structural claim of CL-2026-006 is. The Claim II.2/II.3 failure is present in the theory and has the predicted asymmetry (classical part compressible, quantum part not).

What remains open is **not** the theoretical distinction but the **experimental witness**: whether a measurement can isolate the `γ_Q⁻¹` contribution from the laboratory nuisances that also reduce or mimic a small clock-comparison signal.

### Discriminability gap (load-bearing for classification)

The Coastline's Claim III (and the Weak Falsification clause, v0.3 §Falsifiability) requires that a proposed *witness* of nonclassical proper time be discriminable from channels that reduce the signal by ordinary means. Smith & Ahmadi give a feasibility estimate (C1) but not a witness package that separates the `γ_Q⁻¹` contribution from:

1. Momentum-superposition **preparation infidelity** (e.g. imperfect coherent momentum beam-splitting), which is itself θ- and φ-dependent and so can mimic the structural signature.
2. **Dephasing / decoherence of the COM superposition** over the ~10 s window, which suppresses exactly the coherence that `γ_Q⁻¹` depends on.
3. **Clock-readout and state-verification errors** at the 10⁻¹⁴ s resolution.
4. **Finite coherence time** relative to the required interrogation.

Under any of the operational anchors (Fisher resolution budget, cross-probe `γ_Q⁻¹`, or `I(clock : COM)`), these channels degrade the measured quantum-time-dilation signal without invoking the relativistic coupling. The published proposal does not provide this separation. The entry is therefore framework-underdetermined **at the experimental-witness level** — the same location as CL-2026-006, not (as v0.1 mistakenly held) at the theoretical level.

---

## Classification: **UNDERDETERMINED**

The Smith & Ahmadi claim C2 is classified **UNDERDETERMINED** against Coastline v0.4.

**The theoretical superposition-vs-mixture distinction is established by the paper** (`γ_Q⁻¹` is the coherence-dependent term, Eqs. 24–25, vanishing for a classical mixture); at the formalism level the coherent-superposition regime is a genuine, non-compressible Claim II failure, and C2's structural content is framework-compatible. **What is underdetermined is the experimental witness:** the published proposal does not supply a nuisance-separated measurement that isolates the `γ_Q⁻¹` contribution from preparation infidelity, COM dephasing, and readout/verification errors. The classification weighs the present sufficiency of the *witness*, not the conceptual content.

The classification can move to COMPATIBLE on satisfaction of the discriminant conditions below.

---

## Discriminant Conditions

The classification UNDERDETERMINED may be upgraded to **COMPATIBLE** on demonstration of:

**D1.** A nuisance-channel decomposition of the measured A-vs-B time-dilation signal isolating the `γ_Q⁻¹` (coherence) contribution from (i) momentum-superposition preparation infidelity, (ii) COM dephasing/decoherence, (iii) clock-readout/state-verification error, and (iv) finite-coherence-window effects.

**D2.** A structural null test exploiting `γ_Q⁻¹`'s *known* dependences: it vanishes for θ ∈ {0, π/2} and for p̄_A = p̄'_A, and varies with the relative phase φ and momentum splitting (Eqs. 24–25; Fig. 2). Toggling θ (or φ, or the momentum difference) suppresses `γ_Q⁻¹` while leaving `γ_C⁻¹` and most nuisance channels comparatively unchanged; the difference bounds the quantum contribution — *provided the toggled parameter's effect on the nuisance channels is independently bounded or modelled* (the same independence caveat as CL-2026-006 D2).

**D3.** A feasibility/statistics analysis showing the *isolated* `γ_Q⁻¹` (≈ 10⁻¹⁵ at the quoted ⁸⁷Rb parameters), not merely the raw signal, is resolvable at 10⁻¹⁴ s resolution and ~10 s coherence, with the nuisance budget bounded.

The classification may be downgraded to **INCONSISTENT** (as a witness claim) on demonstration that:

**D−1.** The measured signal attributed to `γ_Q⁻¹` is fully accounted for by the bounded nuisance budget (preparation/dephasing/verification), with no statistically significant residual attributable to the coherent quantum contribution.

The classification may also be re-evaluated under a *different* declared measure in a separate entry (e.g. cross-probe `γ_Q⁻¹` directly, or `I(clock : COM)`).

---

## Notes for Downstream Use

**Relation to CL-2026-006 (Sorci et al.).** The two entries are complementary, and — after the v0.2 correction — they sit at the *same* location: both are framework-compatible at the level of the theory/Hamiltonian and **UNDERDETERMINED at the experimental-witness level**, each lacking a nuisance-separated demonstration. Both turn on a coherence-sensitive measurement: in Smith & Ahmadi the coherence-dependent quantity is `γ_Q⁻¹` (defined to vanish for a mixture); in Sorci et al. it is the squeezing-induced visibility loss. A clock interferometric-visibility or coherence-isolating protocol is the natural experimental bridge for both.

**On the choice of measure (v0.2 correction).** v0.1 declared Fisher information and suggested the classification was "stable across anchors" in a way that implied the registration discipline was doing classificatory work. That was an overclaim: Fisher F[τ] is a single-clock estimability/resolution bound and is *not* the quantity that carries C2's coherence content (which is the cross-probe `γ_Q⁻¹`). Fisher is retained here as the *registered* anchor (it governs the resolution budget for resolving `γ_Q⁻¹`), but the active classification driver is the experimental discriminability of `γ_Q⁻¹` (Claim III). The measure-registration discipline remains useful as a transparency device; this entry no longer claims it as evidence in itself.

**Relation to deferred items in Coastline v0.4.** L₀-scale entry; the CCUF bridge (L₁) remains deferred and uncoupled. Exercises the v0.4 "many vs redundant" terminology (clock–COM is bipartite and non-redundant); does not engage the redundant-temporal-record open problem.

---

## Version History

| Version | Date | Notes |
| --- | --- | --- |
| v0.1 | 2026-05-26 | Initial classification, anchored to Coastline v0.3. UNDERDETERMINED. **Superseded:** v0.1 located the discriminability gap at the *theoretical* level, asserting the paper did not settle whether `γ_Q⁻¹` is coherence-dependent. That was incorrect (see v0.2). |
| v0.3 | 2026-05-26 | **Re-anchored from Coastline v0.3 to Coastline v0.4** (version-consistency, matching CL-2026-006 v0.3 and CL-2026-008 v0.2). **No verdict or discriminant change:** UNDERDETERMINED, Fisher registered as resolution anchor, conditions D1–D3 / D−1 all stand. v0.4's only addition over v0.3 — the GR-regime *Regime of Validity* — is **irrelevant to this bipartite, SR/weak-field, non-curvature case**; the v0.3 Claim II content (many-vs-redundant, transplant gap) the entry already used carries into v0.4 unchanged. Version self-references updated v0.3→v0.4. |
| v0.2 | 2026-05-26 | Correction following Verifier review and re-reading of the source (Eqs. 22–25, Fig. 1–2). The paper **does** establish the superposition-vs-mixture distinction theoretically: `γ_C⁻¹` is the classical-mixture value (Eq. 24) and `γ_Q⁻¹` is the coherence-dependent quantum term (Eq. 25), which vanishes for a mixture. Compressibility analysis corrected accordingly (classical part compressible, quantum part not — a genuine theory-level Claim II.3 failure). Crux **relocated** from the theoretical distinction to the **experimental witness** (isolating `γ_Q⁻¹` from preparation/dephasing/verification nuisances), aligning the entry's gap with CL-2026-006. Discriminant conditions D1–D3 rewritten as experimental/nuisance-isolation conditions (D2 now exploits `γ_Q⁻¹`'s known vanishing at θ ∈ {0, π/2}). Fisher "stable across anchors" overclaim withdrawn; Fisher retained as registered resolution anchor with an explicit caveat. Classification unchanged (UNDERDETERMINED). |

---

*This ledger entry is a framework-relative classification of an external scientific claim. It does not assert correctness or incorrectness of the claim in the framework-independent sense. The declared evaluating measure is part of the classification and may be revised in subsequent entries.*
