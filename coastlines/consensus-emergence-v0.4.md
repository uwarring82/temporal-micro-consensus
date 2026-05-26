# Consensus-Emergence of Classical Proper Time

*A Coastline Note on the Emergence of Classical Proper Time from Microscopic Temporal Records*

| Field | Value |
| --- | --- |
| Version | v0.4 |
| Date | 2026-05-26 |
| Author | U. Warring |
| Affiliation | Physikalisches Institut, Albert-Ludwigs-Universität Freiburg |
| Licence | CC BY-SA 4.0 |
| Status | Draft Coastline — Local Stewardship |
| Predecessor | v0.3 (2026-05-26) |
| Successor | (none yet) |

---

## Endorsement Marker

This document is issued under **Local Stewardship** by U. Warring. It is a Coastline note in the sense of the Open-Science Harbour: a versioned, falsifiable framework proposal. It does **not** claim parity with externally validated physical laws — quantum mechanics, special relativity, general relativity, and the established results of quantum information theory — which are referenced here only as constraints, not as objects of derivation. Authority derives from clarity of use, not from institutional endorsement.

---

## External Constraints (citation only)

This coastline operates within, and does not attempt to derive, extend, or revise, the following established frameworks:

1. **Quantum mechanics** as a unitary theory of evolution and entanglement.
2. **Special relativity** as the structure of proper-time relations among inertial worldlines (the flat-spacetime baseline; the weak-field extension is item 5 and the *Regime of Validity* section).
3. **The Page–Wootters mechanism** (Page & Wootters 1983; modern developments including Smith & Ahmadi 2020, Mendes & Soares-Pinto 2019, Nambu 2022) as the canonical proposal for time emerging from quantum correlations between a clock subsystem and the rest of the universe.
4. **Quantum Darwinism** (Zurek and collaborators, 2003–present) as the canonical proposal for the emergence of classical objectivity through redundant proliferation of information into many environmental fragments. The environment-as-witness formulation of Ollivier, Poulin & Zurek (2004, 2005), and in particular its treatment of objectivity over *time-ordered* sequences of redundant records, is the closest configurational precursor to the temporal specialisation pursued in this coastline.
5. **General relativity**, in the **weak-field / post-Newtonian regime**, as the structure of proper-time relations among worldlines that may be accelerated and located at differing gravitational potential, with spacetime curvature entering perturbatively. The framework operates within this regime (see *Regime of Validity* below); it does not derive, extend, or modify general relativity, and does not address strong-field or quantum-gravitational regimes.

The present coastline does not compete with any of these. It uses their structure to articulate a more specific claim about *proper time as measured by physical clocks*.

---

## Regime of Validity

The framework as written applies to proper-time relations in the **special-relativistic and weak-field (post-Newtonian) regime**:

- **Flat spacetime among inertial worldlines** (special relativity) is the baseline — External Constraints item 2.
- The framework extends to **accelerated worldlines and worldlines at differing gravitational potential**, with spacetime curvature entering **perturbatively** (the post-Newtonian expansion) — External Constraints item 5. There, τ_cl is the general-relativistic proper time along each worldline, and the Claim II criteria and Claim IV measures remain well-defined.

Two provisos make the extension precise:

- **Comparison-protocol proviso.** Claim II's consensus and the Claim IV cross-probe measure presuppose a *well-defined inter-worldline comparison (synchronisation) scheme* — e.g. a shared coordinate time or master-clock reference, as used in classical and proposed quantum clock networks. The framework's temporal-consensus and cross-probe-mismatch statements are defined *relative to* such a protocol. Where curvature or coordinate choice makes the comparison ambiguous, additional structure is required before the criteria apply.
- **Curvature as the incompressible residual.** In the multi-worldline setting, the leading (Newtonian / first-order redshift) agreement among records is the *compressible* part — a single τ_cl organises it — while spacetime curvature appears as the *incompressible cross-probe residual* that no single τ_cl reproduces (e.g. the three-node beat-note residual Δω of distributed-clock proposals). Curvature thus enters the framework through Claim II.3 and Claim IV, not as an exception to them.

**Outside scope without additional structure:** strong-field or non-perturbative curved-spacetime regimes; settings in which no shared comparison protocol exists; and quantum-gravitational regimes (see *Anti-Claims* §7 and *Deferred Items*).

---

## Novel Boundaries

### Claim I — Problem statement

A classical proper-time variable is not assumed to be microscopically sharp. It is treated as an *emergent effective variable*: a parameter that need not have a well-defined value at the level of individual quantum degrees of freedom, and which acquires operational meaning only at the level of coarse-grained collective records.

*Terminology.* Here, **"temporal record"** denotes any physical degree of freedom whose state carries inferentially usable information about elapsed evolution, whether or not that information is classically accessible in a single shot. Both stored quasi-classical imprints and transient phase correlations qualify, provided they support some inferential read-out under a specified measurement scheme.

### Claim II — Emergence criterion

A classical proper-time variable τ_cl emerges for a physical subsystem only when its microscopic degrees of freedom support a temporal inference that is jointly:

1. **Redundant** — many microscopic carriers encode mutually compatible temporal information.
2. **Stable** — the inferred parameter is insensitive to tracing out small subsets of carriers or to local perturbations of individual carriers.
3. **Compressible** — a single coarse-grained parameter τ_cl suffices to organise the temporal behaviour of the observables relevant to the inference task, such that introducing additional microscopic temporal labels yields no statistically or operationally significant gain in predictive or inferential performance.

These three conditions are stated in the spirit of Zurek's quantum-Darwinism criteria for the emergence of classical objectivity, here specialised to *temporal* rather than configurational records.

*Status of the specialisation.* This transplant is, at present, a structural analogy rather than a derived or exhibited result. The quantum-Darwinism criteria were established for *configurational* records (pointer states proliferated into an environment); a worked exemplar of *redundant temporal* records — many carriers independently encoding mutually compatible elapsed-time information — has not yet been demonstrated. The coastline adopts the criteria on the strength of the analogy while registering the absence of such an exemplar as its principal open problem (see *Anti-Claims* and *Deferred Items*).

*On "many" and "redundant."* The redundancy of Claim II.1 requires *independent carriers that each encode mutually compatible temporal information* — the configuration that underwrites stability under marginalisation (Claim II.2). It must be distinguished from two weaker conditions with which it is easily conflated: (i) *multi-channel within a single subsystem* — several observables of one constituent; and (ii) *entanglement-enhanced multipartiteness*, in which many carriers are correlated to improve metrological sensitivity (GHZ-, W-, or NOON-type states) but are deliberately *anti-redundant*, so that tracing out a carrier degrades the joint estimate rather than leaving compatible copies behind. Multipartiteness is necessary but not sufficient for redundancy: a system may be strongly multipartite and yet carry no redundant temporal record.

### Claim III — Failure mode

When the conditions of Claim II fail for a subsystem, the appropriate description is not merely "the clock decohered." More specifically:

> The subsystem no longer supports a classical temporal-consensus variable.

This relocates the failure from an opaque reduction in interferometric coherence to the *breakdown of an explicit emergence criterion*. The distinction is operationally meaningful: it predicts which observables should and should not lose informational content, and against which nuisance channels the failure should be discriminated.

Ordinary dissipation, technical dephasing, and tracing-induced loss of correlations may all degrade temporal consensus by reducing redundancy, stability, or compressibility through entirely conventional mechanisms. The framework therefore requires *discriminating structural consensus failure from generic nuisance-induced coherence loss*. This discrimination is a *necessary step in* converting the criterion of Claim II from a descriptive framework into an experimentally credible witness.

### Claim IV — Operational anchors

The criterion of Claim II is intended to be cashed out in operational terms. Candidate measures, all standard in quantum information and metrology:

- **Fisher information** about elapsed time, distributed across subsystems and probes (cf. Nambu 2022 for the Page–Wootters setting).
- **Mutual information** between temporal records held by different constituents or by different observables of the same constituent.
- **Cross-probe mismatch** between elapsed-time estimates inferred from independent observables of the same physical evolution — including, in the weak-field regime, the residual disagreement among spatially separated probes that encodes spacetime curvature (see *Regime of Validity*).
- **Robustness under coarse-graining** — invariance of the inferred τ_cl under partial trace of small subsets of carriers.

The coastline does not, at v0.4, commit to one of these as canonical. It commits only to the position that *consensus-emergence is operational, not metaphorical*, and that any deployment of the framework must specify which measure is being used.

### Claim V — Positioning

Consensus-emergence sits between two existing frameworks and is distinct from both:

- **Page–Wootters** treats time as a correlation between a designated clock subsystem and "the rest." It is a *bipartite-correlation* framework: it identifies a two-part structure carrying temporal information. Consensus-emergence is distinct in that it concerns *many* microscopic carriers and the conditions under which they *jointly* support a *single* effective temporal parameter. It is a *multipartite-redundancy* framework. Page–Wootters correlations are one available channel of temporal information within the consensus picture, not the consensus itself. Consensus-emergence therefore does not deny that time may be read relationally from subsystem–rest correlations; it claims instead that a classical proper-time variable requires an additional robustness condition across multiple carriers or records.
- **Quantum Darwinism** treats the emergence of classical objectivity through redundant encoding of system information in the environment. Consensus-emergence applies this architecture specifically to *temporal* records and connects it to the metrological question of proper time as measured by physical clocks. The three criteria of Claim II are Zurek's criteria applied to the temporal degree of freedom. The distinction in Claim II's terminology note matters for placement here: distributed-clock and entanglement-enhanced metrology protocols realise a *multipartite* temporal structure but are typically *anti-redundant*, so they occupy the multipartite axis without yet satisfying the redundant-consensus condition this coastline requires.

The contribution is therefore not a new theory of time. It is the specific claim that *proper time as measured by physical clocks is best understood as a consensus variable in the quantum-Darwinism sense, with Page–Wootters-type correlations as one available channel of temporal information*.

---

## Anti-Claims

This coastline explicitly does **not** claim:

1. That "consensus" is a fundamental theory of time emergence. It is a productive interpretive framework subject to operationalisation.
2. That microscopic degrees of freedom literally "decide" or exhibit agent-like behaviour. "Consensus," "agreement," and "support" are placeholders for the operational measures of Claim IV, and the language must be read in that sense. The term *decision* is excluded from this coastline by stipulation; it is reserved for explanatory use in Sails.
3. That Page–Wootters or quantum Darwinism are insufficient or in need of correction. The coastline assumes both as background and specialises their conjunction.
4. Parity with the established physical frameworks of the External Constraints section. The coastline is a framework for interpretation and design, not a derivation of physical law.
5. A bridge to the Causal Clock Unification Framework (CCUF) or to any other Harbour framework. Such bridges may exist (see *Deferred Items*) but are not committed at v0.4.
6. That the quantum-Darwinism emergence criteria have been *established* for temporal records. Claim II transplants criteria proven for configurational records onto temporal ones by structural analogy. The coastline does not claim this transplant has been formally derived or experimentally exhibited; exhibiting a system that instantiates *redundant temporal* records — as opposed to merely multipartite or entanglement-enhanced ones — is its principal open problem (see *Deferred Items*).
7. That the framework applies in **strong-field, non-perturbative, or quantum-gravitational** regimes, or absent a well-defined inter-worldline comparison protocol. Its scope is the SR-and-weak-field (post-Newtonian) regime under the provisos of the *Regime of Validity* section; extension beyond that requires additional structure.

---

## Falsifiability

The framework is falsifiable in the following senses:

**Strong falsification.** If a subsystem can fail the Claim-II conditions in an operationally well-defined sense, yet still admit a single robust classical proper-time variable across independent observables with no measurable inconsistency, the framework is incomplete or incorrect. The coastline must then be revised or retired. The burden of "operationally well-defined" rests on the measures of Claim IV: a falsification must specify which measure of redundancy, stability, or compressibility was found to fail and by what margin.

**Weak falsification.** For any proposed experimental witness of "quantum proper-time effects" in clocks, the framework predicts that the witness must be expressible as a *partial failure* of one or more of the three Claim-II conditions, and must be discriminable from ordinary decoherence channels by a separability analysis grounded in the operational measures of Claim IV. A witness that cannot be so expressed is either misclassified or evidence against the framework.

---

## Deferred Items

The following are noted as plausible future extensions but are **not committed** at v0.4:

- **Worked exemplar of redundant temporal records (principal open problem).** A concrete model in which the *same* elapsed time is redundantly encoded across many independent carriers — neither configurational (quantum Darwinism) nor merely entanglement-enhanced (distributed-clock metrology) — would convert Claim II's temporal transplant from analogy into demonstration. A temporal-redundancy functional in the spirit of Riedel-style quantum-Darwinism information measures is the natural first instrument. This is the framework's principal open problem (cf. *Anti-Claims* §6).
- **CCUF bridge.** Possible structural analogy between L₀ consensus-emergence (microscopic temporal records) and L₁ architectural agreement (CCUF η-parameter, comparison-geometry boundary, "agreement, not oscillation, defines a clock"). Both layers can be read as expressions of one principle — that time is a robust collective variable, not a private property — at distinct scales. Deferred to a future coastline note pending independent maturation of the present framework, in keeping with Lock-Key discipline.
- **Application to trapped-ion clock experiments.** The Sorci et al. (2026, *Phys. Rev. Lett.* 136, 163602) visibility-loss witness is a candidate case study; a Breakwater dossier is the appropriate venue for that classification, not this coastline.
- **Connection to thermodynamic and information-theoretic arrow-of-time discussions.** Noted but not pursued here.
- **Quantitative criteria.** Specific thresholds (e.g. mutual-information requirements, Fisher-information distribution profiles) that would render Claim II quantitatively testable. Deferred pending engagement with concrete experimental settings.
- **Strong-field / non-perturbative curved-spacetime extension.** Extending the Claim II/III criteria beyond the weak-field (post-Newtonian) regime — to strong curvature, or to settings lacking a shared inter-worldline comparison protocol — requires additional structure and is not committed here (cf. *Regime of Validity*; *Anti-Claims* §7).

---

## Load-Bearing Sentence

For citation in dependent documents (Sails, Breakwater entries, future coastlines):

> Classical proper time is not the expectation value of an underlying microscopic time variable, but the robust collective parameter that best organises and stabilises the temporal records of many underlying degrees of freedom.

---

## Version History

| Version | Date | Notes |
| --- | --- | --- |
| v0.1 | 2026-05-23 | Initial draft. Five claims, anti-claims, falsifiability clauses, deferred items, and load-bearing sentence locked. Standalone — no CCUF bridge committed. |
| v0.2 | 2026-05-23 | Surgical tightening pass. (1) Title updated to *Consensus-Emergence of Classical Proper Time*. (2) Claim II.3 "compressible" reformulated in terms of inference-task adequacy and statistical/operational gain. (3) Terminology paragraph defining "temporal record" added to Claim I. (4) Claim III extended with a paragraph naming nuisance-discrimination as load-bearing. (5) Claim V extended with one sentence making PW compatibility explicit. (6) Strong falsification clause softened to require operational well-definition; weak falsification unchanged. No claim retired; no new claim added. |
| v0.3 | 2026-05-26 | Post-literature-review revision (driven by `docs/literature/synthesis-v0.1.md`). **Lineage fixes** (External Constraints): removed *Hartong–Have–Obers–Pikovski 2024* — verified to be a post-Newtonian coupling-prescription paper, not a Page–Wootters development; corrected *Mendes & Soares-Pinto* 2018 → 2019 (publication year); added the *Ollivier–Poulin–Zurek* (2004, 2005) environment-as-witness / objective-histories formulation as the closest configurational precursor. **Conceptual sharpening:** Claim II gains a *status-of-specialisation* paragraph (the configurational→temporal transplant is an analogy lacking a worked exemplar) and a *"many vs redundant"* terminology note (multipartiteness ≠ redundancy; entanglement-enhanced states are anti-redundant); Claim V gains the corresponding placement sentence; new **Anti-Claim #6** disclaims that the temporal transplant is established; **Deferred Items** gains the redundant-temporal-exemplar *principal open problem*. **Claim III** final sentence softened ("is what converts" → "is a *necessary step in* converting"). No claim retired; Load-Bearing Sentence unchanged. **Deferred to a later version** (in roadmap, not folded here): FIT citation + Claim V positioning bullet; GR-regime boundary statement; Claim IV measure-registration protocol. |
| v0.4 | 2026-05-26 | **GR-regime boundary statement** — a v0.3-deferred candidate, made load-bearing by Ledger CL-2026-008 (its D1 showed the framework could not classify curvature/redshift clock-network probes without it). **Decision: extend, not bound.** The framework's stated scope is extended to the **SR-and-weak-field (post-Newtonian) regime** — accelerated worldlines and worldlines at differing gravitational potential, curvature entering perturbatively — rather than capped at SR, because the framework's own machinery already accommodates this regime (a curvature signal is a Claim IV cross-probe mismatch / Claim II.3 incompressible residual). Added: External Constraints item 5 (general relativity, weak-field/post-Newtonian); a new **Regime of Validity** section (scope; comparison-protocol proviso; curvature-as-incompressible-residual; explicit exclusions); **Anti-Claim #7** (no strong-field / quantum-gravity / protocol-free regimes); a curvature clause on the Claim IV cross-probe anchor; a Deferred strong-field-extension item. No claim retired; Load-Bearing Sentence unchanged. **Consequence:** this satisfies the *framework-side* condition of CL-2026-008 D1; that entry may now be re-evaluated against v0.4 (its experimental-discriminability condition D2 still stands). Still deferred: FIT citation + positioning; Claim IV measure-registration protocol. |

---

*This coastline is a framework note under Local Stewardship. It does not claim parity with externally validated physical laws. Citation of this document should reference its version and date.*
