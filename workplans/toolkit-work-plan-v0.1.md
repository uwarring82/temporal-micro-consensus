# Toolkit Work Plan — Numerical Toolkit for Temporal Micro Consensus

**Version:** v0.1 (draft, 2026-05-27; post-review rev. 2026-05-27)
**Endorsement Marker:** Local Stewardship (Ulrich Warring, Physikalisches Institut, Albert-Ludwigs-Universität Freiburg). Authority from use, not endorsement.
**Lineage:** Coastline v0.4 (Consensus-Emergence of Classical Proper Time) → Ledger CL-2026-006 v0.4 (Sorci et al. classification, D1 nuisance-decomposition forward target) → MN v0.2 (Temporal-Redundancy Functional R_δ, §2 analytic poles, §6c open-temporal-instrument sketch) → this plan.
**Placement:** Within `temporal-micro-consensus` repository, at `numerics/`.

---

## §1 — Purpose and scope

### Purpose

To build a numerical toolkit that operationalises the framework's declared anchor measures — `I(C:M)`, Fisher `F[τ]`, and `R_δ` — through master-equation simulation of clock-plus-carrier systems, with two priority deliverables: (a) a quantitative nuisance-budget decomposition for the Sorci et al. (PRL 2026) two-carrier protocol, producing the per-channel decomposition named by Discriminant D1 of Ledger CL-2026-006 (D1 is one of three upgrade conditions — see §6); and (b) a numerically computed `R_δ(N, ε)` in the redundant-pole regime sketched in MN v0.2 §6c — where the per-carrier distinguishability `ε` is derived dynamically, not posited — supplying the framework's principal open problem (Anti-Claim #6) with a candidate worked exemplar within the assumed regime.

### In scope

- Master-equation evolution for clock-plus-N-motional-mode systems under a **four-layer nuisance model**, only one layer of which is Liouvillian: (i) *initial-state* errors — preparation infidelity, applied to `ρ(0)`; (ii) *dynamical* Lindblad dissipators — motional heating `ṅ` and dephasing `γ_φ`; (iii) *stochastic-Hamiltonian* noise — drive-phase noise during interrogation; (iv) *read-out* errors — detection-correlated infidelity, applied at measurement. (Lumping (i), (iii), (iv) into "Lindblad channels" would misrepresent their physics.)
- Squeezed-state preparation primitives (Sorci protocol substrate).
- Multi-carrier evolution under pure-dephasing channels (open-temporal-instrument substrate, redundant-pole regime).
- Post-processors computing `I(C:M)` and Fisher `F[τ]` from evolved states (both state-intrinsic), and `R_δ` from a temporal-record ensemble (read-out model + finite pointer; see Phase 2), under declared fragment partitions.
- Regression tests validating numerical results against MN v0.2 §2 analytic poles.
- Two protocol modules: Sorci-protocol (N=2) and open-temporal-instrument (N≫2, redundant-pole).
- Reproducible example notebooks demonstrating both modules.
- FAIR-compliant documentation: `numerics/README.md`, dependency manifest, test suite, examples directory.

### Out of scope (for v0.1; may be added in later toolkit versions)

- Strong-field general-relativistic regime (deferred per Coastline v0.4).
- Quantum-gravitational regime (deferred per Coastline v0.4 Anti-Claim #7).
- Entangled N≫2 multi-carrier cases requiring full Hilbert-space simulation beyond N≈10 (tensor-network methods deferred; redundant-pole assumption keeps Phase 3 within product-state-tractable territory).
- Distributed-clock-network specific physics relevant to CL-2026-008 (forward target for toolkit v0.2 or later).
- Page-Wootters bipartite protocol simulation relevant to CL-2026-007 (forward target; structurally distinct from Sorci and open-temporal-instrument modules).
- Experimental data analysis or fitting pipelines (the toolkit produces theoretical predictions; experimental analysis is a separate stewardship).

---

## §2 — Locked architectural decisions

The following are committed at v0.1 and require deliberate revision to change. Each carries a citation to its prior justification.

**D1. Placement.** Toolkit lives within the existing `temporal-micro-consensus` repository at `numerics/`. Trade-off accepted: lower stewardship overhead and tighter framework-toolkit coupling, at the cost of mixed update cadences within one Git history. *Justification: tractability under solo stewardship (decision 2026-05-27).*

**D2. Decomposition.** Shared computational core (master-equation evolution + anchor-measure post-processors) feeds two distinct protocol modules. *Justification: ~70% code overlap between Sorci-protocol and open-temporal-instrument computations; symmetric computational substrate forces architectural symmetry between anchors.*

**D3. Computational substrate.**
- *Sorci-protocol module:* QuTiP (`mesolve`, `mcsolve`), parallelised over nuisance parameters.
- *Open-temporal-instrument module:* product-state direct simulation, restricted to the redundant-pole regime where the multi-carrier state factorises across carriers (consistent with MN v0.2 §6c's assumed regime).
- *Tensor-network methods:* deferred until a specific Ledger entry forces them.

*Justification: QuTiP is mature and operator-rich for trapped-ion settings; product-state restriction is honest about the redundant-pole assumption and avoids exponential scaling.*

**D4. Versioning convention.** Toolkit uses semantic versioning (`numerics-v0.1`, `numerics-v0.2`, ...) in a namespace separate from framework artefact versioning (`Coastline v0.x`, `CL-YYYY-NNN v0.x`, `MN v0.x`). Repository-level Zenodo release tags continue the existing convention (`framework-status-YYYY.MM.DD`).

**D5. Regression-test contract.** Phase 2 anchor-measure post-processors must reproduce MN v0.2 §2 analytic poles within a declared numerical tolerance before Phase 3 may begin. This is a gate condition, not an aspiration. *Justification: without analytic-poles regression coverage, Phase 3 numerical results have no audit path back to the framework's analytic foundation.*

**D6. Lock-Key discipline maintained.** Concepts remain stable across versions (anchor measures, Lindblad channel declarations, fragment-partition API); implementations free. Public function signatures stable from v0.1; internal numerics free to evolve.

---

## §3 — Phase structure

The plan locks *ordering* and *gate conditions* between phases. No timeline estimates: solo open-science scheduling is unreliable, and committing to dates creates false accountability. Phases progress when gate conditions are satisfied.

### Phase 0 — Infrastructure

**Deliverables:**
- `numerics/` directory scaffold with `README.md`, `requirements.txt` (or `pyproject.toml`), `tests/`, `examples/`, `src/tmc_numerics/` package skeleton.
- Dependency manifest: `qutip`, `numpy`, `scipy`, `matplotlib`, `pytest`. (Optional: `jupyter` for examples; `tqdm` for progress bars.)
- `.gitignore` updated for `__pycache__/`, virtual environments, build artefacts, cached results.
- `numerics/CITATION.cff` or appended section to repository `CITATION.cff` describing code citation.
- Minimal `pytest` test harness with one trivial pass-through test (verifies CI plumbing).

**Gate to Phase 1:** Repository scaffold committed; `pytest` runs cleanly on a fresh clone with declared dependencies.

### Phase 1 — Core layer

**Deliverables:**
- `MasterEquationSystem` class: clock-plus-N-motional-mode Hamiltonian construction with the four-layer nuisance model — dynamical Lindblad dissipators (heating `ṅ_k`, dephasing `γ_φ,k` per mode) in the Liouvillian; preparation infidelity `ε_prep` applied to the initial state; drive-phase noise as a stochastic-Hamiltonian term; detection infidelity `ε_det` applied at read-out (the read-out layer is shared with the Phase-2 `TemporalRecordEnsemble`).
- `evolve(state, times)` API returning state trajectory.
- Squeezed-state preparation primitive (Sorci-protocol-compatible).
- Product-state initialisation primitive (open-temporal-instrument-compatible).
- Unit tests covering: Hamiltonian construction, channel application correctness, state-output API stability, evolution under known closed-form cases (e.g. damped harmonic oscillator).

**Gate to Phase 2:** Core layer passes all unit tests; API documentation in `numerics/README.md` reflects committed function signatures.

### Phase 2 — Anchor-measure layer

**Deliverables:**
- `mutual_information(state, partition)` post-processor computing the quantum `I(C:M)` classification anchor for an arbitrary clock-environment partition (state-intrinsic).
- `quantum_fisher(state, parameter)` post-processor computing the `F[τ]` resolution anchor (state-intrinsic).
- `TemporalRecordEnsemble`: the read-out abstraction that `R_δ` requires and a density operator does **not** carry — a finite temporal pointer `T` (dimension `d`, prior `P(T)`) and per-carrier fragment read-out maps (POVMs) turning each carrier's state into a noisy estimate of `T`. This makes the load-bearing einselected-pointer + per-carrier-read-out assumption explicit (MN v0.2 §1.1) rather than hiding it.
- `temporal_redundancy(ensemble, deficit)` post-processor computing `R_δ = N / m_δ` per MN v0.2 §1, returning the **undefined** case when the partial information `I(m) = I(T : F_m)` never reaches `(1−δ) H_T`. Note this is mutual information between the *classical pointer* `T` and the fragment read-out — distinct from the quantum `I(C:M)` above.
- Regression test suite: numerical `R_δ` values for canonical cases reproduce MN v0.2 §2 analytic poles (cat-state and product-state limits) within declared tolerance (suggested: 10⁻⁴ relative error).
- Cross-anchor **invariant** tests (explicit assertions, not subjective verdict-matching). The resolution anchor `F[τ]` is *not* a classifier — reading it as one is the named CL-2026-007 v0.1 failure mode (MN v0.2 §4). The suite asserts, on shared states: product (redundant) pole → `R_δ ≫ 1`; GHZ-shadow (anti-redundant) pole → `R_δ = 1` with every proper-fragment `I(T:F) = 0`; the two *classification* anchors `I(C:M)` and `R_δ` co-classify; `F[τ]` is **extensive** (additive over independent carriers, `F_τ(m) = m·F_1`) and **rises** toward the anti-redundant pole exactly where `R_δ` falls — the resolution and classification anchors anti-correlate and are non-substitutable; per-carrier nuisance collapses the `R_δ` plateau with **no** change in entanglement structure (MN v0.2 §2, §5).

**Gate to Phase 3:** All regression tests pass at declared tolerance; the gate condition D5 is satisfied. Failure here returns to Phase 1 or to MN v0.2 revision, not to Phase 3 with reduced standards.

### Phase 3 — Protocol modules (parallel)

The two modules run in parallel after the Phase 2 gate. Different priority profiles: Sorci module is D1-driven (operational payoff for CL-2026-006); open-temporal-instrument module is exemplar-driven (operational payoff for the principal open problem and the post-toolkit journal paper).

**Module 3a — Sorci protocol (N=2):**
- Implementation of the squeezed-state Ramsey protocol from Sorci et al. (PRL 136, 163602, 2026).
- Parameter sweeps over: squeezing strength `r`, heating `ṅ`, motional dephasing `γ_φ`, preparation infidelity, drive-phase noise, mode mixing, detection-correlated infidelity.
- Output: nuisance-budget table decomposing predicted `I(C:M)` (or visibility) loss into per-channel contributions at experimentally relevant parameters. The four nuisance layers map one-to-one onto D1's enumerated contributions: unitary time-dilation entanglement (Hamiltonian), heating + dephasing (dynamical), preparation infidelity (initial-state), detection-correlated infidelity (read-out).
- Cross-check (directional, **not** a curve): at the zero-nuisance limit, reproduce the Sorci visibility / `I(C:M)(r)` scaling (`∝ sinh²(2r)`), and exhibit the single anti-redundancy transition for `R_δ` (`2`→`1`, or undefined→`1`) that CL-2026-006 v0.4's `R_δ`-anchor subsection describes. At `N = 2`, `R_δ ∈ {undefined, 1, 2}` admits no `R_δ(r)` curve (MN v0.2 §3); the continuous observables here are `I(C:M)(r)` and `F[τ](r)`.

**Module 3b — Open temporal instrument (N≫2, redundant-pole):**
- Implementation of N independently pure-dephasing carriers with assumed-einselected temporal pointer (per MN v0.2 §6c).
- Computation of `R_δ(N, ε)` curves across declared parameter ranges, with the per-carrier distinguishability `ε` derived from the single-carrier master equation (`ε = ε(γ_φ, ṅ, t)`), not posited — the dynamical increment over MN v0.2 Appendix A, which fixes `ε` by hand.
- Output: first quantitative redundant-pole results for temporal records; serves as a candidate worked exemplar for the framework's principal open problem (Anti-Claim #6) within the assumed regime (whether any instance counts as *the* exemplar is a Coastline-level steward judgement — Coastline v0.4, MN v0.2 §6).
- *Explicit caveat:* the einselection of the temporal pointer is assumed, not derived. This caveat propagates into any publication derived from Module 3b results.

**Gate to Phase 4:** Both modules produce reproducible results stored in `numerics/examples/` as notebooks; both modules' results documented in `numerics/results/` with declared parameters and reproducibility metadata.

### Phase 4 — Feed-forward

**Deliverables:**
- *Framework feed-forward:* draft of Ledger CL-2026-006 v0.5, incorporating Module 3a nuisance-budget table as quantitative grounding for D1; verdict revisited under quantitative evidence (may move from UNDERDETERMINED to one of the stable Ledger classifications, or remain UNDERDETERMINED with sharpened discriminant conditions).
- *Methodological feed-forward:* draft of MN v0.3, incorporating Module 3b redundant-pole curves as the master-equation companion to MN v0.2's analytic-poles foundation. Configurational counterpart of arXiv:2509.17775 now matched on the temporal side.
- *Publication feed-forward:* numerical results from Modules 3a and 3b incorporated into the post-toolkit journal-submission draft (combining Coastline + MN + worked exemplar). This is the strongest-possible-paper target under the publication staging *proposed* in §7 (a proposal pending the roadmap's still-open external-circulation decision, not a settled stewardship decision).
- *Possible Coastline feed-forward:* if cross-anchor practice across CL-2026-006 v0.5 and a future Ledger entry forces the measure-registration protocol commitment, Coastline v0.5 is drafted at this point.

**Phase 4 has no gate to a Phase 5 — it is the toolkit's handoff back to the framework deliberation stream.**

---

## §4 — Dependencies

**Required (Phase 0):**
- Python ≥ 3.10
- `qutip` ≥ 5.0
- `numpy` ≥ 1.24
- `scipy` ≥ 1.10
- `pytest` ≥ 7.0

**Recommended (Phase 0):**
- `matplotlib` ≥ 3.7 (for examples and result visualisation)
- `jupyter` (for example notebooks)
- `tqdm` (for long-running parameter sweeps)

**Provisional (later phases):**
- `quimb` or `TeNPy` — if and only if a Ledger entry forces tensor-network methods. Deferred.

Dependency pinning policy: minimum versions declared in `requirements.txt`; pinned versions for reproducibility in `requirements-lock.txt` (generated, committed).

---

## §5 — Validation strategy

Three layers, mirroring the framework's three-anchor architecture:

1. *Unit tests* — function-level correctness (Phase 1 onward), run on every commit.
2. *Regression tests against MN v0.2 §2 analytic poles* — architectural integrity gate (Phase 2), must pass before Phase 3. (Note: the §2 poles are classical information-theoretic computations regenerated by MN v0.2 Appendix A; this layer validates the `R_δ` post-processor's audit path, while the master-equation core is validated by the Phase-1 closed-form unit tests.)
3. *Cross-anchor invariant checks* — explicit assertions encoding the resolution/classification split: the two classification anchors `I(C:M)` and `R_δ` co-classify, while the resolution anchor `F[τ]` anti-correlates with `R_δ` and must **not** be read as a classifier (MN v0.2 §4; this guards the CL-2026-007 v0.1 failure mode). Run on shared evolved states (Phase 2 onward).

All test results reproducible by `pytest numerics/tests/`. Failed tests block merges to `main`.

---

## §6 — Connection to framework artefacts

The toolkit's deliverables map to specific framework-side discharge points:

| Toolkit deliverable | Framework discharge |
|---|---|
| Phase 2 regression tests | Validates MN v0.2 §2 analytic poles numerically |
| Module 3a nuisance budget | Produces the per-channel decomposition D1 names (1 of 3 conditions; D2/D3 experimental) |
| Module 3a `I(C:M)(r)` scaling + `R_δ` transition | Confirms CL-2026-006 v0.4 `R_δ`-anchor *directional* reading (N=2: no `R_δ(r)` curve) |
| Module 3b `R_δ(N, ε)` curves | Candidate worked exemplar for Coastline v0.4 Anti-Claim #6 (within assumed regime) |
| Module 3b einselection caveat | Preserves Anti-Claim #6 as an open question outside the regime |

**On Discriminant D1 (necessary, not sufficient).** D1 is one of three conditions (D1–D3) for upgrading CL-2026-006 from UNDERDETERMINED to COMPATIBLE; D2 (null test) and D3 (a *measured* `r`-scan) are experimental and lie outside the toolkit. The toolkit produces the *theoretical* per-channel decomposition D1 names — it does not, by itself, upgrade the verdict; Phase 4 revisits the verdict under the new evidence rather than pre-deciding it. CL-2026-006 also names **CL-2026-005 (the CBG open-quantum-systems pipeline)** as the methodological infrastructure for this very decomposition; whether the Sorci module reuses that pipeline or reimplements its decomposition independently in QuTiP is registered as Q5 (§8), to be settled in Phase 0 rather than silently duplicated.

The toolkit does *not*:
- Resolve Anti-Claim #6 fully (the temporal pointer's einselection remains assumed in Module 3b).
- Resolve Anti-Claim #7 (no strong-field/quantum-gravity regime; deferred).
- Force commitment to Coastline v0.5 measure-registration protocol (this remains operationally previewed in CL-2026-006 v0.4 until accumulated practice forces it).

---

## §7 — Connection to publication strategy

This plan *proposes* the publication staging below. It is a proposal, not a settled stewardship decision — the roadmap still lists the external-circulation / venue choice as pending (`docs/roadmap.md`, *Stewardship decisions pending*). It is registered here to make Module 3b's publication dependency explicit:

- *arXiv Sail* (commentary on Sorci et al.): does not depend on toolkit completion. Proceeds independently on the publication track.
- *arXiv programme paper* (Coastline + MN combination, research-programme framing): does not depend on toolkit completion. Proceeds independently on the publication track.
- *Full journal paper* (Coastline + MN + worked exemplar): **depends on Phase 3 Module 3b completion.** This is the strongest-possible-paper target; the toolkit's Phase 3 deliverables are the structural prerequisite.

The work plan registers this dependency explicitly so that Module 3b's priority reflects publication payoff, not just architectural completeness.

---

## §8 — Architectural questions (registered at v0.1; Q3 resolved, Q5 added)

- *Q1.* Should `numerics/CITATION.cff` be a separate file or a section in the repository-root `CITATION.cff`? (Decision deferred to Phase 0 implementation.)
- *Q2.* Continuous integration (GitHub Actions running `pytest` on push) — yes or no for v0.1? (Recommend yes; defer to Phase 0 implementation.)
- *Q3 (resolved at v0.1).* Result-archival policy: Phase-3 numerical results are committed to `numerics/results/` as static files with reproducibility metadata (parameters, RNG seeds, code version), for citation stability — this is what the Phase 3 gate already requires, so on-demand-only generation is rejected (it would make that gate non-auditable).
- *Q4.* Distribution scaling: at what point (if any) does the toolkit warrant PyPI distribution or its own dedicated documentation site? (Hold until external usage signals appear.)
- *Q5.* Relation to CL-2026-005 (CBG open-quantum-systems pipeline), named by CL-2026-006 as the D1-decomposition infrastructure: does the Sorci module reuse the CBG pipeline or reimplement its decomposition independently in QuTiP? (Resolve in Phase 0, before duplicating effort.)

---

## §9 — Anti-claims for the toolkit

For symmetry with the framework's Coastline-style anti-claim discipline, the toolkit declares its own limits:

**A1.** The toolkit does not establish that classical proper time *is* an emergent collective variable. It quantifies anchor-measure values for specific protocols under specific assumptions; framework-level claims remain framework-level.

**A2.** Numerical reproduction of MN v0.2 §2 analytic poles is a consistency check, not a derivation. The analytic poles themselves rest on assumptions (Schmidt structure, idealised dephasing) that the toolkit inherits, not validates.

**A3.** Module 3b's redundant-pole results are exemplars within an assumed regime. They do not extend to entangled multi-carrier cases or to regimes where the einselection assumption fails.

**A4.** The toolkit's nuisance budget (Module 3a) predicts experimental behaviour under declared Lindblad channels. Channels not declared (e.g. unmodelled correlated noise sources) are not bounded by the budget. Discriminant D1 of CL-2026-006 is satisfied *under the declared channel set*, not absolutely.

**A5.** The toolkit's verdict-level results feed back into Ledger entries via human-deliberated framework revision. Numerical results do not auto-update Ledger verdicts; the Lock-Key discipline keeps interpretation human.

---

## §10 — Version history

- **v0.1** (2026-05-27): Initial draft. Scope, locked architectural decisions (D1–D6), phase structure (Phase 0–4), dependencies, validation strategy, framework-artefact mapping, publication-strategy connection, open questions, anti-claims.
- **v0.1 rev.** (2026-05-27, post-review): Folded a three-pass review (steward + IDE reviewer + Claude), nine findings, tightened in place. **§3/§5:** `R_δ` post-processor now built on an explicit `TemporalRecordEnsemble` read-out abstraction (pointer `T`, `P(T)`, per-carrier read-out maps, deficit `δ`, undefined case), distinguished from quantum `I(C:M)`; cross-anchor tests rewritten as explicit invariants encoding the resolution/classification split (guarding the CL-2026-007 v0.1 failure mode of reading `F[τ]` as a classifier). **§1/§3:** nuisance model split into four layers (initial-state / dynamical-Lindblad / stochastic-Hamiltonian / read-out), mapped onto D1(i)–(v); dropped the stray squeezing knob `r` from the redundant-pole observable (`R_δ(N, ε)`, `ε` dynamically derived); Module 3a `R_δ` cross-check rewritten as a directional N=2 transition (not an `R_δ(r)` curve). **§1/§6:** "satisfies D1" softened to "produces the D1 decomposition" (D1 = 1 of 3 conditions; D2/D3 experimental); CL-2026-005/CBG relation registered (Q5); "first worked exemplar" → "candidate exemplar within the assumed regime". **§7:** publication staging reframed as a proposal pending the roadmap's open external-circulation decision. **§8:** Q3 (result archival) resolved; Q5 (CBG) added. No locked decision (D1–D6) changed.

---

*End of Toolkit Work Plan v0.1.*
