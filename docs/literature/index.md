# Corpus triage index

Running tracker for the literature review ([work plan](../literature-review-plan.md)). One row per corpus entry, keyed to [`references.bib`](references.bib).

**Clusters:** A Page–Wootters · B Quantum Darwinism · C Quantum clocks · D Fisher information · E Relativistic/gravitational decoherence · F Distributed clock networks · G Adjacent foundations.
**Tier:** 1 load-bearing (full note) · 2 contextual (paragraph) · 3 peripheral (abstract).
**Status:** `seed` → `verified` (bib confirmed against primary sources, Phase 1) → `src` (PDF acquired locally to [`sources/`](sources/), Phase 1) → `noted` (findings note written in [`notes/`](notes/)). Source PDFs are local-only and never committed — see [work plan §4](../literature-review-plan.md#4-source-handling-policy).

**Phase 1 verification: complete (2026-05-26).** All entries confirmed against Crossref / arXiv / ADS / publisher.
**Sources acquired + extraction pass: complete (2026-05-26).** 28 PDFs in `sources/` (local-only), each renamed to its citekey; one findings note per PDF in `notes/`. These are *extraction-grade* notes (summary · key points · relevance · flags) — they seed, but do not yet replace, the full per-claim Phase-2 annotation.

| Citekey | Cluster | Tier | Bears on (claim / measure) | Status |
| --- | --- | --- | --- | --- |
| `page1983` | A | 1 | Claim V relational channel; External Constraints | noted |
| `smith2020` | A | 1 | Claim V (bipartite); Claim IV (Fisher); CL-2026-007 | noted |
| `hartong2024` | A | 2† | ⚠ confirmed **not** Page–Wootters — post-Newtonian coupling/methods node (cited by `sorci2026`); down-tiered 1→2 | noted |
| `mendes2019` | A | 2 | Claim I/II (internal-coherence order parameter); Coastline cites as "2018" | noted |
| `nambu2022` | A · D | 1 | Claim IV (Fisher); Claim III (F_Q=0 ⇔ no clock) | noted |
| `hohnsmith2021` | A | 1 | Claim V (relational-dynamics equivalence) | noted |
| `zurek2003` | B | 1 | Claim II (einselection background) | noted |
| `zurek2009` | B | 1 | Claim II (redundancy architecture) | noted |
| `ollivier2004` | B | 1 | Claim II (objectivity criteria) | noted |
| `ollivier2005` | B | 2 | Claim II; ⚠ §VII "objective histories" = closest configurational precursor | noted |
| `riedel2010` | B | 1 | Claim II; toy-model functional | noted |
| `riedel2011` | B | 2 | Claim III (decoherence rate ≠ record-keeping rate) | noted |
| `korbicz2014` | B | 2 | Claim II/III (spectrum-broadcast structure) | noted |
| `brandao2015` | B | 1 | Claim II (generic objectivity) | noted |
| `giovannetti2011` | D | 1 | Claim IV (QFI / Cramér–Rao) | noted |
| `fit2026` | D | 1 | Claim IV (Fisher); kindred single-trajectory proposal | noted |
| `sorci2026` | C | 1 | Claim III witness; Claim IV (visibility); CL-2026-006 | noted |
| `margalit2015` | C · E | 2 | Claim III (which-path / clock) | noted |
| `martinezlahuerta2022` | C · E | 2 | Claim III nuisance (mass defect) | noted |
| `yudin2018` | C · E | 2 | Claim III nuisance (mass defect) | noted |
| `ludlow2015` | C | 2 | Experimental substrate; TAI/UTC consensus-time | noted |
| `zych2011` | E | 1 | Claim III witness lineage (Sail) | noted |
| `pikovski2015` | E | 1 | Claim III nuisance-discrimination | noted |
| `zych2019` | E | 1 | Claim I/III machinery; composite-system action behind `sorci2026` | noted |
| `komar2014` | F | 1 | Claim V (multipartite) | noted |
| `covey2025` | F | 1 | Claim V; Claim IV (3-node cross-probe mismatch); CL-2026-008 | noted |
| `fromonteil2025` | F | 1 | Claim V; CL-2026-008 (preprint) | noted |
| `connes1994` | G | 3 | Claim V positioning (thermal time — non-redundancy emergent time) | noted |
| `rovelli1996` | G | 3 | Claim V positioning (relational QM) | noted |

**29 entries — all with PDFs (local-only) + findings notes.** `zych2019` (source of the `sorci2026` Hamiltonian) was added during extraction and is now complete. † = down-tiered with rationale (see below).

## Phase 1 findings & flags (verification)

All "VERIFY" placeholders resolved to real papers. Notable corrections: `mendes2019` is published **2019** (Coastline cites "2018"; first author **Leandro R. S.** Mendes); `sorci2026` = *Quantum Signatures of Proper Time in Optical Ion Clocks* (Sorci, Foo, **Leibfried**, **Sanner**, Pikovski); `fit2026` verified via arXiv API only (re-check author/title against PDF before external citation).

## Phase 2 findings (extraction)

- ⚠ **`hartong2024` lineage flag — confirmed and acted on.** Reading the PDF confirms it is a covariant **post-Newtonian coupling prescription** (1/c² Klein–Gordon on Newton–Cartan backgrounds, worked for Kerr), with *no* clock-conditioning or relational-time content. The Coastline External Constraints currently lists it among "modern developments" of Page–Wootters — that attribution is **wrong** and must be fixed in the Phase-4 Coastline pass. Corpus action taken: down-tiered A·1 → A·2 and re-described as a methods/lineage node (it is the source of the curved-background coupling used by `sorci2026`).
- ⚠ **`ollivier2005` §VII "objective histories".** The 2005 PRA explicitly frames objectivity over *time-ordered* sequences of redundant records — the closest configurational precursor to the framework's temporal-records premise. Strong lineage-audit candidate (Phase 3) and a potential External-Constraints citation.
- **`covey2025` is a clean Claim IV anchor.** Its three-node beat-note mismatch Δω (curvature residual after the leading consensus is removed) directly operationalises "cross-probe mismatch" for distributed proper-time records — the sharpest experimental instance of a Claim IV measure in the corpus.
- **`fit2026` assessment:** sound but modest/speculative — standard reparameterisation of time by Fisher arc length, *no novel falsifiable prediction*, single-trajectory, path/model-dependent. Its record-based parameter Λ_rec = Σ D(ρ_k‖ρ_{k−1}) is the closest contact point but lacks redundancy/mutual-information/consensus. Cite as a **kindred Fisher-time proposal the framework subsumes and extends**, not a competitor.

## Open steward decision — Tier-1 down-tiering

Tier 1 stands at **18** (within the hard cap of 25, above the 8–12 working expectation — [work plan §6](../literature-review-plan.md#6-plan-revision-protocol--scope-guards)). `hartong2024` already demoted. Further demotion candidates flagged by the extraction: `nambu2022`, `hohnsmith2021`, `brandao2015`, `giovannetti2011`, `fit2026` (each contextual rather than directly claim-/discriminant-bearing). Demoting these would land Tier 1 at ~13. **Steward call.**

## Next

- Corpus assembly + extraction is complete for all 29 entries.
- (If desired) upgrade extraction notes to full per-claim Phase-2 annotation for the final Tier-1 set, after the down-tiering decision.
