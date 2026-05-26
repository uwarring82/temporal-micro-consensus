# giovannetti2011 — Advances in Quantum Metrology

| Field | Value |
| --- | --- |
| Reference | V. Giovannetti, S. Lloyd, L. Maccone, *Advances in Quantum Metrology*, Nat. Photonics **5**, 222–229 (2011). DOI 10.1038/nphoton.2011.35 · arXiv:1102.2318 |
| Cluster · Tier | D · 1 |
| Source PDF | `sources/giovannetti2011.pdf` — 10 pp. ✅ complete |
| Extracted | 2026-05-26 |

## Summary

A compact review of quantum-enhanced parameter estimation. It frames any measurement as probe preparation, interaction, and readout, and contrasts the classical "standard quantum limit" (SQL) error scaling ∝ n^(−1/2) with the quantum "Heisenberg limit" ∝ n^(−1) attainable using entangled or otherwise non-classical probes. The central technical objects are the (classical) Fisher information and the quantum Fisher information J(ρ_x), which set the Cramér–Rao and quantum Cramér–Rao bounds on estimation precision. A large part of the paper addresses how realistic noise (loss, dephasing) degrades these advantages, generally collapsing the Heisenberg-to-SQL gain.

## Key points

- Cramér–Rao bound: estimation error δX_n ≥ 1/√(F_n(x)), with Fisher information F_n(x) = Σ_y (∂_x p_n(y|x))²/p_n(y|x); optimizing over POVMs gives the quantum CR bound δX_n ≥ 1/√(n J(ρ_x)).
- Quantum Fisher information J(ρ_x) defined via the symmetric logarithmic derivative; for pure states ρ_x = e^(−iHx)|0⟩ the q-CR bound reduces to an uncertainty-relation form δX_n ≥ 1/(2√n ΔH), tying precision to the spread of the generator H.
- Additivity J(ρ_x^⊗n) = nJ(ρ_x) yields the SQL n^(−1/2); the asymptotic CR bound is achievable with purely local measurements + adaptive estimators (LOCC), so entanglement is needed at the *preparation* stage, not the readout stage.
- Estimation strategies classified (CC/CQ/QC/QQ parallel schemes, plus sequential/multi-round and ancilla-assisted) according to where entanglement is injected; QQ gives the best, CC the worst scaling.
- Noise analysis: dephasing leaves *phase* estimation's full N^(−1/2) quantum gain intact (if measurement time is short) but destroys the quantum advantage for *frequency* estimation for any nonzero dephasing rate γ; loss in NOON states limits the gain to a constant factor — the metrological advantage is fragile.

## Relevance to the framework

This is the source paper for the Claim IV "Fisher anchor": the quantum Fisher information about elapsed time and the Cramér–Rao bound on temporal-inference precision are exactly the operational tools the framework invokes to quantify how much usable information a record carries about elapsed evolution. The generator-spread form (ΔH ↔ energy spread, and via H the time/phase) is the natural way to formalize "information about elapsed time." The noise discussion (frequency-estimation advantage destroyed by dephasing) is directly relevant to Claim III: it gives a quantitative example of when temporal information stops being robustly extractable, useful for distinguishing structural failure from generic decoherence.

## Flags

Title and authors confirmed (Giovannetti, Lloyd, Maccone). PDF complete (10 pp.). This is a configurational/phase-metrology review, not about temporal records per se — the framework borrows its Fisher-information machinery rather than its physics. None.
