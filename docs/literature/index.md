# Corpus triage index

Running tracker for the literature review ([work plan](../literature-review-plan.md)). One row per corpus entry. Seeded in Phase 0 from [`references.bib`](references.bib); all entries start **unverified**.

**Clusters:** A Page–Wootters · B Quantum Darwinism · C Quantum clocks · D Fisher information · E Relativistic/gravitational decoherence · F Distributed clock networks · G Adjacent foundations.
**Tier:** 1 load-bearing (full note) · 2 contextual (paragraph) · 3 peripheral (abstract).
**Status:** `seed` (placeholder) → `verified` (bib confirmed, Phase 1) → `src` (PDF acquired locally to [`sources/`](sources/), Phase 1) → `noted` (findings annotated, Phase 2). Source PDFs are local-only and never committed — see [work plan §4](../literature-review-plan.md#4-source-handling-policy).

| Citekey | Cluster | Tier | Bears on (claim / measure) | Status |
| --- | --- | --- | --- | --- |
| `page1983` | A | 1 | Claim V relational channel; External Constraints | seed |
| `smith2020` | A | 1 | Claim V (bipartite); CL-2026-007 | seed |
| `hartong2024` | A | 1 | External Constraints (coupling prescription) | seed |
| `mendes2018` | A | 2 | Claim I (time observables) | seed |
| `nambu2022` | A · D | 1 | Claim IV (Fisher information) | seed |
| `zurek2003` | B | 1 | Claim II (einselection background) | seed |
| `zurek2009` | B | 1 | Claim II (redundancy architecture) | seed |
| `ollivier2004` | B | 1 | Claim II (objectivity criteria) | seed |
| `riedel2010` | B | 1 | Claim II; toy-model functional | seed |
| `sorci2026` | C | 1 | Claim III witness; CL-2026-006 | seed |
| `margalit2015` | C · E | 2 | Claim III (which-path / clock) | seed |
| `martinezlahuerta2022` | C · E | 2 | Claim III nuisance (mass defect) | seed |
| `yudin` | C · E | 2 | Claim III nuisance (mass defect) | seed |
| `fit2026` | D | 1 | Claim IV (Fisher); v0.3 citation | seed |
| `zych2011` | E | 1 | Claim III witness lineage (Sail) | seed |
| `pikovski2015` | E | 1 | Claim III nuisance-discrimination | seed |
| `komar2014` | F | 1 | Claim V (multipartite) | seed |
| `covey2025` | F | 1 | Claim V; CL-2026-008 | seed |
| `fromonteil2025` | F | 1 | Claim V; CL-2026-008 | seed |
| `connes1994` | G | 3 | Deferred: thermal/arrow-of-time | seed |
| `rovelli1996` | G | 3 | Relational-QM backdrop | seed |

> **Phase 1 will:** verify every row's bibliography (clear `VERIFY` flags in `references.bib`), confirm tiers, and add the broad-sweep entries not yet seeded (e.g. Giovannetti–Lloyd–Maccone quantum-metrology reviews, Höhn–Smith–Lock relational-dynamics trinity, Korbicz spectrum-broadcast structure, Brandão–Piani–Horodecki generic objectivity, Ludlow et al. optical-clock review). Add rows as they enter the corpus.
