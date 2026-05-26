# covey2025 — Probing curved spacetime with a distributed atomic processor clock

| Field | Value |
| --- | --- |
| Reference | J. P. Covey, I. Pikovski, J. Borregaard, "Probing curved spacetime with a distributed atomic processor clock", PRX Quantum **6**, 030310 (2025). |
| DOI / arXiv | DOI 10.1103/q188-b1cr; arXiv:2502.12954. |
| Cluster · Tier | F · 1 |
| Source PDF | `sources/covey2025.pdf` — 12 pp. |
| Annotated | 2026-05-26 (Phase 2) |

## Core claim
A distributed atomic-processor clock with three nodes at distinct elevations can probe general-relativistic effects *beyond* the Newtonian limit — spacetime curvature (tidal) itself — via a nonlocal "self-interference" observable whose three beat-note frequencies, and specifically their mismatch, encode the curvature.

## Method
Three ¹⁷¹Yb optical-clock nodes separated by ~km-scale elevation differences share a three-qubit W state (one delocalized "clock" plus two "not-clocks"). Each node accumulates differential proper time at its elevation. The clock state `|c(τ)⟩ = (|a⟩ + e^{−iΔEτ/ℏ}|b⟩)/√2` is an explicit proper-time record per node. A Fourier-basis measurement of the W state yields pairwise oscillating terms `|⟨c(τᵢ)|c(τⱼ)⟩| cos(...)` for all three node pairs (Eq. 6), giving three beat frequencies ω₁₂, ω₂₃, ω₁₃ (Eqs. 7–9). To first (Newtonian) order ω₁₂ ≈ ω₂₃; the curvature shows up only at higher order as the mismatch `Δω = ω₁₂ − ω₂₃ ≈ 2(ΔE GM/ℏc²)(d²/R³)` (Eq. 10) — a genuinely post-Newtonian three-point signature. Optional N-atom GHZ "superatoms" within each node amplify the differential proper time by N. Framed explicitly as a test of linearity, unitarity, and the Born rule under relativistic curvature; built on demonstrated ¹⁷¹Yb coherence (~7 s nuclear, ~30 s optical) and Rydberg gate fidelities ~0.995.

## Relation to the five Coastline claims
- **Claim I — emergent proper time / temporal record:** supports. The internal-coherence clock state `|c(τ)⟩` is a clean instance of a "temporal record" — a DOF carrying usable info about elapsed (proper-time) evolution — and three such records are held at distinct nodes.
- **Claim II — redundancy / stability / compressibility:** strains/partial. Three nodes each carry a proper-time record, and the decay of `|⟨c(τᵢ)|c(τⱼ)⟩|` with accumulated proper-time difference is the temporal-decoherence channel. But the three records are entangled into a single W state and read jointly, so this is *multiple records of correlated proper times*, not demonstrated redundant, independently-recoverable copies in the quantum-Darwinism sense. Be honest: it uses multiple nodes; it does not establish redundancy-of-records.
- **Claim III — failure mode / nuisance-discrimination:** supports, indirectly. The whole design isolates the *higher-order* (curvature) residual after the leading-order consensus (ω₁₂ ≈ ω₂₃) is removed — a discrimination of a genuine structural/relativistic signal from the dominant common-mode term. Framing as a test of unitarity/Born-rule violations is a structural-failure probe, distinct from generic technical decoherence.
- **Claim IV — operational anchors (Fisher / mutual info / cross-probe / coarse-graining):** supports — direct cross-probe-mismatch instance. The three-node beat-note mismatch `Δω = ω₁₂ − ω₂₃` (Eq. 10) is precisely a Claim IV cross-probe mismatch: the residual disagreement among pairwise temporal records once the leading consensus is subtracted, and it is what carries the curvature. Proper-time coherence loss is also a Fisher-style sensitivity resource (with N-atom superatom amplification). Mutual-information and coarse-graining-robustness measures are not constructed.
- **Claim V — positioning (PW bipartite vs quantum-Darwinism configurational vs multipartite redundancy):** supports — premier anchor. Three spatially distinct nodes each holding a proper-time record, with the *consensus structure* (which beat notes agree) carrying the physics, is the multipartite-redundancy framing made literal. Moving from two-point/Newtonian (bipartite-like) clock-interferometry to a genuine three-point design is the step that distinguishes multipartite redundancy from the PW bipartite picture.

## Bearing on Ledger / Sail
CL-2026-008 (candidate) — distributed clock networks. covey2025 is the strongest candidate anchor: its three-node design is the literal multipartite instance, and Δω is a textbook Claim IV cross-probe-mismatch observable that the Sail can cite directly. Bridges Cluster E (Zych/Pikovski single-particle proposals) into the distributed-network regime.

## Lineage & citation chain
In-corpus: builds on [[pikovski2015]] / [[zych2011]] (proper-time decoherence and single-particle clock-interferometry) and the network precedent [[komar2014]]; sibling distributed-ensemble proposal [[fromonteil2025]]; shares the composite-mass Hamiltonian lineage of [[zych2019]]. External: Yb optical-clock metrology, Rydberg-gate processor-clock hardware, relativistic-geodesy clock comparisons.

## Open questions / flags
- Title, authors, journal match; DOI 10.1103/q188-b1cr is the new PRX-style identifier (confirmed). Full 12-page article read.
- The W-state records are jointly read and entangled; whether the proper-time information is *redundant* (Claim II) or merely *multipartite* is not addressed. The Δω mismatch is the clearest framework hook (Claim IV), stronger than its Claim II bearing.
