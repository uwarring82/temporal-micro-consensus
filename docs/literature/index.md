# Corpus triage index

Running tracker for the literature review ([work plan](../literature-review-plan.md)). One row per corpus entry, keyed to [`references.bib`](references.bib).

**Clusters:** A Page–Wootters · B Quantum Darwinism · C Quantum clocks · D Fisher information · E Relativistic/gravitational decoherence · F Distributed clock networks · G Adjacent foundations.
**Tier:** 1 load-bearing (full note) · 2 contextual (paragraph) · 3 peripheral (abstract).
**Status:** `seed` → `verified` (bib confirmed against primary sources, Phase 1) → `src` (PDF acquired locally to [`sources/`](sources/), Phase 1) → `noted` (findings note written in [`notes/`](notes/)). Source PDFs are local-only and never committed — see [work plan §4](../literature-review-plan.md#4-source-handling-policy).

**Phase 1 verification: complete (2026-05-26).** All entries confirmed against Crossref / arXiv / ADS / publisher.
**Sources acquired + extraction pass: complete (2026-05-26).** 29 PDFs in `sources/` (local-only), each renamed to its citekey; one findings note per PDF in `notes/`.
**Tier-1 fixed at 13; Phase-2 annotation complete for Tier 1 (2026-05-26).** The 13 Tier-1 notes carry the full per-claim Phase-2 template (core claim · method · relation to all five claims · Ledger/Sail bearing · lineage · open questions); the 16 Tier-2/3 notes remain extraction-grade (summary · key points · relevance · flags).
**Phase 3 synthesis complete (2026-05-26):** [`synthesis-v0.1.md`](synthesis-v0.1.md) — claim-by-claim, measure-by-measure, gaps/falsifications, and the lineage audit. Phase-4 routing collected there.

| Citekey | Cluster | Tier | Bears on (claim / measure) | Status |
| --- | --- | --- | --- | --- |
| `page1983` | A | 1 | Claim V relational channel; External Constraints | noted |
| `smith2020` | A | 1 | Claim V (bipartite); Claim IV (Fisher); CL-2026-007 | noted |
| `hartong2024` | A | 2† | ⚠ confirmed **not** Page–Wootters — post-Newtonian coupling/methods node (cited by `sorci2026`); down-tiered 1→2 | noted |
| `mendes2019` | A | 2 | Claim I/II (internal-coherence order parameter); Coastline cites as "2018" | noted |
| `nambu2022` | A · D | 2† | Claim IV (Fisher); Claim III (F_Q=0 ⇔ no clock) | noted |
| `hohnsmith2021` | A | 2† | Claim V (relational-dynamics equivalence) | noted |
| `zurek2003` | B | 1 | Claim II (einselection background) | noted |
| `zurek2009` | B | 1 | Claim II (redundancy architecture) | noted |
| `ollivier2004` | B | 1 | Claim II (objectivity criteria) | noted |
| `ollivier2005` | B | 2 | Claim II; ⚠ §VII "objective histories" = closest configurational precursor | noted |
| `riedel2010` | B | 1 | Claim II; toy-model functional | noted |
| `riedel2011` | B | 2 | Claim III (decoherence rate ≠ record-keeping rate) | noted |
| `korbicz2014` | B | 2 | Claim II/III (spectrum-broadcast structure) | noted |
| `brandao2015` | B | 2† | Claim II (generic objectivity) | noted |
| `giovannetti2011` | D | 2† | Claim IV (QFI / Cramér–Rao) | noted |
| `fit2026` | D | 2† | Claim IV (Fisher); kindred single-trajectory proposal | noted |
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

## Phase 2 findings (extraction + Tier-1 annotation)

- ⚠ **`hartong2024` lineage flag — confirmed and acted on.** Reading the PDF confirms it is a covariant **post-Newtonian coupling prescription** (1/c² Klein–Gordon on Newton–Cartan backgrounds, worked for Kerr), with *no* clock-conditioning or relational-time content. The Coastline External Constraints currently lists it among "modern developments" of Page–Wootters — that attribution is **wrong** and must be fixed in the Phase-4 Coastline pass. Corpus action taken: down-tiered A·1 → A·2 and re-described as a methods/lineage node (it is the source of the curved-background coupling used by `sorci2026`).
- ⚠ **`ollivier2005` §VII "objective histories".** The 2005 PRA explicitly frames objectivity over *time-ordered* sequences of redundant records — the closest configurational precursor to the framework's temporal-records premise. Strong lineage-audit candidate (Phase 3) and a potential External-Constraints citation.
- **`covey2025` is a clean Claim IV anchor.** Its three-node beat-note mismatch Δω (curvature residual after the leading consensus is removed) directly operationalises "cross-probe mismatch" for distributed proper-time records — the sharpest experimental instance of a Claim IV measure in the corpus.
- **`fit2026` assessment:** sound but modest/speculative — standard reparameterisation of time by Fisher arc length, *no novel falsifiable prediction*, single-trajectory, path/model-dependent. Its record-based parameter Λ_rec = Σ D(ρ_k‖ρ_{k−1}) is the closest contact point but lacks redundancy/mutual-information/consensus. Cite as a **kindred Fisher-time proposal the framework subsumes and extends**, not a competitor.
- ⚠ **Central gap surfaced by the Tier-1 annotation (Phase-3 input).** The framework's core move — transplanting Zurek's *configurational* quantum-Darwinism criteria (redundancy/stability/compressibility) onto *temporal* records — is currently asserted **by analogy** and not formalised: the QD lineage (`zurek2003`, `zurek2009`, `ollivier2004`, `riedel2010`) records configurational, not temporal, variables, while the relativistic proper-time witnesses (`zych2011`, `pikovski2015`, and `sorci2026`) are **bipartite / single-record and silent on redundancy** (and `komar2014`/`covey2025`/`fromonteil2025` use GHZ/W/NOON entanglement that is *anti-redundant* — multipartite but not redundant-of-records). No corpus paper yet supplies a *redundant* multipartite temporal record. Phase 3 must address: (i) a rigorous "temporal pointer basis" and what counts as an independent temporal-record fragment; (ii) whether any experimentally accessible system realises temporal *redundancy* (Claim II) rather than mere multipartiteness.

## Resolved — Tier-1 down-tiering (2026-05-26)

Tier 1 reduced from 18 to **13**, within the 8–12 working-expectation band's intent ([work plan §6](../literature-review-plan.md#6-plan-revision-protocol--scope-guards)). Demoted to Tier 2 (each contextual/methodological rather than directly testing a Coastline claim or a Ledger discriminant): `hartong2024` (methods/PN node), `nambu2022`, `hohnsmith2021`, `brandao2015`, `giovannetti2011`, `fit2026`.

**Final Tier 1 (13):** `page1983`, `smith2020`, `zurek2003`, `zurek2009`, `ollivier2004`, `riedel2010`, `sorci2026`, `zych2011`, `pikovski2015`, `zych2019`, `komar2014`, `covey2025`, `fromonteil2025`. These receive the full per-claim Phase-2 annotation.

## Next

- Phases 1–3 complete: corpus assembled/verified (29), Tier-1 (13) annotated, [`synthesis-v0.1.md`](synthesis-v0.1.md) committed.
- **Phase 4** (artefact edits, governed by the roadmap — *not* this review): Coastline v0.3 (incl. `hartong2024` removal, `mendes2019` year fix, `ollivier2005` precursor, transplant open-problem, multipartite≠redundant); Ledger CL-2026-007 / CL-2026-008; Sail external-circulation decision (co-authorship); methodological notes. See [`synthesis-v0.1.md` §5](synthesis-v0.1.md).
