# ollivier2004 — Objective Properties from Subjective Quantum States

| Field | Value |
| --- | --- |
| Reference | H. Ollivier, D. Poulin, W. H. Zurek, *Objective Properties from Subjective Quantum States: Environment as a Witness*, Phys. Rev. Lett. **93**, 220401 (2004). |
| DOI / arXiv | 10.1103/PhysRevLett.93.220401 · arXiv:quant-ph/0307229 |
| Cluster · Tier | B · 1 |
| Source PDF | `sources/ollivier2004.pdf` — 4 pp. |
| Annotated | 2026-05-26 (Phase 2) |

## Core claim
A property of an open system is *objective* iff its imprint on the environment is both complete and redundant; the authors prove that the unique observable satisfying this is the system's maximally-refined pointer observable π. Many ignorant observers reading disjoint environment fragments therefore reach consensus only about pointer states, without prior agreement and without perturbing the system.

## Method
Operational definition of objectivity via three requirements (simultaneous accessibility to many observers, discoverability without prior knowledge, consensus without prior agreement), translated into an information-theoretic framework using the system–environment quantum mutual information I(σ:ε). Completeness is Î_N(σ) ≈ H(σ); redundancy is quantified as R_δ(σ) = N/m_δ(σ), where m_δ is the smallest fragment carrying all but a fraction δ of the information. A uniqueness theorem proves the completely-and-redundantly imprinted observables are characterized by a single π, with Î_m(σ) = I(σ:π) for any σ. Illustrated on a spin-½ coupled to N = 50 environment subsystems (bound H₂(cos²(μ/2)) ≤ δ → |μ| < 0.23 for objectivity).

## Relation to the five Coastline claims
- **Claim I — emergent proper time / temporal record:** Silent on time specifically. But it supplies the configurational template the framework adapts: an "objective property" is operationally defined as a multiply-readable environmental imprint, not as the expectation of a system observable — structurally the same move Claim I makes by defining a temporal record as any DOF carrying usable info rather than as a microscopic time variable.
- **Claim II — redundancy / stability / compressibility:** Supports the redundancy and stability legs directly, and is the precise origin of Claim II's borrowed architecture. **Redundancy:** R_δ = N/m_δ ≫ 1 is shown to be the selective criterion (completeness alone is too permissive — many observables read out of the *whole* environment). **Stability:** the paper notes the interaction action a_k sets only the *magnitude* of redundancy, not which observable becomes objective — pointer selection is robust to interaction strength/duration, the stability leg. **Compressibility:** instantiated indirectly — the optimal inference strategy is to estimate π first and deduce everything else from its correlations (Eq. 6), i.e. the objective information compresses to one variable; this is the configurational analogue the framework specializes to *temporal* compressibility.
- **Claim III — failure mode / nuisance-discrimination:** Supports the discrimination logic at the configurational level. The completeness-vs-redundancy gap is exactly a structural-failure diagnostic: a property can be globally complete (recoverable from all of ε) yet fail objectivity because it is not redundant — e.g. Schrödinger-cat superpositions need the whole environment and so support no consensus. Translated to time, an evolution can leave a complete-but-non-redundant imprint that decoheres without supporting a temporal-consensus variable.
- **Claim IV — operational anchors (Fisher / mutual info / cross-probe / coarse-graining):** Supports mutual-information, cross-probe, and coarse-graining anchors; silent on Fisher information. Mutual info I(σ:ε) and R_δ are the central quantities. Cross-probe consensus is the definitional payload (independent observers agree). Coarse-graining/robustness is explicit: objective info must survive *realizable*, non-optimal ("sloppy") measurements and is insensitive to interrogation strategy and tensor-decomposition choices to O(1).
- **Claim V — positioning (PW bipartite vs quantum-Darwinism configurational vs multipartite redundancy):** This is a foundational anchor for the multipartite-redundancy pole. It is the rigorous statement of quantum-Darwinism objectivity: a *multipartite* (N-fragment) environment redundantly recording one observable. Critically it records a **configurational** property (the pointer observable of a static system), not a temporal one — so it marks precisely the gap the framework must cross to claim a TEMPORAL specialization, and is not Page–Wootters (no clock/system bipartition).

## Bearing on Ledger / Sail
None direct. Architectural backbone: defines the redundancy/uniqueness machinery any Sail ledger entry asserting "emergent classical temporal consensus" must instantiate. The |μ| < 0.23 threshold is a model-specific illustration, not a transferable number.

## Lineage & citation chain
Founds the [[zurek2003]] einselection/quantum-Darwinism program in operational form; companion to [[ollivier2005]] (extended proofs) and developed quantitatively by [[riedel2010]]/[[riedel2011]] and by the SBS/[[korbicz2014]] line. External roots: Zurek's predictability sieve and pointer-state work (Phys. Rev. D 24, 1516 (1981)); Bohr's amplification idea; Cover & Thomas information theory.

## Open questions / flags
Title, authors, DOI confirmed; PDF complete (4 pp.). The uniqueness theorem is for *configurational* (commuting, time-independent) observables read from a static system; the framework needs an analogue for *temporal* records where the "observable" is elapsed evolution — non-trivial because the system itself is dynamical and π would have to be time-indexed. The tensor-product locality assumption (which decomposition of ε defines fragments) is acknowledged as a priori arbitrary; for temporal records the corresponding choice (which DOF count as independent probes of elapsed time) is unresolved.
