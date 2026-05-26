# Tutorial — Reading the Temporal Consensus Harbour

*A guided introduction to the concepts, architecture, and current state of the repository.*

| Field | Value |
| --- | --- |
| Version | v0.1 |
| Date | 2026-05-26 |
| Licence | CC BY-SA 4.0 |
| Scope | Conceptual tutorial — no prior knowledge of the Harbour architecture assumed |

---

## 1. What this repository is

This repository contains a **research framework** called *Consensus-Emergence of Classical Proper Time*, together with the tools used to build and stress-test it. The framework asks a specific question:

> **When does a classical proper-time variable emerge from microscopic quantum dynamics?**

The short answer proposed here: *when many independent microscopic carriers agree on the same elapsed time* — not because some underlying clock is ticking, but because the collective behaviour of many degrees of freedom stabilises a single effective parameter. Time, on this view, is a **consensus variable**, not a private property of any single subsystem.

The repository is organised into three artefact families — **Coastlines**, **Ledgers**, and **Sails** — each with a distinct role. This tutorial explains what they are, what concepts they carry, and how to read them in order.

---

## 2. The Harbour architecture

The repository uses a controlled vocabulary from the broader **Open-Science Harbour** architecture. You do not need to know the full architecture, but four terms recur everywhere:

| Term | Meaning | Analogue |
| --- | --- | --- |
| **Coastline** | A versioned framework note — the "shoreline" where ideas are anchored. It states claims, anti-claims, and falsifiability conditions. | A theory paper or framework document |
| **Ledger** | A **Breakwater Claim Analysis Ledger** entry — a classification of an external scientific claim against a named Coastline. | A structured peer review or claim assessment |
| **Sail** | A commentary or essay that translates framework content into prose for broader readership. | A News & Views, commentary, or essay |
| **Local Stewardship** | The status of every document here: draft, versioned, and maintained by a named steward. **Not** peer-reviewed, **not** institutionally endorsed. | A preprint or working paper |

Every document carries an explicit version number (v0.1, v0.2, …). Citations **must** include the version, because claims evolve. The Git history provides the external audit trail.

### Why three families?

- The **Coastline** states the framework in its own terms. It is abstract and self-contained.
- The **Ledger** tests the framework against the real literature: "Given this Coastline, how does Smith & Ahmadi (2020) sit?"
- The **Sail** translates the result into prose: "Here is why the Sorci proposal matters, and what remains to do."

This separation prevents framework drift. The Coastline cannot silently absorb a Ledger finding; the Ledger cannot soften its verdict to suit a Sail's narrative. Each family is **Lock-Key disciplined**: changes to one do not automatically propagate to the others.

---

## 3. The core framework: Consensus-Emergence

### 3.1 The starting intuition

In everyday life, we read the time from a clock and treat it as objective. But a single atom has no sharp "time." Its internal state evolves, and we can *infer* elapsed time from that evolution, but the inference is probabilistic, fragile, and tied to the atom's own dynamics.

The framework starts from two well-established ideas:

1. **Page–Wootters mechanism** (1983, and modern descendants): time can be understood as a *correlation* between a "clock" subsystem and the rest of the universe. If the universe is in an energy eigenstate, no time passes; time emerges from the correlation structure.
2. **Quantum Darwinism** (Zurek and collaborators): classical objectivity emerges when information about a system is *redundantly* encoded in many environmental fragments. Many independent observers can each access the same information without disturbing the system or each other.

The Coastline's move is to **specialise Quantum Darwinism to temporal records**. Instead of asking "how many environmental fragments record the position of a pointer?", it asks "how many independent carriers record the same elapsed time?" When the answer is "many, stably, and compressibly," a classical proper-time variable τ_cl has emerged.

### 3.2 The load-bearing sentence

The framework is summarised in one sentence, intended for citation in dependent documents:

> **Classical proper time is not the expectation value of an underlying microscopic time variable, but the robust collective parameter that best organises and stabilises the temporal records of many underlying degrees of freedom.**

Read this carefully. It denies that τ_cl = ⟨τ̂⟩ for some microscopic time operator τ̂. Instead, τ_cl is an *effective* variable that summarises collective behaviour — like temperature in statistical mechanics, or pressure in a gas.

---

## 4. The Five Claims

The Coastline is organised around five **Claims** (I–V). Understanding them is the key to reading every document in the repository.

### Claim I — Problem statement

Classical proper time is treated as an **emergent effective variable**, not a microscopic sharp property. A **temporal record** is any physical degree of freedom whose state carries inferentially usable information about elapsed evolution — whether classically accessible or not.

*What this means:* an atom's internal clock state is a temporal record. So is its motional state, if the motion is coupled to the clock. So is the phase of a photon that interacted with the atom. The framework does not require these records to be classical; it requires only that they support some inferential read-out.

### Claim II — Emergence criterion (the heart of the framework)

A classical proper-time variable τ_cl emerges only when three conditions are jointly satisfied:

| Condition | Meaning | Quantum-Darwinism analogue |
| --- | --- | --- |
| **Redundancy** | Many microscopic carriers encode *mutually compatible* temporal information. | Many environmental fragments record the same pointer state. |
| **Stability** | The inferred parameter is insensitive to tracing out small subsets of carriers or to local perturbations. | Objectivity: observers can independently access information without disturbing the system. |
| **Compressibility** | A single coarse-grained parameter τ_cl suffices; adding microscopic labels yields no inferential gain. | The redundant imprint is complete — no further environmental fragments add information. |

*Critical caveat — the transplant gap:* these three criteria were proven for **configurational** records (position, pointer states). The Coastline **transplants** them to **temporal** records by structural analogy. At present, **no worked exemplar** of redundant temporal records exists in the literature. This is the framework's **principal open problem**, registered explicitly as Anti-Claim #6 and in the Deferred Items.

*Critical distinction — multipartite ≠ redundant:* "many carriers" is not enough. Entanglement-enhanced metrology (GHZ, W, NOON states) uses many carriers that are deliberately **anti-redundant** — tracing out one carrier destroys the joint signal. Multipartiteness is necessary but not sufficient for redundancy. This distinction, added in Coastline v0.3, guards against mis-citing clock-network papers as demonstrations of consensus.

### Claim III — Failure mode

When Claim II fails, the appropriate description is not merely "the clock decohered." It is:

> **The subsystem no longer supports a classical temporal-consensus variable.**

This relocates the failure from an opaque loss of interferometric coherence to a **breakdown of an explicit emergence criterion**. The framework therefore demands that we **discriminate structural consensus failure from generic nuisance-induced coherence loss** (heating, dephasing, preparation infidelity, detection noise). This discrimination is a *necessary step* in making the framework experimentally credible.

### Claim IV — Operational anchors

Claim II is intended to be **operational**, not metaphorical. Four candidate measures are offered:

| Anchor | What it measures | Best for |
| --- | --- | --- |
| **Fisher information** F[τ] | How much elapsed-time information a state carries | Bounding temporal resolution |
| **Mutual information** I(C:M) | Shared structure between two temporal records (e.g. clock and motion) | Redundancy / consensus between records |
| **Cross-probe mismatch** Δω | Residual disagreement between independent elapsed-time estimates | Distributed / multipartite records; curvature signatures |
| **Coarse-graining robustness** | Invariance of inferred τ_cl under partial trace of carriers | Stability under marginalisation |

The Coastline does not commit to one anchor as canonical. It commits only that **any deployment must declare its measure upfront**.

*Refinement (from Ledger practice):* distinguish a **resolution anchor** (bounds what must be resolved — e.g. Fisher information) from a **classification anchor** (carries the structural content being classified — e.g. cross-probe mismatch or mutual information). Conflating them is a known failure mode.

### Claim V — Positioning

Consensus-emergence sits **between** two established frameworks and is distinct from both:

- **Page–Wootters** is *bipartite*: clock vs. rest. Consensus-emergence is *multipartite-redundant*: many carriers jointly supporting one parameter. PW correlations are one channel of temporal information within the consensus picture, not the consensus itself.
- **Quantum Darwinism** is *configurational*: redundant records of position/pointer states. Consensus-emergence is *temporal*: redundant records of elapsed time.

The framework's distinctive cell — **multipartite and redundant, applied to temporal records** — is currently **empty** in the literature. The corpus brackets it without occupying it.

---

## 5. The Ledger: how claims are classified

A **Breakwater Ledger entry** classifies an external scientific claim against a named Coastline under a **declared evaluating measure**. The possible classifications are:

| Classification | Meaning |
| --- | --- |
| **COMPATIBLE** | The claim aligns with the framework's structural commitments under the declared measure. |
| **INCONSISTENT** | The claim contradicts the framework's structural commitments under the declared measure. |
| **UNDERDETERMINED** | The claim is framework-legible but the evidence is insufficient to decide compatibility or inconsistency. |

### Anatomy of a Ledger entry

Every entry contains:

1. **The External Claim** — restated in the entry's own words, often split into components (e.g. C1 = sensitivity, C2 = interpretive).
2. **Declared Evaluating Measure(s)** — the Claim IV anchor(s) used for the classification, with justification.
3. **Classification Analysis** — engagement with each relevant Coastline claim.
4. **Verdict** — COMPATIBLE, INCONSISTENT, or UNDERDETERMINED.
5. **Discriminant Conditions** — explicit conditions for upgrade or downgrade. These are the entry's most load-bearing content: they say *what would change the verdict*.

### Example: CL-2026-006 (Sorci et al. 2026)

- **Claim evaluated:** C2 — that observed visibility loss in a squeezed trapped-ion clock would witness quantum proper-time dynamics.
- **Declared measure:** Mutual information I(C:M) between clock and motional records.
- **Classification:** **UNDERDETERMINED**.
- **Reason:** The Hamiltonian-level structure aligns with a partial failure of Claim II (stability and compressibility fail for the reduced clock). But the published proposal does not **discriminate** this structural failure from generic decoherence (heating, dephasing, preparation infidelity).
- **Discriminant conditions D1–D3:** nuisance decomposition, null-test protocol, and r-dependence test. Satisfying all three would upgrade to COMPATIBLE.

### The three active Ledger entries

| Entry | Source | Classification | Anchor | Key gap |
| --- | --- | --- | --- | --- |
| **CL-2026-006** | Sorci et al. 2026 | UNDERDETERMINED | Mutual information I(C:M) | Discriminability from nuisance channels |
| **CL-2026-007** | Smith & Ahmadi 2020 | UNDERDETERMINED | Fisher F[τ] (registered); coherence term γ_Q⁻¹ noted as carrying the structural content | Experimental witness isolating γ_Q⁻¹ from nuisances |
| **CL-2026-008** | Covey 2025; Fromonteil 2025 | UNDERDETERMINED | Cross-probe mismatch Δω (classification); QFI (resolution) | Discriminability of GR signature from technical decoherence |

All three rest on the **experimental-witness gap**: the structural claims are framework-compatible, but the evidence packages are not yet discriminating.

---

## 6. The Sail: translating into prose

The **Sail** (*Visibility, the Right Witness*, v0.4) is a commentary on Sorci et al. 2026, anchored to Coastline v0.4 — with its Ledger anchor kept at CL-2026-006 **v0.2** (a documented *mixed anchor*; the Ledger entry is itself now at v0.3, and the v0.2→v0.3 re-anchor changed no verdict, so the citation remains valid). It translates the Ledger's UNDERDETERMINED classification into a thesis:

> The Sorci proposal is a valuable operationalisation step. Its demarcation between semiclassically-reproducible frequency shifts and genuinely nonclassical visibility loss is the right demarcation. But sensitivity ≠ discriminability. The path to isolating evidence runs through explicit nuisance decomposition, an r-dependence test, and a calibrated null-test protocol.

Sails are where **authorial voice** is load-bearing. They are licensed more restrictively (CC BY-NC-SA 4.0) than Coastlines or Ledgers (CC BY-SA 4.0) because the prose itself is part of the contribution.

---

## 7. How the literature review feeds everything

The repository's upstream work is a **comprehensive field map** of 29 papers across seven thematic clusters:

| Cluster | Topic | Framework role |
| --- | --- | --- |
| A | Page–Wootters & relational time | The bipartite channel (Claim V) |
| B | Quantum Darwinism | The configurational architecture (Claim II) |
| C | Quantum clocks (trapped ions, optical) | Experimental substrate (Claim III) |
| D | Fisher information & metrology | Operational anchor (Claim IV) |
| E | Relativistic / gravitational decoherence | SR/weak-field boundary (External Constraints) |
| F | Distributed clock networks | Multipartite structure (Claim V) |
| G | Adjacent foundations (thermal time, relational QM) | Contrast and positioning |

The review proceeded in **five phases**:

1. **Phase 0 — Infrastructure:** scaffolding (bib, templates, triage tracker).
2. **Phase 1 — Corpus assembly:** 29 papers verified, tiered (13 Tier-1 load-bearing, 16 contextual).
3. **Phase 2 — Deep reading:** full per-claim annotation of Tier-1 papers.
4. **Phase 3 — Synthesis:** cross-cutting analysis (claim-by-claim, measure-by-measure, gaps, lineage audit).
5. **Phase 4 — Artefact edits:** routing findings into Coastline, Ledger, and Sail revisions.

Phases 1–3 are complete. Phase 4 is ongoing.

### The synthesis headline

The central finding of the synthesis ([`docs/literature/synthesis-v0.1.md`](literature/synthesis-v0.1.md)):

> The framework's defining move — transplanting Zurek's redundancy/stability/compressibility from configurational to temporal records — has **no worked exemplar** in the corpus. The relativistic witnesses are bipartite and silent on redundancy; the clock networks are multipartite but anti-redundant. The framework's distinctive cell (multipartite **and** redundant, temporal) is **empty**.

This is not a failure. It is a **sharpening**: it tells us exactly what would convert the framework from analogy to demonstration — a system in which the *same* elapsed time is redundantly encoded across many independent carriers, none of them entangled for metrological enhancement.

---

## 8. Regime of Validity

Coastline v0.4 added an explicit **Regime of Validity**:

- **In scope:** special-relativistic and **weak-field (post-Newtonian)** regimes — accelerated worldlines, differing gravitational potential, curvature entering perturbatively.
- **Proviso:** a well-defined inter-worldline comparison protocol (synchronisation scheme) must exist.
- **Curvature as residual:** in the multi-worldline setting, the leading Newtonian agreement is compressible; spacetime curvature appears as the **incompressible cross-probe residual** (e.g. Covey's Δω).
- **Out of scope:** strong-field / non-perturbative regimes; settings with no shared comparison protocol; quantum gravity.

This was made load-bearing by CL-2026-008, which classifies curvature/redshift probes. Before v0.4, the framework cited only SR among inertial worldlines; it could not address those probes.

---

## 9. How to read this repository (recommended order)

If you are new to the repository, read in this order:

1. **This tutorial** (you are here) — concepts and architecture.
2. [`coastlines/consensus-emergence-v0.4.md`](../coastlines/consensus-emergence-v0.4.md) — the framework itself, in full.
3. [`sails/sorci-commentary-v0.4.md`](../sails/sorci-commentary-v0.4.md) — see the framework applied to a concrete case.
4. [`ledger/CL-2026-006-sorci-v0.3.md`](../ledger/CL-2026-006-sorci-v0.3.md) — the Ledger classification underwriting the Sail.
5. [`docs/literature/synthesis-v0.1.md`](literature/synthesis-v0.1.md) — how the literature review stress-tested the framework.
6. [`docs/roadmap.md`](roadmap.md) — what is in active development and what is deferred.

Earlier versions are retained for transparency; always use the latest version for current claims.

---

## 10. Open problems and next steps

The framework's **principal open problem** (Coastline v0.4 Deferred Items):

> A **worked exemplar of redundant temporal records** — a concrete model in which the same elapsed time is redundantly encoded across many independent carriers, neither configurational (quantum Darwinism) nor merely entanglement-enhanced (clock metrology) — would convert Claim II from analogy to demonstration.

Other deferred items:
- A **CCUF bridge** between microscopic consensus (L₀) and architectural clock agreement (L₁).
- **Quantitative thresholds** for Claim II (mutual-information requirements, Fisher profiles, redundancy bounds).
- **Strong-field / non-perturbative extension** (beyond the post-Newtonian regime).
- **Methodological notes:** a temporal-redundancy toy functional (Riedel-style); a platform-general nuisance-discrimination kit.

The next research step (per roadmap, on hold) is the **temporal-redundancy toy functional**: borrow from Functional Information in Quantum Darwinism to compute a redundancy measure for a few-ion clock with motional squeezing. This would concretise both the Coastline's Claim II and the Ledger's discriminant conditions.

---

## 11. Key distinctions to keep in mind

| Distinction | Why it matters |
| --- | --- |
| **Bipartite vs. multipartite** | Page–Wootters is bipartite (clock vs. rest); consensus-emergence requires many carriers. |
| **Multipartite vs. redundant** | Many carriers can be entangled (anti-redundant) or independent (redundant). Only the latter satisfies Claim II.1. |
| **Configurational vs. temporal** | Quantum Darwinism proves redundancy for position/pointer records. The temporal transplant is unproven. |
| **Sensitivity vs. discriminability** | A signal can be measurable without being isolable from nuisance channels. The Ledger's UNDERDETERMINED verdicts all rest on this gap. |
| **Resolution anchor vs. classification anchor** | Fisher information bounds what must be resolved; cross-probe mismatch or mutual information carries the structural content. Conflating them is a failure mode. |
| **Structural alignment vs. satisfied criterion** | A paper can align with the framework's language without satisfying its conditions. The Sorci protocol *aligns* with Claim II failure but does not *demonstrate* redundant consensus. |

---

## 12. Version history

| Version | Date | Notes |
| --- | --- | --- |
| v0.1 | 2026-05-26 | Initial tutorial. Covers Harbour architecture, five Claims, Ledger system, literature-review methodology, synthesis headline, regime of validity, reading order, open problems, and key distinctions. Anchored to Coastline v0.4, Ledger entries 006 v0.3 / 007 v0.3 / 008 v0.2, Sail v0.4, synthesis v0.1. |

---

*This tutorial is a documentation artefact under Local Stewardship. It does not claim parity with externally validated physical laws. For the authoritative framework statement, see the current Coastline; for authoritative classifications, see the current Ledger entries.*
