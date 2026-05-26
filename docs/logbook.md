# Project Logbook

*A chronological, append-only record of substantive activities, decisions, and corrections in the Harbour — Temporal Consensus repository. It exists for **provenance and reproducibility** (the "R" of FAIR): each entry says what was done, when, by whom, why, and which artefacts/commits resulted.*

| Field | Value |
| --- | --- |
| Purpose | Provenance / audit trail (FAIR-Reusable) |
| Convention | **Append-only.** Entries are added chronologically (oldest first); existing entries are not rewritten. Corrections are logged as new entries that reference the earlier one. |
| Actors | **Steward** = U. Warring (decisions, authorship). **Agent** = Claude Code (execution under steward direction). |
| Scope | Decisions, version issuances, phase transitions, factual corrections. Routine edits are captured by the Git history, not duplicated here. |

---

## 2026-05-23 — Repository origin

- **Actor:** Steward. **Commit:** `c18af36` (Initial repository scaffold).
- Repository scaffolded under Local Stewardship: Coastline *Consensus-Emergence of Classical Proper Time* (v0.1 → v0.2), Ledger CL-2026-006 (v0.1 → v0.2), Sail *Visibility, the Right Witness* (v0.1 → v0.2), roadmap v0.1, split licensing (MIT / CC-BY-SA-4.0 / CC-BY-NC-SA-4.0).

## 2026-05-26 — Public remote established

- **Actor:** Steward (executed via Agent assistance). 
- Public GitHub remote created at `github.com/uwarring82/temporal-micro-consensus` and `main` pushed. Resolved the roadmap's "public visibility of repository" stewardship decision.

## 2026-05-26 — Literature review opened (plan v0.2, Phase 0)

- **Actor:** Steward (decisions) / Agent (drafting). **Commits:** `2030399`, `bc5ddce`.
- Established [`literature-review-plan.md`](literature-review-plan.md) (v0.2 after a Guardian-stance review): comprehensive broad-sweep field map, seven clusters, five phases, Tier-1 scope cap, CCUF-bridge lock, source-handling policy (PDFs local-only, git-ignored). Phase 0 scaffolding under [`literature/`](literature/) landed in a second commit for an auditable boundary.

## 2026-05-26 — Phase 1: corpus verified

- **Actor:** Agent (under steward direction). **Commit:** `d059320`.
- All corpus entries verified against Crossref / arXiv / ADS / publisher; `VERIFY` flags cleared; placeholders resolved (incl. `sorci2026`, `hartong2024`, `covey2025`, `fromonteil2025`, `fit2026`). Lineage flags recorded for later audit.

## 2026-05-26 — Phase 1/2: sources acquired, extraction notes

- **Actor:** Steward (PDF acquisition) / Agent (extraction). **Commits:** `932e6ea`, `78d3653`.
- 29 PDFs acquired into local-only `sources/`, renamed to citekeys; one findings note per paper (own-words summaries — copyright). `zych2019` added as the composite-system-action source behind `sorci2026`.

## 2026-05-26 — Phase 2: Tier-1 fixed at 13, full annotation

- **Actor:** Steward (down-tiering call) / Agent (annotation). **Commit:** `53127f5`.
- Tier 1 reduced 18 → 13; six papers down-tiered with rationale. The 13 Tier-1 notes upgraded to the full per-claim Phase-2 template. Structural-finding evaluation recorded (`hartong2024`: no v0.3 *plan* revision required; artefact-level fix logged).

## 2026-05-26 — Phase 3: synthesis

- **Actor:** Agent (under steward direction). **Commit:** `d6f00c3`.
- [`literature/synthesis-v0.1.md`](literature/synthesis-v0.1.md) committed: claim-by-claim, measure-by-measure, gaps/falsifications, lineage audit. **Headline finding:** the configurational→temporal transplant (Claim II redundancy) has no temporal exemplar in the corpus.

## 2026-05-26 — Coastline v0.3 issued

- **Actor:** Steward (explicit go) / Agent (drafting). **Commit:** `a2d037f`.
- [`coastlines/consensus-emergence-v0.3.md`](../coastlines/consensus-emergence-v0.3.md) issued (v0.2 frozen). Lineage fixes (Hartong removed, Mendes 2018→2019, Ollivier–Poulin–Zurek precursor added); transplant gap registered (Claim II paragraph, Anti-Claim #6, Deferred priority); "multipartite ≠ redundant" added; Claim III softened. FIT / GR-boundary / measure-registration deferred.

## 2026-05-26 — FAIR principles adopted; logbook established

- **Actor:** Steward (direction) / Agent (execution). **Commit:** *(this change).*
- Adopted FAIR principles (see [README §FAIR](../README.md)): added machine-readable citation metadata ([`CITATION.cff`](../CITATION.cff)) and established this logbook. Next step toward full *Findability* is a tagged release minted to a Zenodo DOI (requires steward action: connect Zenodo to the GitHub repo, then publish a release; optionally add the steward's ORCID to `CITATION.cff`).

## 2026-05-26 — Correction: no steward relationship with C. Sanner

- **Actor:** Steward (factual correction). **Commit:** *(this change).*
- The steward reports having **never met or directly interacted with C. Sanner**. This corrects an earlier inference (logged 2026-05-26, Phase 3) that treated both Leibfried and Sanner as "close contacts" of the steward.
- **Effect:** The Sail's Acknowledgements (`sails/sorci-commentary-v0.2.md`) state "ongoing exchanges" with C. Sanner — this is **factually inaccurate** and is flagged for correction. The genuine prior association is with **D. Leibfried** (discussions at NIST Boulder, 2010–2012). Both Leibfried and Sanner are co-authors of the subject paper (Sorci et al.); the independence-of-commentary consideration for any external circulation therefore concerns the steward's prior association with **Leibfried** alone.
- **Propagated:** `literature/synthesis-v0.1.md` §4 and `roadmap.md` (external-circulation item) corrected. **Pending:** the Sail acknowledgement itself awaits the steward's decision on correction (remove the Sanner clause / reformulate / handle in the Phase-4 Sail pass).

## 2026-05-26 — Sail v0.3 issued (Sanner acknowledgement removed)

- **Actor:** Steward (decision: minimal factual correction) / Agent (drafting). **Commit:** *(this change).*
- Resolves the "Pending" item in the entry above. [`sails/sorci-commentary-v0.3.md`](../sails/sorci-commentary-v0.3.md) issued (v0.2 frozen); the only changes versus v0.2 are the metadata block, the removal of the C. Sanner acknowledgement clause (the steward has no relationship with Sanner), and the version-history row. The D. Leibfried acknowledgement is retained.
- **Deliberately *not* changed:** anchoring remains Coastline **v0.2** / Ledger CL-2026-006 v0.2 (re-anchoring to Coastline v0.3 is a substantive change), and the broader acknowledgement decision (retain / reformulate / remove) remains open — both deferred to the Phase-4 Sail pass.

## 2026-05-26 — Phase 4 step 1: Ledger CL-2026-007 opened

- **Actor:** Steward (direction: "go step by step" through Phase 4) / Agent (drafting). **Commit:** *(this change).*
- [`ledger/CL-2026-007-smith-ahmadi-v0.1.md`](../ledger/CL-2026-007-smith-ahmadi-v0.1.md) issued (v0.1), classifying Smith & Ahmadi (2020) **UNDERDETERMINED** against **Coastline v0.3**. Declared measure: Fisher information F[τ] (deliberately distinct from CL-2026-006's mutual information, road-testing measure pluralism). Crux/discriminant: whether the quantum time-dilation correction is coherence-dependent (superposition ≠ classical mixture) — the coherence-sensitive test it lacks is what the Sorci visibility witness (CL-2026-006) provides.
- Roadmap "possible future Ledger entries" updated (CL-2026-007 → opened); README Ledger mention + structure tree updated. **Next steps (Phase 4):** CL-2026-008 (distributed networks); Sail re-anchor to v0.3; methodological notes.
