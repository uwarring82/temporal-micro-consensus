# Examples

Reproducible example notebooks — the **Phase-3 gate condition**. Each is executed end-to-end and regenerates a committed result under [`../results/`](../results/) from scratch.

- [`sorci_module.ipynb`](sorci_module.ipynb) — **Module 3a** (Sorci protocol): the CL-2026-006 **D1** nuisance budget. Baseline Eq. (12)-coefficient validation (`→ 1/16`), the latent/observed budget table (the detection row's latent `ΔI = ΔL_state ≡ 0`), and the ²⁷Al⁺ `V≈0.94` extrapolation. Regenerates [`../results/sorci_nuisance_budget_v0.1.json`](../results/sorci_nuisance_budget_v0.1.json).
- [`open_instrument_module.ipynb`](open_instrument_module.ipynb) — **Module 3b** (open temporal instrument): `R_δ(N, γ_φ t)` curves. Derives `ε = (1−e^{−γ_φ t})/2`, the D5 cross-link (`ε=0.20 → R_{0.10}=64/9` exactly), the curves (plot), and the undefined boundary rising with N. Carries the **einselection caveat verbatim**. Regenerates [`../results/open_instrument_redundancy_v0.1.json`](../results/open_instrument_redundancy_v0.1.json).

Run (from this directory, with the package installed via `pip install -e "..[examples]"`):

```
jupyter nbconvert --to notebook --execute --inplace *.ipynb
```

or open them in Jupyter. The committed copies are pre-executed (outputs included) as the gate record.
