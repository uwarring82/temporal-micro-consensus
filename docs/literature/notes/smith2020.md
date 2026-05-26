# smith2020 — Quantum Clocks Observe Classical and Quantum Time Dilation

| Field | Value |
| --- | --- |
| Reference | A. R. H. Smith & M. Ahmadi, "Quantum clocks observe classical and quantum time dilation", *Nat. Commun.* **11**, 5360 (2020). |
| DOI / arXiv | DOI 10.1038/s41467-020-18264-4 · arXiv:1904.12390 |
| Cluster · Tier | A · 1 |
| Source PDF | `sources/smith2020.pdf` — 9 pp. |
| Annotated | 2026-05-26 (Phase 2) |

## Core claim
Extending Page–Wootters to relativistic particles carrying an internal clock, the conditional probability that clock A reads proper time τ_A given clock B reads τ_B reproduces ordinary special-relativistic time dilation when centre-of-mass states are momentum-localized, but acquires a genuinely quantum correction when one clock is in a superposition of localized momentum wave packets.

## Method
Relativistic Page–Wootters / conditional-probability formalism. Proper time is a covariant POVM T_clock with effect operators E_clock(τ) (not a self-adjoint operator); the clock mass M_clock = m + H_clock/c² is the self-adjoint observable. A Helstrom–Holevo argument gives a time–energy/mass uncertainty relation ΔM_clock ΔT_clock ≥ 1/(2c²); optimal covariant clocks saturate the Mandelstam–Tamm and quantum Cramér–Rao bounds with Fisher information F[τ; ρ(τ)] = 4⟨(ΔH_clock)²⟩. Two regimes are computed: Gaussian momentum packets (classical) and momentum superpositions (quantum).

## Relation to the five Coastline claims
- **Claim I — emergent proper time / temporal record:** Supports. Proper time is POVM-encoded and read inferentially via conditional probabilities, not as the expectation of a sharp microscopic time variable — the internal clock DOF is precisely a "temporal record" carrying inferentially usable info about elapsed evolution.
- **Claim II — redundancy / stability / compressibility:** Largely silent. The setting is two clocks (bipartite/relational), not a many-record redundancy architecture; there is no proliferation, consensus, or compressibility analysis. At most, the existence of a stable classical-dilation value in the localized regime hints at the "stable" leg, but redundancy is absent.
- **Claim III — failure mode / nuisance-discrimination:** Supports. The quantum time-dilation correction marks the regime where a single classical time-dilation value no longer suffices — the clock in superposition has no well-defined proper-time reading agreeing with the classical relation, an instance of the framework's structural breakdown of a temporal-consensus variable. Distinguishing this nonclassical correction from a generic dephasing nuisance is exactly the discrimination Claim III demands.
- **Claim IV — operational anchors (Fisher / mutual info / cross-probe / coarse-graining):** Strong anchor. (i) Fisher information about elapsed proper time is explicit: F = 4⟨(ΔH_clock)²⟩, tying clock energy spread to temporal estimability. (ii) Cross-probe mismatch is built in: two clocks reading different proper times, with τ_A = (γ_B/γ_A)τ_B classically and ⟨T_A⟩ = (γ_C⁻¹ + γ_Q⁻¹)τ_B in the quantum regime (the γ_Q⁻¹ term is the mismatch). No mutual-information-between-records or coarse-graining-robustness analysis.
- **Claim V — positioning (PW bipartite vs quantum-Darwinism configurational vs multipartite redundancy):** Supports the PW-bipartite pole. This is the modern, relativistic, operational realization of the bipartite Page–Wootters correlation — exactly the "one available channel, not the consensus itself" that the framework positions against. It demonstrates how rich a *single* clock-pair channel can be while still lacking multipartite redundancy.

## Bearing on Ledger / Sail
CL-2026-007 candidate. This is the primary bipartite quantum/classical time-dilation reference for the ledger. Directly comparable to CL-2026-006 = [[sorci2026]] (trapped-ion quantum proper-time witness), which provides an experimental, possibly single-ion realization of the same quantum-vs-classical proper-time distinction; smith2020 supplies the theoretical conditional-probability scaffold. Experimental feasibility estimate (⁸⁷Rb clocks, v ≈ 5 and 15 m/s branches, γ_Q⁻¹ ≈ 10⁻¹⁵, ~10 s coherence at 10⁻¹⁴ s resolution) is the Sail-relevant number for assessing detectability.

## Lineage & citation chain
Builds directly on [[page1983]] (Page–Wootters conditional-probability formalism). External lineage: Giovannetti–Lloyd–Maccone "Quantum time" (2015); Zych–Costa–Pikovski–Brukner gravitational/quantum-clock interferometry; Helstrom and Holevo quantum estimation bounds; Mandelstam–Tamm. In-corpus sibling for experiment: [[sorci2026]].

## Open questions / flags
- Is the quantum time-dilation correction best read as a Claim III structural failure, or as a (still-classical, just averaged) shifted consensus value? The framework needs a sharp criterion to classify it — flag for Phase 3.
- The bipartite POVM here uses a single comparison clock; how it would extend to the multipartite-redundancy reading of Claim V is open and not addressed by the paper.
- No bibliographic flags: title, authors, journal, DOI, arXiv id all match. Final 2 pp. are extended methods, not read in full detail.
