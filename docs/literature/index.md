# Corpus triage index

Running tracker for the literature review ([work plan](../literature-review-plan.md)). One row per corpus entry, keyed to [`references.bib`](references.bib).

**Clusters:** A Page–Wootters · B Quantum Darwinism · C Quantum clocks · D Fisher information · E Relativistic/gravitational decoherence · F Distributed clock networks · G Adjacent foundations.
**Tier:** 1 load-bearing (full note) · 2 contextual (paragraph) · 3 peripheral (abstract).
**Status:** `seed` → `verified` (bib confirmed against primary sources, Phase 1) → `src` (PDF acquired locally to [`sources/`](sources/), Phase 1) → `noted` (findings annotated, Phase 2). Source PDFs are local-only and never committed — see [work plan §4](../literature-review-plan.md#4-source-handling-policy).

**Phase 1 bibliographic verification: complete (2026-05-26).** All entries confirmed against Crossref / arXiv / ADS / publisher. PDF acquisition (`src`) and final tiering follow.

| Citekey | Cluster | Tier | Bears on (claim / measure) | Status |
| --- | --- | --- | --- | --- |
| `page1983` | A | 1 | Claim V relational channel; External Constraints | verified |
| `smith2020` | A | 1 | Claim V (bipartite); CL-2026-007 | verified |
| `hartong2024` | A | 1 | External Constraints — ⚠ lineage flag (see below) | verified |
| `mendes2019` | A | 2 | Claim I (time observables); Coastline cites as "2018" | verified |
| `nambu2022` | A · D | 1 | Claim IV (Fisher information) | verified |
| `hohnsmith2021` | A | 1 | Claim V (relational-dynamics unification) | verified |
| `zurek2003` | B | 1 | Claim II (einselection background) | verified |
| `zurek2009` | B | 1 | Claim II (redundancy architecture) | verified |
| `ollivier2004` | B | 1 | Claim II (objectivity criteria) | verified |
| `ollivier2005` | B | 2 | Claim II (2005 follow-up) | verified |
| `riedel2010` | B | 1 | Claim II; toy-model functional | verified |
| `riedel2011` | B | 2 | Claim II (NJP companion) | verified |
| `korbicz2014` | B | 2 | Claim II (spectrum-broadcast structure) | verified |
| `brandao2015` | B | 1 | Claim II (generic objectivity) | verified |
| `giovannetti2011` | D | 1 | Claim IV (QFI / Cramér–Rao) | verified |
| `fit2026` | D | 1 | Claim IV (Fisher); v0.3 citation — recency caveat | verified |
| `sorci2026` | C | 1 | Claim III witness; CL-2026-006 | verified |
| `margalit2015` | C · E | 2 | Claim III (which-path / clock) | verified |
| `martinezlahuerta2022` | C · E | 2 | Claim III nuisance (mass defect) | verified |
| `yudin2018` | C · E | 2 | Claim III nuisance (mass defect) | verified |
| `ludlow2015` | C | 2 | Experimental substrate (clock review) | verified |
| `zych2011` | E | 1 | Claim III witness lineage (Sail) | verified |
| `pikovski2015` | E | 1 | Claim III nuisance-discrimination | verified |
| `komar2014` | F | 1 | Claim V (multipartite) | verified |
| `covey2025` | F | 1 | Claim V; CL-2026-008 (GR boundary) | verified |
| `fromonteil2025` | F | 1 | Claim V; CL-2026-008 (preprint) | verified |
| `connes1994` | G | 3 | Deferred: thermal/arrow-of-time | verified |
| `rovelli1996` | G | 3 | Relational-QM backdrop | verified |

**28 entries** (21 seeded — 3 renamed to publication year/full key — plus 7 broad-sweep additions: `hohnsmith2021`, `ollivier2005`, `riedel2011`, `korbicz2014`, `brandao2015`, `giovannetti2011`, `ludlow2015`).

## Phase 1 findings & flags

**Placeholders resolved.** All "VERIFY" placeholders are now real papers:
- `hartong2024` → SciPost Phys. 16, 088 (2024), *A coupling prescription for post-Newtonian corrections in quantum mechanics*.
- `mendes2019` → Proc. R. Soc. A 475, 20190470 (**2019**), *Time as a consequence of internal coherence*; first author **Leandro R. S.** Mendes (seed had "Lucas C." — corrected).
- `nambu2022` → Universe 8, 99 (2022), *Qubit Clock in Quantum Cosmology*.
- `sorci2026` → PRL 136, 163602 (2026), *Quantum signatures of proper time in optical ion clocks* (Sorci, Foo, Leibfried, Sanner, Pikovski).
- `martinezlahuerta2022` → PRA 106, 032803 (2022); `yudin2018` → Laser Phys. Lett. 15, 035703 (2018).
- `covey2025` → PRX Quantum 6, 030310 (2025); `fromonteil2025` → arXiv:2509.19501 (preprint only).
- `fit2026` → arXiv:2605.03958 (2026), sole author J. Sumaya-Martinez — verified via arXiv API only (not yet web-indexed; re-confirm author/title against the PDF before external citation).

**Lineage flags for the Phase 3 audit (do not edit artefacts now — Phase 4):**
1. ⚠ **`hartong2024`** — Coastline External Constraints lists this among "modern developments" of Page–Wootters, but the paper is a covariant post-Newtonian (1/c²) coupling prescription, *not* a relational-time paper. The attribution needs revisiting.
2. **`mendes2019`** — Coastline cites "Mendes & Soares-Pinto **2018**"; the published paper is **2019** (2018 is the preprint year). Minor citation-year fix.
3. **`sorci2026`** — full author list now known: **Leibfried & Sanner are co-authors** of the subject paper. This directly informs the roadmap's pending Sail acknowledgement decision (proximity-signal risk) — they are not third parties but authors of the work being commented on.

**Tiering note.** The Tier-1 set currently stands at **18 papers** — within the plan's hard cap (25) but above the 8–12 working expectation ([work plan §6](../literature-review-plan.md#6-plan-revision-protocol--scope-guards)). A steward down-tiering pass is recommended before Phase 2 (candidates to demote to Tier 2: `hartong2024`, `nambu2022`, `hohnsmith2021`, `brandao2015`, `giovannetti2011`, `fit2026`).

## Next in Phase 1

- Acquire PDFs into [`sources/`](sources/) (local-only). All except `page1983` are open-access on arXiv.
- Optional broad-sweep additions still uncaptured (add only under the Cluster-G/entry-gate rules): GLM 2011 *Quantum Cramér–Rao* review (have `giovannetti2011`), Höhn–Smith–Lock follow-ups, Smith–Ahmadi 2019 *quantizing time*, Marletto–Vedral. Promote only if a Tier-1 paper cites them or they bear on a named anti-claim/deferred item.
