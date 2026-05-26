# Breakwater Claim Analysis Ledger — Entry CL-2026-008

*Distributed Entanglement-Enhanced Clock-Network Proposals as Multipartite Witnesses of Quantum Proper Time (Covey–Pikovski–Borregaard 2025; Fromonteil et al. 2025)*

| Field | Value |
| --- | --- |
| Ledger ID | CL-2026-008 |
| Date | 2026-05-26 |
| Author | U. Warring |
| Schema | Breakwater Claim Analysis Ledger v1.0-rc |
| Classification | **UNDERDETERMINED** |
| Framework reference | Consensus-Emergence of Classical Proper Time, Coastline **v0.3** |
| Declared classification anchor | Cross-probe mismatch (Covey's three-node beat-note residual Δω) |
| Declared resolution anchor | Quantum Fisher information / coherence-time budget (N-scaling; τ_dec) |
| Sources | J. P. Covey, I. Pikovski, J. Borregaard, *PRX Quantum* **6**, 030310 (2025), DOI 10.1103/q188-b1cr; C. Fromonteil *et al.*, *Non-local mass superpositions and optical clock interferometry in atomic ensemble quantum networks*, arXiv:2509.19501 (2025) |
| Version | v0.1 |
| Predecessor | (none) |

---

## Endorsement Marker

This ledger entry is issued under Local Stewardship by U. Warring. It is a classification of an external scientific claim against a named Harbour framework. It does not assert that the external claim is correct or incorrect in the framework-independent sense; it asserts only how the claim sits relative to the framework's structural commitments, given the declared evaluating measures. Authority derives from explicit framework selection, declared measure, and stated discriminant conditions, not from institutional endorsement.

---

## The External Claim

This entry classifies a **class** of proposals rather than a single paper, because the two current representatives diverge in protocol and in the GR effect they target while sharing the structural feature the framework cares about. (This framing follows the guardrail that, where representatives diverge, the claim be stated as the class, not as one paper.)

> **Distributed, entanglement-enhanced atomic clock / ensemble network proposals can probe quantum proper-time and general-relativistic effects by distributing entangled states across spatially separated nodes at different gravitational potential.**

Two instances:

- **Covey, Pikovski & Borregaard (2025).** Three ¹⁷¹Yb atomic-processor nodes at elevations `d_j = jd` share a **W state** `|W⟩ = (1/√3)(|agg⟩ + |gag⟩ + |gga⟩)` (Eq. 2). Each node holds a clock record `|c(τ_i)⟩ = (1/√2)(|a⟩ + e^{−iΔEτ_i/ℏ}|b⟩)`. A nonlocal Fourier-basis measurement (Eq. 6) yields pairwise beat notes `ω₁₂, ω₂₃, ω₁₃` (Eqs. 7–9). To leading (Newtonian) order `ω₁₂ ≈ ω₂₃`; **spacetime curvature appears only in the higher-order residual** `Δω = ω₁₂ − ω₂₃ ≈ 2 (ΔEGM/ℏc²)(d²/R³)` (Eq. 10), resolvable for a "wall time" `T ≈ 1/Δω` (Eq. 11; ~0.02 Hz, T ≈ 500 s, single-atom T₂ ≈ 50 s at d = 1 km; N-atom GHZ "superatoms" amplify by N). Explicitly framed as a test of linearity, unitarity, and the Born rule in curved spacetime.
- **Fromonteil et al. (2025).** N-atom ensemble nodes with mass operator `M̂_n = Nm + (m_eg/2)Σ σ_z^(i)` evolve under `Ĥ = Σ_n (M̂_n c² + M̂_n φ(r_n))` (Eq. 7), the gravitational redshift coupling each node's location to its internal energy. **Non-local mass superpositions** `|Ψ⟩ = Σ_M Ψ_M |M⟩_A ⊗ |M'⟩_B ⊗ …` (Eq. 6) — entangled across nodes — emulate atom-clock-interferometer physics: a visibility modulation with periodic decay and revival, and a GR-induced gravitational decoherence with relativistic time `τ_dec = √2 ℏc² / (ΔE g Δz)` (Eq. 5). Emphasis on N-enhanced scalability and large internode distance.

The claim has two components, separated here for ledger purposes:

- **C1 (sensitivity/feasibility):** the entangled-network architecture places the predicted GR proper-time signatures (Covey's curvature residual Δω; Fromonteil's redshift/decoherence visibility signatures) within reach of near-state-of-the-art hardware, at separations and interrogation times unavailable to single-system matter-wave interferometry.
- **C2 (interpretive/structural):** these signatures are genuine **multipartite** witnesses of quantum proper-time dynamics distributed across nodes at different gravitational potential.

The Ledger evaluates **C2** against Coastline v0.3. C1 is a feasibility statement reviewable on its own merits.

---

## Declared Evaluating Measures

This entry is the first to apply the **resolution-anchor vs classification-anchor** distinction (roadmap measure-registration refinement, from CL-2026-007 v0.2):

> **Classification anchor — cross-probe mismatch.** Concretely, Covey's `Δω = ω₁₂ − ω₂₃` (Eq. 10): the residual disagreement among pairwise elapsed-time comparisons that survives after the leading inter-node consensus (`ω₁₂ ≈ ω₂₃`) is removed. For Fromonteil, the analogue is the relative-phase mismatch between mass-superposition branches that drives the visibility modulation. Cross-probe mismatch is the Coastline Claim IV anchor that directly carries the multi-node structural content this claim is about.
>
> **Resolution anchor — quantum Fisher information / coherence-time budget.** The N-scaling of the entangled states (Covey's N-fold GHZ amplification; Fromonteil's `F_Q`-enhancement and `τ_dec`) bounds *what must be resolved* to see the signature; it does not carry the structural content. Registered separately so it is not conflated with the classification anchor.

Mutual information `I` (CL-2026-006) and Fisher F[τ] (CL-2026-007) remain available alternative anchors; the choice is registered and may be revised.

---

## Classification Analysis

### Engagement with Coastline v0.3 Claim II (Redundancy, Stability, Compressibility)

**Redundancy — the decisive engagement, and the first live test of the v0.3 "multipartite ≠ redundant" distinction.** These proposals are genuinely **multipartite**: temporal information is distributed across three (Covey) or several (Fromonteil) spatially separated nodes. But the states are **entangled** — a single delocalized excitation (W), an N-atom GHZ, or a non-local mass superposition — and are read out **nonlocally** (Covey's joint Fourier-basis measurement; Fromonteil's collective interference). They are therefore **anti-redundant by design**: tracing out a node does not leave an independent compatible copy of the elapsed-time inference; it degrades or destroys the joint signal (this is the very source of the metrological enhancement). Under Coastline v0.3, **multipartiteness is necessary but not sufficient for redundancy**, and these networks sit squarely on the *multipartite-but-not-redundant* side. **Status under Claim II.1: not satisfied — multipartite, anti-redundant.**

*This is not, in itself, a strike against C2.* C2 claims a multipartite cross-probe witness, **not** a demonstration of redundant temporal records or of consensus emergence. Anti-redundancy counts against a claim only if that claim is advanced as evidence for redundancy; it is not here. The framework's verdict is that these proposals occupy the multipartite axis of Claim V *without* engaging the redundancy condition — which is exactly where the framework positions them.

**Stability.** Because the states are anti-redundant, the inferred elapsed-time signal is by construction *not* stable under partial trace of a node. Again this is the intended design (entanglement-enhanced sensing), not a Claim-III consensus breakdown. **Status under Claim II.2: not satisfied, by design.**

**Compressibility.** Covey's structure is an unusually clean operational instance of the framework's compressibility analysis. The leading-order inter-node agreement `ω₁₂ ≈ ω₂₃` is the **compressible** part — a single classical `τ_cl` (Newtonian redshift) organises it. The curvature residual `Δω` (Eq. 10) is precisely the part that **no single `τ_cl` reproduces**: it is the incompressible cross-probe mismatch that survives after the consensus is subtracted. **Status under Claim II.3: the Newtonian consensus is compressible; the curvature residual Δω is the operational incompressibility — a clean Claim IV cross-probe realisation.**

### GR-boundary stress test (load-bearing for this entry)

Coastline v0.3 External Constraints cite **special relativity** as "the structure of proper-time relations among **inertial worldlines**," and the framework's Claim II/III machinery is articulated in that regime; an explicit GR-regime boundary statement is a **deferred** v0.3 candidate (roadmap). This entry is where that deferral becomes load-bearing:

- Covey's signal `Δω ∝ d²/R³` is a **spacetime-curvature (tidal)** effect — second-order in the gravitational potential, *beyond* the Newtonian/weak-field regime the Coastline currently scopes.
- Fromonteil's nodes sit at **different gravitational potentials** and the effect is the gravitational **redshift** coupling location to internal energy.

The framework therefore **cannot definitively classify C2** for the curvature regime: it has not committed whether, and how, Claim II's compressibility/redundancy criteria extend to proper-time relations across regions of differing gravitational potential and non-zero curvature. The classification is underdetermined *partly because the framework owes a boundary statement* — a gap this entry exposes rather than conceals.

### Verdict on the structural claim

At the level of the formalism, C2's structural content is **framework-legible and, for the cross-probe anchor, framework-compatible**: `Δω` is a textbook Claim IV cross-probe mismatch, and the leading-consensus-cancels / curvature-residual-survives structure operationalises Claim II.3 compressibility cleanly. But two conditions block a COMPATIBLE classification: (i) the **GR-boundary gap** above, and (ii) the **experimental-witness** gap shared with CL-2026-006/007 — the GR signature must be discriminable from technical decoherence (Covey: global magnetic-field/nuclear-Zeeman noise; Fromonteil: technical dephasing vs the claimed *gravitational* decoherence), which the proposals argue is feasible but do not yet decompose.

---

## Classification: **UNDERDETERMINED**

The class claim C2 is classified **UNDERDETERMINED** against Coastline v0.3.

**These proposals are the cleanest available realisation of the cross-probe-mismatch Claim IV anchor and the sharpest instance of the multipartite-but-anti-redundant pole of Claim V — they sharpen the framework even while underdetermined.** The classification is underdetermined for two reasons, the first specific to this entry: (i) the framework's **GR-regime boundary is unwritten** (deferred), so a curvature/redshift probe cannot yet be definitively classified; and (ii) the **experimental discriminability** of the GR signature from technical decoherence is argued but not decomposed. The classification weighs the present sufficiency of the witness and of the framework's stated scope — not the conceptual programme, which these proposals advance.

The classification can move to COMPATIBLE on satisfaction of the discriminant conditions below.

---

## Discriminant Conditions

The classification UNDERDETERMINED may be upgraded to **COMPATIBLE** on:

**D1 (framework — GR boundary).** Commitment of a Coastline GR-regime boundary statement (currently deferred) that brings proper-time relations across differing gravitational potential and non-zero curvature within the framework's scope, and re-evaluation of C2 against it. This is a condition on the *framework*, not the claim; it is the load-bearing item for this entry and feeds back to the roadmap.

**D2 (experiment — discriminability).** A nuisance-channel decomposition isolating the GR cross-probe signature — Covey's `Δω`, or Fromonteil's gravitational-decoherence visibility signature `τ_dec` — from technical decoherence (global magnetic-field/nuclear-Zeeman noise; collective dephasing), such that the cross-probe-mismatch witness exceeds the bounded nuisance budget. The independence caveat of CL-2026-006 D2 applies (a toggled parameter must not silently change the nuisance channels).

The classification may be downgraded to **INCONSISTENT** (as a witness claim) on:

**D−1.** Demonstration that the predicted GR signature is fully accounted for by technical nuisances with no statistically significant residual (a failure of C1's sensitivity claim).

---

## Notes for Downstream Use

**Relation to the §3.1 open problem (redundant temporal records).** These networks are explicitly *not* a worked exemplar of the framework's principal open problem (synthesis-v0.1 §3.1; Coastline v0.3 Deferred Items): they are multipartite but anti-redundant. A genuinely *redundant* multi-node clock arrangement — many independent nodes each carrying a compatible, separately-readable elapsed-time record (not an entangled collective state) — would, distinctly, bear on Claim II.1 and could be the sought exemplar. This entry sharpens the contrast: entanglement-enhanced networks maximise cross-probe sensitivity precisely by *forgoing* redundancy.

**Feedback to the roadmap.** D1 demonstrates that the GR-boundary statement is **load-bearing, not optional**: the framework cannot classify the most natural multipartite proper-time experiments (curvature/redshift probes) until it commits a curved-spacetime boundary. This elevates the GR-boundary item from a tidy-up to a prerequisite for the distributed-network programme.

**Relation to CL-2026-006 / CL-2026-007.** All three sit at UNDERDETERMINED. CL-2026-006 (Sorci, bipartite) and CL-2026-007 (Smith & Ahmadi, bipartite) are underdetermined at the experimental-witness level within the SR/weak-field regime; CL-2026-008 adds a *second*, framework-internal reason (the GR boundary) and is the first entry where the multipartite (Claim V) and curvature (External Constraints) commitments are exercised. Declared anchors across the three: mutual information (006), Fisher resolution (007), cross-probe mismatch (008) — the Claim IV pluralism is now exercised across the corpus.

**Relation to deferred items.** CCUF bridge (L₁) remains deferred and uncoupled; this is an L₀ classification, though the distributed-network setting is the natural place a future L₀/L₁ bridge discussion would begin.

---

## Version History

| Version | Date | Notes |
| --- | --- | --- |
| v0.1 | 2026-05-26 | Initial classification, anchored to Coastline v0.3. Class claim (Covey–Pikovski–Borregaard 2025; Fromonteil et al. 2025) — framed as a class because the two diverge (curvature via 3-node W vs redshift/decoherence via N-atom ensembles) while sharing the entanglement-enhanced/anti-redundant structure. **UNDERDETERMINED** for two reasons: (i) the framework's GR-regime boundary is unwritten (deferred), blocking definitive classification of a curvature/redshift probe — the load-bearing point (D1); (ii) experimental discriminability of the GR signature from technical decoherence (D2). First entry to: apply the resolution/classification anchor distinction (classification anchor = cross-probe mismatch Δω; resolution anchor = QFI/coherence budget); exercise the v0.3 "multipartite ≠ redundant" distinction (these networks are multipartite but anti-redundant, and *do not* claim redundancy — so anti-redundancy is not held against C2); and show the GR-boundary roadmap item is load-bearing, not optional. |

---

*This ledger entry is a framework-relative classification of an external scientific claim. It does not assert correctness or incorrectness of the claim in the framework-independent sense. The declared evaluating measures are part of the classification and may be revised in subsequent entries.*
