# nambu2022 — Qubit Clock in Quantum Cosmology

| Field | Value |
| --- | --- |
| Reference | Y. Nambu, "Qubit Clock in Quantum Cosmology", *Universe* **8**, 99 (2022). DOI 10.3390/universe8020099, arXiv:2201.02770. |
| Cluster · Tier | A/D · 2 (down-tiered from 1 — contextual Fisher/PW application) |
| Source PDF | `sources/nambu2022.pdf` — 8 pp. ✅ complete |
| Extracted | 2026-05-26 |

## Summary
Implements the Page–Wootters emergent-time scenario in a minisuperspace quantum-cosmology model: a spatially flat FLRW universe (volume ρ as the gravitational DOF) coupled to a two-level "qubit clock," with the total Hamiltonian constrained to vanish (Wheeler–DeWitt equation). Conditioning the timeless universe wavefunction on the qubit clock state yields a standard Schrödinger equation for the universe, and the paper shows explicitly that the qubit's quantum Fisher information quantifies the clock–universe entanglement and the condition for a workable clock.

## Key points
- Model: H = N(H_U ⊗ I + I ⊗ H_C); WDW constraint annihilates |Ψ⟩⟩; clock-conditioned wavefunction ψ(ρ,T) obeys a Schrödinger equation (Eq. 39) containing a Berry connection from the clock–geometry coupling.
- Workable-clock condition: nonzero quantum Fisher information F_Q(ρ) = (θ')²|α|²|β|², i.e. |αβ| ≠ 0; the clock fails iff it is in an energy eigenstate (|α|=0 or 1), where F_Q = 0 and the time-dependence is lost.
- Time–energy uncertainty: ⟨(ΔE)²⟩⟨(ΔT)²⟩ ≥ 1/4, with F_Q = 4⟨(ΔE)²⟩/... saturating a Cramér–Rao bound for estimating the cosmological "time" ρ; max accuracy at |α|² = 1/2.
- Fisher information enters the universe's effective dynamics as a *negative* matter energy density (because F_Q ≥ 0), modifying the expansion law; the qubit's bare contribution behaves like a dust fluid (∝ ρ⁻¹).
- Entanglement = mixedness of the reduced universe state ∝ |α|²|β|², exactly the F_Q dependence: Fisher information is shown to *be* the entanglement quantifier here; no entanglement ⇒ no clock.

## Relevance to the framework
Tight **Claim IV** anchor: makes quantum Fisher information about elapsed (cosmological) time the explicit, central operational measure, and ties it to a time–energy uncertainty relation. Strong **Claim II/III** content: gives a sharp, computable failure criterion (F_Q = 0 ⇔ energy eigenstate ⇔ no usable temporal variable), exactly the structural-failure-vs-working-clock discrimination the framework needs. Bipartite (clock + universe), so it sits in the **Claim V** Page–Wootters comparison class, but with a quantitative Fisher/entanglement order parameter.

## Flags
none — title, author, journal, DOI, and arXiv id all match. Full 8-page Communication read.
