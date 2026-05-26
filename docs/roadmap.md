# Roadmap — Harbour Temporal Consensus

*Forward-looking documentation for active development items, deferred items, and stewardship decisions.*

| Field | Value |
| --- | --- |
| Version | v0.2 |
| Date | 2026-05-26 |
| Steward | U. Warring |
| Status | Living document — updated as items advance or are retired |

---

## Active development

### Literature review (upstream of everything below)

An extensive, broad-sweep **comprehensive field map** is the current upstream workstream, governed by its own plan: [`docs/literature-review-plan.md`](literature-review-plan.md). It assembles and verifies one reusable corpus ([`docs/literature/`](literature/)) feeding all three artefact families. The Coastline v0.3 candidates, candidate Ledger entries, and Sail reference apparatus listed below are its intended downstream consumers (Phase 4 of that plan).

### Coastline v0.3 — issued 2026-05-26

Coastline v0.3 ([`coastlines/consensus-emergence-v0.3.md`](../coastlines/consensus-emergence-v0.3.md)) was drafted after the literature review (Phases 1–3) road-tested the framework, drawing on [`docs/literature/synthesis-v0.1.md`](literature/synthesis-v0.1.md).

**Folded into v0.3:**
- **"Many" specification** — done, as the Claim II *"many vs redundant"* terminology note, extended (per synthesis) to distinguish redundant carriers from *entanglement-enhanced (anti-redundant)* multipartiteness; mirrored by a placement sentence in Claim V.
- **Claim III softening** — done ("is what converts" → "is a *necessary step in* converting").
- **Lineage fixes** (new, from the synthesis lineage audit) — removed the Hartong–Have–Obers–Pikovski mis-attribution from the Page–Wootters list; corrected Mendes & Soares-Pinto 2018→2019; added the Ollivier–Poulin–Zurek objective-histories formulation as the closest configurational precursor.
- **Transplant gap** (new, the synthesis headline) — the configurational→temporal transplant registered as the *principal open problem* (Claim II status-of-specialisation paragraph, Anti-Claim #6, Deferred Items priority).

**Deferred to a later Coastline version (still open, in roadmap):**
- **Registration protocol for Claim IV measure selection.** Require any deployment — Ledger entry, Sail, methodological note — to declare its chosen operational measure and threshold upfront, with explicit justification. Closes the measure-shifting vulnerability while preserving Claim IV pluralism. (The Ledger CL-2026-006 already does this in practice via its declared I(C:M); the Coastline-level requirement is not yet written.) **Refinement (from CL-2026-007 v0.2, Verifier review):** the protocol should distinguish a *resolution anchor* (the measure that bounds what must be resolved — e.g. Fisher information F[τ] setting the temporal resolution) from a *classification anchor* (the measure that actually carries the structural content being classified — e.g. the cross-probe γ_Q⁻¹ or mutual information). A deployment may register one of each; conflating them is the failure mode CL-2026-007 v0.1 fell into.
- **FIT citation in External Constraints.** Add Fisher-Informational Time (arXiv 2605.03958, 2026) as an external citation. FIT operates at the single-trajectory layer; consensus-emergence at the multipartite-redundancy layer — compatible but distinct (synthesis §3.5: the framework *subsumes/extends* FIT, not competes).
- **FIT positioning bullet in Claim V.** Make the trajectory-vs-multipartite distinction explicit; FIT-style accumulated Fisher distance is one realisation of the Claim IV Fisher anchor, not a substitute for redundancy/stability/compressibility across many records.
- **GR boundary statement.** Add an explicit note that the framework operates in the SR-and-weak-field regime; extension to strongly accelerated worldlines or curved spacetime requires additional structure. Becomes load-bearing when the framework is applied to distributed-clock networks across differing gravitational potential (CL-2026-008).

### Ledger schema candidates

- **Layer A/B/C architecture.** Guardian proposal during CL-2026-006 review: future Ledger entries make explicit three layers — (A) structural dynamics, (B) measure adequacy, (C) experimental discriminability. The current entry already does all three in substance; explicit labelling would make the schema more reusable across cases.

### Sail v0.3 candidates

Pending for the Sorci commentary if it is to leave internal circulation:

- **Reference apparatus.** The current draft cites ideas and lineages in prose; an external venue requires a proper bibliography. Estimated 25–35 references including: Sorci et al. and the trapped-ion clock literature it cites, Page & Wootters, Zych–Costa–Pikovski–Brukner line, Pikovski et al. gravitational decoherence work, Zurek and quantum Darwinism literature, Margalit et al. self-interfering clock, Nambu Fisher-information cosmological clock, Mendes & Soares-Pinto on time observables, Hartong–Have–Obers–Pikovski coupling prescription, Martínez-Lahuerta et al. trapped-ion mass defect, Yudin & Taichenachev mass defect effects, FIT preprint, and recent distributed-clock-network work.
- **Acknowledgements decision.** *Updated 2026-05-26:* the inaccurate C. Sanner acknowledgement was removed in **Sail v0.3** (steward has no relationship with Sanner; see logbook). What remains is the **D. Leibfried** acknowledgement (NIST Boulder, 2010–2012) — and the open decision on whether to retain it, reformulate it as a brief disclosure note, or remove it before any external venue, given that Leibfried is a co-author of the subject paper (an independence-of-commentary question).
- **Licensing harmonisation.** If the Sail is to be compiled with Coastline content (e.g. a handbook, an extended technical report), the current CC BY-NC-SA 4.0 of the Sail and CC BY-SA 4.0 of the Coastline create a non-commercial-clause inheritance issue. Scout flag. Decision pending: harmonise to CC BY-SA 4.0, retain the split, or maintain a separate licence-by-document policy.

### Possible future Ledger entries

- **CL-2026-007 — opened 2026-05-26, refined to v0.2** ([`ledger/CL-2026-007-smith-ahmadi-v0.2.md`](../ledger/CL-2026-007-smith-ahmadi-v0.2.md)). Smith & Ahmadi (2020). **UNDERDETERMINED** against Coastline v0.3. v0.2 (after Verifier review + re-reading the source) corrects v0.1's crux: the paper *does* establish the superposition-vs-mixture distinction theoretically — γ_Q⁻¹ is the coherence-dependent term (Eqs. 24–25), vanishing for a classical mixture — so the coherent regime is a genuine theory-level Claim II failure. The gap is the **experimental witness** (isolating the ~10⁻¹⁵ γ_Q⁻¹ from preparation/dephasing/verification nuisances), the same location as CL-2026-006. Fisher retained as registered resolution anchor (overclaim withdrawn).
- **CL-2026-008 (candidate).** Distributed clock-network proposals (Covey–Pikovski–Borregaard 2025; Fromonteil et al. 2025). Move from L₀ minimal-multipartite case to genuinely multipartite case across spatially separated nodes. Would also stress-test the GR boundary.

### Possible future Sails or methodological notes

- **Methodological note on operational measures.** Develop one or more of the Claim IV anchors (mutual information distribution across subsystems, Fisher information distribution across probes, cross-probe phase mismatch under inferred τ_cl) into a self-contained methodological note suitable for adoption in concrete experimental analyses.
- **Toy-model functional for temporal redundancy.** Verifier-suggested concrete next step. Borrow from Functional Information in Quantum Darwinism (Riedel-style) to compute a temporal-redundancy functional for a few-ion clock with motional squeezing. Concretises both the Coastline's Claim II and the Ledger's discriminant conditions for the Sorci case.

## Deferred items (from Coastline v0.2)

These are noted as plausible future extensions but not committed in the current Coastline. They are tracked here without commitment.

- **CCUF bridge.** Possible structural analogy between L₀ consensus-emergence (microscopic temporal records) and L₁ architectural agreement (CCUF η-parameter, comparison-geometry boundary, "agreement, not oscillation, defines a clock"). The proposed unification would identify both layers as expressions of one principle — time as a robust collective variable, not a private property — at distinct scales. Disciplined approach: a separate Coastline note bridging the two frameworks, drafted only after each has matured independently. Lock-Key discipline.
- **Application to thermodynamic / arrow-of-time discussions.** Noted in Coastline v0.2 as plausible but not pursued. Connection to thermal time, fluctuation theorems, and arrow-of-time emergence in quantum systems may be productive but requires its own dedicated treatment.
- **Quantitative thresholds.** Specific numerical thresholds (e.g. mutual-information requirements in bits per carrier, Fisher-information distribution profiles, redundancy lower bounds) that would render Claim II quantitatively testable in concrete experimental settings. Deferred pending engagement with specific protocols beyond Sorci.

## Stewardship decisions pending

- **External circulation of Sail.** Decision points before any external venue: (i) acknowledgements; (ii) reference apparatus completion; (iii) optional courtesy contact with subject-paper authors before deposit. *Factual correction done 2026-05-26 in **Sail v0.3** (see [`logbook.md`](logbook.md)):* the inaccurate acknowledgement of "ongoing exchanges" with C. Sanner was removed — the steward has no relationship with Sanner. The genuine prior association is with **D. Leibfried** (NIST Boulder, 2010–2012). Both are co-authors of the subject paper, so the *remaining* independence-of-commentary question (i) concerns **Leibfried**. The broader acknowledgement decision (retain / reformulate as disclosure / remove) is still open for the Phase-4 Sail pass.
- **arXiv vs journal-comment vs preprint-only.** If external circulation is pursued, the route — arXiv-only deposit, formal Comment to PRL, Nature Physics News & Views via Dr Pichon route, or other — needs deliberation. Each has different timelines, audiences, and discipline requirements.
- **Public visibility of repository.** *Resolved 2026-05-26:* repository is now public at `github.com/uwarring82/temporal-micro-consensus`. This remains separable from external circulation of the Sail — public hosting of versioned draft artefacts under Local Stewardship does not itself constitute external circulation of the Sorci commentary, which retains its own decision points below.

## Retired or completed items

- **Literature review, Phases 1–3 (2026-05-26).** Comprehensive field map: 29-entry corpus assembled and verified, Tier-1 fixed at 13 with full per-claim annotation, [`docs/literature/synthesis-v0.1.md`](literature/synthesis-v0.1.md) committed. Governed by [`docs/literature-review-plan.md`](literature-review-plan.md). Phase 4 (artefact edits) is the downstream work tracked above.
- **Coastline v0.3 (2026-05-26).** Issued — see the "Coastline v0.3 — issued" subsection above. Folded the "many" specification, Claim III softening, three lineage fixes, and the transplant-gap open problem; deferred FIT/GR-boundary/measure-registration.

---

## Version History

| Version | Date | Notes |
| --- | --- | --- |
| v0.1 | 2026-05-23 | Initial roadmap. Captures v0.3 candidate items for Coastline, Ledger schema, and Sail; deferred items from Coastline v0.2; possible future Ledger entries and Sails; stewardship decisions pending. |
| v0.2 | 2026-05-26 | Added literature-review workstream pointer (new `docs/literature-review-plan.md`) as upstream of all active-development items. Resolved the public-visibility stewardship decision (repository now public). |
