# Temporal Micro Consensus

A Harbour repository for the *Consensus-Emergence of Classical Proper Time* framework, with associated Breakwater Ledger entries and Sails.

| Field | Value |
| --- | --- |
| Status | Draft — Local Stewardship |
| Steward | U. Warring (Physikalisches Institut, Albert-Ludwigs-Universität Freiburg) |
| Origin date | 2026-05-23 |
| Scope | Framework note (Coastline), claim classifications (Ledger), commentaries (Sails), presentational vantage-points (Views); supported by methodological notes (`docs/notes/`), a numerical toolkit (`numerics/`), and work plans (`workplans/`) |
| Website | <https://uwarring82.github.io/temporal-micro-consensus/> (current versions; GitHub Pages) |
| Latest release | `framework-status-2026.05.29` (2026-05-29; first to include the Harbour View artefact category and the first Harbour View, v0.1). Its Zenodo version DOI is minted post-tag and folded back at the post-mint commit. |
| Prior release | `framework-status-2026.05.27`, DOI [10.5281/zenodo.20411120](https://doi.org/10.5281/zenodo.20411120). |

## What this repository contains

This repository holds four related artefact families:

1. **Coastline** (`coastlines/`) — versioned framework notes. The current Coastline is *Consensus-Emergence of Classical Proper Time*, a proposal that classical proper time should be treated as an emergent collective variable supported redundantly across many microscopic temporal records, in the spirit of the Page–Wootters mechanism and quantum Darwinism but distinct from both.
2. **Ledger** (`ledger/`) — classification entries in the Breakwater Claim Analysis Ledger (schema v1.0-rc). Each entry classifies an external scientific claim against a named Harbour framework under a declared evaluating measure, with explicit discriminant conditions for upgrade or downgrade. Entries: CL-2026-006 (Sorci et al., PRL 136, 163602, 2026), CL-2026-007 (Smith & Ahmadi, Nat. Commun. 11, 5360, 2020), and CL-2026-008 (distributed entanglement-enhanced clock networks — Covey et al. 2025 + Fromonteil et al. 2025), classified under the Coastline.
3. **Sails** (`sails/`) — commentaries and essays that translate framework-relative work into prose for broader readership. The current Sail (v0.4) is a commentary on Sorci et al., anchored to Coastline v0.4, with its Ledger anchor kept at CL-2026-006 v0.2 (a mixed anchor noted in the Sail).
4. **Views** (`views/`) — presentational vantage-points: externally-readable, citable consolidations of a body of project work derived from but *not authoritative over* the underlying Coastline / Ledger / Sail notes. The artefact category is specified by [`docs/harbour-view-structural-deliberation-note-v0.6.md`](docs/harbour-view-structural-deliberation-note-v0.6.md). The first View is *Harbour View — Temporal Redundancy and Emergent Proper Time* ([`views/view-framework-overview-v0.1.md`](views/view-framework-overview-v0.1.md)).

Two supporting families sit alongside the four artefact families above:

- A **numerical toolkit** ([`numerics/`](numerics/)) — the `tmc-numerics` package implementing the framework's declared anchor measures (`I(C:M)`, `F[τ]`, `R_δ`) under a master-equation backbone, with two priority modules: Module 3a (Sorci D1 nuisance budget) and Module 3b (the open temporal instrument). Backed by an 85-test suite ([`numerics/README.md`](numerics/README.md)).
- Forward-looking **work plans** ([`workplans/`](workplans/)) — the toolkit work plan and the D6-locked Phase-1 / Phase-2 API contracts and per-module contracts (Module 3a, Module 3b).

A `docs/` subdirectory holds forward-looking documentation (roadmap, logbook, literature-review plan) and the [`tutorial`](docs/tutorial.md) — a guided on-ramp for first-time visitors. Authored **methodological notes** (instruments for the framework — e.g. the temporal-redundancy functional) live in [`docs/notes/`](docs/notes/).

## Repository structure

```
temporal-micro-consensus/
├── README.md
├── CITATION.cff                      (machine-readable citation metadata)
├── LICENSE-MIT                       (code, scripts, configuration)
├── LICENSE-CC-BY-SA-4.0              (Coastlines, Ledger entries, docs/)
├── LICENSE-CC-BY-NC-SA-4.0           (Sails, authored prose)
├── .gitignore
├── coastlines/
│   ├── consensus-emergence-v0.1.md
│   ├── consensus-emergence-v0.2.md
│   ├── consensus-emergence-v0.3.md
│   └── consensus-emergence-v0.4.md   (current)
├── ledger/
│   ├── CL-2026-006-sorci-v0.1.md
│   ├── CL-2026-006-sorci-v0.2.md
│   ├── CL-2026-006-sorci-v0.3.md
│   ├── CL-2026-006-sorci-v0.4.md
│   ├── CL-2026-006-sorci-v0.5.md
│   ├── CL-2026-006-sorci-v0.5.1.md        (current; patch revision — stale MN cross-refs)
│   ├── CL-2026-007-smith-ahmadi-v0.1.md
│   ├── CL-2026-007-smith-ahmadi-v0.2.md
│   ├── CL-2026-007-smith-ahmadi-v0.3.md   (current)
│   ├── CL-2026-008-clock-networks-v0.1.md
│   └── CL-2026-008-clock-networks-v0.2.md (current)
├── sails/
│   ├── sorci-commentary-v0.1.md
│   ├── sorci-commentary-v0.2.md
│   ├── sorci-commentary-v0.3.md
│   └── sorci-commentary-v0.4.md     (current)
├── views/                            (presentational vantage-points — Harbour Views)
│   ├── view-framework-overview-v0.1.md     (current; first View)
│   └── figures/                      (View-resident figures: schematics + data figures)
├── numerics/                         (tmc-numerics toolkit — master-equation backbone + anchor measures)
│   ├── README.md
│   ├── pyproject.toml                (dependency lower bounds; exact env pinned per Toolkit Provenance in views/)
│   ├── requirements.txt
│   ├── src/                          (tmc_numerics package)
│   ├── tests/                        (85-test suite)
│   ├── examples/                     (notebooks regenerating committed results)
│   └── results/                      (committed JSON results — Module 3a + Module 3b)
├── docs/
│   ├── tutorial.md                   (guided on-ramp for first-time visitors)
│   ├── roadmap.md
│   ├── logbook.md                    (project logbook — provenance / FAIR)
│   ├── literature-review-plan.md
│   ├── harbour-view-structural-deliberation-note-v0.6.md  (Views artefact-category specification)
│   ├── view-framework-overview-v0.1-pilot-reader-brief.md (first-View pilot-reader brief, closed-call audit record)
│   ├── notes/                        (methodological notes — instruments for the framework)
│   │   ├── temporal-redundancy-functional-v0.1.md
│   │   ├── temporal-redundancy-functional-v0.2.md
│   │   └── temporal-redundancy-functional-v0.3.md  (current)
│   ├── memos/                        (research-direction memoranda; not artefacts, not under review discipline)
│   │   └── anti-claim-6-analytical-route.md       (parked 2026-05-28: relational temporal Darwinism)
│   └── literature/                   (literature review)
│       ├── README.md
│       ├── references.bib            (verified bibliography)
│       ├── index.md                  (corpus triage tracker)
│       ├── synthesis-v0.1.md         (Phase-3 synthesis)
│       ├── notes/                    (per-paper findings — public)
│       └── sources/                  (original PDFs — local-only, git-ignored)
└── workplans/
    ├── toolkit-work-plan-v0.1.md                          (numerical toolkit work plan — current)
    ├── toolkit-phase1-api-contract-v0.1.md                (D6-locked Phase-1 public API)
    ├── toolkit-phase2-api-contract-v0.1.md                (D6-locked Phase-2 anchor-measure post-processors)
    ├── toolkit-module3a-sorci-contract-v0.1.md            (Module 3a — Sorci D1 nuisance budget)
    └── toolkit-module3b-open-instrument-contract-v0.1.md  (Module 3b — open temporal instrument)
```

## Version conventions

Every document in this repository carries an explicit version number (e.g. *v0.2*) in its metadata table and filename. Citations of documents in this repository **must** include the version number; the documents are versioned because the framework is under active development and earlier versions may differ in load-bearing ways from later ones.

Version history is recorded internally in each document's *Version History* table. The repository's Git history provides the external audit trail.

Documents in this repository are issued under **Local Stewardship**. They do not claim parity with externally validated physical laws and are not endorsed by any institution.

## Citation

When citing a document from this repository in dependent work, use the following template:

> Warring, U. *[Document title]*, version [v0.X], Temporal Micro Consensus repository, [date]. Commit hash: [hash].

For example:

> Warring, U. *Consensus-Emergence of Classical Proper Time*, v0.2, Temporal Micro Consensus repository, 2026-05-23.

To cite the repository as a whole at a fixed snapshot, use the Zenodo version DOI for that snapshot's release:

- **`framework-status-2026.05.29`** (current; 2026-05-29) — Zenodo version DOI minted post-tag and folded back into this README + [`CITATION.cff`](CITATION.cff) at the post-mint commit.
- **`framework-status-2026.05.27`** (prior) — DOI [10.5281/zenodo.20411120](https://doi.org/10.5281/zenodo.20411120).

Internal cross-references between documents in this repository use document name and version only (e.g. *Coastline v0.2*, *CL-2026-006 v0.2*).

## FAIR principles

This repository is maintained according to the **FAIR** principles (Findable, Accessible, Interoperable, Reusable):

- **Findable** — machine-readable citation metadata in [`CITATION.cff`](CITATION.cff) (GitHub renders a "Cite this repository" button); every document carries an explicit version, and the Git history is the external audit trail; a verified, DOI/arXiv-tagged bibliography lives in [`docs/literature/references.bib`](docs/literature/references.bib). The repository is archived at persistent **Zenodo DOIs** per release: current `framework-status-2026.05.29` (DOI minted post-tag), prior `framework-status-2026.05.27` ([10.5281/zenodo.20411120](https://doi.org/10.5281/zenodo.20411120)). FAIR-Findability is complete; the per-release DOI chain is the time-stamped citation backbone.
- **Accessible** — public repository, open licences (below), no access barriers; all content is plain-text Markdown and BibTeX, retrievable over standard HTTP(S)/Git. (Original article PDFs are *not* redistributed — they are copyrighted; the public record is our own findings notes. See [`docs/literature/sources/README.md`](docs/literature/sources/README.md).)
- **Interoperable** — standard, tool-neutral formats (Markdown, BibTeX, Citation File Format, SPDX licence identifiers); references carry DOIs/arXiv IDs; the internal controlled vocabulary (Coastline / Ledger / Sail / Breakwater, and the framework's claim labels) is defined in-document.
- **Reusable** — explicit split licensing, per-document *Version History* tables, end-to-end provenance via the project logbook ([`docs/logbook.md`](docs/logbook.md)) and Git, and a documented source-handling policy. Each artefact states what it does and does not claim (Endorsement Marker, Anti-Claims).

The **project logbook** ([`docs/logbook.md`](docs/logbook.md)) is the append-only provenance record: it logs decisions, version issuances, phase transitions, and factual corrections, each stamped with date, actor, rationale, and resulting commit.

## Split licence

This repository uses a three-part split licence following the T(h)reehouse convention:

- **MIT licence** — any code, scripts, configuration files, or computational artefacts. See `LICENSE-MIT`.
- **CC BY-SA 4.0** — Coastline framework notes and Breakwater Ledger entries (`coastlines/`, `ledger/`). These are the framework infrastructure; they are shareable and adaptable under attribution and share-alike. See `LICENSE-CC-BY-SA-4.0`.
- **CC BY-NC-SA 4.0** — Sails and other authored prose (`sails/`). These are commentaries and essays where authorial voice is load-bearing; they are shareable for non-commercial use under attribution and share-alike. See `LICENSE-CC-BY-NC-SA-4.0`.

When in doubt about which licence applies to a particular file, the document type indicated by its directory placement governs. The `docs/` directory contains documentation and planning artefacts (`tutorial.md`, `roadmap.md`, `logbook.md`, `literature-review-plan.md`, the Views-category specification and pilot-reader brief) under the same **CC BY-SA 4.0** licence as Coastlines and Ledgers; the `workplans/` directory (planning artefacts) and the `views/` directory (presentational vantage-points derived from framework-internal Coastline/Ledger/MN material) are likewise **CC BY-SA 4.0**; the `numerics/` directory (code, scripts, configuration, test suite, example notebooks, committed JSON results) is **MIT** per `numerics/pyproject.toml`. Authored methodological notes or prose essays in `docs/` would fall under **CC BY-NC-SA 4.0** if authorial voice is load-bearing. A future consolidation into a single CC BY-SA 4.0 licence may be considered if multi-licence compilation downstream becomes the dominant use case; this question is registered in the roadmap.

## Relationship to other Harbour artefacts

This repository operates within the broader Open-Science Harbour architecture maintained by the steward. Relevant adjacent artefacts (not contained here):

- **CCUF** (Causal Clock Unification Framework) — a separate framework operating at the L₁ (architectural / network) scale, where Consensus-Emergence operates at the L₀ (microscopic) scale. A possible L₀/L₁ bridge is registered as a deferred item in Coastline v0.2 and tracked in the roadmap.
- **Open-Science Harbour council architecture** — Council-3 ADM-EC (and its Council-5 extension with Scout and Verifier stances) provides the deliberation protocol under which this repository's documents have been developed.
- **Breakwater Claim Analysis Ledger** — the schema (v1.0-rc) is maintained outside this repository; entries in `ledger/` instantiate that schema for claims classified under this repository's Coastline.

## How to read this repository

If you are encountering this repository for the first time:

1. Start with the [`docs/tutorial.md`](docs/tutorial.md) for a guided introduction to the concepts, architecture, and current state. Foundations-metrology readers with no prior project background may prefer the first **Harbour View** ([`views/view-framework-overview-v0.1.md`](views/view-framework-overview-v0.1.md)) — a single externally-readable presentation of the framework, its methodology, and its first worked exemplar.
2. Read the most recent Coastline (`coastlines/consensus-emergence-v0.4.md`) for the authoritative framework statement.
3. Read the most recent Sail (`sails/sorci-commentary-v0.4.md`) to see how the framework is applied in a concrete case.
4. Consult the Sorci Ledger entry (`ledger/CL-2026-006-sorci-v0.5.1.md`) for the framework-relative classification underwriting the Sail. (v0.5 is the substantive issuance — Module 3a quantitative grounding of D1; v0.5.1 is a 2026-05-29 patch revision that updated three stale MN v0.2 → MN v0.3 cross-references with no content change.)
5. Consult `docs/roadmap.md` for what is in active development and what is deferred.

Earlier versions are retained for transparency; readers comparing against current claims should always use the latest version.

## Contact

Repository steward: U. Warring, Physikalisches Institut, Albert-Ludwigs-Universität Freiburg.

Documents are draft and under Local Stewardship. Substantive engagement is welcome through the steward; the repository does not yet have a public issue-tracking or contribution workflow.

---

*This README is part of the repository scaffolding and is itself versioned by Git. The repository was scaffolded on 2026-05-23.*
