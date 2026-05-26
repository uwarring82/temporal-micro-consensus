# fromonteil2025 — Non-local mass superpositions and optical clock interferometry in atomic ensemble quantum networks

| Field | Value |
| --- | --- |
| Reference | C. Fromonteil, D. V. Vasilyev, T. V. Zache, K. Hammerer, A. M. Rey, J. Ye, H. Pichler, P. Zoller, "Non-local mass superpositions and optical clock interferometry in atomic ensemble quantum networks", arXiv:2509.19501 (2025). |
| DOI / arXiv | arXiv:2509.19501; DOI 10.48550/arXiv.2509.19501. |
| Cluster · Tier | F · 1 |
| Source PDF | `sources/fromonteil2025.pdf` — 16 pp. |
| Annotated | 2026-05-26 (Phase 2) |

## Core claim
Entangled atomic *ensembles* distributed across a quantum network can emulate atom and atom-clock interferometry — including gravitationally induced phase shifts and decoherence — without placing individual atoms in spatial superposition, by reinterpreting optical-clock internal excitations as mass superpositions (`m_eg = ℏω_eg/c²`) and building collective non-local mass-superposition states.

## Method
A node of N two-level atoms is mapped to a ladder of mass eigenstates `M_σ = ℓ_σ ℏω_eg/c²`, so global driving alone (no per-atom control) builds the superpositions (Fig. 2). The architecture realizes a "generalized non-local Ramsey interferometer" whose interference pattern carries gravitational redshift phase shifts. A shallow, N-independent "double-twisting" (one-axis-twisting) circuit prepares a non-local NOON-like cat `|0⟩_A|N−1⟩_B + e^{iφ}|N−1⟩_A|0⟩_B` with quantum Fisher information `F_Q = (N−1)²` (≈ Heisenberg limit); an energy-tuning unitary tunes ΔE² and hence the decoherence rate. The scheme reproduces three gravity-quantum signatures in a network: reduced visibility in an atom-clock interferometer (the proper-time witness), a GR analog of the Colella-Overhauser-Werner (COW) experiment, and gravitationally induced decoherence with `τ_dec = √2 ℏc²/(ΔE g Δz)` (Eq. 5; same relativistic ℏ/c/g form as Pikovski 2015), set by `ΔE = ΔM c²`. Estimate: N = 100 atoms/node, ω_eg/2π = 0.5×10¹⁵ Hz, Δz = 1 m → τ_dec ≈ 0.5 s (tabletop). Observing Gaussian decay *and revivals* (set by the state's mass distribution) is proposed to confirm gravitational vs technical origin.

## Relation to the five Coastline claims
- **Claim I — emergent proper time / temporal record:** supports. Internal excitations are explicit mass/energy superpositions whose phase records accumulated proper time / redshift; the reduced-visibility "proper-time witness" is a temporal-record decoherence observable.
- **Claim II — redundancy / stability / compressibility:** strains/partial — but the cleanest of the batch. Proper-time/mass-energy information is distributed across many atoms in many nodes, and *collective global-driving operations* compress per-atom records into a single ensemble observable, which is a genuine compressibility statement. Stability via the engineered cat preparation. However the states are NOON-like / one-axis-twisted entangled cats — non-redundant collective variables, not independently-readable redundant copies — so it is honest to say it operationalizes compressibility and multipartiteness without establishing redundancy-of-records in the quantum-Darwinism sense.
- **Claim III — failure mode / nuisance-discrimination:** supports — clean discrimination test. It explicitly proposes distinguishing the *gravitational structural signature* from technical imperfections by testing the energy/mass dependence (tune ΔE) and the functional form predicted by GR (Gaussian decay plus revivals). That is exactly a structural-vs-generic-decoherence discrimination, the heart of Claim III.
- **Claim IV — operational anchors (Fisher / mutual info / cross-probe / coarse-graining):** supports. Direct quantum-Fisher-information anchor `F_Q = (N−1)² ≈ N²`; `τ_dec` set by ΔE is a quantitative decoherence anchor; tunable ΔE² gives a controlled handle on the rate. The ensemble (vs single-atom) framing is itself a coarse-graining-robustness argument — collective observables survive when individual-atom control is unavailable. No explicit mutual-information or cross-probe-mismatch construction (contrast covey2025's Δω).
- **Claim V — positioning (PW bipartite vs quantum-Darwinism configurational vs multipartite redundancy):** supports — strong anchor. Proper-time information genuinely distributed across many atoms in many nodes, with consensus observables built by collective operations, is the multipartite framing made literal at ensemble scale. Distinct from the bipartite PW picture and from configurational Darwinism records; the mass-superposition reinterpretation also ties Cluster E (composite mass) to Cluster F (networks).

## Bearing on Ledger / Sail
CL-2026-008 (candidate) — distributed clock networks. fromonteil2025 is the ensemble-scale multipartite anchor and contributes the strongest Claim III discrimination protocol of the batch (ΔE-tuning + Gaussian-decay-plus-revival signature) and a clean F_Q ≈ N² Claim IV resource. Complements covey2025 (which supplies the cross-probe-mismatch Δω) and the komar2014 baseline.

## Lineage & citation chain
In-corpus: shares the proper-time-decoherence form of [[pikovski2015]] and the composite-mass Hamiltonian lineage of [[zych2019]]; sibling distributed-clock proposal [[covey2025]]; builds on the network precedent [[komar2014]]. External: one-axis-twisting / spin-squeezing metrology, COW neutron-interferometry analog, gravitationally-induced-decoherence proposals.

## Open questions / flags
- Title, authors, DOI/arXiv all match (read as arXiv v1, 23 Sep 2025). Full 16-page preprint; main text plus methods appendices A–B read, later circuit appendices C–F skimmed for context.
- Like covey2025/komar2014, it uses many nodes/atoms but with *non-redundant* collective (NOON/cat) entanglement; the gap between "multipartite + compressible" and genuine Claim II redundancy-of-records is open and is where this paper is silent.
