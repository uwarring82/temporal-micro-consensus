# Assets — Source and Checksum Record

Distributed-copy record per [`threehouse-plus-ec/cd-rules`](https://github.com/threehouse-plus-ec/cd-rules) blueprint §0.10 (Asset Propagation — Model B).

## Source pin

| Field | Value |
| --- | --- |
| Source repository | [`threehouse-plus-ec/cd-rules`](https://github.com/threehouse-plus-ec/cd-rules) |
| Source tag | `cd-v1.7.1` |
| Source commit | `ee01c80352dd8446f189c3159a3d9e347463902c` |
| Source date | 2026-04-17 |
| Copied on | 2026-05-29 |
| Copy method | `gh api repos/threehouse-plus-ec/cd-rules/contents/<file>?ref=ee01c80…` |
| Consuming repo | `uwarring82/temporal-micro-consensus` |

All files in this folder are byte-identical to the source at the pinned commit (verified by `git hash-object` against the GitHub blob SHA; see "Drift detection" below).

## Files and checksums

SHA-256 hashes (computed locally with `shasum -a 256`; consumer-side audit per blueprint §0.10):

| File | SHA-256 | Source layer | Licence |
| --- | --- | --- | --- |
| `emblem-16.svg` | `7298b11e6231d27d3454a16380c4d511e1c2251c7c168c5f66cafa8bc05fe44b` | Handbook (design asset) | MIT |
| `emblem-32.svg` | `e799f0bd9ddc5d36c6904c43690c8507215ea78d5d12cc5fec53992bade9ff0b` | Handbook (design asset) | MIT |
| `emblem-64.svg` | `48bf761c7f903d09b7b98a5cc8b813c035d8c34b31bdece685f0b9c51387fe55` | Handbook (design asset) | MIT |
| `wordmark-full.svg` | `84defa4091307bd59a30b262ea83d1e244da0d317770dbf56661baaa09add0f2` | Handbook (design asset) | MIT |
| `wordmark-silent.svg` | `164e8317cd8058c3eb3c3fab8c3a2aa15e2b008300dbb4046f7a0a77090e73fb` | Handbook (design asset) | MIT |
| `tokens.css` | `097b5903dc3983d3215fb46b4b76948a716e5d2448a1175910b884c25af63962` | Handbook (design asset) | MIT |

## Git-blob audit (verifies byte-identity to the source pin)

| File | Source repo blob SHA at `ee01c80` |
| --- | --- |
| `emblem-16.svg` | `0254394bfaa4831169ac27b7fd0acfa6810c8485` |
| `emblem-32.svg` | `aba4cf1a81336efed109b39be693cfa693608d7b` |
| `emblem-64.svg` | `816f3e777efbd3842061a8cd81fb8b003b78fa9d` |
| `wordmark-full.svg` | `b1db6be1448e818c3a63bc8c8ff6a67cc0d8f32b` |
| `wordmark-silent.svg` | `0a4938f620f73bdfc5e666bd389fe315ad404ef8` |
| `tokens.css` | `330ce206f4b3fc109e6d7326da9a5678e131c8ba` |

Each local file's `git hash-object` value matched the corresponding source-repo blob SHA at the pinned commit at copy time (2026-05-29). The MIT licence text for this folder lives in [`./LICENCE`](LICENCE).

## Drift detection

Per blueprint §0.10:

> Compare local file hashes against `corporate-design/` tagged hashes. If mismatch exists and no local justification is documented, the local copy is stale.

To check drift against the *current* source `main` (informational; not the pinned version):

```sh
PIN=ee01c80352dd8446f189c3159a3d9e347463902c
for f in emblem-16.svg emblem-32.svg emblem-64.svg wordmark-full.svg wordmark-silent.svg tokens.css; do
  remote=$(gh api "repos/threehouse-plus-ec/cd-rules/contents/$f?ref=main" --jq '.sha')
  local_git=$(git hash-object "$f")
  echo "$f  remote_main=$remote  local=$local_git  match=$([ "$remote" = "$local_git" ] && echo OK || echo DRIFT)"
done
```

When `threehouse-plus-ec/cd-rules` tags a new release, update this folder within one release cycle and bump the *Source tag*, *Source commit*, *Source date*, *Copied on*, SHA-256, and *Git-blob audit* rows above. Any local justification for a non-drift-tracking deviation is documented inline immediately below the affected file row.

## Update history

| Date | Source tag | Source commit | Files updated | Notes |
| --- | --- | --- | --- | --- |
| 2026-05-29 | `cd-v1.7.1` | `ee01c80` | initial copy of all 6 files | first import; introduced alongside the custom `_layouts/default.html` that replaces `jekyll-theme-cayman`; see [`docs/logbook.md`](../docs/logbook.md) 2026-05-29 entry. |
