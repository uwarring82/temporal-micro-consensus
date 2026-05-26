# Harbour — Temporal Consensus

A Harbour repository for the *Consensus-Emergence of Classical Proper Time* framework, with associated Breakwater Ledger entries and Sails.

| Field | Value |
| --- | --- |
| Status | Draft — Local Stewardship |
| Steward | U. Warring (Physikalisches Institut, Albert-Ludwigs-Universität Freiburg) |
| Origin date | 2026-05-23 |
| Scope | Framework note (Coastline), claim classifications (Ledger), commentaries (Sails) |

## What this repository contains

This repository holds three related artefact families:

1. **Coastline** (`coastlines/`) — versioned framework notes. The current Coastline is *Consensus-Emergence of Classical Proper Time*, a proposal that classical proper time should be treated as an emergent collective variable supported redundantly across many microscopic temporal records, in the spirit of the Page–Wootters mechanism and quantum Darwinism but distinct from both.
2. **Ledger** (`ledger/`) — classification entries in the Breakwater Claim Analysis Ledger (schema v1.0-rc). Each entry classifies an external scientific claim against a named Harbour framework under a declared evaluating measure, with explicit discriminant conditions for upgrade or downgrade. The current entry is CL-2026-006, classifying Sorci et al. (PRL 136, 163602, 2026) under the Coastline.
3. **Sails** (`sails/`) — commentaries and essays that translate framework-relative work into prose for broader readership. The current Sail is a commentary on Sorci et al., anchored to Coastline v0.2 and Ledger CL-2026-006 v0.2.

A `docs/` subdirectory holds forward-looking documentation including the active roadmap.

## Repository structure

```
harbour-temporal-consensus/
├── README.md
├── LICENSE-MIT                       (code, scripts, configuration)
├── LICENSE-CC-BY-SA-4.0              (Coastlines, Ledger entries)
├── LICENSE-CC-BY-NC-SA-4.0           (Sails, authored prose)
├── .gitignore
├── coastlines/
│   ├── consensus-emergence-v0.1.md
│   └── consensus-emergence-v0.2.md
├── ledger/
│   ├── CL-2026-006-sorci-v0.1.md
│   └── CL-2026-006-sorci-v0.2.md
├── sails/
│   ├── sorci-commentary-v0.1.md
│   └── sorci-commentary-v0.2.md
└── docs/
    └── roadmap.md
```

## Version conventions

Every document in this repository carries an explicit version number (e.g. *v0.2*) in its metadata table and filename. Citations of documents in this repository **must** include the version number; the documents are versioned because the framework is under active development and earlier versions may differ in load-bearing ways from later ones.

Version history is recorded internally in each document's *Version History* table. The repository's Git history provides the external audit trail.

Documents in this repository are issued under **Local Stewardship**. They do not claim parity with externally validated physical laws and are not endorsed by any institution.

## Citation

When citing a document from this repository in dependent work, use the following template:

> Warring, U. *[Document title]*, version [v0.X], Harbour — Temporal Consensus repository, [date]. Commit hash: [hash].

For example:

> Warring, U. *Consensus-Emergence of Classical Proper Time*, v0.2, Harbour — Temporal Consensus repository, 2026-05-23.

Internal cross-references between documents in this repository use document name and version only (e.g. *Coastline v0.2*, *CL-2026-006 v0.2*).

## Split licence

This repository uses a three-part split licence following the T(h)reehouse convention:

- **MIT licence** — any code, scripts, configuration files, or computational artefacts. See `LICENSE-MIT`.
- **CC BY-SA 4.0** — Coastline framework notes and Breakwater Ledger entries (`coastlines/`, `ledger/`). These are the framework infrastructure; they are shareable and adaptable under attribution and share-alike. See `LICENSE-CC-BY-SA-4.0`.
- **CC BY-NC-SA 4.0** — Sails and other authored prose (`sails/`). These are commentaries and essays where authorial voice is load-bearing; they are shareable for non-commercial use under attribution and share-alike. See `LICENSE-CC-BY-NC-SA-4.0`.

When in doubt about which licence applies to a particular file, the document type indicated by its directory placement governs. A future consolidation into a single CC BY-SA 4.0 licence may be considered if multi-licence compilation downstream becomes the dominant use case; this question is registered in the roadmap.

## Relationship to other Harbour artefacts

This repository operates within the broader Open-Science Harbour architecture maintained by the steward. Relevant adjacent artefacts (not contained here):

- **CCUF** (Causal Clock Unification Framework) — a separate framework operating at the L₁ (architectural / network) scale, where Consensus-Emergence operates at the L₀ (microscopic) scale. A possible L₀/L₁ bridge is registered as a deferred item in Coastline v0.2 and tracked in the roadmap.
- **Open-Science Harbour council architecture** — Council-3 ADM-EC (and its Council-5 extension with Scout and Verifier stances) provides the deliberation protocol under which this repository's documents have been developed.
- **Breakwater Claim Analysis Ledger** — the schema (v1.0-rc) is maintained outside this repository; entries in `ledger/` instantiate that schema for claims classified under this repository's Coastline.

## How to read this repository

If you are encountering this repository for the first time:

1. Start with the most recent Coastline (`coastlines/consensus-emergence-v0.2.md`) to understand the framework.
2. Read the most recent Sail (`sails/sorci-commentary-v0.2.md`) to see how the framework is applied in a concrete case.
3. Consult the most recent Ledger entry (`ledger/CL-2026-006-sorci-v0.2.md`) for the framework-relative classification underwriting the Sail.
4. Consult `docs/roadmap.md` for what is in active development and what is deferred.

Earlier versions are retained for transparency; readers comparing against current claims should always use the latest version.

## Contact

Repository steward: U. Warring, Physikalisches Institut, Albert-Ludwigs-Universität Freiburg.

Documents are draft and under Local Stewardship. Substantive engagement is welcome through the steward; the repository does not yet have a public issue-tracking or contribution workflow.

---

*This README is part of the repository scaffolding and is itself versioned by Git. The repository was scaffolded on 2026-05-23.*
