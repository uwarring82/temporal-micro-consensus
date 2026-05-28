# First Harbour View — Commented Bibliography Draft (Q11 assembly worksheet)

**Document type:** Pre-View assembly worksheet for the **commented bibliography** block of the first Harbour View's reference apparatus (per spec v0.6 §6 / Q11a). Each entry carries the three required fields: **anchor**, **role annotation** (controlled vocabulary), and — for external-constraint entries — an **endorsement-scope marker** (constraint-only / no-parity, per A4 + Q7).

**Companion to:** [`view-framework-overview-v0.1-toc-outline.md`](view-framework-overview-v0.1-toc-outline.md) (LOCKED 2026-05-28).

**Status:** Draft worksheet. Folded into the View's reference apparatus at prose stage (spec §12 next-move 7 → 8). Acknowledgements & COI (Q11c) remain in a **separate** block (Block 5 of the apparatus), never conflated with citations here.

**Source corpus:** [`docs/literature/references.bib`](literature/references.bib) (Phase-1-verified Tier-1/Tier-2 entries) + the Coastline v0.4 External Constraints section + steward-confirmed canonical-text anchors for the external-endorsed coastlines (A1–A5 below; these textbook anchors are **not** currently in `references.bib` — they are introduced at the View bibliography per Q11a discipline. Folding into `references.bib` at View-issue time is a registered drafter task — BibTeX entries added for any external-constraint anchor that survives the §2/§3 prose stage).

**Conventions:**
- Role annotation from the controlled vocabulary: *external-constraint* / *prior-art* / *method-source* / *contrast-contested*.
- Endorsement-scope marker for external-constraint entries: *constraint-only; no parity claimed* (A4 + Q7 mirror).
- "Surfaced where" lists the View section(s) that draw on the reference. A reference not surfaced in the body should be removed before issuance (the bibliography is not a corpus dump).
- Entries marked **MANDATORY** are required by the current §1–§5 outline; **OPTIONAL** entries are surfaced only if the drafter exercises the relevant choice at prose stage (e.g. item-7 cross-View pointers); **STEWARD-CONFIRM** entries propose a canonical-text anchor where the Coastline does not pin one.

---

## A. External constraints (constraint-only; no parity claimed)

The Coastline v0.4 names five externally-endorsed coastlines in its "External Constraints" section. Each must appear with an explicit constraint-only marker (Q11a / A4 mirror). The Coastline does not pin a specific canonical text for **quantum mechanics**, **special relativity**, **general relativity**, **quantum information theory**, or **thermodynamics** — anchors **LOCKED 2026-05-28** by steward call.

### A1 — Quantum mechanics  **LOCKED 2026-05-28**

- **Anchor:** Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information* (10th Anniversary Edition). Cambridge University Press. ISBN 978-1-107-00217-3.
- **Role:** *external-constraint*.
- **Endorsement-scope marker:** constraint-only; no parity claimed. The View operates within unitary quantum mechanics as established; it does not derive, extend, or revise it.
- **Surfaced where:** §1 (Endorsement-Marker sentence), §2 (Coastline anchoring), §3 (master-equation framework).
- **Steward note:** Nielsen & Chuang is the canonical QIT-canon choice and double-counts for QIT (A4 below) — the Coastline names QM and QIT as separate constraints but they share a canonical reference; this consolidation is honest.

### A2 — Special relativity  **LOCKED 2026-05-28**

- **Anchor:** Misner, C. W., Thorne, K. S., & Wheeler, J. A. (1973). *Gravitation*. W. H. Freeman. ISBN 978-0-7167-0344-0. (Used for both SR and GR; see A3.)
- **Role:** *external-constraint*.
- **Endorsement-scope marker:** constraint-only; no parity claimed. The View operates within SR for the flat-spacetime baseline (Regime of Validity); it does not derive, extend, or modify it.
- **Surfaced where:** §2 (Regime of Validity sub-bullet; flat-spacetime baseline).
- **Steward note:** MTW is a doorstop, but it is *the* doorstop — signals seriousness to the foundations-metrology audience. Consolidation of SR + GR into one anchor (A2 + A3) is correct.

### A3 — General relativity (weak-field / post-Newtonian regime only)  **LOCKED 2026-05-28**

- **Anchor:** Misner, Thorne & Wheeler (1973), *Gravitation* (as A2).
  - **Accessibility alternative (apparatus only, not primary):** Carroll, S. M. (2004). *Spacetime and Geometry: An Introduction to General Relativity*. Addison Wesley. ISBN 978-0-8053-8732-2. Promoted from "alternative" to listed-secondary only on pilot-reader signal that MTW is overkill for a 12–15-page View. Default: MTW alone.
- **Role:** *external-constraint*.
- **Endorsement-scope marker:** constraint-only; no parity claimed. The View operates within GR's **weak-field (post-Newtonian) regime** only; strong-field, non-perturbative, and quantum-gravitational regimes are explicitly out of scope (Coastline Anti-Claim #7 + Regime of Validity).
- **Surfaced where:** §2 (GR-regime boundary statement; the Q11b anchor for any "consistent with weak-field GR" sentence MUST cite Coastline v0.4 External Constraints item 5 + Anti-Claim #7 + Regime of Validity — this is the load-bearing Q11b/A7 enforcement point).

### A4 — Quantum information theory  **LOCKED 2026-05-28**

- **Anchor:** Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information* (10th Anniversary Edition) (as A1).
  - **Conditional secondary anchor (drafter decision at §3 prose stage):** Hayashi, M. (2017). *Quantum Information Theory: Mathematical Foundation* (2nd ed.). Springer. ISBN 978-3-662-49723-4. Folded in **only if §3 prose leans on rigorous Helstrom / Holevo / distinguishability machinery** beyond what Nielsen & Chuang covers; otherwise omit.
- **Role:** *external-constraint*.
- **Endorsement-scope marker:** constraint-only; no parity claimed. The View uses the established results of QIT (trace distance, Helstrom bound, Holevo information, mutual information) as background; it does not derive, extend, or revise them.
- **Surfaced where:** §3 (the four-way coincidence trace-distance / Helstrom / projective / Holevo for `ε`); §4 (model-conditional findings phrased in `I(C:M)`).

### A5 — Thermodynamics  **CONDITIONAL LOCK 2026-05-28**

- **Anchor (if retained):** Callen, H. B. (1985). *Thermodynamics and an Introduction to Thermostatistics* (2nd ed.). Wiley. ISBN 978-0-471-86256-7.
- **Role:** *external-constraint*.
- **Endorsement-scope marker:** constraint-only; no parity claimed.
- **Condition:** **keep only if** the View body surfaces a thermodynamics relationship claim at §2 prose stage (e.g. "consistent with the second law"). **If no such claim appears, remove the entry** per Q11 discipline — a reference not surfaced in the body has no business in the bibliography. Drafter decides at §2 prose stage.

---

## B. Prior art (Page–Wootters lineage)

Cluster A from the literature corpus. Each is *prior-art* in the Q11 controlled vocabulary; no endorsement-scope marker (markers are external-constraint-only).

### B1 — Page & Wootters (1983)  **MANDATORY**

- **BibTeX key:** `page1983`.
- **Citation:** Page, D. N., & Wootters, W. K. (1983). Evolution without evolution: Dynamics described by stationary observables. *Physical Review D*, 27(12), 2885–2892.
- **Anchor (DOI):** [10.1103/PhysRevD.27.2885](https://doi.org/10.1103/PhysRevD.27.2885).
- **Role:** *prior-art* (canonical bipartite-correlation channel for time emerging from quantum correlations).
- **Surfaced where:** §1 (executive question), §2 (Claim V positioning — "Page–Wootters bipartite slice within the consensus picture").

### B2 — Mendes & Soares-Pinto (2019)  **MANDATORY**

- **BibTeX key:** `mendes2019`.
- **Citation:** Mendes, L. R. S., & Soares-Pinto, D. O. (2019). Time as a consequence of internal coherence. *Proceedings of the Royal Society A*, 475(2231), 20190470.
- **Anchor (DOI):** [10.1098/rspa.2019.0470](https://doi.org/10.1098/rspa.2019.0470). Preprint: arXiv:1806.09669.
- **Role:** *prior-art* (modern Page–Wootters development; Coastline External Constraints item 3).
- **Surfaced where:** §2 (Claim V positioning; Page–Wootters modern lineage).
- **Note:** The Coastline v0.4 cites this as "2019" (publication year), fixing the v0.3+ lineage correction (preprint year 2018 was used in earlier versions).

### B3 — Smith & Ahmadi (2020)  **OPTIONAL (item 7)**

- **BibTeX key:** `smith2020`.
- **Citation:** Smith, A. R. H., & Ahmadi, M. (2020). Quantum clocks observe classical and quantum time dilation. *Nature Communications*, 11, 5360.
- **Anchor (DOI):** [10.1038/s41467-020-18264-4](https://doi.org/10.1038/s41467-020-18264-4). Preprint: arXiv:1904.12390.
- **Role:** *prior-art* (Page–Wootters modern development; Coastline External Constraints item 3; subject of Ledger CL-2026-007 v0.2).
- **Surfaced where:** §2 *or* §5 (item-7 resolution; one-bullet cross-View pointer to CL-2026-007 v0.2; Guardian leans §5.1).

### B4 — Nambu (2022)  **OPTIONAL**

- **BibTeX key:** `nambu2022`.
- **Citation:** Nambu, Y. (2022). Qubit Clock in Quantum Cosmology. *Universe*, 8(2), 99.
- **Anchor (DOI):** [10.3390/universe8020099](https://doi.org/10.3390/universe8020099). Preprint: arXiv:2201.02770.
- **Role:** *prior-art*.
- **Surfaced where:** Coastline cites it in External Constraints item 3 (modern Page–Wootters developments); whether the View body surfaces it depends on prose density of the Claim V positioning paragraph. Drafter decides. If unsurfaced, remove.

---

## C. Prior art (Quantum Darwinism lineage)

Cluster B from the literature corpus.

### C1 — Zurek (2003)  **MANDATORY**

- **BibTeX key:** `zurek2003`.
- **Citation:** Zurek, W. H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Reviews of Modern Physics*, 75(3), 715–775.
- **Anchor (DOI):** [10.1103/RevModPhys.75.715](https://doi.org/10.1103/RevModPhys.75.715). Preprint: arXiv:quant-ph/0105127.
- **Role:** *prior-art* (foundational decoherence/einselection — the einselection caveat anchors here at the configurational level; MN v0.3 §1.1 and §8.6 carry the temporal-side caveat).
- **Surfaced where:** §2 (Claim V positioning — quantum Darwinism foundational); §3 (verbatim einselection caveat citation lineage).

### C2 — Zurek (2009)  **MANDATORY**

- **BibTeX key:** `zurek2009`.
- **Citation:** Zurek, W. H. (2009). Quantum Darwinism. *Nature Physics*, 5, 181–188.
- **Anchor (DOI):** [10.1038/nphys1202](https://doi.org/10.1038/nphys1202). Preprint: arXiv:0903.5082.
- **Role:** *prior-art* (the architecture Claim II specialises to temporal records — three Zurek criteria).
- **Surfaced where:** §2 (Claim II — emergence criterion); §5.1 (Anti-Claim #6 framing — "criteria proven for configurational records").

### C3 — Ollivier, Poulin & Zurek (2004)  **MANDATORY**

- **BibTeX key:** `ollivier2004`.
- **Citation:** Ollivier, H., Poulin, D., & Zurek, W. H. (2004). Objective Properties from Subjective Quantum States: Environment as a Witness. *Physical Review Letters*, 93, 220401.
- **Anchor (DOI):** [10.1103/PhysRevLett.93.220401](https://doi.org/10.1103/PhysRevLett.93.220401). Preprint: arXiv:quant-ph/0307229.
- **Role:** *prior-art* (closest configurational precursor to the temporal specialisation — Coastline v0.3 lineage addition; redundancy/objectivity criteria are the configurational model for Claim II conditions).
- **Surfaced where:** §2 (Claim II + Claim V positioning); §5.1 (Anti-Claim #6 — "configurational precursor lacking a temporal exemplar").

### C4 — Ollivier, Poulin & Zurek (2005)  **MANDATORY**

- **BibTeX key:** `ollivier2005`.
- **Citation:** Ollivier, H., Poulin, D., & Zurek, W. H. (2005). Environment as a Witness: Selective Proliferation of Information and Emergence of Objectivity in a Quantum Universe. *Physical Review A*, 72, 042113.
- **Anchor (DOI):** [10.1103/PhysRevA.72.042113](https://doi.org/10.1103/PhysRevA.72.042113). Preprint: arXiv:quant-ph/0408125.
- **Role:** *prior-art* (PRA follow-up to C3; paired-citation convention).
- **Surfaced where:** §2 (paired with C3).

### C5 — Brandão, Piani & Horodecki (2015)  **OPTIONAL**

- **BibTeX key:** `brandao2015`.
- **Citation:** Brandão, F. G. S. L., Piani, M., & Horodecki, P. (2015). Generic emergence of classical features in quantum Darwinism. *Nature Communications*, 6, 7908.
- **Anchor (DOI):** [10.1038/ncomms8908](https://doi.org/10.1038/ncomms8908). Preprint: arXiv:1310.8640.
- **Role:** *prior-art* (objectivity emerges generically — strengthens the Claim II configurational architecture).
- **Surfaced where:** §2 only if the framework's positioning vs configurational quantum Darwinism is given a deeper paragraph. Drafter decides at prose stage; the corpus tiered it Tier-2.

### C6 — Riedel & Zurek (2010)  **OPTIONAL**

- **BibTeX key:** `riedel2010`.
- **Citation:** Riedel, C. J., & Zurek, W. H. (2010). Quantum Darwinism in an Everyday Environment: Huge Redundancy in Scattered Photons. *Physical Review Letters*, 105, 020404.
- **Anchor (DOI):** [10.1103/PhysRevLett.105.020404](https://doi.org/10.1103/PhysRevLett.105.020404). Preprint: arXiv:1001.3419.
- **Role:** *prior-art* / *method-source* (concrete configurational `R_δ`-style redundancy computation; methodological precursor to the MN's temporal-redundancy functional).
- **Surfaced where:** §3 (MN methodology lineage — if the drafter chooses to anchor `R_δ` lineage at prose stage). Optional but recommended for §3 since it establishes the configurational `R_δ` precedent the MN transplants.

---

## D. Prior art (worked exemplar / candidate witness)

### D1 — Sorci et al. (2026)  **MANDATORY**

- **BibTeX key:** `sorci2026`.
- **Citation:** Sorci, G., Foo, J., Leibfried, D., Sanner, C., & Pikovski, I. (2026). Quantum signatures of proper time in optical ion clocks. *Physical Review Letters*, 136, 163602.
- **Anchor (DOI):** [10.1103/qhj9-pc2b](https://doi.org/10.1103/qhj9-pc2b). Preprint: arXiv:2509.09573.
- **Role:** *prior-art* / candidate-witness.
- **Surfaced where:** §1 (headline finding cites the Ledger entry, which classifies this paper); §2 (deferred-item pointer; §4 anchor); §4 (Module 3a is the toolkit's D1 nuisance budget for the Sorci witness; entire section anchors here via CL-2026-006 v0.5).
- **Note (audit cross-link to Block 5 / Q11c):** Leibfried and Sanner are co-authors; the COI structure runs through Leibfried alone per the 2026-05-26 logbook correction — see Block 5 (Acknowledgements & COI) in the View's reference apparatus, **not here**. The bibliography records the paper; the acknowledgement structure is separate.

---

## E. Prior art (structural-match anchor)

### E1 — Tank (2025)  **MANDATORY**

- **BibTeX key:** `tank2025`.
- **Citation:** Tank, A. B. (2025). Functional Information in Quantum Darwinism: An Operational Measure of Classical Objectivity. arXiv preprint arXiv:2509.17775.
- **Anchor (DOI / arXiv):** [10.48550/arXiv.2509.17775](https://doi.org/10.48550/arXiv.2509.17775).
- **Role:** *prior-art* (structural-match anchor for MN v0.3 §8.5: the configurational `R_δ` ~ `N/m*_δ` definition that the MN's temporal-side `R_δ` matches **structurally**, not numerically — the configurational/temporal asymmetry closed at the level of computation).
- **Surfaced where:** §3 (MN methodology; the §8.5 match wording).
- **Note:** Preprint, no journal venue yet. The MN v0.3 §8.5 wording is **verbatim** — the View's §3 carries it without rewording per A7.

---

## F. Optional — cross-View pointer references (item-7 resolution)

If the drafter exercises the item-7 resolution at prose stage and includes the one-bullet cross-View pointer (Guardian leans §5.1 over §2), the following appear here. Otherwise omit.

### F1 — Covey, Pikovski & Borregaard (2025)  **OPTIONAL (item 7)**

- **BibTeX key:** `covey2025`.
- **Citation:** Covey, J. P., Pikovski, I., & Borregaard, J. (2025). Probing curved spacetime with a distributed atomic processor clock. *PRX Quantum*, 6, 030310.
- **Anchor (DOI):** [10.1103/q188-b1cr](https://doi.org/10.1103/q188-b1cr). Preprint: arXiv:2502.12954.
- **Role:** *prior-art* (Ledger CL-2026-008 v0.2 subject; clock-network class; stress-tested the GR boundary that drove Coastline v0.4).
- **Surfaced where:** §5.1 (or §2, drafter's choice) if cross-View pointers included.

### F2 — Fromonteil et al. (2025)  **OPTIONAL (item 7)**

- **BibTeX key:** `fromonteil2025`.
- **Citation:** Fromonteil, C., Vasilyev, D. V., Zache, T. V., Hammerer, K., Rey, A. M., Ye, J., Pichler, H., & Zoller, P. (2025). Non-local mass superpositions and optical clock interferometry in atomic ensemble quantum networks. arXiv preprint arXiv:2509.19501.
- **Anchor (DOI / arXiv):** [10.48550/arXiv.2509.19501](https://doi.org/10.48550/arXiv.2509.19501).
- **Role:** *prior-art* (Ledger CL-2026-008 v0.2 subject; the second member of the clock-network class).
- **Surfaced where:** §5.1 (or §2, drafter's choice) paired with F1.
- **Note:** Preprint only — no journal venue / volume / pages yet (re-check before issuance, per the references.bib note).

---

## Q11b enforcement checklist (audit at prose stage)

For every sentence in the View body of the form "consistent with X," "compatible with X," "respects X," or any equivalent relationship claim about external physics, audit:

1. **Is X an external coastline named in the Coastline v0.4 External Constraints section?** (QM, SR, weak-field GR, QIT, thermodynamics.) If not — the sentence is making a relationship claim not licensed by the Coastline; **delete or reroute**.
2. **Is the sentence anchored to a Breakwater Ledger entry or a Coastline section?** Per Q11b (load-bearing), a relationship claim with no Ledger or Coastline anchor is an **A7 violation** (the View asserting more than the underlying artefacts support). **Anchor or delete.**
3. **Does the entry in this bibliography carry the constraint-only / no-parity marker?** If A1–A5, yes; if a prior-art entry, the relationship claim is misclassified (the framework's relationship is to a *constraint*, not to prior-art work). Re-classify.

**Specific load-bearing audit points already identified in the outline:**

- **§2 GR-regime sentence.** Must anchor to **A3 (GR weak-field) + Coastline v0.4 External Constraints item 5 + Anti-Claim #7 + Regime of Validity**. Three-way anchor; no anchor → delete.
- **§4 "consistent with Sorci visibility" or similar.** Must anchor to **Ledger CL-2026-006 v0.5** (not directly to D1 / Sorci 2026 — the relationship is the Ledger's classification, not the paper itself).

---

## Drafter checklist before folding into the View's apparatus

- [x] **Steward confirmation on A1–A5 canonical-text anchors — LOCKED 2026-05-28.** Nielsen & Chuang 2010 (A1, A4); MTW 1973 (A2, A3, with Carroll 2004 as pilot-reader-conditional accessibility alternative for A3); Callen 1985 (A5, conditional on body surfacing).
- [ ] **Drafter resolves item-7 (cross-View pointers):** include F1 + F2 + B3, or omit all three.
- [ ] **Drafter resolves A5 (thermodynamics) surfacing at §2:** keep only if a body sentence references it; otherwise remove.
- [ ] **Drafter resolves A4 (Hayashi 2017) secondary anchor at §3:** fold in only if §3 leans on rigorous Helstrom/Holevo machinery beyond Nielsen & Chuang.
- [ ] **Drafter resolves C5, C6, B4 surfacing at prose stage:** keep only if a body sentence references them; otherwise remove.
- [ ] **Q11b audit pass** on every "consistent with" / "compatible with" / "respects" sentence in §§2–4 — at least the §2 GR-regime sentence and the §4 Sorci-visibility claim must be explicit ledger-or-Coastline-anchored.
- [ ] **Audit acknowledgements & COI (Block 5) is separate** — no entry in this bibliography mentions Leibfried or Sanner as acknowledgements.
- [ ] **Final ordering:** A (external constraints) → B (PW lineage) → C (QD lineage) → D (worked exemplar) → E (structural-match anchor) → F (cross-View pointers, optional). Each entry retains its three Q11a fields in the rendered View.
- [ ] **Pilot-reader audit point (for schematic figures, not the bibliography itself):** colourblind accessibility and greyscale-print viability of the §1 and §2 SVG schematics. Standard figure-honesty check at the pilot-reader stage.
- [ ] **BibTeX fold-back to `references.bib`:** for any external-constraint anchor that survives the §2/§3 prose stage (default: A1/A4 Nielsen & Chuang; A2/A3 MTW; conditional A3 Carroll; conditional A4 Hayashi; conditional A5 Callen), add a `@book` BibTeX entry to `docs/literature/references.bib` so the corpus reflects the final commitment.

---

*End of bibliography draft. Awaiting steward confirmation on A1–A5 canonical anchors; remainder is body-surfaced and ready to fold into the View's reference apparatus at prose stage.*
