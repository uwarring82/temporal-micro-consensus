# Literature notes area

Working materials for the literature review governed by [`../literature-review-plan.md`](../literature-review-plan.md).

| File / dir | Purpose |
| --- | --- |
| [`references.bib`](references.bib) | Single source of truth for all citations. Every entry is cluster-tagged in a `keywords` field and carries a `VERIFY` note until its bibliographic data is confirmed against the primary source (Phase 1). |
| [`index.md`](index.md) | Triage tracker — one row per corpus entry: cluster, tier, the Coastline claim(s) / Claim IV measure(s) it bears on, and status. |
| [`_note-template.md`](_note-template.md) | Template for a per-paper deep-reading note (Phase 2). Copy into `notes/<citekey>.md`. |
| [`sources/`](sources/) | Original article PDFs — **local-only, git-ignored, never committed.** Only its [README](sources/README.md) is tracked. See the policy there and in [the work plan §4](../literature-review-plan.md#4-source-handling-policy). |
| `notes/` | **Findings** — one annotation file per **Tier-1** paper. Public, tracked. Created during Phase 2. This is the public record of the review, not the PDFs. |
| `synthesis-v0.1.md` | Phase 3 cross-cutting synthesis memo. Public, tracked. Created during Phase 3. |

## Conventions

- **Citekey** = `lastname<year>` (e.g. `page1983`, `zurek2009`); for multiple same-author/year, append a letter (`smith2020a`).
- **Clusters** A–G are defined in [the work plan, §2](../literature-review-plan.md#2-thematic-clusters-the-field-map).
- **Tiers** (1 load-bearing / 2 contextual / 3 peripheral) are defined in [the work plan, Phase 1](../literature-review-plan.md#phase-1--corpus-assembly--triage-broad-sweep).
- Nothing here revises an artefact. Findings flow into artefacts only via Phase 4 and the roadmap.
