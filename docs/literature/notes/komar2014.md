# komar2014 — A quantum network of clocks

| Field | Value |
| --- | --- |
| Reference | P. Kómár, E. M. Kessler, M. Bishof, L. Jiang, A. S. Sørensen, J. Ye, M. D. Lukin, "A quantum network of clocks", Nat. Phys. **10**, 582–587 (2014). |
| DOI / arXiv | DOI 10.1038/nphys3000; arXiv:1310.6045. |
| Cluster · Tier | F · 1 |
| Source PDF | `sources/komar2014.pdf` — 6 pp. |
| Annotated | 2026-05-26 (Phase 2) |

## Core claim
A cooperative protocol can run K geographically separated optical atomic clocks as a single "world clock" that reaches the Heisenberg precision limit set by quantum theory, by pooling all atoms across nodes into network-wide entangled states and distributing the resulting ultra-stable time scale in real time.

## Method
Network-wide GHZ states are built by teleportation from a center node and grown by local entangling at each node, so the collective phase `Φ = Ñ δ_COM T` accumulates with full-N (Heisenberg) sensitivity to the center-of-mass (COM) detuning of all local oscillators (Eq. 1). Each node interrogates the shared entangled state with its local oscillator; the center node collects parity outcomes, extracts the deviation of the COM frequency, and feeds it back to stabilize every node. A phase-estimation protocol over a hierarchy of GHZ groups of growing size beats the laser-noise limit, giving 1/N scaling of the Ramsey phase error up to a log correction `ΔΦ_LO = (8/π) log(N)/N` (Eq. 2). The achievable Allan deviation interpolates between Heisenberg-limited 1/τ at short times (Eq. 3) and the ultimate `√(γ_i/N)` bound (Eq. 4), with a √K gain over independent operation. Feasibility: ~10 entangled Yb⁺/Al⁺-type ion clocks → ~4×10⁻¹⁷ at 1 s; networks of 1000-atom Sr clocks → ~2×10⁻¹⁸ at 1 s. Built-in security via QKD on classical channels; nodes retain sovereignty (fall back to local clocks if links fail).

## Relation to the five Coastline claims
- **Claim I — emergent proper time / temporal record:** supports, weakly/operationally. Each node's local-oscillator phase is a usable record of elapsed evolution, and the extracted COM phase is a network-level temporal variable; but the paper treats time as an external parameter to be measured precisely, not as something *emergent* from the records. The "temporal record" reading is ours.
- **Claim II — redundancy / stability / compressibility:** strains/partial. The architecture has many nodes (apparent redundancy), feedback (stability), and a single COM phase distilled from K parity records (apparent compressibility) — but this is *engineered entanglement to a single GHZ-correlated variable*, not redundant, independently-readable copies of a temporal record. GHZ correlations are fragile and non-redundant (one loss collapses the whole), which is the opposite of quantum-Darwinism redundancy. So it uses multiple nodes without establishing redundancy-of-records in the Claim II sense; be honest that the resemblance is structural, not mechanistic.
- **Claim III — failure mode / nuisance-discrimination:** touches it. The fall-back-to-local-clocks logic and sabotage/eavesdropping detection are explicit handling of a node ceasing to support the shared consensus variable — an operational analog of a subsystem dropping out of temporal consensus. No structural-vs-generic-decoherence discrimination is offered, however.
- **Claim IV — operational anchors (Fisher / mutual info / cross-probe / coarse-graining):** supports. The phase-estimation protocol and Heisenberg-limited Allan deviation are direct Fisher-style precision anchors; the √K cooperative gain quantifies the metrological value of the multipartite structure. No mutual-information or cross-probe-mismatch construction, and coarse-graining robustness is not analyzed.
- **Claim V — positioning (PW bipartite vs quantum-Darwinism configurational vs multipartite redundancy):** supports — core anchor. This is the regime where the multipartite framing becomes *literal*: many spatially separated clocks share a time scale. It instantiates the distributed-clock-network setting the framework points to, even though its entanglement is GHZ (non-redundant) rather than Darwinism-redundant.

## Bearing on Ledger / Sail
CL-2026-008 (candidate) — distributed clock networks where multipartite redundancy becomes literal. komar2014 is the founding "quantum network of clocks" proposal and the precedent that covey2025/fromonteil2025 build on. Useful as the engineering baseline against which to argue that *redundancy* (Claim II) requires more than shared GHZ entanglement.

## Lineage & citation chain
In-corpus: foundational precedent for [[covey2025]] and [[fromonteil2025]] (distributed-network clock interferometry). External: clock-network metrology (Ye/Lukin programs), GHZ/Heisenberg-limited Ramsey spectroscopy, quantum key distribution for the feedback channels.

## Open questions / flags
- Title, authors, journal, DOI all match the PDF; full 6-page article read (supplementary not bundled).
- Key tension to flag: GHZ entanglement maximizes metrological sensitivity but is *anti-redundant*. Whether a clock network can be reframed to give genuinely redundant temporal records (Claim II) — rather than a single fragile collective variable — is open and is precisely where this paper is silent.
