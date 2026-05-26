# fromonteil2025 — Non-local Mass Superpositions and Optical Clock Interferometry in Atomic-Ensemble Quantum Networks

| Field | Value |
| --- | --- |
| Reference | C. Fromonteil, D. V. Vasilyev, T. V. Zache, K. Hammerer, A. M. Rey, J. Ye, H. Pichler & P. Zoller, "Non-local mass superpositions and optical clock interferometry in atomic ensemble quantum networks", arXiv:2509.19501 (2025). DOI 10.48550/arXiv.2509.19501. |
| Cluster · Tier | F · 1 |
| Source PDF | `sources/fromonteil2025.pdf` — 16 pp. ✅ complete (read pp. 1–4 abstract/intro/interference/non-local superpositions + pp. 8–10 scalability/outlook/appendices A–B) |
| Extracted | 2026-05-26 |

## Summary
The authors propose using entangled atomic *ensembles* distributed across a quantum network to emulate atom and atom-clock interferometry without placing individual atoms in spatial superposition. Optical-clock internal excitations are reinterpreted as mass superpositions (m_eg = ℏω_eg/c²), so collective operations within ensembles build many-body, non-local mass-superposition states sensitive to gravitational redshift. The resulting architecture realizes a "generalized, non-local Ramsey interferometer" whose interference pattern carries gravitationally induced phase shifts, extending the reachable spatial separations, interrogation times and effective masses beyond conventional single-atom interferometry.

## Key points
- Internal excitations are *equivalent to mass superpositions*: a node of N two-level atoms is mapped to a ladder of mass eigenstates M_σ = ℓ_σ ℏω_eg/c², letting global driving alone (no per-atom control) build the superpositions (Fig. 2).
- The scheme reproduces, in a network, three known gravity-quantum signatures: reduced visibility in an atom-clock interferometer (the proper-time witness), a GR analog of the Colella-Overhauser-Werner (COW) experiment, and gravitationally induced decoherence.
- Gravitational decoherence time τ_dec = √2 ℏc²/(ΔE g Δz) (Eq. 5) — same relativistic ℏ/c/g form as Pikovski 2015 — set by the mass/energy uncertainty ΔE = ΔM c².
- A shallow, N-independent "double-twisting" (one-axis-twisting) circuit prepares a non-local NOON-like cat state |0⟩_A|N−1⟩_B + e^{iφ}|N−1⟩_A|0⟩_B with quantum Fisher information F_Q = (N−1)² ≈ Heisenberg limit; an energy-tuning unitary tunes ΔE² and hence the decoherence rate.
- Concrete estimate: N = 100 atoms/node, ω_eg/2π = 0.5×10¹⁵ Hz, Δz = 1 m gives τ_dec ≈ 0.5 s — tabletop-feasible; observing Gaussian decay *and revivals* (set by the state's mass distribution) is proposed to confirm the gravitational (vs technical) origin.

## Relevance to the framework
Strong **Cluster F** anchor and the most explicit "multipartite redundancy made literal" case (**Claim V**): proper-time / mass-energy information is distributed across many atoms in many nodes, and collective (compressible, global-driving) operations build the consensus observable from ensemble records (**Claim II**). The proper-time-witness, COW, and gravitational-decoherence trio it reproduces ties Clusters E and F together. Directly relevant to **Claim IV**: it gives a quantum-Fisher-information resource F_Q ≈ N² and a τ_dec set by ΔE, and explicitly proposes *distinguishing the gravitational structural signature from technical imperfections* by testing the energy/mass dependence and the functional (Gaussian + revival) form predicted by GR — a clean **Claim III** discrimination test. The ensemble (vs single-atom) framing is itself a coarse-graining-robustness argument (**Claim IV**).

## Flags
none — title, authors, DOI/arXiv all match (read as arXiv v1, 23 Sep 2025). Full 16-page preprint; main text plus methods appendices A–B read, later appendices (circuit details C–F) skimmed for context only.
