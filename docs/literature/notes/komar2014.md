# komar2014 — A Quantum Network of Clocks

| Field | Value |
| --- | --- |
| Reference | P. Kómár, E. M. Kessler, M. Bishof, L. Jiang, A. S. Sørensen, J. Ye & M. D. Lukin, "A quantum network of clocks", *Nat. Phys.* **10**, 582–587 (2014). DOI 10.1038/nphys3000, arXiv:1310.6045. |
| Cluster · Tier | F · 1 |
| Source PDF | `sources/komar2014.pdf` — 6 pp. ✅ complete (read pp. 582–587: abstract, concept, entangled-state prep, interrogation, stability, security, outlook, references) |
| Extracted | 2026-05-26 |

## Summary
The paper proposes a cooperative protocol for operating a network of K geographically separated optical atomic clocks as a single "world clock." Each node interrogates a network-wide entangled (GHZ) state with its local oscillator (LO); a centre node collects the parity outcomes, extracts the deviation of the centre-of-mass (COM) frequency of all LOs, and feeds it back to stabilize every node. By pooling all atoms across nodes into nonlocal entangled states, the network reaches the fundamental (Heisenberg) precision limit set by quantum theory and distributes the resulting ultra-stable time scale in real time.

## Key points
- Network-wide GHZ states are built by teleportation from a centre node, then grown by local entangling at each node, so collective phase Φ = Ñ δ_COM T accumulates with full-N (Heisenberg) sensitivity to COM detuning (Eq. 1).
- A phase-estimation-style protocol over a hierarchy of GHZ groups of growing size beats the laser-noise limit, giving 1/N scaling of the Ramsey phase error up to a log correction ΔΦ_LO = (8/π) log(N)/N (Eq. 2).
- Achievable Allan deviation interpolates between Heisenberg-limited 1/τ scaling at short times (Eq. 3) and the ultimate metrological √(γ_i/N) bound (Eq. 4); cooperative quantum scheme gains an extra √K over independent operation.
- Quoted feasibility: ~10 entangled Yb⁺/Al⁺-type ion clocks could give ~4×10⁻¹⁷ fractional uncertainty after 1 s; networks of 1000-atom JILA-type Sr clocks could reach ~2×10⁻¹⁸ after 1 s, approaching the sensitivity needed to use the network as a gravitational/geodesy sensor.
- Built-in security: distributed structure plus quantum key distribution on the classical feedback channels defends against eavesdropping and sabotage, and nodes retain sovereignty (fall back to local clocks if links fail).

## Relevance to the framework
Core **Cluster F** anchor — the regime where multipartite redundancy of temporal records becomes *literal* (**Claim V**). The COM-frequency variable extracted from many spatially separated, entangled clocks is precisely a distributed, multipartite temporal-consensus variable: redundancy (many nodes), stability (feedback stabilizes the shared signal), and compressibility (the centre extracts one COM phase from K parity records) — the quantum-Darwinism-for-time criteria of **Claim II**. The Heisenberg-limited Allan deviation and Fisher-style phase estimation are direct **Claim IV** quantitative anchors. The fall-back-to-local-clocks and sabotage-detection logic touch on **Claim III** (a node ceasing to support the shared consensus variable).

## Flags
none — title, authors, journal, DOI all match. Full 6-page article including outlook and references is present (supplementary not bundled).
