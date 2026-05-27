# tmc-numerics — Numerical Toolkit for Temporal Micro Consensus

Numerical toolkit operationalising the *Consensus-Emergence of Classical Proper Time* framework's declared anchor measures — mutual information `I(C:M)`, quantum Fisher information `F[τ]`, and the temporal-redundancy functional `R_δ` — through master-equation simulation of clock-plus-carrier systems.

**Status: Phase 0 (infrastructure scaffold).** Only the package skeleton, dependency manifest, and a smoke-test harness exist. The core layer (Phase 1) and the anchor-measure layer (Phase 2) are not yet implemented.

The authoritative scope, phase gates, locked architectural decisions, and the public-API contract live in the work plan: [`../workplans/toolkit-work-plan-v0.1.md`](../workplans/toolkit-work-plan-v0.1.md). This README is a scaffold and will grow with the API (the Phase 1 gate requires it to reflect committed function signatures).

## Layout

```
numerics/
├── pyproject.toml      authoritative build + dependency config (package: tmc-numerics)
├── requirements.txt    minimum-version manifest (work-plan §4)
├── src/tmc_numerics/   package source (src-layout)
├── tests/              pytest suite (Phase 0: smoke test only)
├── examples/           reproducible example notebooks (Phase 3)
└── results/            committed numerical results + reproducibility metadata (Phase 3)
```

## Install (development)

```
python -m pip install -e ".[test]"
```

Run from this directory. Requires Python ≥ 3.10. Core dependencies: `qutip` ≥ 5.0, `numpy` ≥ 1.24, `scipy` ≥ 1.10. Optional extras: `viz` (matplotlib), `examples` (jupyter + matplotlib), `progress` (tqdm).

## Test

```
pytest
```

Continuous integration runs the suite on Python 3.10–3.12 on every push touching `numerics/` (`.github/workflows/numerics-ci.yml`). Failed tests block merges (work-plan §5).

## Licence

The toolkit is **MIT-licensed** (code, per the repository split licence; see the root [`LICENSE-MIT`](../LICENSE-MIT) and README §"Split licence"). This is distinct from the CC BY-SA 4.0 of the framework notes.

## Citing

Cite the toolkit per the appended code-citation section in the repository [`CITATION.cff`](../CITATION.cff); the repository as a whole is archived at [doi:10.5281/zenodo.20411120](https://doi.org/10.5281/zenodo.20411120).

## Phase 0 decisions (work plan §8)

- **Q1 (resolved):** code citation is an **appended section** in the root `CITATION.cff`, not a separate `numerics/CITATION.cff`.
- **Q2 (resolved):** GitHub Actions CI **enabled** for v0.1 (`.github/workflows/numerics-ci.yml`).
- **Q3 (resolved earlier):** Phase-3 results are **committed** to `results/` with reproducibility metadata, not generated on-demand.
- **Q5 (resolved):** reconciliation with CL-2026-005 (the Colla–Breuer–Gasbarri / "CBG" non-Markovian TCL pipeline, `oqs-cbg-pipeline`) — **reimplement in QuTiP** (per work-plan D3). CBG computes the coherent effective Hamiltonian `K(t)` (non-Markovian), not the Markovian-Lindblad nuisance/MI budget D1 needs, and carries a permanent trapped-ion stewardship-conflict flag. It is retained only as an *optional* non-Markovian validation backend (HEOM/pseudomode cross-checks, later) and a methodological template (benchmark-card / validity-envelope discipline). See work-plan §6/§8.
