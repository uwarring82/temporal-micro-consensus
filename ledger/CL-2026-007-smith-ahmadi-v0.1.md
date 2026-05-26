# Breakwater Claim Analysis Ledger — Entry CL-2026-007

*Quantum Time Dilation as a Witness of Nonclassical Proper Time (Smith & Ahmadi 2020)*

| Field | Value |
| --- | --- |
| Ledger ID | CL-2026-007 |
| Date | 2026-05-26 |
| Author | U. Warring |
| Schema | Breakwater Claim Analysis Ledger v1.0-rc |
| Classification | **UNDERDETERMINED** |
| Framework reference | Consensus-Emergence of Classical Proper Time, Coastline **v0.3** |
| Declared evaluating measure | Fisher information about elapsed proper time, F[τ] = 4⟨(ΔH_clock)²⟩ (Claim IV anchor) |
| Source | A. R. H. Smith & M. Ahmadi, *Quantum clocks observe classical and quantum time dilation*, *Nat. Commun.* **11**, 5360 (2020), DOI 10.1038/s41467-020-18264-4 |
| Version | v0.1 |
| Predecessor | (none) |

---

## Endorsement Marker

This ledger entry is issued under Local Stewardship by U. Warring. It is a classification of an external scientific claim against a named Harbour framework. It does not assert that the external claim is correct or incorrect in the framework-independent sense; it asserts only how the claim sits relative to the framework's structural commitments, given the declared evaluating measure. Authority derives from explicit framework selection, declared measure, and stated discriminant conditions, not from institutional endorsement.

---

## The External Claim

Smith & Ahmadi (2020) extend the Page–Wootters conditional-probability formalism to relativistic particles carrying an internal clock. Proper time is encoded as a covariant POVM (not a self-adjoint operator); the clock mass `M_clock = m + H_clock/c²` is the self-adjoint observable, and a Helstrom–Holevo argument yields the time–energy/mass uncertainty relation `ΔM_clock · ΔT_clock ≥ 1/(2c²)`, with optimal covariant clocks saturating the quantum Cramér–Rao bound at Fisher information `F[τ] = 4⟨(ΔH_clock)²⟩`.

In this formalism, the average proper time read by a clock whose centre-of-mass (COM) is in a superposition of localized momentum wave packets is

> ⟨T⟩ = (γ_C⁻¹ + γ_Q⁻¹) τ_ref,

where `γ_C⁻¹` reproduces the ordinary special-relativistic ("classical") time dilation set by the mean Lorentz factor, and `γ_Q⁻¹` is an additional correction the authors term **quantum time dilation**, set by the spread of the COM momentum.

The claim has two components, separated here for ledger purposes:

- **C1 (effect claim):** within the relativistic Page–Wootters formalism, a clock in a COM momentum superposition acquires the computable correction `γ_Q⁻¹` to its average proper-time reading beyond the classical value. A feasibility estimate (⁸⁷Rb clocks, branch velocities ≈ 5 and 15 m/s, `γ_Q⁻¹ ≈ 10⁻¹⁵`, ~10 s coherence at 10⁻¹⁴ s resolution) is offered.
- **C2 (interpretive claim):** this correction is a *genuinely quantum* time-dilation effect — the clock observes "quantum time dilation" distinct from classical time dilation, characterising a regime in which a single classical proper-time value no longer describes the clock.

The Ledger evaluates **C2** against the Coastline. C1 is a derivation reviewable on its own technical merits; it is not the object of this entry.

---

## Declared Evaluating Measure

Per the Claim IV measure-registration discipline (Coastline v0.3; carried forward from the Scout horizon signal on measure indeterminacy registered for CL-2026-006), this entry declares its evaluating measure upfront:

> **Fisher information about elapsed proper time, F[τ] = 4⟨(ΔH_clock)²⟩, as it distributes over the clock's internal degree of freedom and its centre-of-mass momentum degree of freedom.**

Justification of choice: Smith & Ahmadi's result is fundamentally about the *estimability and variance* of a clock's proper-time reading under a momentum distribution — `γ_Q⁻¹` is a variance functional of the COM momentum, and Fisher information is the canonical measure of temporal estimability, derived explicitly by the authors as the bound their optimal clocks saturate. Mutual information `I(clock : COM)` (the measure declared for CL-2026-006) and cross-probe mismatch are the available alternative anchors; Fisher information is selected here because the claim is structurally about *how sharply elapsed proper time can be inferred* given a momentum spread. Declaring a *different* Claim IV anchor than CL-2026-006 also road-tests the framework's measure pluralism: a robust classification should be statable under more than one anchor. The choice is registered; it does not foreclose re-evaluation under another anchor in a subsequent entry.

---

## Classification Analysis

### Engagement with Coastline v0.3 Claim II (Redundancy, Stability, Compressibility)

**Redundancy.** The setting engages *two* temporal records: the clock's internal state (carrying phase information through `H_clock`) and the COM momentum (modulating the clock's rate through the Lorentz factor). Under Coastline v0.3, the COM qualifies as a temporal record because its state co-determines the elapsed proper time the clock reads. This is the minimum nontrivial bipartite case — two carriers, not many — and, in the v0.3 "many vs redundant" terminology, it is explicitly **not redundant**: there is a single clock and a single COM channel, no independent compatible copies. **Status under Claim II.1: minimally engaged; not redundant.**

**Stability.** In the momentum-localized (classical) regime, the inferred proper time is stable and equals the classical SR value. In the superposition regime, tracing out the COM yields a clock reading shifted by `γ_Q⁻¹`; whether this constitutes a *failure* of stability under marginalisation, or merely a stable-but-shifted value, is the load-bearing question (below). **Status under Claim II.2: regime-dependent; the superposition regime is the candidate failure.**

**Compressibility.** This is the crux. The classical regime is compressible to a single `τ_cl` (the SR-dilated value). The published result computes `γ_Q⁻¹` as a functional of the COM momentum *distribution*. **The decisive question for C2 is whether `γ_Q⁻¹` is coherence-dependent** — i.e. whether a coherent momentum *superposition* yields a correction that a classical momentum *mixture with the identical distribution* does not. If the mean correction is reproduced by a classical mixture, then under the framework it is **compressible** to a shifted classical proper-time value (a re-labelled `τ_cl`), and it is *not* a structural failure of Claim II. If instead the observable content requires coherence, the superposition regime is genuinely non-compressible. The mean-value result `⟨T⟩ = (γ_C⁻¹ + γ_Q⁻¹)τ_ref` does not, on its own, settle this. **Status under Claim II.3: undetermined pending a superposition-vs-mixture distinction.**

### Verdict on the structural claim

C2 asserts that the quantum time-dilation correction is a genuinely nonclassical proper-time effect. Under the framework, this is equivalent to asserting that the correction is *not compressible* to a shifted classical `τ_cl` — that it marks a genuine Claim II failure rather than a classical statistical average over momenta. The published derivation establishes the correction's existence and magnitude (C1) but evaluates it as a mean over the momentum distribution; it does not exhibit an observable that distinguishes a coherent superposition from a classical mixture with the same distribution. The framework therefore cannot yet classify C2 as COMPATIBLE.

### Discriminability gap (load-bearing for classification)

The Coastline's Claim III (and the Weak Falsification clause, v0.3 §Falsifiability) requires that any proposed witness of nonclassical proper time be discriminable from descriptions that admit a classical reproduction. Here the relevant "nuisance" is not laboratory decoherence but a *classical statistical ensemble of momenta*: such an ensemble also has a momentum variance and would, by the same mean-value computation, contribute a correction to ⟨γ⟩. The available Claim IV anchors — Fisher information included — are computed from the state's statistics and do not, by themselves, certify that the correction is coherence-dependent rather than mixture-reproducible. Smith & Ahmadi's analysis does not supply this separation. Under the declared measure F[τ], the entry is therefore framework-underdetermined.

---

## Classification: **UNDERDETERMINED**

The Smith & Ahmadi claim C2 is classified **UNDERDETERMINED** against Coastline v0.3 under the declared evaluating measure F[τ].

**The relativistic Page–Wootters effect (C1) is established and framework-legible; the interpretive elevation to "genuinely quantum time dilation" (C2) is framework-underdetermined.** The structural reading is real: the bipartite clock–COM coupling is exactly the minimal (non-redundant) temporal-record structure the framework describes, and the superposition regime is the candidate Claim II failure. But the framework requires that a nonclassical proper-time effect be non-compressible — discriminable from a classical momentum mixture — and the published mean-value result does not establish that `γ_Q⁻¹` is coherence-dependent.

The classification can move to COMPATIBLE on satisfaction of the discriminant conditions below.

---

## Discriminant Conditions

The classification UNDERDETERMINED may be upgraded to **COMPATIBLE** on demonstration of:

**D1.** A coherence-dependence result: that the quantum time-dilation correction (or some derived observable of the clock) **differs between a coherent COM momentum superposition and a classical mixture with the identical momentum distribution**. This is the framework's non-compressibility requirement made operational.

**D2.** A coherence-sensitive observable — e.g. a reduction of clock interferometric visibility, or a quantum-Fisher-information gap over the classical-mixture value — that realises the D1 distinction in a measurement, and is discriminable from ordinary dephasing of the clock or COM.

**D3.** A feasibility/statistics analysis showing the D1–D2 distinction (not merely the mean `γ_Q⁻¹`) is resolvable at the quoted parameters (⁸⁷Rb-class clocks, ~10 s coherence, 10⁻¹⁴ s resolution), with the nuisance budget bounded.

The classification may be downgraded to **INCONSISTENT** (as a nonclassicality claim) on demonstration that:

**D−1.** The full observable content of the quantum time-dilation correction is reproduced by a classical momentum mixture with the same distribution — i.e. `γ_Q⁻¹` and all derived clock observables are compressible to a shifted classical `τ_cl`. Under the framework this is the *expected* behaviour of a compressible consensus variable; it would refute C2's nonclassicality assertion while *confirming* the framework's compressibility prediction (Claim II.3).

The classification may also be upgraded under a *different* declared evaluating measure in a separate entry; selecting F[τ] here does not foreclose mutual-information- or cross-probe-anchored re-evaluations.

---

## Notes for Downstream Use

**Relation to CL-2026-006 (Sorci et al.).** The two entries are complementary halves of one question. Smith & Ahmadi supply the *theoretical* relativistic Page–Wootters scaffold; Sorci et al. supply a candidate *experimental* witness (trapped-ion visibility loss). Crucially, the discriminant that CL-2026-007 lacks — a coherence-dependent, superposition-vs-mixture observable — is exactly what the Sorci visibility witness (CL-2026-006) is structured to provide. A clock interferometric-visibility measurement is the natural bridge: it is coherence-sensitive where the mean `γ_Q⁻¹` is not. Both entries presently sit at UNDERDETERMINED, and both upgrade through the same kind of evidence.

**On the choice of measure.** This entry deliberately declares Fisher information where CL-2026-006 declared mutual information. The classification is robust to the choice: under either anchor the gap is the same (the framework's compressibility/discriminability requirement is not met by a mean-value or statistics-only result). This stability across anchors is itself weak evidence that the measure-registration discipline (Coastline v0.3 deferred candidate) is not merely bookkeeping.

**Relation to deferred items in Coastline v0.3.** This entry classifies a claim at the L₀ (microscopic) scale; the CCUF bridge (L₁) remains deferred and uncoupled here. The entry exercises the v0.3 "many vs redundant" terminology (the clock–COM channel is bipartite and non-redundant) but does not engage the redundant-temporal-record open problem.

---

## Version History

| Version | Date | Notes |
| --- | --- | --- |
| v0.1 | 2026-05-26 | Initial classification, anchored to Coastline v0.3. UNDERDETERMINED under declared measure F[τ] = 4⟨(ΔH_clock)²⟩. C1/C2 decomposition; engagement with Claim II (redundancy minimally engaged / non-redundant, stability regime-dependent, compressibility the crux); discriminant conditions D1–D3 (upgrade to COMPATIBLE) and D−1 (downgrade to INCONSISTENT), all turning on a superposition-vs-classical-mixture distinction. Complementary to CL-2026-006: the coherence-dependent discriminant CL-2026-007 lacks is what the Sorci visibility witness supplies. |

---

*This ledger entry is a framework-relative classification of an external scientific claim. It does not assert correctness or incorrectness of the claim in the framework-independent sense. The declared evaluating measure is part of the classification and may be revised in subsequent entries.*
