# Roadmap — Temporal Micro Consensus

*Forward-looking documentation for active development items, deferred items, and stewardship decisions.*

| Field | Value |
| --- | --- |
| Version | v0.5 |
| Date | 2026-05-27 |
| Steward | U. Warring |
| Status | Living document — updated as items advance or are retired |

---

## Active development

### Literature review (upstream of everything below)

An extensive, broad-sweep **comprehensive field map** is the current upstream workstream, governed by its own plan: [`docs/literature-review-plan.md`](literature-review-plan.md). It assembles and verifies one reusable corpus ([`docs/literature/`](literature/)) feeding all three artefact families. The Coastline v0.3 candidates, candidate Ledger entries, and Sail reference apparatus listed below are its intended downstream consumers (Phase 4 of that plan).

### Coastline — issued revisions & remaining candidates

Coastline v0.3 ([`coastlines/consensus-emergence-v0.3.md`](../coastlines/consensus-emergence-v0.3.md)) was drafted after the literature review (Phases 1–3) road-tested the framework, drawing on [`docs/literature/synthesis-v0.1.md`](literature/synthesis-v0.1.md).

**Folded into v0.3:**
- **"Many" specification** — done, as the Claim II *"many vs redundant"* terminology note, extended (per synthesis) to distinguish redundant carriers from *entanglement-enhanced (anti-redundant)* multipartiteness; mirrored by a placement sentence in Claim V.
- **Claim III softening** — done ("is what converts" → "is a *necessary step in* converting").
- **Lineage fixes** (new, from the synthesis lineage audit) — removed the Hartong–Have–Obers–Pikovski mis-attribution from the Page–Wootters list; corrected Mendes & Soares-Pinto 2018→2019; added the Ollivier–Poulin–Zurek objective-histories formulation as the closest configurational precursor.
- **Transplant gap** (new, the synthesis headline) — the configurational→temporal transplant registered as the *principal open problem* (Claim II status-of-specialisation paragraph, Anti-Claim #6, Deferred Items priority).

**Deferred to a later Coastline version (still open, in roadmap):**
- **Registration protocol for Claim IV measure selection.** Require any deployment — Ledger entry, Sail, methodological note — to declare its chosen operational measure and threshold upfront, with explicit justification. Closes the measure-shifting vulnerability while preserving Claim IV pluralism. (The Ledger CL-2026-006 already does this in practice via its declared I(C:M); the Coastline-level requirement is not yet written.) **Refinement (from CL-2026-007 v0.2, Verifier review):** the protocol should distinguish a *resolution anchor* (the measure that bounds what must be resolved — e.g. Fisher information F[τ] setting the temporal resolution) from a *classification anchor* (the measure that actually carries the structural content being classified — e.g. the cross-probe γ_Q⁻¹ or mutual information). A deployment may register one of each; conflating them is the failure mode CL-2026-007 v0.1 fell into. **Basis now available (2026-05-27):** the temporal-redundancy functional note ([`docs/notes/temporal-redundancy-functional-v0.2.md`](notes/temporal-redundancy-functional-v0.2.md), §4) supplies a principled reason for the split — the classification anchor (mutual information) is *bounded* and plateaus, the resolution anchor (Fisher) is *extensive* and does not, and the two can move oppositely (the GHZ pole has maximal joint Fisher and zero redundancy). A future Coastline version can cite this when writing the protocol. **Now operationally previewed (2026-05-27):** Ledger CL-2026-006 v0.4 registers R_δ as a second classification anchor alongside I(C:M), with Fisher/QFI as the resolution anchor — exercising the split in the Ledger (its proper venue) ahead of any Coastline commitment; the verdict is unchanged (UNDERDETERMINED, cross-consistent under both anchors).
- **FIT citation in External Constraints.** Add Fisher-Informational Time (arXiv 2605.03958, 2026) as an external citation. FIT operates at the single-trajectory layer; consensus-emergence at the multipartite-redundancy layer — compatible but distinct (synthesis §3.5: the framework *subsumes/extends* FIT, not competes).
- **FIT positioning bullet in Claim V.** Make the trajectory-vs-multipartite distinction explicit; FIT-style accumulated Fisher distance is one realisation of the Claim IV Fisher anchor, not a substitute for redundancy/stability/compressibility across many records.
- **GR boundary statement.** ✅ **Done in Coastline v0.4 (2026-05-26).** Resolved by *extending* (not bounding) the framework to the SR-and-weak-field (post-Newtonian) regime — see [`coastlines/consensus-emergence-v0.4.md`](../coastlines/consensus-emergence-v0.4.md) (External Constraints item 5; new *Regime of Validity* section; Anti-Claim #7). Made load-bearing by CL-2026-008 D1, whose framework-side condition this now satisfies. *(Retained here for traceability; see "Retired or completed items".)*

### Ledger schema candidates

- **Layer A/B/C architecture.** Guardian proposal during CL-2026-006 review: future Ledger entries make explicit three layers — (A) structural dynamics, (B) measure adequacy, (C) experimental discriminability. The current entry already does all three in substance; explicit labelling would make the schema more reusable across cases.

### Sail — pending decisions & candidates

Pending for the Sorci commentary if it is to leave internal circulation:

- **Reference apparatus.** The current draft cites ideas and lineages in prose; an external venue requires a proper bibliography. Estimated 25–35 references including: Sorci et al. and the trapped-ion clock literature it cites, Page & Wootters, Zych–Costa–Pikovski–Brukner line, Pikovski et al. gravitational decoherence work, Zurek and quantum Darwinism literature, Margalit et al. self-interfering clock, Nambu Fisher-information cosmological clock, Mendes & Soares-Pinto on time observables, Hartong–Have–Obers–Pikovski coupling prescription, Martínez-Lahuerta et al. trapped-ion mass defect, Yudin & Taichenachev mass defect effects, FIT preprint, and recent distributed-clock-network work.
- **Acknowledgements decision.** *Updated 2026-05-26:* the inaccurate C. Sanner acknowledgement was removed in **Sail v0.3** (steward has no relationship with Sanner; see logbook). What remains is the **D. Leibfried** acknowledgement (NIST Boulder, 2010–2012) — and the open decision on whether to retain it, reformulate it as a brief disclosure note, or remove it before any external venue, given that Leibfried is a co-author of the subject paper (an independence-of-commentary question).
- **Licensing harmonisation.** If the Sail is to be compiled with Coastline content (e.g. a handbook, an extended technical report), the current CC BY-NC-SA 4.0 of the Sail and CC BY-SA 4.0 of the Coastline create a non-commercial-clause inheritance issue. Scout flag. Decision pending: harmonise to CC BY-SA 4.0, retain the split, or maintain a separate licence-by-document policy.

### Ledger entries opened from candidates

*(Both former candidates are now open and anchored to the current Coastline v0.4; see also "Retired or completed items.")*

- **CL-2026-007 — open, current v0.3** ([`ledger/CL-2026-007-smith-ahmadi-v0.3.md`](../ledger/CL-2026-007-smith-ahmadi-v0.3.md)). Smith & Ahmadi (2020). **UNDERDETERMINED** against Coastline v0.4. The verdict-bearing pass was v0.2 (after Verifier review + re-reading the source): the paper *does* establish the superposition-vs-mixture distinction theoretically — γ_Q⁻¹ is the coherence-dependent term (Eqs. 24–25), vanishing for a classical mixture — so the gap is the **experimental witness** (isolating the ~10⁻¹⁵ γ_Q⁻¹ from preparation/dephasing/verification nuisances), the same location as CL-2026-006. v0.3 is a pure re-anchor to Coastline v0.4 (GR boundary irrelevant to this bipartite case). Fisher registered as resolution anchor.
- **CL-2026-008 — open, current v0.2** ([`ledger/CL-2026-008-clock-networks-v0.2.md`](../ledger/CL-2026-008-clock-networks-v0.2.md)). Distributed entanglement-enhanced clock-network proposals, framed as a **class claim** (Covey–Pikovski–Borregaard 2025 — curvature via 3-node W-state Δω; Fromonteil et al. 2025 — redshift/decoherence via N-atom ensembles). **UNDERDETERMINED** against Coastline v0.4. First entry to: declare cross-probe mismatch as the **classification anchor** (with QFI/coherence as a separate **resolution anchor**); exercise **multipartite ≠ redundant** (multipartite but anti-redundant, and not claiming redundancy); and show the **GR-boundary item was load-bearing** (its D1) — now satisfied by Coastline v0.4's Regime of Validity, so v0.2 rests on the experimental condition D2 alone.

### Possible future Sails or methodological notes

- **Methodological note on operational measures.** Develop one or more of the Claim IV anchors (mutual information distribution across subsystems, Fisher information distribution across probes, cross-probe phase mismatch under inferred τ_cl) into a self-contained methodological note suitable for adoption in concrete experimental analyses.
- **Toy-model functional for temporal redundancy.** ✅ **Drafted; current v0.2 (2026-05-27)** — [`docs/notes/temporal-redundancy-functional-v0.2.md`](notes/temporal-redundancy-functional-v0.2.md) (v0.1 frozen). Defines a Riedel-style redundancy functional `R_δ[τ]` on a finite temporal pointer; computes the redundant (product) vs anti-redundant (GHZ-shadow) poles, rendering *multipartite ≠ redundant* numerical (`R_{0.10} = 7.1` vs `1`); maps onto the Sorci squeezed-motion case (CL-2026-006) and its D1–D3; and grounds the resolution/classification-anchor split (above). **Residual open problem (carried forward):** the toy does *not* close Anti-Claim #6 — a non-toy exemplar (continuous-`τ`, dynamically einselected, many-carrier; e.g. a master-equation `R_δ` for `N` independently dephasing ions) is the next instrument toward the Coastline's principal open problem. Whether any such instance counts as *the* worked exemplar is a Coastline-level steward decision.

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
- **Coastline v0.3 (2026-05-26).** Issued — see the "Coastline — issued revisions & remaining candidates" subsection above. Folded the "many" specification, Claim III softening, three lineage fixes, and the transplant-gap open problem; deferred FIT/GR-boundary/measure-registration.
- **Ledger CL-2026-007 (2026-05-26).** Opened (Smith & Ahmadi); corrected to v0.2 after Verifier review (crux relocated to the experimental-witness level).
- **Ledger CL-2026-008 (2026-05-26).** Opened (distributed entanglement-enhanced clock networks, class claim); first to exercise *multipartite ≠ redundant* and the resolution/classification anchor split; its D1 made the GR boundary load-bearing.
- **Coastline v0.4 (2026-05-26).** Issued the **GR-regime boundary statement** ([`coastlines/consensus-emergence-v0.4.md`](../coastlines/consensus-emergence-v0.4.md)). Decision: *extend* to the SR-and-weak-field (post-Newtonian) regime, not bound at SR. Satisfies the framework-side condition of CL-2026-008 D1. Still deferred: FIT citation + positioning; Claim IV measure-registration protocol.
- **Version-consistency re-anchors (2026-05-26).** Closing the loop after Coastline v0.4: **CL-2026-006 → v0.3** (re-anchored to Coastline v0.4; verdict and discriminants unchanged — the v0.2→v0.4 changes are refinements the entry already anticipated) and **CL-2026-008 → v0.2** (re-evaluated against v0.4 — D1's framework-side gap now satisfied by the Regime of Validity; classification stays UNDERDETERMINED, now resting on D2 alone). *Pending optional touch:* Sail v0.4 still cites CL-2026-006 v0.2 (valid; no verdict change) — a Sail pointer update to v0.3 can ride the next Sail revision.

---

## Version History

| Version | Date | Notes |
| --- | --- | --- |
| v0.1 | 2026-05-23 | Initial roadmap. Captures v0.3 candidate items for Coastline, Ledger schema, and Sail; deferred items from Coastline v0.2; possible future Ledger entries and Sails; stewardship decisions pending. |
| v0.2 | 2026-05-26 | Added literature-review workstream pointer (new `docs/literature-review-plan.md`) as upstream of all active-development items. Resolved the public-visibility stewardship decision (repository now public). |
| v0.3 | 2026-05-27 | Marked the temporal-redundancy toy functional **drafted at v0.1** (`docs/notes/`), with the non-toy-exemplar question carried forward toward the Coastline's principal open problem; recorded that the note's §4 supplies the bounded-vs-extensive basis for the deferred Claim IV measure-registration split. |
| v0.4 | 2026-05-27 | Re-pointed the temporal-redundancy functional references from v0.1 to **v0.2** after a Guardian-stance review of the note (v0.1 frozen): §1.1 einselection reframed as the central deferral, anti-redundant pole derived via the Schmidt structure (new Appendix B), §3/§4/§5 tightened, and the configurational functional-information measure arXiv:2509.17775 cited as the transplant source. No roadmap item status change. |
| v0.5 | 2026-05-27 | Recorded **Ledger CL-2026-006 v0.4** (v0.3 frozen): R_δ (MN v0.2) added as a second declared classification anchor alongside I(C:M), operationally previewing the deferred Claim IV measure-registration split in the Ledger (not the Coastline). Verdict unchanged (UNDERDETERMINED, cross-consistent). Per the Guardian decision (2026-05-27), the MN is cited from the Ledger, **not** the Sail; the instrument-vs-fitting placement of methodological notes stays deferred. |
