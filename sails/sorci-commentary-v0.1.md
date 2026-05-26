# Visibility, the Right Witness

*On Quantum Proper-Time Signatures in Optical Ion Clocks: A Commentary on Sorci et al.*

| Field | Value |
| --- | --- |
| Version | v0.1 |
| Date | 2026-05-23 |
| Author | U. Warring |
| Affiliation | Physikalisches Institut, Albert-Ludwigs-Universität Freiburg |
| Licence | CC BY-NC-SA 4.0 (authored work) |
| Status | Draft Sail — for internal review |
| Anchoring frameworks | Coastline *Consensus-Emergence of Classical Proper Time* v0.2; Ledger *CL-2026-006* v0.2 |
| Subject paper | G. Sorci, J. Foo, D. Leibfried, C. Sanner, I. Pikovski, *Phys. Rev. Lett.* **136**, 163602 (2026), DOI 10.1103/qhj9-pc2b |

---

## Thesis

The recent proposal by Sorci and colleagues for observing time-dilation-induced clock–motion entanglement in motionally squeezed trapped-ion optical clocks is a valuable operationalisation step in a long-standing conceptual programme. Its central move — locating the genuinely nonclassical signature in interferometric visibility loss rather than in frequency shifts that admit a semiclassical reproduction — is the correct demarcation, and the predicted visibility reduction to roughly 0.93 for state-of-the-art ²⁷Al⁺ parameters places the proposal within striking distance of present capabilities. The proposal as published does not yet close the question its language opens. Under a multipartite-redundancy account of how a classical proper-time variable emerges across microscopic temporal records, the predicted visibility loss is structurally aligned with a partial failure of the conditions under which a single effective τ_cl supports the reduced clock subsystem — exactly the kind of failure mode for which visibility is the appropriate witness. But under any operationally well-defined measure of clock–motion correlation, generic decoherence that destroys the squeezed state's quantum coherence can reduce the witness signal as effectively as the time-dilation Hamiltonian does. The Hamiltonian-level structure is consistent with the proposed quantum-proper-time interpretation; the published evidentiary package is not yet sufficient to make that interpretation experimentally discriminating. The path from operational advance to isolating evidence runs through a master-equation-level open-system analysis with explicit nuisance decomposition, an r-dependence test that separates sinh²(2r) scaling from squeezing-preparation-infidelity scaling, and a null-test protocol that suppresses the predicted contribution while independently bounding the nuisance budget. Visibility, as Sorci and colleagues correctly emphasise, is the right witness; what remains is to make it experimentally isolating.

---

## 1. The operational advance

The conceptual ingredients of the paper — quantum proper time, clock–motion entanglement, interferometric visibility as a witness — are established in the line of work running from Page and Wootters through Zych, Pikovski, Brukner and collaborators. The principal contribution of Sorci et al. is therefore not the introduction of these ideas but their translation into a platform-specific Hamiltonian treatment of trapped-ion optical clocks, an explicit hierarchy of relativistic frequency-shift effects, and the identification of a concrete parameter regime in which a non-trivial witness should become observable.

The Hamiltonian framing is elegant. Beginning from a composite-system action argument due to Zych, Rudnicki and Pikovski, the authors arrive at

> Ĥ = Ĥ_c + ℏω (n̂ + 1/2) − (ℏω / 2mc²) Ĥ_c P̂²

for a harmonically trapped clock atom, with the last term encoding the relativistic clock–motion coupling. The unitary evolution then admits a clean factorisation in which the dominant motional rotation acquires a clock-state-dependent frequency, and the residual squeezing operators capture the higher-order qSODS contributions. This is the cleanest derivation I have encountered of the trapped-ion mass-defect and time-dilation structure, and it serves to organise four distinct frequency shifts — the standard second-order Doppler shift (SODS), the vacuum SODS, the squeezing-induced SODS, and the quantum SODS — within a single formalism.

The most important single insight in the paper, however, is the authors' explicit demarcation between effects that can and cannot be reproduced by a semiclassical description of proper time. They show, to first order in ε_c, that frequency-shift signatures admit the reduction

> ⟨e^(−iω'_c(n̂) t)⟩ ≃ e^(−iω'_c(⟨n̂⟩) t),

so that the clock evolves *as if* under a single classically averaged proper time ⟨τ⟩ ≈ t(1 − ⟨v²⟩/(2c²)). Both the SODS and the vSODS are recovered in this way. The genuine quantum-mechanical content of the proper-time dynamics therefore cannot be located in the frequency shifts themselves. It must be sought in observables that the classical-averaging argument cannot reach.

This is where the visibility argument enters. For an initial motional squeezed state |ξ⟩ = Ŝ(ξ)|0⟩ with squeezing parameter r, the off-diagonal elements of the reduced clock state acquire an interferometric visibility

> V ≃ 1 − (ε_m ω_c t)² sinh²(2r) / 16

which is *not* reproducible by any classical proper-time average. The visibility loss is a genuine multipartite-quantum effect: it arises only because the squeezed motional state and the clock state become entangled through the relativistic clock–motion coupling, and it leaves an imprint on the clock alone that cannot be reabsorbed into a semiclassical description.

For ²⁷Al⁺ parameters (ε_m = 3.3 × 10⁻¹⁸), a 20 MHz trap, t ≃ 1 s, and r ≈ 2.26 — a squeezing level demonstrated in trapped-ion experiments — this yields V ≃ 0.93. That is a striking number. It places the witness within reach of state-of-the-art optical clocks, given simultaneous capabilities in motional squeezing, free-evolution coherence, and detection fidelity.

The demarcation between semiclassically reproducible and genuinely multipartite-quantum signatures is, in my view, the strongest single contribution of the paper. It draws the line in the right place.

## 2. The framework underwriting the appreciation

Read through a multipartite-redundancy account of how a classical proper-time variable emerges across microscopic carriers, the Sorci proposal organises itself naturally. The relevant question is not whether one can write proper time as an operator τ̂(x̂, p̂) — which is a representational choice — but whether the resulting observables carry experimentally isolable content beyond standard energy-dependent dynamical coupling. The visibility witness identified by the authors is, structurally, a candidate for exactly such content.

In a consensus-emergence picture, a classical proper-time variable τ_cl emerges for a physical subsystem only when its microscopic degrees of freedom support a temporal inference that is jointly redundant, stable under partial trace, and compressible to a single coarse-grained parameter. The Sorci protocol exercises exactly two temporal records — the clock internal state and the squeezed motional state — and the framework's predictions for this minimally multipartite case are sharp.

Frequency shifts (SODS, vSODS, sqSODS) remain compressible: a single τ_cl organises the clock's phase evolution adequately, and no inferential improvement is gained by resolving the underlying motional substructure. Visibility loss is precisely the failure of *stability under partial trace*: it is what one observes when the motional record cannot be marginalised away without informational cost. The authors' insistence that visibility is the load-bearing witness amounts, in this language, to the recognition that a classical proper-time variable for the reduced clock subsystem ceases to be a faithful summary of the joint dynamics. That is the conceptually right place to locate a quantum proper-time effect, and it is what makes the proposal worth taking seriously.

The framework also makes one further prediction. Because the Sorci protocol engages only two carriers, the redundancy condition is satisfied in only the weakest possible sense. The witness does not reveal a *strong* failure of classical proper-time emergence — the kind one might expect to encounter in distributed-clock networks across curved spacetime — but the *minimum nontrivial* failure compatible with a coherent multipartite-quantum description. This is a feature, not a limitation: it suggests that Sorci-type experiments and distributed-clock proposals occupy distinct positions on a common ladder, with the former providing the earliest accessible rung.

## 3. The experimental bottleneck

The principal weakness of the proposal as published lies not in its sensitivity claim — which appears defensible — but in its identification of the visibility signal with the time-dilation interpretation. The two are not the same claim. A signal can be measurable without yet being evidentially discriminating, and the gap between the two is the centre of the present work.

Ramsey interferometric visibility is one of the most extensively studied and intensively engineered quantities in atomic and ion physics. It is also vulnerable to a long list of standard nuisance channels. Motional heating during the t ≃ 1 s free-evolution window contributes a fractional visibility loss that scales with the heating rate ṅ and with t. Motional dephasing γ_φ acting on the squeezed state degrades its quantum coherence in a manner that depends sensitively on r — the more strongly squeezed the state, the more fragile it is to any process that does not preserve the squeezing axis. Squeezing-preparation infidelity, both in the initial state and in any state-dependent reversal operations, contributes its own r-dependent visibility reduction. Drive-phase noise during the Ramsey interrogation produces a visibility envelope unrelated to motion. In multi-ion clock architectures such as the ²⁷Al⁺ logic-ion configuration, anomalous mode mixing between the targeted motional mode and other normal modes can imprint phase information that, on partial trace, looks like visibility loss. Detection-side infidelity correlated with the motional state — a common feature of state-dependent fluorescence — closes the loop.

Each of these channels reduces the mutual information between the clock and motional degrees of freedom by reducing the coherent two-mode structure that the time-dilation Hamiltonian would otherwise produce. Under any operationally well-defined measure of clock–motion correlation — mutual information, quantum Fisher information about elapsed time, cross-probe phase mismatch — a generic decoherence channel that destroys the squeezed state's quantum coherence reduces the witness signal as effectively as the unitary entanglement generated by the relativistic coupling. The authors quote a target visibility of V ≃ 0.93. Without an explicit nuisance budget bounding the contributions of the channels listed above, that target cannot be assigned to the time-dilation interpretation in preference to any of several conventional explanations.

This is the central point. The Sorci proposal demonstrates a *sensitivity* regime in which the predicted time-dilation contribution to the visibility loss is large enough to be seen. It does not yet demonstrate a *discriminability* regime in which the contribution can be cleanly separated from generic decoherence. Sensitivity is a necessary condition for an isolating experiment; it is not a sufficient one. "Within reach," when applied to a witness claim, must mean both — and the second of the two is the harder requirement.

## 4. Toward isolating evidence

What would convert the Sorci proposal from a sensitivity argument into a discriminating one? Three specifications appear to be sufficient, and they are platform-general.

*First*, a master-equation-level open-system analysis decomposing the predicted visibility loss into contributions from the unitary time-dilation Hamiltonian and from each named nuisance channel. The required infrastructure exists: Lindblad and stochastic-master-equation simulations of trapped-ion squeezed-state Ramsey protocols are within standard scope, and recent work on driven-dissipative ion-trap systems provides a natural template. The output of such an analysis is a nuisance budget — a quantitative statement of how much of the observed visibility reduction can be attributed to mechanisms that do not depend on the relativistic coupling. The signal must then exceed this budget in a statistically meaningful sense before any visibility loss can be assigned to the time-dilation interpretation.

*Second*, an r-dependence test. The Sorci prediction is that the time-dilation contribution to the visibility loss scales as sinh²(2r) — a particularly aggressive scaling with squeezing strength. Squeezing-preparation infidelity, by contrast, contributes a visibility reduction with a typically different r-dependence, often closer to linear or cubic in r over the accessible range. A measured r-scan that follows sinh²(2r) over a finite range of r, after subtraction of the nuisance budget bounded by the first specification, provides a positive structural test that the time-dilation prediction is operating. A measured r-scan that does not follow sinh²(2r), or that follows it only over a range narrower than the model's region of validity, places the interpretation in difficulty.

*Third*, a null-test protocol. The natural toggle is the dimensionless parameter ε_m = ℏω/(mc²), which can be reduced by lowering the trap frequency, increasing the ion mass, or lowering the clock frequency. The predicted time-dilation contribution to the visibility loss should fall accordingly, while the nuisance channels typically do not scale with ε_m. A clean null test compares the visibility reduction observed in the signal configuration with that observed in a configuration in which ε_m has been suppressed by some calibrated factor. The difference, after correcting for any associated and independently bounded changes in the nuisance channels under the parameter shift, places a direct experimental bound on the time-dilation contribution. The independence assumption is critical: a null test is only as clean as the model that supports its independence claim, and that model must itself be defended.

None of the three specifications requires capabilities beyond those already demonstrated, in isolation, in trapped-ion clock laboratories. Their joint demonstration would constitute, in my view, the first experimentally discriminating observation of a quantum proper-time signature in any atomic clock.

## 5. Closing posture

The path from a proposed witness to an isolating witness is, in atomic physics generally, the harder half of the work. The strength of Sorci, Foo, Leibfried, Sanner and Pikovski's contribution is that they have placed the proposed witness on a footing solid enough for that harder half to begin. The demarcation they draw between semiclassically reproducible frequency shifts and genuinely multipartite-quantum visibility loss is the right demarcation; the experimental parameters they identify are realistic; and the conceptual programme they advance is one worth pursuing.

The present commentary should not be read as a critique of the conceptual programme. It is a request that the witness claim be raised to the evidentiary standard the programme deserves. Visibility, as Sorci and colleagues correctly emphasise, is the right witness; what remains is to make it experimentally isolating.

---

## Anchoring Frameworks

This Sail is anchored to and derives its interpretive structure from:

- *Consensus-Emergence of Classical Proper Time*, Coastline v0.2 (Warring, 2026-05-23). The framework underwriting §2 of this Sail. The Coastline's Claim II (redundancy, stability, compressibility) provides the language in which the structural alignment of the Sorci visibility witness is articulated, and its Falsifiability §Weak provides the discriminability requirement load-bearing in §3.
- *Breakwater Claim Analysis Ledger Entry CL-2026-006*, v0.2 (Warring, 2026-05-23). The Ledger entry that classifies the Sorci interpretive claim C2 as UNDERDETERMINED against Coastline v0.2 under the declared evaluating measure I(C : M). The three specifications offered in §4 of this Sail are restatements, in journal-comment prose, of the Ledger's discriminant conditions D1, D3, and D2 respectively.

Both anchoring documents are issued under Local Stewardship. Their version numbers are part of the citation; this Sail's claims are tied to them and would need to be re-evaluated against any later versions.

## Acknowledgements

I am grateful to D. Leibfried for many discussions during my time at NIST Boulder (2010–2012), which shaped my understanding of trapped-ion clock metrology, and to C. Sanner for ongoing exchanges on precision-measurement programmes. The present commentary takes its appreciative-but-demanding posture in part from those relationships.

## Version History

| Version | Date | Notes |
| --- | --- | --- |
| v0.1 | 2026-05-23 | Initial draft. Five-section structure built on Coastline v0.2 and Ledger CL-2026-006 v0.2. Tone: appreciative-clarifying-demanding-not-dismissive. For internal review prior to any external circulation. |

---

*This Sail is a commentary issued under Local Stewardship. It does not represent the position of any institution. Citations of Sorci et al. and of related literature use standard scientific conventions; citations of anchoring Harbour frameworks use Local-Stewardship version conventions.*
