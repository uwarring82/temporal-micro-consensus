# Harbour View — Temporal Redundancy and Emergent Proper Time

**Document type:** Harbour View. A presentational vantage-point document under Local Stewardship — neither a peer-reviewed publication nor an authoritative version of any of the framework artefacts it presents.
**Version:** v0.1
**Date:** 2026-05-28 (full draft complete; awaiting tagged release).
**Endorsement Marker:** Local Stewardship (Ulrich Warring, Physikalisches Institut, Albert-Ludwigs-Universität Freiburg). Authority from use, not endorsement; the externally validated physical theories cited below — quantum mechanics, special relativity, and general relativity in its weak-field regime — are referenced only as *constraints* on the framework, not as objects of derivation or as endorsers of the work.
**Lineage:** Coastline v0.4 (*Consensus-Emergence of Classical Proper Time*) + Methodological Note v0.3 (*The Temporal-Redundancy Functional*) + Breakwater Ledger entries CL-2026-006 v0.5, CL-2026-007 v0.3, CL-2026-008 v0.2 + the temporal-micro-consensus numerics toolkit at commit `15f444f`. Presented as a single window onto this body of work; the underlying artefacts remain the authoritative versions of every claim and result reported here.
**Status:** **Pre-release draft. §§1–5 and reference apparatus complete.** An external pilot read was sought for §1 + §2 — through an open call (2026-05-28; see the [closed-call brief](../docs/view-framework-overview-v0.1-pilot-reader-brief.md) for the audit record) and through direct invitation. Both routes closed on 2026-05-28 without a qualifying (human, foundations-metrology, outside the Freiburg–NIST orbit) reader. Per Guardian determination (logged 2026-05-28), the artefact-category specification's first-instance pilot-reader requirement is reclassified from *mandatory pre-release, no omission* to *best-effort pre-release with disclosed limitation*: the audience the gate assumed does not yet exist (the View is what creates it). The omission is documented here rather than held silent. A Q12 self-audit (logged 2026-05-28) substitutes for the missing pilot read on §1 + §2. Reader feedback on any version remains invited and is foldable via supersession (Q9) at the next View version.
**Primary audience:** Physicists working at the interface of foundations and metrology. The §1 executive overview is intended to be followable by such a reader with no prior familiarity with this project's vocabulary; specialist terms are anchored briefly on first use, and a short glossary appears immediately below.

---

## A note on language, and a short glossary

This document avoids project-internal shorthand where possible. Terms such as *Coastline*, *Methodological Note*, *Breakwater Ledger*, and *Sail* are used only where they identify a specific project artefact; the scientific claim itself is stated in ordinary descriptive language first.

A short glossary follows; the full reference apparatus (commented bibliography, Toolkit Provenance, Figure Provenance, Acknowledgements & Conflict-of-Interest, citation metadata) sits at the foot of the document.

- **Harbour View** — this document's artefact category. A presentational, externally-readable, citable document that surveys a body of project work from one declared vantage point; presents adapted content from the underlying notes but is not authoritative over them.
- **Coastline** — a versioned, falsifiable framework proposal under Local Stewardship. The present View is anchored to *Coastline v0.4 — Consensus-Emergence of Classical Proper Time.*
- **Breakwater Ledger** — the project's claim-status classifications: each Ledger entry classifies a specific external proposal (an experimental paper, a theoretical model) as *compatible*, *underdetermined*, or *inconsistent* with the Coastline at a declared version.
- **Methodological Note (MN)** — an instrument-and-measure document defining a specific operational tool used by the framework. The present View is anchored to *MN v0.3 — The Temporal-Redundancy Functional.*
- **Sail** — a commentary or essay document; the project's explanatory-register channel, distinct from the framework artefacts above. Sails are out of scope for the present View.

---

## §1 — Executive overview

**The question.** *Is classical proper time emergent from many microscopic quantum degrees of freedom, and if so, what would it take to demonstrate that it is?* This document reports the current state of a framework that takes the question seriously, and the methodological and numerical work done so far to operationalise it.

**The headline — the transplant.** The framework borrows one structure from **quantum Darwinism** (Zurek 2003, 2009) — the idea that classical behaviour appears when many independent fragments of an environment each carry a redundant record of the same information — and applies it to proper time. The bipartite correlation between a "clock" subsystem and the rest of the world that the **Page–Wootters mechanism** (Page & Wootters 1983) describes is treated as one special case embedded in this wider multipartite-redundancy picture, not as the picture itself.

**The headline — the regime caveat.** That structural transfer has been *made more precise, but not solved*. The framework's principal open problem (discussed in §2) is whether redundant *temporal* records can be exhibited rather than merely assumed: a candidate numerical exemplar exists (Methodological Note v0.3 §8; Breakwater Ledger entry CL-2026-006 v0.5), but only within an assumed regime in which the temporal pointer is taken as *einselected* — already environment-selected, in the Zurek sense. Whether such a temporal pointer can be *derived* rather than assumed is not addressed here. The framework remains a falsifiable proposal; this document presents what is currently known and where the open boundaries are.

**What this document is.** A *Harbour View* is this project's name for an externally-readable, citable presentation of a body of work — a vantage point onto the framework's current state, derived from but not authoritative over the underlying notes. The authoritative versions of every claim, anti-claim, and result live in the cited Coastline, Breakwater Ledger entries, and Methodological Note (see glossary above). No claim, definition, or anti-claim is introduced in this document that is not already on record in those underlying notes; **the View summarises those records, it does not replace them**.

**A vantage point, sketched.**

![Schematic 1 — many microscopic carriers coupling to a single shared effective proper-time variable; the Page–Wootters bipartite case (one carrier + the proper-time variable) as the highlighted nested slice, marked by a thicker arrow, a dashed enclosure, and an explicit "(bipartite)" label.](figures/schematic-01-framework-orientation.svg)

*Figure 1. The framework, in one schematic. Many microscopic carriers `F_1, F_2, …, F_N` each couple to a single shared effective proper-time variable `τ`. The Page–Wootters case — the bipartite configuration of one carrier (`F_1` in the highlighted slice) plus the proper-time variable `τ` — is drawn highlighted and nested inside the wider many-carrier picture, visually marked by a thicker arrow, a dashed enclosure around the slice, and an explicit "Page–Wootters slice (bipartite)" label. (The label avoids the numeral `N = 2` because `N` is the carrier count throughout the figure; *bipartite* refers to the two-party configuration carrier + `τ`, not to two carriers.) The reading: proper time as a robust collective variable across many carriers, not as a private property of any one of them. The figure carries no operating-point claim — that comes in §3 and §4.*

---

## §2 — Framework

This section presents the framework's current public statement — Coastline v0.4, *Consensus-Emergence of Classical Proper Time* — at the level needed to read the rest of this document. It does not replace the Coastline note: every claim below is restated from there with a section pointer, and every limit and anti-claim is preserved verbatim or by cross-reference. A *Coastline* is the project's term for a versioned, falsifiable framework proposal under Local Stewardship; the present one was first issued at v0.1 in May 2026 and is, at the time of this View, at v0.4.

### What the framework claims

The framework states one specific thesis about classical proper time, decomposed into five published claims (Coastline v0.4, *Novel Boundaries* §§I–V):

- **Claim I — Problem statement.** A classical proper-time variable is *not* assumed to be microscopically sharp. It is treated as an emergent effective variable: a parameter that need not be well-defined at the level of individual quantum degrees of freedom and that acquires operational meaning only at the level of coarse-grained collective records (Coastline v0.4 §I).
- **Claim II — Emergence criterion.** The conditions under which many independent microscopic carriers *jointly* support a single effective proper-time variable are taken to be the temporal analogue of the three Zurek criteria for quantum Darwinism — *redundancy*, *stability*, *compressibility* (Zurek 2003, 2009; Ollivier, Poulin & Zurek 2004, 2005) — applied to the temporal degree of freedom. The framework is explicit that this is a *structural transplant by analogy*, not a derivation: exhibiting a system that satisfies the temporal version of those criteria is the framework's principal open problem (Anti-Claim #6 below; Coastline v0.4 §II, *Status of specialisation*).
- **Claim III — Failure mode.** If the consensus is lost — if independent carriers cease to agree, by the operational measures of Claim IV — then a single classical proper-time variable is no longer well-defined for the system. Falsifiability here depends on a decisive test: distinguishing a genuine loss of temporal consensus from ordinary measurement noise (Coastline v0.4 §III).
- **Claim IV — Operational anchors.** Three measures are registered for evaluating the Claim II criteria: a mutual-information measure `I(C : M)` between a clock register `C` and a macrofragment `M` of the carrier set; a Fisher-information measure `F[τ]` for resolving `τ` against the carriers; and a redundancy measure `R_δ`, the number of disjoint carrier-fragments that each independently carry the temporal record to within a deficit `δ` (Coastline v0.4 §IV).

  Two distinct roles for these measures are also recognised, and the framework explicitly defers a full *measure-registration protocol* — a complete account of which measure plays which role — to a later Coastline version. The distinction is between **resolution anchors** and **classification anchors**. In clock language: a resolution anchor asks how well the carrier set can distinguish nearby values of `τ` at all; a classification anchor asks whether the temporal record is *distributed redundantly*, so that several disjoint carrier-fragments each support the same effective `τ` rather than only the full many-body state doing so (Coastline v0.4 §IV; cross-reference: design note logged in the project's roadmap, 2026-05-26).
- **Claim V — Positioning.** The framework is *not* a new theory of time. The Page–Wootters mechanism (Page & Wootters 1983; modern developments by Mendes & Soares-Pinto 2019 and Smith & Ahmadi 2020) is the canonical proposal for time emerging from quantum correlations between a "clock" subsystem and "the rest" of a closed quantum system; this framework treats the Page–Wootters bipartite case as one channel of temporal information within a wider multipartite-redundancy picture, not as the picture itself. Quantum Darwinism is the canonical proposal for the emergence of classical *configurational* objectivity through redundant proliferation of information into many environmental fragments; this framework specialises that architecture to the *temporal* degree of freedom (Coastline v0.4 §V).

### The seven anti-claims

The Coastline explicitly does *not* claim the following (Coastline v0.4, *Anti-Claims* §§1–7):

1. That "consensus" is a fundamental theory of time emergence. It is a productive interpretive framework subject to operationalisation through the Claim IV measures.
2. That microscopic carriers literally "decide" or exhibit agent-like behaviour. *Consensus*, *agreement*, and *support* are placeholders for the Claim IV operational measures; the term *decision* is stipulatively excluded from the framework's body and is reserved for the explanatory register used in the project's commentary documents (its *Sails*).
3. That the Page–Wootters mechanism or quantum Darwinism are deficient. Both are assumed as background, and the framework specialises their conjunction; it does not seek to correct either.
4. Parity with the established frameworks of the Coastline's *External Constraints* section — quantum mechanics, special relativity, the Page–Wootters mechanism, quantum Darwinism, and general relativity in its weak-field regime. The framework is a proposal for interpretation and design, not a derivation of physical law. (The Coastline's Endorsement-Marker paragraph separately names quantum information theory as constraint-only background; the View uses QIT techniques operationally in §3 and §4 under that same no-parity discipline.)
5. A bridge to any other framework. The framework's sibling-by-name *Causal Clock Unification Framework* (CCUF) is registered as a deferred item; no bridge is committed at v0.4.
6. **That the quantum-Darwinism emergence criteria have been *established* for temporal records.** Claim II transplants criteria proven for *configurational* records onto *temporal* ones by structural analogy. Exhibiting a system that instantiates *redundant temporal* records — as opposed to merely multipartite or entanglement-enhanced ones — is the framework's principal open problem. This anti-claim is the one around which this Harbour View is organised: the methodology presented in §3 and the worked exemplar in §4 are the framework's first quantitative steps toward this open problem, and §§3–4 themselves state explicitly that those steps do *not* discharge it — they operate within an assumed-einselection regime, and Anti-Claim #6 remains open beyond that regime.
7. That the framework applies in **strong-field, non-perturbative, or quantum-gravitational** regimes, or in settings without a well-defined inter-worldline comparison protocol. The framework's scope is the special-relativistic and weak-field (post-Newtonian) regime; extension beyond that requires additional structure not committed at v0.4.

### Multipartite is not redundant

A small terminological point carries forward into §3 and §4 and is worth surfacing here. *Multipartite* states — states with many sub-systems — are *not* the same as *redundant* states. A maximally entangled state of `N` parts is in fact *anti-redundant*: no proper subset of the parts carries on its own the information that the whole carries. Distributed-clock and entanglement-enhanced metrology protocols realise multipartite temporal structures but are typically anti-redundant in precisely this sense; the framework's redundant-consensus condition is a strictly stronger requirement than multipartiteness, and methods that satisfy multipartiteness alone do not satisfy it (Coastline v0.4 §II *Many vs redundant*; §V *Positioning vs distributed-clock metrology*).

### Regime of validity: SR and weak-field GR only

The framework operates within special relativity for the flat-spacetime baseline and within general relativity in its **weak-field (post-Newtonian) regime** for worldlines that may be accelerated or located at differing gravitational potential. Spacetime curvature enters perturbatively, as the leading-order contribution to a *cross-probe residual* that no single proper-time variable reproduces — i.e., as a Claim II.3 incompressible residual and a Claim IV cross-probe-mismatch quantity (Coastline v0.4, *External Constraints* item 5; *Regime of Validity*; *Anti-Claims* §7). Strong-field, non-perturbative, and quantum-gravitational regimes are explicitly out of scope, as are settings in which no shared inter-worldline comparison protocol exists. The framework's relationship to general relativity in this regime is one of *respect, not parity*: GR is used as a constraint on the framework, not derived, extended, or modified by it (per Anti-Claim §4 above). Two specific Breakwater Ledger entries — the project's claim-status classifications against the framework — record the framework's first contact with concrete experimental and theoretical proposals at the regime boundary: CL-2026-007 v0.3 (a bipartite quantum-time-dilation proposal) and CL-2026-008 v0.2 (a class of distributed clock-network proposals). Both are classified *underdetermined* with respect to the framework as currently written and are discussed in §5.

### A vantage point on multipartite ≠ redundant

![Schematic 2 — side-by-side contrast of an anti-redundant entanglement-enhanced state (fragments shown with dashed borders and an explicit ✗ R "no record" marker — no proper fragment carries R) versus a redundant consensus state (fragments shown with solid borders and an explicit ✓ R "carries record" marker — many fragments each carry R). Contrast encoded by colour, shape/line-style, and explicit marker so the figure remains legible under colourblindness and in greyscale.](figures/schematic-02-comparison-geometry.svg)

*Figure 2. The framework's structural distinction between multipartite and redundant temporal records. On the left, an entanglement-enhanced state `Ψ_total` whose proper fragments (drawn with dashed borders and an explicit "✗ R" marker) do not individually carry the temporal record `R` — multipartite but anti-redundant. On the right, a redundant consensus state in which many fragments (drawn with solid borders and an explicit "✓ R" marker) each carry `R` — the condition Claim II asks for. The contrast is *structural* — which fragments carry the record — never parametric; it is encoded by colour, shape/line-style, and explicit marker, so the figure remains legible without colour.*

This concludes §2. §3 (methodology) operationalises the Claim II emergence criterion through a specific functional defined on multi-carrier states, and §4 (worked exemplar) is the framework's **first candidate** numerical instance of a redundant *temporal* record **within the assumed-einselection regime** that Anti-Claim #6 names as the open problem — not a resolution of Anti-Claim #6, which remains open beyond that regime. Both follow once §1 and §2 have been read.

---

## §3 — Methodology

This section presents the framework's first methodological instrument — *Methodological Note v0.3* (*MN v0.3*), *The Temporal-Redundancy Functional* — at the level needed to read §4. As with §2, every statement below is restated from MN v0.3 with a section pointer; no new definitions, no new claims. A *Methodological Note* is the project's term for a versioned instrument-and-measure document that operationalises a Coastline claim; the present one operationalises Claim II's redundancy condition by re-basing the configurational quantum-Darwinism redundancy count `R_δ` of Riedel & Zurek (2010) and Tank (2025) onto a temporal pointer.

### What the functional is, what it measures

The *temporal-redundancy functional* `R_δ(N, ε)` counts the effective number of disjoint carrier-fragments that each independently fix an elapsed-time bin to within a deficit `δ`, when there are `N` carriers and each carrier has a **per-carrier flip/error probability** `ε` derived from its distinguishability against a reference reading of the temporal pointer (`ε ∈ [0, 1/2]`; `ε = 0` means perfect distinguishability, `ε = 1/2` means none; MN v0.3 §1). It is the temporal analogue of the configurational redundancy count Zurek (2009) introduced and Riedel & Zurek (2010) computed for environmental records of a spatial pointer.

In the Claim IV vocabulary of §2: **`R_δ` is a classification anchor.** It plateau-collapses under per-carrier nuisance (the plateau retreats and may disappear entirely; MN v0.3 §2, §5) and **co-classifies with `I(C : M)`** at the registered analytic poles and in the toolkit's cross-anchor invariant tests (MN v0.3 §3; toolkit work plan v0.1 §5). It is not asserted that `R_δ` and `I(C : M)` co-move under arbitrary channels — Module 3a's per-channel signs are explicitly non-uniform (§4.1) — only that the two classification anchors agree on the *registered* poles and the *registered* invariants. The framework's resolution anchor `F[τ]` for the same carrier set scales as `F_τ(m) = m · F_1` (extensive in the fragment size `m`; MN v0.3 §4) and *anti-correlates* with `R_δ` — `F[τ]` rises toward the anti-redundant pole exactly where `R_δ` falls. Reading `F[τ]` as a classifier is the named CL-2026-007 v0.1 failure mode the framework explicitly guards against (MN v0.3 §4).

### The single-carrier dynamical bridge

The per-carrier flip/error probability `ε` is **derived dynamically** from the single-carrier distinguishability, not posited (MN v0.3 §8.1). Evolving a single carrier prepared in `|+⟩` under the pure-dephasing master equation `(γ_φ/2) D[σ_z]` gives the carrier's residual `T`-pointer coherence `c = e^{−γ_φ t}` (the carrier's distinguishability between the two `T`-conditioned states), and the corresponding flip/error probability

  `ε(γ_φ, t) = (1 − c) / 2 = (1 − e^{−γ_φ t}) / 2`.

Four standard quantum-information calculations on the binary-pointer read-out — the trace distance between the two `T`-conditioned states, the Helstrom optimal-decision error, the optimal projective bit-decision error, and the Holevo information — all yield the same effective flip/error parameter `ε(γ_φ, t)`: the first three equal `ε` directly, and the Holevo information is the strictly-monotonic `χ = 1 − h₂(ε)` (a function of `ε`, not `ε` itself). MN v0.3 §8.1 names this the *four-way coincidence*. The agreement means that `ε(γ_φ, t)` is not a measure-choice artefact: it is the per-carrier read-out error for a single bit of `T`, derived from the dephasing dynamics with no infidelity knob.

### Where the functional is defined, and where it is not

MN v0.3 §2 gives two analytic poles of `R_δ`. The *product pole* (independent carriers in a product state) realises the redundant case: many small fragments each fix the bin. The *cat / anti-redundant pole* (a GHZ-shadow `(|0…0⟩ + (−1)^T |1…1⟩) / √2`) realises the opposite: no proper fragment carries `T` at all, so the redundancy collapses to the entire set (`R_δ = 1`). Between the two, `R_δ(N, ε)` may be **undefined** rather than merely small — a stronger failure in which even the full carrier set never reaches the redundancy threshold `(1 − δ) H_T`, distinguished from `R_δ = 1` in MN v0.3 §2.

The dynamical `ε` bridge above lets `R_δ(N, γ_φ t)` be computed numerically; the MN v0.3 §2 poles are recovered as analytic limits. A specific cross-link from MN v0.3 §8.3 anchors the numerical computation to the §2 analytics: at `γ_φ t = ln(5/3)` (so `ε = 0.20`) and `N = 64`, the numerical `R_{0.10}` matches `64/9` exactly to numerical tolerance — the dynamical path lands on the §2 analytic pole.

### Multipartite is not redundant — the dynamical version of the §2 distinction

The §2 *multipartite ≠ redundant* distinction has two faces in the dynamical picture, and the two should not be conflated.

*(i) At the anti-redundant pole, the redundancy count is `R_δ = 1` already statically.* For the GHZ-shadow state `(|0…0⟩ + (−1)^T |1…1⟩) / √2`, the Schmidt structure (MN v0.3 §2 and Appendix B) makes the reduced state of any proper fragment *T*-independent — no proper fragment carries the temporal record on its own. The redundancy is therefore `R_δ = 1` (only the entire set fixes the bin), *not* zero; the "no proper fragment" condition is what makes this pole the *anti-redundant* pole. No open-system process is invoked; the structure is anti-redundant by construction (MN v0.3 §2, Appendix B).

*(ii) Dynamically, with independent product carriers under dephasing, the plateau collapses as `ε` approaches `1/2`.* Independent-product carriers maintain a redundant plateau at small `γ_φ t` and lose it as the per-carrier flip/error probability grows. The redundancy plateau retreats with growing `γ_φ t` and eventually becomes undefined (the boundary curve `γ_φ t_crit(N)` of Figure 3 and Figure 4; MN v0.3 §8.4); this is a distinct phenomenon from the static `R_δ = 1` of the anti-redundant pole. Together, the two faces certify that a `R_δ` plateau, when it exists, is structurally significant: it certifies *redundant* multipartite encoding rather than merely multipartite encoding.

### Match to the configurational computation

A recent preprint (Tank 2025, arXiv:2509.17775) computes a *configurational* pure-dephasing redundancy `R_δ` with the expected early-growth and plateau structure, under the operational definition `FI(δ) = log₂ R_δ`. MN v0.3 §8.5 reports that this temporal-side `R_δ` matches the Tank configurational `R_δ` in structure — the configurational/temporal pair is now computed on *both* sides, closing at the level of the *computation* the asymmetry that remained at MN v0.2 (configurational computed, temporal analytic only). One asymmetry is **not** closed: the temporal side carries an einselection assumption the configurational side does not need (see the verbatim caveat below).

### Sweet and anti-sweet operating points

The redundancy plateau is well-defined only in a restricted region of the `(N, γ_φ t)` plane. Figure 3 below shows the dynamical `R_δ` at three representative carrier counts; the *sweet* region is where the plateau exists and the carriers redundantly fix the temporal bin; the *anti-sweet* region is where dephasing has driven the per-carrier flip/error probability `ε` close enough to `1/2` that no redundancy plateau is supported, and `R_δ` becomes undefined (no `m_δ` exists). The boundary `γ_φ t_crit(N)` *rises* with `N` (MN v0.3 §8.2): more independent carriers tolerate more per-carrier nuisance before the plateau disappears.

![Figure 3 — R_δ vs γ_φt at N ∈ {4, 32, 128}: sweet region (small γ_φt, all three N's redundant) shaded green; anti-sweet region (γ_φt past the largest-N boundary; all three N's undefined) shaded red; per-N undefined-boundary verticals dashed in the trace colour.](figures/figure-03-redundancy-functional-snr.svg)

*Figure 3. Type-(b) signal-to-noise display: dynamical `R_δ` against the per-carrier dephasing time `γ_φ t`, at three representative carrier counts `N ∈ {4, 32, 128}`. The sweet region (where all three N's keep `R_δ` well-defined) is shaded green; the anti-sweet region (where no N supports a redundancy plateau and `R_δ` becomes undefined) is shaded red. Dashed verticals mark each N's first-undefined `γ_φ t`; the boundary rises with `N` (`0.273 → 1.136 → 1.827` at `N = 4, 32, 128` respectively; the operating points are read from the committed sweep `numerics/results/open_instrument_redundancy_v0.1.json`, regenerated by `numerics/examples/open_instrument_module.ipynb` at the figure-citing commit `15f444f`). The figure carries no parity claim against experiment; it displays the regions in which the methodology defines a usable measurement, and the regions in which it does not.*

### What §3 does not settle — the einselection caveat (verbatim from MN v0.3 §8.6)

The numerical `R_δ` curves above presuppose that the temporal pointer `T` is *einselected* — i.e. that some environmental decoherence process has already selected the pointer basis in which `R_δ` is computed. MN v0.3 §8.6 preserves this assumption verbatim; the View carries the same block:

> Module 3b computes `R_δ(N, γ_φ, t)` *conditional on the assumption that the temporal pointer `T` is einselected* (MN v0.2 §1.1). The existence of a dynamically-derived temporal-pointer basis — the temporal analogue of environment-induced superselection — is the hardest part of the Coastline's principal open problem (**Anti-Claim #6**) and is **not** addressed: it is *assumed*, not derived. Module 3b is therefore a **candidate** worked exemplar of a *redundant temporal record* **within the assumed regime**, not a resolution of Anti-Claim #6, which **remains open**. Whether any such instance counts as *the* worked exemplar that converts Coastline Claim II from analogy to demonstration is a Coastline-level judgement reserved to the steward (Lock-Key).

This caveat is the methodological boundary `§3` operates within. §4 reports on what the framework's first numerical instrument has produced *inside* this boundary; the boundary itself is not crossed.

---

## §4 — Worked exemplar

This section reports what the framework's first numerical instrument has produced. It draws on two committed toolkit modules — *Module 3a* (the Sorci nuisance-budget computation) and *Module 3b* (the open temporal instrument introduced in §3) — at the figure-citing commit `15f444f`. The Ledger anchor is **CL-2026-006 v0.5** (*Sorci et al. — Quantum Signatures of Proper Time in Optical Ion Clocks*); every relationship statement against the experimental proposal is anchored there, and the §2 *respect, not parity* posture extends to §4 as *consistent-with the Ledger classification, not consistent-with the published paper as physics*.

The Ledger entry CL-2026-006 v0.5 classifies the Sorci proposal as **UNDERDETERMINED** with respect to Coastline v0.4. **§4 reports on a verdict that is, and stays, unchanged.** Module 3a supplies quantitative grounding for the entry's Discriminant Condition D1; the grounding *sharpens* what D1 demands without *discharging* D1. Discriminant Conditions D2 and D3 are experimental and remain unmet. The Lock-Key discipline forbids the numerics from auto-updating the verdict; the human-deliberated classification is the load-bearing object, and the toolkit is its quantitative substrate (toolkit Anti-Claim A5; CL-2026-006 v0.5).

### §4.1 — Module 3a: the Sorci D1 nuisance budget

The Sorci protocol uses a two-carrier squeezed-state Ramsey interferometer in a single trapped ion to witness a coherence-dependent proper-time correction in the clock observable's visibility. Ledger discriminant D1 asks for a *nuisance-channel decomposition* of the visibility loss: which fraction is the proper-time signal, which fraction is each mundane channel (heating, dephasing, preparation infidelity, detection infidelity). Module 3a produces the decomposition under a four-layer nuisance model (initial-state preparation infidelity / dynamical-Lindblad heating + motional dephasing / stochastic-Hamiltonian drive-phase noise / detection-side correlated infidelity), in the rotating-frame secular-dispersive model that reproduces Sorci Eq. (12) (derived coupling `g_md = −ε_m ω_c / 4` validated to the published coefficient; ²⁷Al⁺ extrapolation `V ≈ 0.943`, matching the published `V ≃ 0.93`).

The result lives in `numerics/results/sorci_nuisance_budget_v0.1.json` (committed; regenerated end-to-end by `numerics/examples/sorci_module.ipynb` at commit `15f444f`). CL-2026-006 v0.5 reports three model-conditional findings the View carries verbatim by reference:

1. **Per-channel signs are channel- and regime-specific, not uniform.** Heating and motional dephasing *reduce* `I(C : M)` (the mutual information between the clock register and the carrier macrofragment) by approximately `0.021` and `0.034` bits at the scaled operating point — as generic decoherence channels do. The modelled squeezing-preparation infidelity, on the other hand, *raises* `I(C : M)` by approximately `0.16` bits and dominates the budget. The naïve intuition *"any nuisance lowers the shared-structure measure"* is therefore false. The discriminant cannot rest on the sign or magnitude of a single channel's `I(C : M)` contribution; it can rest only on the channel's controlled scaling — exactly what Discriminant Conditions D2 and D3 demand experimentally (CL-2026-006 v0.5, *Quantitative grounding* item 1).
2. **The detection layer is latent-invariant.** Detection-side correlated infidelity leaves `I(C : M)` and the latent clock coherence *exactly unchanged* (`ΔI = ΔV_state = 0`); it degrades only the observed visibility (`Δ(1 − V_obs) ≈ 0.10` at `ε_det = 0.05`). The detection contribution is therefore an *observed-readout* effect, structurally distinct from the dynamical channels. Any experimental implementation of D1 must respect this distinction; the budget makes it explicit (CL-2026-006 v0.5, item 2).
3. **The decomposition is model-conditional** (toolkit Anti-Claim A4), and the budget exposes two sensitivities an experimental D1 must pin down: (i) motional dephasing is *visibility-invisible in the secular dispersive model* — `D[n̂]` leaves the Fock populations, hence the dispersive clock coherence `V_state`, unchanged — *yet it still lowers quantum `I(C : M)`* by destroying motional-Fock coherences (`ΔI ≈ −0.034`), and it would additionally shift `V_state` in the full `σ_z P̂²` model; (ii) the v0.1 symmetric-depolarising preparation-infidelity model is *aggressive for a high-cutoff bosonic mode* (it spreads population across all Fock levels), which is why it dominates the budget. A physically faithful squeezing-preparation model (`r`-jitter / thermal admixture) is a registered toolkit-v0.2 refinement (CL-2026-006 v0.5, item 3; *Quantitative grounding* closing paragraph). The interaction residual (`ΔI ≈ −0.021`) further confirms the channels are *non-additive* at finite nuisance.

In the Claim IV vocabulary of §2 and §3: the budget measures **`I(C : M)`** (a classification anchor) and the **observed visibility** under controlled nuisance. The redundancy measure `R_δ` is *not* an additional budget object — at `N = 2` it functions only as a directional cross-anchor consistency check, with values restricted to `{undefined, 1, 2}` (one structural transition, not a continuous curve; MN v0.3 §3). The framework's **resolution anchor** `F[τ]` is likewise *not* the object the budget classifies; the budget studies how `I(C : M)` and the observed visibility degrade under declared channels, not how finely `τ` can be resolved.

**Bearing on the discriminant (verbatim posture from CL-2026-006 v0.5).** D1's *theoretical* component — *"an explicit nuisance-channel decomposition of the `I(C : M)` loss"* — is now produced and reproducible. But the budget shows that the per-channel attribution is model-conditional, so the toolkit *sharpens* D1 into a demand on controlled scaling and explicit channel models, rather than supplying a model-free attribution. D2 (a null test against the zero-coherence baseline) and D3 (a measured `r`-scan distinguishable from squeezing-preparation-infidelity scaling) remain experimental and unmet. **The classification therefore stays UNDERDETERMINED.** D1 is grounded; D1–D3 are sharpened; none is discharged.

**Note on infrastructure (the v0.5 CBG correction).** An earlier Ledger version stated that the *Colla–Breuer–Gasbarri* (CBG) open-quantum-systems pipeline produced "precisely the nuisance-channel decomposition required by D1". CL-2026-006 v0.5 corrects this: CBG computes the coherent minimal-dissipation effective Hamiltonian `K(t)` in the non-Markovian regime, **not** the Markovian-Lindblad mutual-information nuisance budget that D1 requires. The D1 decomposition is produced by *Module 3a* (this project's toolkit); CBG is retained only as an optional non-Markovian validation backend (HEOM and pseudomode cross-checks) and as a methodological template (its benchmark-card and validity-envelope discipline). The View carries that correction by reference (CL-2026-006 v0.5, *Relation to other Ledger entries*; toolkit work plan v0.1 §8 Q5).

### §4.2 — Module 3b: the open temporal instrument

Module 3b applies the methodology of §3 numerically. It computes the dynamical `R_δ(N, γ_φ t)` grid for `N ∈ {4, 8, 16, 32, 64, 128}` and `γ_φ t ∈ [0.1, 2.0]` (12 points), with deficit `δ = 0.10`, derives the per-carrier flip/error probability `ε(γ_φ, t)` from the single-carrier master equation, and reports the *first-undefined* `γ_φ t_crit(N)` for each carrier count.

The result lives in `numerics/results/open_instrument_redundancy_v0.1.json` (committed; regenerated end-to-end by `numerics/examples/open_instrument_module.ipynb` at commit `15f444f`). The boundary `γ_φ t_crit(N)` *rises* with `N`: `0.273` at `N = 4`, rising monotonically to `1.827` at `N = 128`. More independent carriers tolerate more per-carrier dephasing before the redundancy plateau disappears — the dynamical realisation of the *redundancy-supports-many-carriers* point Claim II makes structurally.

The §3 D5 cross-link is satisfied: at `γ_φ t = ln(5/3)` and `N = 64`, the numerical `R_{0.10}` agrees with the §2 analytic value `64/9` to numerical tolerance (`|ΔR| < 10⁻⁹`). The dynamical path lands on the analytic pole.

**Einselection caveat carried.** The verbatim block from MN v0.3 §8.6 transcribed in §3 applies in full to Module 3b. The numerical curves are computed *within an assumed-einselection regime*; the existence of a dynamically-derived temporal-pointer basis is not addressed and Anti-Claim #6 remains open. Module 3b is a candidate exemplar of a redundant temporal record within that regime, not a resolution.

![Figure 4 — R_δ(N, γ_φt) landscape (heatmap, log-scaled colour) with the rising undefined-boundary curve overlaid (dark red, with markers) and the anti-sweet region (above the curve, R_δ undefined) explicitly demarcated. Dotted horizontal cross-link lines at N ∈ {4, 32, 128} mark the §3 type-(b) slices.](figures/figure-04-redundancy-landscape.svg)

*Figure 4. Type-(c) parameter-space landscape: `R_δ(N, γ_φ t)` over the committed sweep grid (same grid as `open_instrument_redundancy_v0.1.json`). The colour map encodes `R_δ` on a log scale where the plateau is well-defined. The dark-red curve marks the undefined-boundary `γ_φ t_crit(N)`, rising monotonically with `N`; the anti-sweet region above the curve — where the functional is still evaluated but the redundancy threshold `(1 − δ) H_T` is never reached, so no finite `m_δ` exists and `R_δ` is returned as *undefined* on that grid — is shaded explicitly per the artefact-category specification's figure-honesty rule (no figure displaying operating points may show only the favourable region). The three thin dotted horizontal cross-links at `N = 4, 32, 128` correspond to the §3 type-(b) slices, locating Figure 3's three traces within the full landscape.*

**Live interactive notebook (Q10d).** A live link to the generating notebook is provided as a convenience layer:

> [Open `open_instrument_module.ipynb` in Google Colab at commit `15f444f`](https://colab.research.google.com/github/uwarring82/temporal-micro-consensus/blob/15f444f/numerics/examples/open_instrument_module.ipynb)

Per the artefact-category specification: the static SVG figures are the citable artefacts; the live notebook is a convenience layer for visitor exploration, bounded to model-valid parameter regimes (the einselection caveat surfaces verbatim in the notebook's first cell, before any code executes). If the live link is unavailable, the notebook at commit `15f444f` reproduces all figures.

### §4.3 — Module-conditionality summary

Both modules are *model-conditional* under the toolkit anti-claims A1–A5 (this project's *toolkit work plan v0.1* §9): the master-equation channels declared in the budget are the channels the budget bounds, no others; analytic-pole regression is a consistency check on the implementation, not a derivation of the analytic poles themselves; redundant-pole numerical results are exemplars within an assumed-einselection regime; nuisance-channel attribution holds under the declared channel set, not absolutely; and human-deliberated framework revision — not the numerics — moves Ledger verdicts. The Acknowledgements & Conflict-of-Interest block immediately below this drafted region declares the steward's prior NIST-Boulder association with D. Leibfried (a Sorci co-author) explicitly, per the project's Q11c separation discipline (Leibfried acknowledged; Sanner explicitly not, per the 2026-05-26 logbook correction).

---

## §5 — Open problems, neighbouring work, invitations to engage

This closing section names what is open and what is invited. Every open problem cites the underlying note that records it; no new claims, no new anti-claims.

### §5.1 — Open problems (anchored to the underlying notes)

- **The principal open problem (Coastline v0.4 Anti-Claim #6, MN v0.3 §8.6, CL-2026-006 v0.5).** Whether redundant *temporal* records can be exhibited rather than merely assumed: a continuous-`τ`, dynamically-einselected, many-carrier exemplar — beyond the candidate produced by Module 3b within the assumed-einselection regime — remains the framework's principal open problem. §3 and §4 supply the first quantitative steps; they do not discharge the open problem and §3 + §4 are explicit on that point.
- **The Claim IV measure-registration protocol (Coastline v0.4 §IV, deferred).** A full account of which Claim IV measure plays which role across the registered cases — *resolution anchor* vs *classification anchor* — is explicitly deferred to a later Coastline version. The §2 / §3 / §4 split (`F[τ]` as resolution anchor, additive in `N`, anti-correlated with `R_δ`; `I(C : M)` and `R_δ` as classification anchors that *co-classify* at the registered analytic poles and in the cross-anchor invariant tests, with `R_δ` additionally exhibiting plateau-collapse under per-carrier nuisance; broader claims of generic co-movement or shared plateau-collapse under arbitrary channels are not asserted) is the operating discipline in this View; the protocol that would render it self-contained for all measures and all registered cases is still pending. The drafter's *resolution-anchor-vs-classification-anchor* design note (project roadmap, 2026-05-26) records the design path; the Coastline-level commitment awaits accumulated practice.
- **D2 and D3 of the Sorci dossier (CL-2026-006 v0.5 Discriminant Conditions).** D1's theoretical decomposition is grounded by Module 3a (§4.1); D2 (the structural null test against zero-coherence baselines) and D3 (a measured `r`-scan distinguished from squeezing-preparation-infidelity scaling) remain experimental and unmet. The framework's verdict on the Sorci proposal stays *underdetermined* until D2 and D3 are satisfied jointly with the Module-3a-grounded D1.
- **Toolkit refinement registered (CL-2026-006 v0.5 *Quantitative grounding* + toolkit work plan v0.1 §10 rev. (d)).** A physically faithful squeezing-preparation-infidelity model — `r`-jitter or thermal admixture — is registered as a *tmc-numerics* v0.2 refinement to replace the v0.1 symmetric-depolarising model that dominates the current Module-3a budget. A toolchain-hygiene item (single-environment reproducibility setup; pinned `requirements.txt`; editable install) is also registered at v0.1 rev. (d).
- **Strong-field / non-perturbative / quantum-gravitational extension (Coastline v0.4 Anti-Claim #7, *Deferred Items*).** The framework's scope is special-relativistic and weak-field (post-Newtonian) only. Extension to strong-field, non-perturbative, or quantum-gravitational regimes — and to settings where no inter-worldline comparison protocol is defined — requires additional structure not committed at Coastline v0.4. This is deferred, not declined.

### §5.2 — Neighbouring Ledger entries (the framework operationalised against external work)

Two further Breakwater Ledger entries record the framework's contact with concrete external proposals at the regime boundary. Both are classified *underdetermined*; each names a Discriminant Condition that would resolve the classification.

- **CL-2026-007 v0.3 (Smith & Ahmadi 2020 — *Quantum clocks observe classical and quantum time dilation*).** The Smith–Ahmadi proposal makes the superposition-vs-mixture distinction theoretically at the level of the time-dilation correction (`γ_Q⁻¹` vs `γ_C⁻¹`, with `γ_Q⁻¹` vanishing for a classical mixture). The framework-relative gap is *experimental-witness-level*: isolating `γ_Q⁻¹` from preparation, COM-dephasing, clock-readout, and finite-coherence-window nuisances at the witness scale. The Ledger entry's D2 names the structural null test (toggling `θ` to suppress `γ_Q⁻¹` while leaving the classical contribution comparatively unchanged) that would discharge the underdetermination. CL-2026-007 v0.3 is the authoritative version.
- **CL-2026-008 v0.2 (Covey et al. 2025 + Fromonteil et al. 2025 — distributed entanglement-enhanced clock networks).** The class claim covers entanglement-enhanced distributed clock proposals that probe curved spacetime through cross-probe mismatch (Covey's `Δω`, Fromonteil's gravitational-decoherence visibility `τ_dec`). The framework-side Discriminant Condition D1 (a GR-regime boundary statement) was satisfied by Coastline v0.4's *Regime of Validity* addition; the remaining condition for *compatible* is D2, the experimental nuisance-channel decomposition isolating the GR cross-probe signature from technical decoherence (global magnetic-field / nuclear-Zeeman noise; collective dephasing). CL-2026-008 v0.2 is the authoritative version.

Both entries sit at the same place as CL-2026-006: *theory-compatible, experimental-witness-underdetermined.*

### §5.3 — How to cite, reproduce, and engage

- **Citation locator** (per the artefact-category specification, regime O6). At tagged release, the citation form is `{Zenodo version DOI of the release} / views/view-framework-overview-v0.1.md`. The Zenodo version DOI is assigned at release; the file path within the release is stable.
- **Reproduction pointer.** All numerical results behind §3 and §4 are reproducible from the project repository at commit `15f444f`. Module 3a (the D1 nuisance budget) is regenerated end-to-end by [`numerics/examples/sorci_module.ipynb`](../numerics/examples/sorci_module.ipynb); Module 3b (the open temporal instrument) by [`numerics/examples/open_instrument_module.ipynb`](../numerics/examples/open_instrument_module.ipynb). The QuTiP 5.2.3 / Python 3.13 environment is recorded in `numerics/pyproject.toml`; the 85-test suite is run from `numerics/` with `pytest`. Both notebooks executed end-to-end with zero errors at the figure-citing commit (project logbook, 2026-05-28 entries).
- **Reader feedback on the View.** Feedback on this View, including on §1 + §2, is welcome by email to the steward (`u.j.warring@gmail.com`). Per the artefact-category specification's reclassified first-instance pilot-reader requirement (logged 2026-05-28), feedback received between View versions is folded via *supersession* at the next View version (Q9 discipline); the open call that ran on 2026-05-28 is closed (see the [closed-call brief](../docs/view-framework-overview-v0.1-pilot-reader-brief.md) for the audit record) but the standing post-release invitation is not.
- **Direct contact.** U. Warring, Physikalisches Institut, Albert-Ludwigs-Universität Freiburg. Email above.

### §5.4 — What is not yet supported

In keeping with the artefact-category specification's *invitation-to-engage clarity* recommendation, the View is honest about the modes of collaboration the framework does not yet operate:

- **No public issue tracker** for the framework artefacts (Coastline, Ledger, MN, Sail). The project is not yet at the scale where issue-tracker collaboration is the right discipline; the contact path above is the operating channel.
- **No pull requests against framework artefacts via the View.** The View summarises; it does not edit. Suggestions for sharpening a Coastline claim, an anti-claim, or a Ledger classification route through the next version of the underlying artefact under the steward's deliberation, not through the View. (This is the Lock-Key discipline of the View as a *window onto* the framework, not a door into it.)
- **No external-circulation discovery campaign at this version.** Deferred per the project roadmap; the present release is the first time the body of work is presented in this consolidated form, and the discovery question is the next stewardship decision.

The framework remains a falsifiable proposal under Local Stewardship. The View is a window onto its current state; the underlying notes carry the evidence.

---

## Reference apparatus

Six blocks per the artefact-category specification §6: commented bibliography (Q11a); version-pinning appendix; Toolkit Provenance (Q4); Figure Provenance (Q10f); Acknowledgements & Conflict-of-Interest (Q11c, separate from citations); citation-metadata stub. Each entry carries the fields the specification demands.

### Block 1 — Commented bibliography

Each entry carries an **anchor** (DOI for papers; canonical citation for textbooks; archived URL for software), a **role annotation** from the controlled vocabulary (*external-constraint*, *prior-art*, *method-source*, *contrast-contested*), and — for *external-constraint* entries — an explicit **constraint-only / no-parity marker** mirroring the Coastline's Anti-Claim §4 and the artefact-category specification §4 Q7.

#### A. External constraints (constraint-only; no parity claimed)

Three externally-validated physical frameworks the View operates within and does not derive, extend, or revise. The Coastline v0.4 *External Constraints* section names five items in total; the other two (Page–Wootters mechanism and quantum Darwinism) are theoretical frameworks the Coastline structurally inherits from and are catalogued as *prior-art* in Blocks B and C below. Quantum information theory appears in the Coastline's Endorsement-Marker paragraph as constraint-only background and is recorded as A4 (a *method-source* in this bibliography).

- **A1 — Quantum mechanics.** Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information* (10th Anniversary Edition). Cambridge University Press. ISBN 978-1-107-00217-3. **Role:** *external-constraint*. **Endorsement-scope marker:** constraint-only; no parity claimed. The View operates within unitary quantum mechanics as established; it does not derive, extend, or revise it. **Surfaced where:** §1 Endorsement-Marker; §2 Coastline anchoring; §3 master-equation framework.
- **A2 — Special relativity.** Misner, C. W., Thorne, K. S., & Wheeler, J. A. (1973). *Gravitation*. W. H. Freeman. ISBN 978-0-7167-0344-0. **Role:** *external-constraint*. **Endorsement-scope marker:** constraint-only; no parity claimed. The View operates within special relativity for the flat-spacetime baseline. **Surfaced where:** §2 *Regime of validity*.
- **A3 — General relativity (weak-field / post-Newtonian regime only).** Misner, Thorne & Wheeler (1973), *Gravitation* (as A2). **Role:** *external-constraint*. **Endorsement-scope marker:** constraint-only; no parity claimed. The View operates within general relativity's weak-field (post-Newtonian) regime; strong-field, non-perturbative, and quantum-gravitational regimes are out of scope (Coastline v0.4 Anti-Claim #7 + *Regime of Validity*). **Surfaced where:** §2 GR-regime sentence, three-way anchored to Coastline v0.4 *External Constraints* item 5 + *Regime of Validity* + *Anti-Claims* §7.

#### A4 — Quantum information theory (method-source)

- **A4.** Nielsen, M. A., & Chuang, I. L. (2010), *Quantum Computation and Quantum Information* (same volume as A1). **Role:** *method-source* (the §3 trace-distance / Helstrom / projective / Holevo distinguishability machinery and the `I(C : M)` mutual-information measure of §4 are QIT techniques adopted by the View). QIT is not in the Coastline's *External Constraints* section; it appears in the Endorsement-Marker paragraph as constraint-only background. The constraint-only marker therefore applies at the View's top-level Endorsement Marker, not at the bibliographic role. **Surfaced where:** §3 four-way coincidence for `ε`; §4.1 `I(C : M)` model-conditional findings.

#### B. Prior art — Page–Wootters lineage

- **B1.** Page, D. N., & Wootters, W. K. (1983). Evolution without evolution: Dynamics described by stationary observables. *Physical Review D*, 27(12), 2885–2892. DOI [10.1103/PhysRevD.27.2885](https://doi.org/10.1103/PhysRevD.27.2885). **Role:** *prior-art*. **Surfaced where:** §1 headline transplant; §2 Claim V positioning.
- **B2.** Mendes, L. R. S., & Soares-Pinto, D. O. (2019). Time as a consequence of internal coherence. *Proceedings of the Royal Society A*, 475(2231), 20190470. DOI [10.1098/rspa.2019.0470](https://doi.org/10.1098/rspa.2019.0470); preprint arXiv:1806.09669. **Role:** *prior-art* (Coastline v0.4 *External Constraints* item 3, modern Page–Wootters lineage). **Surfaced where:** §2 Claim V positioning.
- **B3.** Smith, A. R. H., & Ahmadi, M. (2020). Quantum clocks observe classical and quantum time dilation. *Nature Communications*, 11, 5360. DOI [10.1038/s41467-020-18264-4](https://doi.org/10.1038/s41467-020-18264-4); preprint arXiv:1904.12390. **Role:** *prior-art* (modern Page–Wootters lineage; subject of Breakwater Ledger entry CL-2026-007 v0.3). **Surfaced where:** §2 Claim V positioning; §5.2 cross-View pointer.

#### C. Prior art — quantum-Darwinism lineage

- **C1.** Zurek, W. H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Reviews of Modern Physics*, 75(3), 715–775. DOI [10.1103/RevModPhys.75.715](https://doi.org/10.1103/RevModPhys.75.715); preprint arXiv:quant-ph/0105127. **Role:** *prior-art* (foundational decoherence / einselection review; anchors the einselection caveat carried verbatim in §3 / §4). **Surfaced where:** §1 headline transplant; §2 Claim V positioning; §3 einselection caveat lineage.
- **C2.** Zurek, W. H. (2009). Quantum Darwinism. *Nature Physics*, 5, 181–188. DOI [10.1038/nphys1202](https://doi.org/10.1038/nphys1202); preprint arXiv:0903.5082. **Role:** *prior-art* (the architecture Coastline Claim II specialises to the temporal degree of freedom). **Surfaced where:** §1 headline transplant; §2 Claim II + Claim V.
- **C3.** Ollivier, H., Poulin, D., & Zurek, W. H. (2004). Objective Properties from Subjective Quantum States: Environment as a Witness. *Physical Review Letters*, 93, 220401. DOI [10.1103/PhysRevLett.93.220401](https://doi.org/10.1103/PhysRevLett.93.220401); preprint arXiv:quant-ph/0307229. **Role:** *prior-art* (the closest configurational precursor to the temporal specialisation Coastline v0.3 recognised). **Surfaced where:** §2 Claim II + Claim V.
- **C4.** Ollivier, H., Poulin, D., & Zurek, W. H. (2005). Environment as a Witness: Selective Proliferation of Information and Emergence of Objectivity in a Quantum Universe. *Physical Review A*, 72, 042113. DOI [10.1103/PhysRevA.72.042113](https://doi.org/10.1103/PhysRevA.72.042113); preprint arXiv:quant-ph/0408125. **Role:** *prior-art* (paired-citation companion to C3). **Surfaced where:** §2, paired with C3.

#### D. Prior art — Worked-exemplar dossier subject

- **D1.** Sorci, G., Foo, J., Leibfried, D., Sanner, C., & Pikovski, I. (2026). Quantum signatures of proper time in optical ion clocks. *Physical Review Letters*, 136, 163602. DOI [10.1103/qhj9-pc2b](https://doi.org/10.1103/qhj9-pc2b); preprint arXiv:2509.09573. **Role:** *prior-art* / candidate-witness (subject of Breakwater Ledger entry CL-2026-006 v0.5, the worked exemplar drawn on in §1 + §4). **Surfaced where:** §1 headline finding; §4 throughout (via the Ledger entry). **COI cross-link to Block 5:** D. Leibfried is a co-author and is declared in the Acknowledgements & COI block; C. Sanner is also a co-author and is explicitly not declared (per the 2026-05-26 logbook correction).

#### E. Prior art — structural-match anchor for §3 / MN v0.3 §8.5

- **E1.** Tank, A. B. (2025). Functional Information in Quantum Darwinism: An Operational Measure of Classical Objectivity. arXiv preprint arXiv:2509.17775. DOI [10.48550/arXiv.2509.17775](https://doi.org/10.48550/arXiv.2509.17775). **Role:** *prior-art* (the configurational `R_δ` ~ `N / m_δ*` definition under `FI(δ) = log₂ R_δ` that MN v0.3 §8 transplants onto the temporal axis; structural match documented in MN v0.3 §8.5 and surfaced verbatim in §3 of this View). **Surfaced where:** §3 *Match to the configurational computation*.

### Block 2 — Version-pinning appendix

The authoritative versions of every internal framework artefact cited by this View at issue time. Each is anchored to a specific version; supersession at the next version of an underlying artefact does not retroactively change this View's citation, per Lock-Key.

- **Coastline:** [`coastlines/consensus-emergence-v0.4.md`](../coastlines/consensus-emergence-v0.4.md) — v0.4.
- **Methodological Note:** [`docs/notes/temporal-redundancy-functional-v0.3.md`](../docs/notes/temporal-redundancy-functional-v0.3.md) — v0.3.
- **Breakwater Ledger CL-2026-006 (Sorci dossier):** [`ledger/CL-2026-006-sorci-v0.5.md`](../ledger/CL-2026-006-sorci-v0.5.md) — v0.5.
- **Breakwater Ledger CL-2026-007 (Smith & Ahmadi dossier):** [`ledger/CL-2026-007-smith-ahmadi-v0.3.md`](../ledger/CL-2026-007-smith-ahmadi-v0.3.md) — v0.3.
- **Breakwater Ledger CL-2026-008 (distributed clock-network class):** [`ledger/CL-2026-008-clock-networks-v0.2.md`](../ledger/CL-2026-008-clock-networks-v0.2.md) — v0.2.

### Block 3 — Toolkit Provenance (per Q4 + Scout EC-6)

- **Committing commit hash:** `15f444f` (figure-citing commit; the toolkit notebook extension this View cites is committed there, the upstream computational results are byte-identical to commit `a6518a7`, and the 85-test suite was verified green at `15f444f` at commit time — project logbook, 2026-05-28 Item 2).
- **Results files (committed; byte-identical to `a6518a7`):**
  - [`numerics/results/sorci_nuisance_budget_v0.1.json`](../numerics/results/sorci_nuisance_budget_v0.1.json) — Module 3a D1 budget.
  - [`numerics/results/open_instrument_redundancy_v0.1.json`](../numerics/results/open_instrument_redundancy_v0.1.json) — Module 3b `R_δ(N, γ_φ t)` grid + undefined-boundary table.
- **Notebook files (regenerate the results files end-to-end):**
  - [`numerics/examples/sorci_module.ipynb`](../numerics/examples/sorci_module.ipynb) — Module 3a; Eq. (12)-coefficient validation, latent / observed D1 budget table, ²⁷Al⁺ extrapolation.
  - [`numerics/examples/open_instrument_module.ipynb`](../numerics/examples/open_instrument_module.ipynb) — Module 3b; `ε` bridge derivation; `R_δ(N, γ_φ t)` curves; undefined-boundary table; D5 cross-link; einselection caveat in the first markdown cell (Q10e accessible-regime guardrail).
- **Environment:** QuTiP 5.2.3; Python 3.13.7; NumPy 2.4.4; matplotlib 3.10.8; pytest 9.0.3. The `tmc-numerics` package is installed from `numerics/pyproject.toml` (editable install supported via `pip install -e numerics/` inside a virtual environment — see toolkit work plan v0.1 §10 rev. (d) for the registered toolchain-hygiene refinement).
- **Inherited toolkit anti-claims (A1–A5; toolkit work plan v0.1 §9):**
  - **A1.** The toolkit does not establish that classical proper time *is* an emergent collective variable; it quantifies anchor-measure values for specific protocols under specific assumptions.
  - **A2.** Numerical reproduction of MN v0.3 §2 analytic poles is a consistency check, not a derivation.
  - **A3.** Module 3b's redundant-pole results are exemplars within an assumed regime (the einselection caveat verbatim).
  - **A4.** The toolkit's nuisance budget predicts experimental behaviour under declared Lindblad channels; channels not declared are not bounded by the budget.
  - **A5.** Toolkit verdict-level results feed back into Ledger entries via human-deliberated framework revision; numerical results do not auto-update Ledger verdicts (the load-bearing rule preserved verbatim in §4).

### Block 4 — Figure Provenance (per Q10f, two pinning regimes)

Two regimes per the spec's Q10c carve-out for schematics (logbook 2026-05-28, Lock Record): type-(a) schematics are source-file-pinned vector graphics; type-(b) and type-(c) data figures are notebook-pinned per Q10c at the figure-citing commit. Per-figure record below.

- **Figure 1 — Type (a) schematic; framework orientation.**
  - Source file: [`views/figures/schematic-01-framework-orientation.svg`](figures/schematic-01-framework-orientation.svg).
  - Pinning: source-file-pinned at commit **`d9aae87`** (the commit at which the SVG last changed in the repository — `git log -1 --format='%H' -- views/figures/schematic-01-framework-orientation.svg`).
  - Accessibility encoding: PW slice triple-encoded (thicker stroke; dashed enclosure; explicit "Page–Wootters slice (bipartite)" label) in addition to blue colour; remains legible under deuteranopia, protanopia, and greyscale. (Label uses "bipartite" rather than "N = 2" to avoid collision with the carrier-count `N` used elsewhere in the figure.)
  - Q10b status: no operating-point claim; rule does not bind.
- **Figure 2 — Type (a) schematic; multipartite-vs-redundant contrast.**
  - Source file: [`views/figures/schematic-02-comparison-geometry.svg`](figures/schematic-02-comparison-geometry.svg) (filename retained for repository stability; v0.1 of this View carries only the multipartite-vs-redundant contrast — a comparison-geometry top panel was present in an earlier draft of this commit-sequence and was dropped after a Guardian-cross-artefact-anchoring check; see logbook 2026-05-28).
  - Pinning: source-file-pinned at commit **`d9aae87`** (the commit at which the SVG last changed — the comparison-geometry top-panel removal and `git log -1 --format='%H' -- views/figures/schematic-02-comparison-geometry.svg`).
  - Accessibility encoding: anti-redundant fragments triple-encoded (red colour; dashed borders; explicit "✗ R" markers) symmetric with the redundant fragments (green colour; solid borders; explicit "✓ R" markers).
  - Q10b status: no operating-point claim; rule does not bind.
- **Figure 3 — Type (b) signal-to-noise; `R_δ(γ_φ t)` at three carrier counts.**
  - Source file: [`views/figures/figure-03-redundancy-functional-snr.svg`](figures/figure-03-redundancy-functional-snr.svg).
  - Pinning: notebook-pinned. **Generator:** [`numerics/examples/open_instrument_module.ipynb`](../numerics/examples/open_instrument_module.ipynb) at commit `15f444f`. **Residency:** toolkit-resident (per spec §6 first-instance notebook-residency rule).
  - Environment: QuTiP 5.2.3; Python 3.13.7 (see Block 3 for the full environment pin).
  - Parameter values: `N ∈ {4, 32, 128}`; `γ_φ t ∈ {0.1, 0.273, 0.445, …, 2.0}` (12 points, the same grid as the committed `open_instrument_redundancy_v0.1.json`); deficit `δ = 0.10`; dephasing rate `γ_φ = 1.0`.
  - Sweet vs anti-sweet labelling: explicit. Sweet region `γ_φ t ∈ (0, 0.273]` (all three `N` keep `R_δ` well-defined); anti-sweet region `γ_φ t ∈ (1.827, 2.0]` (no `N` supports a redundancy plateau and `R_δ` is undefined). Per-N first-undefined values dashed in the trace colour.
  - Live-link fallback: *"if this link is unavailable, the notebook at commit `15f444f` reproduces all figures"* (the live Colab link is in §4.2).
- **Figure 4 — Type (c) parameter-space landscape; `R_δ(N, γ_φ t)` heatmap.**
  - Source file: [`views/figures/figure-04-redundancy-landscape.svg`](figures/figure-04-redundancy-landscape.svg).
  - Pinning: notebook-pinned (as Figure 3). **Generator:** same notebook + commit as Figure 3.
  - Environment: same as Figure 3.
  - Parameter values: `N ∈ {4, 8, 16, 32, 64, 128}` (the full committed grid); `γ_φ t ∈ {0.1, …, 2.0}` (12 points); same `δ` and `γ_φ` as Figure 3.
  - Anti-sweet demarcation (Q10b v0.5 closure): the region above the undefined-boundary curve `γ_φ t_crit(N)` is shown as the `cmap.set_bad` colour (light red, separately from the colour-mapped sweet region) and labelled explicitly inside the figure.
  - Live-link fallback: as Figure 3.

### Block 5 — Acknowledgements and Conflict-of-Interest

This block is **separate** from Block 1 by the artefact-category specification's Q11c discipline: persons and institutional associations recorded here are *not* claimed as endorsing the View.

- **D. Leibfried (NIST Boulder)** is acknowledged for valuable prior exchanges with the steward at NIST Boulder, 2010–2012. D. Leibfried is a co-author of *Sorci et al.* (PRL 136, 163602, 2026), the experimental proposal the framework's worked-exemplar dossier (CL-2026-006 v0.5) is built on. **This prior association is the only independence-relevant relationship between the steward and the Sorci author list, and it is acknowledged explicitly here for full transparency.** The framework's classification of the Sorci proposal is *underdetermined* and is the same as it would have been had the prior association not existed; nevertheless, the relationship is disclosed.
- **C. Sanner** is also a co-author of *Sorci et al.* (2026). The steward has **no prior relationship** with C. Sanner — never met or directly interacted with — and explicitly **does not acknowledge** C. Sanner here, in correction of an earlier inference in the project (logged 2026-05-26) that treated both Leibfried and Sanner as close steward contacts. The genuine prior association is with Leibfried alone.
- **Institutional acknowledgement.** This work is hosted at the Physikalisches Institut, Albert-Ludwigs-Universität Freiburg, under Local Stewardship. The framework is not endorsed by the institution; the View is not endorsed by the institution; the framework claims no institutional parity.
- **No funding or commercial conflicts** are declared at this version. Future versions will declare any that arise.

### Block 6 — Citation-metadata stub

To be populated at tagged release with a `CITATION.cff`-compatible block and the resolved O6-regime-(ii) citation locator (`{Zenodo version DOI of the release} / views/view-framework-overview-v0.1.md`). The repository's existing [`CITATION.cff`](../CITATION.cff) records the steward as the primary author at the repository level; the per-View citation form refines that pointer to the specific file at the specific release.

---

*End of Harbour View v0.1 draft. §§1–5 and reference apparatus complete; Lock-Key held: Coastline / Methodological Note / Breakwater Ledger / Sail untouched.*
