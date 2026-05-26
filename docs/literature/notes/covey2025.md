# covey2025 — Probing Curved Spacetime with a Distributed Atomic Processor Clock

| Field | Value |
| --- | --- |
| Reference | J. P. Covey, I. Pikovski & J. Borregaard, "Probing curved spacetime with a distributed atomic processor clock", *PRX Quantum* **6**, 030310 (2025). DOI 10.1103/q188-b1cr, arXiv:2502.12954. |
| Cluster · Tier | F · 1 |
| Source PDF | `sources/covey2025.pdf` — 12 pp. ✅ complete (read pp. 1–4 abstract/intro/protocol/curvature signature + pp. 9–12 concluding discussion/references) |
| Extracted | 2026-05-26 |

## Summary
The authors propose a distributed atomic-processor clock that probes general-relativistic effects *beyond* the Newtonian limit — i.e. spacetime curvature itself. Three ¹⁷¹Yb optical-clock nodes separated by ~kilometre-scale elevation differences share a three-qubit W state (one delocalized "clock" plus two "not-clocks"), and the differential proper time accumulated at the three elevations produces a nonlocal "self-interference" observable. Because three elevations are involved, the interference shows three distinct beat notes whose mismatch encodes the curvature (tidal) of the gravitational field, going past the two-point/Newtonian tests of prior clock-interferometry proposals.

## Key points
- The clock state |c(τ)⟩ = (|a⟩ + e^{−iΔEτ/ℏ}|b⟩)/√2 is an explicit *proper-time record*; each node records its local proper time τⱼ in this internal coherence.
- A Fourier-basis measurement of the W state yields pairwise oscillating terms |⟨c(τᵢ)|c(τⱼ)⟩| cos(...) for all three node pairs (Eq. 6), giving three beat frequencies ω₁₂, ω₂₃, ω₁₃ (Eqs. 7–9).
- First-order (Newtonian) gives ω₁₂ ≈ ω₂₃; the *curvature* shows up only at higher order, Δω = ω₁₂ − ω₂₃ ≈ 2(ΔEGM/ℏc²)(d²/R³) (Eq. 10) — a genuinely post-Newtonian, three-point signature.
- N-atom GHZ "superatoms" within each node amplify the differential proper time by a factor N, boosting interrogation bandwidth (optional enhancement).
- Explicitly framed as a test of the *linearity, unitarity, and the Born rule* of quantum theory in the presence of relativistic spacetime curvature; built on demonstrated ¹⁷¹Yb coherence (~7 s nuclear, ~30 s optical) and Rydberg gate fidelities ~0.995.

## Relevance to the framework
Premier **Cluster F** anchor where multipartite redundancy is *literal* (**Claim V**): three spatially distinct nodes each hold a proper-time record, and the consensus structure (which beat notes agree) is what carries the physics. The three-node design directly operationalizes **Claim IV** "cross-probe mismatch" — Δω is precisely the mismatch among pairwise temporal records, and it is the *higher-order* (curvature) residual after the leading consensus is removed. The internal-coherence clock state is a clean "temporal record" (**Claim I**), and the loss of |⟨c(τᵢ)|c(τⱼ)⟩| with accumulated proper-time difference is the temporal-decoherence channel (**Claim II/III**). Strong bridge from Zych/Pikovski single-particle proposals (Cluster E) into the distributed-network regime.

## Flags
none — title, authors, journal, DOI all match (DOI 10.1103/q188-b1cr is the new PRX-style identifier). Full 12-page article including concluding discussion and references read.
