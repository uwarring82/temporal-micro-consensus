# riedel2010 — Quantum Darwinism in an Everyday Environment

| Field | Value |
| --- | --- |
| Reference | C. J. Riedel, W. H. Zurek, *Quantum Darwinism in an Everyday Environment: Huge Redundancy in Scattered Photons*, Phys. Rev. Lett. **105**, 020404 (2010). |
| DOI / arXiv | 10.1103/PhysRevLett.105.020404 · arXiv:1001.3419 |
| Cluster · Tier | B · 1 |
| Source PDF | `sources/riedel2010.pdf` — 4 pp. |
| Annotated | 2026-05-26 (Phase 2) |

## Core claim
Quantum Darwinism is shown to operate in a physically realistic everyday setting: a dielectric sphere in a position superposition illuminated by blackbody radiation imprints its location redundantly into the scattered-photon environment, with redundancies orders of magnitude larger than in prior solvable toy models — a 1 µm dust grain in sunlight for 1 µs records its position roughly 10⁸ times.

## Method
Collisional-decoherence model of a sphere (radius a, permittivity ε) scattering thermal photons; computes the quantum mutual information I(S:F_f) between the object S and a fragment F of fraction f of the photon environment (V, N → ∞ at fixed density). Redundancy R_δ = 1/f_δ counts disjoint fragments each carrying all but deficit δ of the classical information. Decoherence rate 1/τ_D = C_Γ(3 + 11cos²θ)·Iā⁶Δx²k_B⁵T⁵/(c⁶ℏ⁶) (Eq. 6). Compares point-source vs isotropic illumination.

## Relation to the five Coastline claims
- **Claim I — emergent proper time / temporal record:** Silent on time. Concerns a *configurational* record (position). Relevant only by structural analogy: the record is carried by environmental DOF (scattered photons), aligning with Claim I's "any DOF carrying usable info" stance, but the recorded quantity here is a static position, not elapsed evolution.
- **Claim II — redundancy / stability / compressibility:** Strongly supports redundancy and compressibility; touches stability. **Redundancy:** the central result — the I(S:F_f) curve develops the characteristic plateau at the classical plateau value H_S = ln2 ≈ 0.69 nats for t ≫ τ_D, and R_δ ≈ (1/ln[(2δln2)⁻¹])·(t/τ_D) grows *linearly in time* and depends only logarithmically on δ (Eq. 15). **Compressibility:** the first few photons reveal almost everything; remaining fragments are redundant copies — the record compresses to a tiny fraction f ≪ 1. **Stability:** the record is "kept forever" by escaped photons (an effectively frozen, persistent imprint), the stability leg, though stability is asserted rather than stress-tested. NB the recorded variable is configurational, so this instantiates Claim II's borrowed architecture, not its TEMPORAL specialization.
- **Claim III — failure mode / nuisance-discrimination:** Supports the discrimination logic via a clean structural-failure example. **Isotropic** illumination decoheres the object just as fast (Γ is the angular average) yet yields essentially *zero* redundancy (Eq. 17, I → 0 for all proper fragments as t → ∞) because the photon directional states are already fully mixed and cannot store new information. This separates decoherence from record formation: a channel can destroy coherence while supporting no consensus variable — exactly the structural-failure/nuisance distinction Claim III demands. Real (non-uniform) illumination loses only an O(1) factor of redundancy.
- **Claim IV — operational anchors (Fisher / mutual info / cross-probe / coarse-graining):** Supports mutual-info and coarse-graining anchors; silent on Fisher and explicit cross-probe consensus. I(S:F_f) is computed throughout (partial-information plot, Fig. 2). Robustness under coarse-graining is the headline message: huge R means information survives sloppy capture of only a small fragment. No Fisher-information formulation; cross-probe agreement is implicit in the redundancy interpretation but not operationalized as a mismatch metric.
- **Claim V — positioning (PW bipartite vs quantum-Darwinism configurational vs multipartite redundancy):** The concrete physical exemplar of the multipartite-redundancy pole — a genuinely many-fragment (N → ∞) photon environment redundantly recording the object's state. Definitively **configurational** (records position, not time) and not Page–Wootters. It is the proof-of-realism the framework points to when arguing the same multipartite-redundancy machinery should apply to laboratory temporal records.

## Bearing on Ledger / Sail
None direct. Indirect leverage: the linear-in-time growth of R_δ is suggestive for *temporal* records (longer elapsed evolution → more redundant proper-time imprint), a hypothesis the Sail could test. The isotropic null result is a transferable design caution — a candidate temporal-record channel may decohere a probe while storing no usable elapsed-time information.

## Lineage & citation chain
Builds directly on [[ollivier2004]] (objectivity = complete + redundant imprint) and [[ollivier2005]], and on [[zurek2003]]; same program continued in [[riedel2011]] (spatial structure of redundancy) and the SBS/[[korbicz2014]] line. External roots: Joos–Zeh collisional decoherence (Z. Phys. B 59, 223 (1985)); Hornberger–Sipe scattering decoherence; Blume-Kohout & Zurek partial-information-plot formalism.

## Open questions / flags
Title, authors, DOI confirmed; PDF complete (4 pp.). The decoherence rate (and hence τ_D used in R_δ) is valid in the dipole limit Δx ≪ λ; the rate saturates for Δx ≫ λ — relevant if mapping to large temporal separations. The redundancy's precise value depends on the (a priori arbitrary) photon tensor decomposition; locality is invoked as the guide. For the framework's purposes, the open question is whether elapsed-time information forms a plateau at all and what the temporal analogue of "directional saturation" (the isotropic failure) would be.
