# Literature Review — Work Plan

*A staged plan for an extensive, broad-sweep literature review feeding the Coastline, Ledger, and Sails of Temporal Micro Consensus.*

| Field | Value |
| --- | --- |
| Version | v0.2.1 |
| Date | 2026-05-26 |
| Steward | U. Warring |
| Status | Living document — phases updated as they advance or close |
| Predecessor | v0.1 (2026-05-26, pre-review draft; not committed) |
| Companion | [`docs/roadmap.md`](roadmap.md) (forward-looking items), [`docs/literature/`](literature/) (corpus, notes, bibliography) |

---

## 1. Purpose

This plan governs a single **comprehensive field map** of the literature surrounding *Consensus-Emergence of Classical Proper Time* ([Coastline v0.2](../coastlines/consensus-emergence-v0.2.md)). It is the upstream input to all three artefact families:

- **Coastline** — stress-testing and refining the five claims, and resolving the v0.3 candidates (FIT citation, GR boundary, measure-registration, "many" specification — see [roadmap](roadmap.md)).
- **Ledger** — supplying the evidence base for candidate entries CL-2026-007 (Smith & Ahmadi) and CL-2026-008 (distributed clock networks).
- **Sails** — assembling and verifying the reference apparatus and lineage claims required before any external circulation of the Sorci commentary.

The review is deliberately **broad-sweep**: it spans not only the works already named in the Coastline and roadmap but also adjacent foundations (thermal/relational time, arrow-of-time, gravitational decoherence, distributed metrology). Breadth is a one-time investment; the resulting corpus is reused across every downstream artefact.

The review does **not** by itself revise any artefact. It produces a verified corpus and a synthesis memo; artefact edits are separate, downstream acts governed by the roadmap and by Lock-Key discipline.

**This is a structural plan.** It commits to phases, exits, and scope guards, *not* to calendar durations. Mapping phases to weeks — sensitive to teaching load (FP-2/FP-EDU), thesis supervisions, the HPC referee report, and the Clock School project — is a separate exercise (a future `docs/work-plan-calendar.md` or a dated annotation of this document). The structural plan is robust to calendar re-planning.

---

## 2. Thematic clusters (the field map)

The broad sweep is organised into seven clusters. Each paper entering the corpus is tagged with one primary cluster and any secondary clusters, and with the Coastline claim(s) and Claim IV measure(s) it bears on.

| ID | Cluster | Role in the framework |
| --- | --- | --- |
| **A** | Emergence of time from quantum correlations (Page–Wootters and descendants) | The relational-time channel named in External Constraints and Claim V. |
| **B** | Quantum Darwinism & emergence of classical objectivity | The architecture the Coastline specialises to *temporal* records (Claim II). |
| **C** | Quantum clocks & clock metrology (trapped ions, optical standards) | The experimental substrate; source of candidate witnesses (Claim III). |
| **D** | Quantum metrology of time / Fisher information | The leading Claim IV operational anchor; includes FIT. |
| **E** | Relativistic & gravitational effects on quantum coherence | The SR/weak-field boundary (roadmap GR-boundary item); mass-defect couplings. **High-traffic cluster:** the Sorci Hamiltonian descends from the Zych–Rudnicki–Pikovski composite-system action argument, so this is load-bearing for the programme, not merely contextual. |
| **F** | Distributed clock networks & multipartite metrology | Where the *multipartite* structure (Claim V) becomes literal — though, per synthesis-v0.1, these protocols are typically entanglement-enhanced and hence *anti-redundant*, so they realise multipartiteness without the Claim II redundancy; CL-2026-008. |
| **G** | Adjacent foundations | Thermal/relational time, arrow-of-time, decoherence reviews, relational QM. Broad-sweep extension; entry-gated and tier-capped (see Phase 1). |

A seeded, cluster-tagged bibliography lives in [`docs/literature/references.bib`](literature/references.bib); the running triage table lives in [`docs/literature/index.md`](literature/index.md). Some papers (e.g. Nambu, Mendes & Soares-Pinto) sit legitimately in two clusters; the primary-cluster choice is a **decision, not a fact**, and is recorded as such in `index.md` with a one-line rationale.

---

## 3. Phases

### Phase 0 — Infrastructure

Stand up the review machinery so later phases only add content, never structure. **Phase 0 lands in two commits for an auditable boundary:** first the plan (with the boxes below *unchecked*), then the scaffolding (which ticks them).

- [x] This work plan.
- [x] `docs/literature/` notes area with README.
- [x] `references.bib` seeded from the works already named in the Coastline and roadmap, every entry flagged `VERIFY` until Phase 1 confirms it.
- [x] `_note-template.md` — per-paper annotation template.
- [x] `index.md` — triage tracker (cluster, tier, claim/measure bearing, status).
- [x] `sources/` (local-only, git-ignored) and `notes/` directories with the source-handling policy README (§4).

**Exit:** structure committed and pushed; scaffolding-commit boxes ticked.

### Phase 1 — Corpus assembly & triage *(broad sweep)*

Populate the corpus across clusters A–G and verify every citation.

- Expand `references.bib` to the full broad-sweep corpus; **verify all bibliographic data** (authors, venue, year, volume/pages, DOI/arXiv) against primary sources — no entry leaves Phase 1 with a `VERIFY` flag.
- Acquire the original article for each corpus entry as a PDF into [`docs/literature/sources/`](literature/sources/) — **local-only, git-ignored** (see §4, Source-handling policy).
- For each entry, record in `index.md`: primary + secondary cluster, a one-line relevance note, the Coastline claim(s) and Claim IV measure(s) it touches, and a **tier**:
  - **Tier 1 (load-bearing)** — directly cited by, or directly testing, a Coastline claim or a Ledger discriminant. Receives a full Phase-2 note.
  - **Tier 2 (contextual)** — situates a cluster; skimmed, one-paragraph note.
  - **Tier 3 (peripheral)** — logged for completeness; abstract-level note only.
- **Cluster G entry gate.** A Cluster G paper enters the corpus only if (a) it is cited by ≥1 Tier-1 paper, or (b) it bears on a named Coastline anti-claim or deferred item. Cluster G papers are **capped at Tier 2** unless explicitly promoted, which requires a cluster reassignment recorded in `index.md`.
- **Scope cap.** If the Tier-1 set exceeds **25 papers**, stop and escalate to plan revision (§6) *before* proceeding to Phase 2. (Working expectation: Tier 1 ≈ 8–12.)
- Non-canonical triage calls (a paper that could sit in two clusters) are recorded in `index.md` as decisions with a one-line rationale, not asserted as facts.

**Exit:** complete, fully-verified bibliography; sources acquired locally; every entry triaged and tiered in `index.md`; Tier-1 set within cap (or plan revised).

### Phase 2 — Deep reading & structured annotation

Read and annotate the Tier-1 corpus. **The findings notes are the public record** (the PDFs are not — see §4).

- One note per Tier-1 paper from [`_note-template.md`](literature/_note-template.md), capturing: core claim, method, the relation to each of the five Coastline claims, which Claim IV measure (Fisher / mutual information / cross-probe mismatch / coarse-graining robustness) it instantiates or could, its relevance to nuisance-discrimination (Claim III), and its lineage/citation chain.
- Tier-2 papers get a one-paragraph note inline in `index.md`.
- **Ledger-candidate flagging.** A paper that itself makes a framework-relevant interpretive claim (Sorci-grade) is flagged in its note as `Ledger-candidate` with a one-line rationale. **No Ledger entry is opened mid-stream.** Triage of Ledger candidates occurs at the start of Phase 4.

**Exit:** every Tier-1 paper has a committed note; Tier-2 paragraphs in place; Ledger candidates flagged.

### Phase 3 — Synthesis

Cross-cut the notes into a single synthesis memo (`docs/literature/synthesis-v0.1.md`).

- **Claim-by-claim:** where the literature supports, strains, or is silent on each of the five Coastline claims.
- **Measure-by-measure:** state of the art for each Claim IV anchor, and which is best operationalised for temporal records.
- **Gaps & open questions:** including candidate falsification settings (Coastline Falsifiability §) and unresolved nuisance-discrimination problems.
- **Lineage audit:** confirm every "in the spirit of / following" attribution in the Coastline and Sail is bibliographically sound.

**Exit:** synthesis memo committed; gap list and lineage audit complete.

### Phase 4 — Feed-forward into artefacts

Map the synthesis onto concrete, roadmap-aligned deliverables. Each is a *separate* downstream act, opened only after Phase 3. **Begin by triaging the Phase-2 Ledger candidates** into open / defer / decline, with rationale.

- **Coastline v0.3:** resolve FIT citation + positioning bullet, GR-boundary statement, measure-registration protocol, "many" specification, Claim III softening.
- **Ledger:** open CL-2026-007 (Smith & Ahmadi 2020) and CL-2026-008 (distributed clock networks), plus any promoted Ledger candidates, grounded in the verified corpus.
- **Sail:** complete the reference apparatus (~25–35 refs) and lineage verification for the Sorci commentary; feeds the external-circulation stewardship decision.
- **Methodological notes:** open a methodological note (e.g. operational-measures note, temporal-redundancy toy-model functional — see roadmap) *if* the Phase-3 measure-by-measure synthesis surfaces a self-contained contribution warranting separate treatment.

**Exit:** Ledger candidates triaged; synthesis findings routed into named roadmap items; this plan's review phases marked complete.

---

## 4. Source-handling policy

Original article PDFs are **collected locally and never committed.** The public record of the review is our own analysis — the findings notes and synthesis — not the source documents.

- **Where:** `docs/literature/sources/`, git-ignored (only its `README.md` is tracked). Filenames match citekeys (`page1983.pdf`). See [`sources/README.md`](literature/sources/README.md).
- **Why:** publisher and preprint PDFs are copyrighted; redistributing them in a public repository would infringe. Our contribution — the per-paper findings in `notes/` and the synthesis — is original work under the repository's CC licences. Full identification in `references.bib` (DOI/arXiv) lets any reader obtain the same source independently, so reproducibility is preserved without redistribution.
- **Enforcement:** `.gitignore` blocks `docs/literature/sources/**` (except its README) and any `*.pdf` under the literature area. If `git status` shows a tracked `.pdf`, remove it from the index before committing.

---

## 5. Deliverables & repo layout

```
docs/
  literature-review-plan.md     ← this plan
  roadmap.md                    ← existing forward-looking items
  literature/
    README.md                   ← how the notes area is organised
    references.bib              ← single source of truth for citations
    index.md                    ← triage tracker (cluster · tier · bearing · status)
    _note-template.md           ← per-paper annotation template
    sources/                     ← original PDFs — LOCAL ONLY, git-ignored (README tracked)
      README.md
      <citekey>.pdf              (not committed)
    notes/                       ← findings: one file per Tier-1 paper (Phase 2) — PUBLIC
      <citekey>.md
    synthesis-v0.1.md            ← Phase 3 output — PUBLIC
```

---

## 6. Plan-revision protocol & scope guards

This plan is itself revisable, with explicit triggers so review cycles have termination and structural-revision conditions:

- **Tier-1 scope cap.** Tier 1 > 25 papers ⇒ stop, revise the plan, then resume (Phase 1).
- **Structural-finding trigger.** If Phase 1 or Phase 2 surfaces a finding that invalidates a cluster assignment or a Coastline claim, a **new plan version is drafted before the next phase exit**. The structural finding is not silently absorbed.
- A plan revision bumps the version (this doc) and records the trigger in the version history.

### Structural-finding log

- **2026-05-26 — `hartong2024` mis-attribution (Phase 2).** PDF extraction confirmed Hartong–Have–Obers–Pikovski (SciPost Phys. 16, 088) is a post-Newtonian *coupling-prescription* paper, not a Page–Wootters / relational-time paper. **Evaluation against the structural-finding trigger:** it does **not** invalidate the A–G cluster scheme (the paper stays in Cluster A as a methods/lineage node, down-tiered 1→2 — a triage decision, not a scheme change) and does **not** invalidate any of the five Coastline claims. It invalidates one *External-Constraints attribution inside the Coastline* — an artefact-level issue logged for the **Phase 4** Coastline pass, not a plan-structure issue. **Decision: no structural plan revision (v0.3) required;** recorded here so the finding is not silently absorbed.
- **2026-05-26 — Tier-1 down-tiering (steward call).** After extraction, Tier 1 was reduced 18 → 13 (demoted: `hartong2024`, `nambu2022`, `hohnsmith2021`, `brandao2015`, `giovannetti2011`, `fit2026`). Normal triage within the cap (the >25 trigger was never reached); recorded in `index.md`. No plan revision required.

---

## 7. Completion criteria

The review is complete when: (1) `references.bib` is fully verified with no `VERIFY` flags; (2) every corpus entry is tiered in `index.md` and the Tier-1 set is within cap (or the plan was revised); (3) every Tier-1 paper has a committed findings note; (4) the synthesis memo and lineage audit are committed; and (5) Phase-4 Ledger-candidate triage is done and findings are routed into named roadmap items.

---

## 8. Decisions

### Locked

- **CCUF-bridge material is excluded from this corpus.** CCUF-adjacent literature (L₀/L₁ unification, η-parameter work, comparison-geometry, timescale-coordination across gravitational potentials) is **held for a separate bridge review** and does not enter this plan's corpus. This honours the Coastline v0.2 deferral of the CCUF bridge under Lock-Key discipline; importing CCUF-adjacent literature here would implicitly import the bridge question into the present review's scope. The bridge review, if undertaken, gets its own work plan. *(Locked 2026-05-26, per Guardian review.)*

### Open

- **Reference manager.** BibTeX flat file (current default, version-controllable) vs. an exported library from a manager (Zotero/JabRef). Revisit if the corpus exceeds ~60 entries.
- **Tier-1 reading depth for Cluster G.** Adjacent foundations are entry-gated and Tier-2-capped (Phase 1); confirm during Phase 1 whether any Cluster-G work merits promotion (with cluster reassignment).

---

## 9. Version history

| Version | Date | Notes |
| --- | --- | --- |
| v0.1 | 2026-05-26 | Initial draft (pre-review). Comprehensive field map, broad-sweep scope; seven clusters; five phases; tier triage; VERIFY discipline. Not committed — superseded by v0.2 after Guardian review. |
| v0.2 | 2026-05-26 | Guardian-review refinements: (1) Tier-1 scope cap (≤25, else plan revision); (2) Cluster G entry gate + Tier-2 cap; (3) Ledger-candidate flagging deferred to Phase 4; (4) plan-revision protocol with structural-finding trigger (§6); (5) two-commit Phase 0 boundary. CCUF-bridge material **locked** out of corpus (§8). Added: structural-plan/calendar-separation note (§1); **source-handling policy** — PDFs local-only/git-ignored, findings notes public (§4); Phase-4 methodological-notes deliverable; Cluster E flagged high-traffic; non-canonical cluster calls recorded as decisions. |
| v0.2.1 | 2026-05-26 | Documentation/decision update (no structural change). Recorded the §6 structural-finding log: `hartong2024` mis-attribution evaluated — no v0.3 revision required (artefact-level, logged for Phase 4); Tier-1 down-tiering 18→13 recorded. Not a structural revision; clusters/claims/phases unchanged. |

---

*This is a living planning document under Local Stewardship. It governs an upstream literature review and does not itself revise any Coastline, Ledger, or Sail artefact.*
