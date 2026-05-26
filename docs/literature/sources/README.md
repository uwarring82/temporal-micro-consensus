# Source documents — LOCAL ONLY

This directory holds **original article PDFs** acquired during the literature review. Its contents are **deliberately git-ignored** and never committed: only this README is tracked.

## Why local-only

1. **Copyright.** Publisher and preprint PDFs are copyrighted works. Redistributing them in a public repository would infringe those rights. This repository is public (`github.com/uwarring82/temporal-micro-consensus`).
2. **The public record is our own.** Our contribution is the *findings* — the per-paper notes in [`../notes/`](../notes/) and the synthesis memo — which are original analysis under the repository's CC licences. The sources are inputs to that analysis, not part of the published record.
3. **Reproducibility without redistribution.** Every source is fully identified in [`../references.bib`](../references.bib) (with DOI/arXiv once verified), so any reader can obtain the same document from the publisher or preprint server.

## Conventions

- **Filename = citekey + extension**, e.g. `page1983.pdf`, `zurek2009.pdf` — matching the citekey in `references.bib`.
- One file per corpus entry. Supplementary material may use `<citekey>-supp.pdf`.
- Do **not** rename, annotate-in-place, or redistribute these files. Annotations and findings go in `../notes/<citekey>.md`.

## What is enforced by `.gitignore`

```
docs/literature/sources/**          # ignore everything here…
!docs/literature/sources/README.md  # …except this README
docs/literature/**/*.pdf            # and no PDF anywhere in the literature area
```

If `git status` ever shows a `.pdf` as tracked or staged, stop and remove it from the index before committing.
