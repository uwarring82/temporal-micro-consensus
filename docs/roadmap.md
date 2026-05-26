# Roadmap — Harbour Temporal Consensus

*Forward-looking documentation for active development items, deferred items, and stewardship decisions.*

| Field | Value |
| --- | --- |
| Version | v0.1 |
| Date | 2026-05-23 |
| Steward | U. Warring |
| Status | Living document — updated as items advance or are retired |

---

## Active development

### Coastline v0.3 candidates

The following revisions to *Consensus-Emergence of Classical Proper Time* are collected for a future v0.3, to be drafted after Sail v0.2 (and any subsequent Sail revisions) road-test the framework in earnest.

- **Registration protocol for Claim IV measure selection.** Require any deployment of the framework — Ledger entry, Sail, methodological note — to declare its chosen operational measure and threshold upfront, with explicit justification. Preserves the pluralism of Claim IV while closing the measure-shifting vulnerability identified in the Scout horizon scan of Coastline v0.2.
- **FIT citation in External Constraints.** Add Fisher-Informational Time (arXiv 2605.03958, May 2026) as a fourth external citation alongside quantum mechanics, special relativity, Page–Wootters, and quantum Darwinism. FIT operates at the single-trajectory layer; consensus-emergence at the multipartite-redundancy layer. The two are compatible but distinct.
- **FIT positioning bullet in Claim V.** Add a third positioning bullet making the trajectory-vs-multipartite distinction explicit. FIT-style accumulated Fisher distance is one available realisation of the Fisher-information anchor in Claim IV, not a substitute for the redundancy/stability/compressibility criteria across many records.
- **GR boundary statement.** External Constraints currently cite SR proper-time relations among inertial worldlines. Add an explicit boundary note that the framework operates in the SR-and-weak-field regime; extension to strongly accelerated worldlines or curved-spacetime regimes requires additional structure. Becomes relevant when the framework is applied to distributed-clock networks across regions of differing gravitational potential.
- **"Many" specification.** Distinguish between *multi-carrier across subsystems* (the multipartite case proper) and *multi-channel within one subsystem* (multiple observables of a single constituent). Both can satisfy the redundancy condition, but the structural content differs. Guardian flag on Coastline v0.2.
- **Claim III softening.** Final sentence currently reads "This discrimination is what converts the criterion of Claim II from a description into a witness." Guardian recommends "This discrimination is a *necessary step in* converting the criterion of Claim II from a descriptive framework into an experimentally credible witness." Slightly more careful; necessary not sufficient.

### Ledger schema candidates

- **Layer A/B/C architecture.** Guardian proposal during CL-2026-006 review: future Ledger entries make explicit three layers — (A) structural dynamics, (B) measure adequacy, (C) experimental discriminability. The current entry already does all three in substance; explicit labelling would make the schema more reusable across cases.

### Sail v0.3 candidates

Pending for the Sorci commentary if it is to leave internal circulation:

- **Reference apparatus.** The current draft cites ideas and lineages in prose; an external venue requires a proper bibliography. Estimated 25–35 references including: Sorci et al. and the trapped-ion clock literature it cites, Page & Wootters, Zych–Costa–Pikovski–Brukner line, Pikovski et al. gravitational decoherence work, Zurek and quantum Darwinism literature, Margalit et al. self-interfering clock, Nambu Fisher-information cosmological clock, Mendes & Soares-Pinto on time observables, Hartong–Have–Obers–Pikovski coupling prescription, Martínez-Lahuerta et al. trapped-ion mass defect, Yudin & Taichenachev mass defect effects, FIT preprint, and recent distributed-clock-network work.
- **Acknowledgements decision.** Current v0.2 retains the acknowledgement of D. Leibfried and C. Sanner with an internal note flagging proximity-signal risk for external circulation. The decision — retain, reformulate as a brief disclosure note, or remove — is to be taken before any external venue.
- **Licensing harmonisation.** If the Sail is to be compiled with Coastline content (e.g. a handbook, an extended technical report), the current CC BY-NC-SA 4.0 of the Sail and CC BY-SA 4.0 of the Coastline create a non-commercial-clause inheritance issue. Scout flag. Decision pending: harmonise to CC BY-SA 4.0, retain the split, or maintain a separate licence-by-document policy.

### Possible future Ledger entries

- **CL-2026-007 (candidate).** Smith & Ahmadi, *Quantum clocks observe classical and quantum time dilation*, *Nat. Commun.* 11, 5360 (2020). Page–Wootters-grounded analysis of quantum vs classical time dilation effects. Classification against Coastline v0.2 would test the framework against a different (bipartite, momentum-superposition) protocol than the Sorci case.
- **CL-2026-008 (candidate).** Distributed clock-network proposals (Covey–Pikovski–Borregaard 2025; Fromonteil et al. 2025). Move from L₀ minimal-multipartite case to genuinely multipartite case across spatially separated nodes. Would also stress-test the GR boundary.

### Possible future Sails or methodological notes

- **Methodological note on operational measures.** Develop one or more of the Claim IV anchors (mutual information distribution across subsystems, Fisher information distribution across probes, cross-probe phase mismatch under inferred τ_cl) into a self-contained methodological note suitable for adoption in concrete experimental analyses.
- **Toy-model functional for temporal redundancy.** Verifier-suggested concrete next step. Borrow from Functional Information in Quantum Darwinism (Riedel-style) to compute a temporal-redundancy functional for a few-ion clock with motional squeezing. Concretises both the Coastline's Claim II and the Ledger's discriminant conditions for the Sorci case.

## Deferred items (from Coastline v0.2)

These are noted as plausible future extensions but not committed in the current Coastline. They are tracked here without commitment.

- **CCUF bridge.** Possible structural analogy between L₀ consensus-emergence (microscopic temporal records) and L₁ architectural agreement (CCUF η-parameter, comparison-geometry boundary, "agreement, not oscillation, defines a clock"). The proposed unification would identify both layers as expressions of one principle — time as a robust collective variable, not a private property — at distinct scales. Disciplined approach: a separate Coastline note bridging the two frameworks, drafted only after each has matured independently. Lock-Key discipline.
- **Application to thermodynamic / arrow-of-time discussions.** Noted in Coastline v0.2 as plausible but not pursued. Connection to thermal time, fluctuation theorems, and arrow-of-time emergence in quantum systems may be productive but requires its own dedicated treatment.
- **Quantitative thresholds.** Specific numerical thresholds (e.g. mutual-information requirements in bits per carrier, Fisher-information distribution profiles, redundancy lower bounds) that would render Claim II quantitatively testable in concrete experimental settings. Deferred pending engagement with specific protocols beyond Sorci.

## Stewardship decisions pending

- **External circulation of Sail.** Decision points before any external venue: (i) acknowledgements; (ii) reference apparatus completion; (iii) optional courtesy contact with subject-paper authors before deposit. Not urgent.
- **arXiv vs journal-comment vs preprint-only.** If external circulation is pursued, the route — arXiv-only deposit, formal Comment to PRL, Nature Physics News & Views via Dr Pichon route, or other — needs deliberation. Each has different timelines, audiences, and discipline requirements.
- **Public visibility of repository.** Currently private / Local-Stewardship draft. Public hosting on GitHub, GitLab, or institutional infrastructure is a separable decision from external circulation of the Sail; the repository can remain private while individual artefacts are circulated externally.

## Retired or completed items

*None yet. This section will track items that have been advanced (moved into a versioned document) or formally retired with rationale.*

---

## Version History

| Version | Date | Notes |
| --- | --- | --- |
| v0.1 | 2026-05-23 | Initial roadmap. Captures v0.3 candidate items for Coastline, Ledger schema, and Sail; deferred items from Coastline v0.2; possible future Ledger entries and Sails; stewardship decisions pending. |
