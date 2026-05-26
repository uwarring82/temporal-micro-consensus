# Literature Synthesis — v0.1

*Phase 3 cross-cutting synthesis of the 29-entry corpus for the Coastline* Consensus-Emergence of Classical Proper Time *(v0.2).*

| Field | Value |
| --- | --- |
| Version | v0.1 |
| Date | 2026-05-26 |
| Steward | U. Warring |
| Inputs | [`index.md`](index.md) (29 entries), [`notes/`](notes/) (13 full Phase-2 + 16 extraction), [`references.bib`](references.bib) |
| Governs | Phase 3 of [`../literature-review-plan.md`](../literature-review-plan.md). Produces findings only; artefact edits are Phase 4. |

This memo cross-cuts the corpus four ways: **claim-by-claim** (§1), **measure-by-measure** (§2), **gaps and candidate falsifications** (§3), and a **lineage audit** of the Coastline and Sail attributions (§4). Phase-4 routing is collected in §5.

---

## 1. Claim-by-claim

### Claim I — classical proper time is an emergent effective variable; "temporal record"

**Supported, and from two independent directions.** The relational-time lineage gives the root: [[page1983]] (time as a correlation, not an external parameter), [[hohnsmith2021]] (the Page–Wootters, Dirac-observable, and Heisenberg pictures are equivalent), and [[mendes2019]] (time as a consequence of *internal coherence*, with an explicit order parameter that vanishes when no temporal variable exists). The relativistic-clock lineage makes "temporal record" physical: [[zych2011]] and [[pikovski2015]] treat proper time as a physical record whose distinguishability `|⟨τ₁|τ₂⟩|` drives decoherence, and [[sorci2026]] states the framework's own thesis almost verbatim — the operator `τ̂(x̂,p̂)` versus the semiclassical parameter `⟨τ⟩` is exactly "classical proper time is not the expectation value of a microscopic time variable." [[nambu2022]] supplies an operational existence criterion: `F_Q = 0 ⇔ energy eigenstate ⇔ no clock`.

**Strained / by analogy only.** The quantum-Darwinism cluster ([[zurek2003]], [[zurek2009]], [[ollivier2004]], [[riedel2010]]) supports Claim I's *record* notion only configurationally — these are records of position/pointer observables, not of elapsed time. The transplant from configurational to temporal records is the framework's central unproven move (see §3.1). [[connes1994]] (thermal time) and [[rovelli1996]] (relational QM) endorse "time is not a fundamental external parameter" but via mechanisms (modular flow, relational state-assignment) that are *not* record-redundancy based — they are alternative emergent-time programmes, useful for Claim V positioning rather than support.

### Claim II — redundancy · stability · compressibility

This is the framework's load-bearing claim and the corpus's sharpest tension.

- **The architecture is fully supplied — but configurational.** [[zurek2009]] is the direct template: redundancy ratio `R_δ`, and the mutual-information plateau `I(S:F) → H_S` as compressibility. [[ollivier2004]] gives the objectivity criteria (complete + redundant imprint, unique pointer); [[riedel2010]] the concrete computation (`R_δ` linear in time, ~10⁸ redundant copies in scattered photons); [[brandao2015]] the genericity; [[korbicz2014]] the spectrum-broadcast sharpening (both decoherence *and* distinguishability required). All of this is for **configurational** records.
- **No corpus paper exhibits a *redundant multipartite temporal* record.** The relativistic witnesses ([[sorci2026]], [[zych2011]], [[pikovski2015]]) are **bipartite / single-record** and silent on redundancy — they exercise *stability* (failure under marginalisation = the visibility witness) and *compressibility* (frequency shifts compress to one `τ_cl`; visibility loss does not), but never redundancy across many carriers. The distributed-clock papers ([[komar2014]], [[covey2025]], [[fromonteil2025]]) are multipartite but use GHZ/W/NOON entanglement, which is **anti-redundant** by design (entanglement-enhanced metrology deliberately avoids independent redundant copies). Their records are *jointly read*, not *redundantly broadcast*.
- **Net:** the corpus brackets the framework's distinctive position without occupying it — redundant-but-configurational (QD) on one side, multipartite-but-anti-redundant (clock networks) on the other. Claim II.1 (redundancy) has **no temporal exemplar**. This is the single most important finding of the review (§3.1).

The cleanest *operational* instances of II.2/II.3 are in [[sorci2026]] (stability-under-marginalisation failure = visibility loss; compressibility holds for frequency shifts), exactly as the Ledger CL-2026-006 analysis records.

### Claim III — failure mode; discriminate structural failure from nuisance

**Richly supported — this is the corpus's strongest claim.** [[sorci2026]] is the spine: the demarcation between semiclassically-reproducible frequency shifts and the genuinely non-classical visibility loss *is* Claim III's failure-mode-vs-nuisance distinction. [[riedel2011]] supplies the general warning — *decoherence rate ≠ record-keeping (redundancy) rate* — which is precisely "don't conflate decoherence with consensus failure." [[korbicz2014]] sharpens what counts as failure (decoherence alone is insufficient without distinguishability). On the discrimination side: [[zych2011]] (witness vs which-path nuisance), [[pikovski2015]] (universal time-dilation decoherence vs collisional/collapse models), and especially [[fromonteil2025]], whose `ΔE`-tuning plus Gaussian-decay-with-revival GR signature is the **strongest structural discrimination protocol in the corpus**. [[nambu2022]]'s `F_Q = 0` is a sharp structural-failure criterion.

**Gap:** discrimination is done case-by-case; there is no general theory of nuisance-discrimination for temporal records. The Sail/Ledger D1–D3 conditions are the only worked instance (§3.3).

### Claim IV — operational anchors

Engaged across the corpus; treated measure-by-measure in §2. In brief: Fisher ([[giovannetti2011]], [[nambu2022]], [[smith2020]], [[fit2026]]); mutual information ([[zurek2009]] plateau; the Ledger's declared `I(C:M)`); cross-probe mismatch ([[covey2025]]); coarse-graining robustness ([[riedel2010]], [[zurek2003]]).

### Claim V — positioning (multipartite-redundancy, vs PW-bipartite, vs QD-configurational)

The corpus cleanly populates the two poles the framework positions *between*:

- **PW / bipartite pole:** [[page1983]], [[smith2020]], [[hohnsmith2021]], [[nambu2022]], [[mendes2019]].
- **QD / configurational pole:** [[zurek2003]], [[zurek2009]], [[ollivier2004]], [[ollivier2005]], [[riedel2010]], [[riedel2011]], [[korbicz2014]], [[brandao2015]].
- **Multipartite (but anti-redundant):** [[komar2014]], [[covey2025]], [[fromonteil2025]].
- **Alternative emergent-time programmes (contrast):** [[connes1994]], [[rovelli1996]].

The framework's claimed position — *multipartite **and** redundant, applied to temporal records* — is exactly the cell no corpus paper occupies. Claim V's positioning is therefore well-supported as a *map* but the framework's own coordinate is currently empty (§3.1, §3.2).

---

## 2. Measure-by-measure (Claim IV anchors)

| Anchor | State of the art in corpus | Best for | Limitation for the framework |
| --- | --- | --- | --- |
| **Fisher information** about elapsed time | [[giovannetti2011]] (QFI / Cramér–Rao, SQL↔Heisenberg, noise fragility); [[nambu2022]] (`F_Q` as workable-clock criterion); [[smith2020]] (Fisher + mass–time uncertainty for two-clock dilation); [[fit2026]] (Fisher arc-length as time parameter) | Single-record "how much elapsed-time information" | A single-record quantity; does not natively express redundancy across carriers |
| **Mutual information** between temporal records | [[zurek2009]] plateau `I(S:F)→H_S` (configurational template); Ledger CL-2026-006 adopts `I(C:M)` for the Sorci two-record case | Shared structure between records → the natural redundancy/consensus measure | Hard to compute across many fragments; entanglement-enhanced cases give high `I` *without* redundancy |
| **Cross-probe mismatch** | [[covey2025]] three-node beat-note `Δω = ω₁₂ − ω₂₃` — curvature residual after the leading consensus is removed | Distributed / multipartite records; "do independent probes agree on elapsed time" | Needs ≥3 probes to separate consensus from residual; demonstrated only as a GR-curvature signature so far |
| **Robustness under coarse-graining** | [[riedel2010]], [[zurek2003]] (invariance under partial trace of fragment subsets); [[sorci2026]] (the *negative* instance — stability fails) | The stability condition (II.2) | Least developed as an explicit *temporal* measure |

**Reading.** The Claim IV pluralism is healthy, but the anchors are not interchangeable for the *redundancy* condition specifically. **Mutual information across many carriers** is the natural measure for Claim II.1, and the corpus contains no temporal multi-carrier `I` computation. [[covey2025]]'s cross-probe mismatch is the sharpest *experimental* anchor and the natural declared measure for the distributed-network Ledger entries (CL-2026-008), complementing the `I(C:M)` choice the Sorci Ledger (CL-2026-006) already made. The roadmap's "temporal-redundancy toy functional" (Riedel-style, from [[riedel2010]]) is the obvious instrument to fill the gap.

---

## 3. Gaps, open questions, and candidate falsifications

### 3.1 The configurational→temporal transplant is unformalised *(central gap)*

The framework's defining move — applying Zurek's redundancy/stability/compressibility criteria to *temporal* records — is asserted by analogy and has **no worked exemplar** in the corpus. Concretely missing: (i) a rigorous **temporal pointer basis** (what is the einselected basis for a temporal record?); (ii) a definition of an **independent temporal-record fragment**; (iii) any system in which the *same* elapsed time is **redundantly** recorded across many carriers. Until one of these exists, Claim II for temporal records rests on the strength of the analogy alone. This should be stated openly in the Coastline (a candidate anti-claim or explicit open-problem) and is the natural target of a methodological note.

### 3.2 Multipartite ≠ redundant

The clock-network corpus ([[komar2014]], [[covey2025]], [[fromonteil2025]]) shows that "many carriers" and "redundant carriers" are different things: entanglement-enhanced metrology is deliberately **anti-redundant**. The framework needs an explicit distinction between *metrologically multipartite* (correlated for sensitivity) and *redundantly multipartite* (independent compatible copies, the Claim II sense). This sharpens Claim V and guards against mis-citing clock-network results as redundancy demonstrations.

### 3.3 No general nuisance-discrimination theory

Claim III's discrimination requirement is operationalised only case-by-case. The Sorci case (Ledger D1–D3: nuisance decomposition, null-test, `r`-scan) is the sole worked instance. A platform-general "discrimination kit" (which measures, which null tests, separating structural failure from heating/dephasing/prep-infidelity) would generalise it. [[fromonteil2025]]'s decay-plus-revival structural signature is a second template worth abstracting.

### 3.4 Candidate falsification settings

- **Weak falsification (framework passes, instance):** the Coastline requires any "quantum proper-time" witness to be expressible as a partial failure of Claim II discriminable from decoherence. [[sorci2026]] is exactly expressible this way — the Ledger CL-2026-006 confirms the structural alignment and locates the open question precisely at discriminability. Good: the framework's weak-falsifiability machinery has a real, non-trivial instance.
- **Weak falsification (second instance):** [[fromonteil2025]]'s GR revival signature is a second witness that should be expressible as a Claim-II failure; classifying it (a CL-2026-008 candidate) would test whether the machinery generalises beyond the two-carrier case.
- **Strong falsification target:** a system that fails the Claim-II conditions yet admits a single robust `τ_cl` with no measurable inconsistency. Distributed clock networks across differing gravitational potential ([[covey2025]]) are the natural hunting ground — does the three-node residual `Δω` ever vanish (consensus holds) in a regime where the framework predicts failure, or persist where it predicts consensus?

### 3.5 Fisher-time contact point

[[fit2026]]'s record-based parameter `Λ_rec = Σ D(ρ_k‖ρ_{k−1})` is the nearest external "record-based time," but single-trajectory. Whether the framework's redundancy can be built as a *multi-trajectory* generalisation of `Λ_rec` is an open and concrete question — and the cleanest way to position the framework as subsuming, not competing with, FIT.

---

## 4. Lineage audit

Verifying every "in the spirit of / following" attribution in the Coastline and Sail against the verified corpus.

### Coastline v0.2

- ⚠ **External Constraints, item 3 (Page–Wootters "modern developments"):** the list includes **"Hartong–Have–Obers–Pikovski 2024"**, but [[hartong2024]] is a *post-Newtonian coupling-prescription* paper (SciPost Phys. 16, 088 — 1/c² Klein–Gordon on Newton–Cartan backgrounds), **not** a Page–Wootters / relational-time development. **Confirmed mis-attribution** (verified against the PDF). *Phase-4 fix:* remove it from the PW-developments list. If retained anywhere, it belongs with the composite-system/mass-energy lineage ([[zych2019]]) that underwrites the trapped-ion Hamiltonian, not the relational-time channel.
- **External Constraints, item 3:** **"Mendes & Soares-Pinto 2018"** — the published paper is **2019** (Proc. R. Soc. A 475, 20190470; 2018 is the preprint), first author **Leandro R. S.** Mendes. Minor citation-year fix.
- **External Constraints, item 3:** Page & Wootters 1983 ✓, Smith & Ahmadi 2020 ✓, Nambu 2022 ✓ — all correctly attributed as PW-lineage.
- **External Constraints, item 4 (quantum Darwinism, "Zurek and collaborators 2003–present"):** ✓ well-supported ([[zurek2003]], [[zurek2009]], [[ollivier2004]], [[ollivier2005]], [[riedel2010]], [[riedel2011]], [[korbicz2014]], [[brandao2015]]). *Recommendation (addition, not error):* [[ollivier2005]] §VII frames objectivity over *time-ordered* sequences of redundant records — the closest configurational precursor to the temporal-records premise — and would be a well-targeted explicit citation in Claim II or External Constraints.
- **Claim IV:** "Fisher information … (cf. Nambu 2022 for the Page–Wootters setting)" ✓ — [[nambu2022]] is correctly a PW Fisher-information clock.

### Sail v0.2 (Sorci commentary)

- **§1 lineage:** "the line of work running from Page and Wootters through Zych, Pikovski, Brukner and collaborators" ✓ sound ([[page1983]], [[zych2011]], [[pikovski2015]]). "a composite-system action argument due to Zych, Rudnicki and Pikovski" ✓ — [[zych2019]] (PRD 99, 104029). The quoted Hamiltonian, `V ≃ 0.93`, and ²⁷Al⁺ parameters all match [[sorci2026]].
- **Subject-paper citation** (Sail header and Ledger): "Sorci, Foo, Leibfried, Sanner, Pikovski, PRL 136, 163602 (2026), DOI 10.1103/qhj9-pc2b" ✓ exact match to the verified bib.
- ⚠ **Acknowledgements / external-circulation decision — corrected 2026-05-26.** *Correction (see [`../logbook.md`](../logbook.md)):* the steward reports **no relationship with C. Sanner** (never met or directly interacted). The Sail's Acknowledgements claim "ongoing exchanges" with C. Sanner — this is **factually inaccurate** and must be corrected before any external venue. The genuine prior association is with **D. Leibfried** (discussions at NIST Boulder, 2010–2012). Both Leibfried and Sanner are **co-authors of the subject paper** (Sorci et al.), so the independence-of-commentary consideration for external circulation concerns the steward's prior association with **Leibfried** — a co-author of the critiqued paper — and not any Sanner relationship. *(This supersedes the v0.1 framing, which inferred from the Sail that both were close contacts.)*

### Ledger v0.2 (CL-2026-006)

- Declared measure `I(C:M)` ✓ consistent with §2; the entry correctly notes Fisher (Nambu/FIT) as the alternative anchor. [[covey2025]]'s cross-probe mismatch is the additional anchor to register for the distributed-network entries (CL-2026-008).
- All quoted Sorci equations/parameters ✓ match [[sorci2026]].

---

## 5. Phase-4 routing

Findings above, mapped to the roadmap's downstream artefact work (not executed here):

1. **Coastline v0.3:** (a) remove `hartong2024` from the PW-developments list (§4); (b) fix "Mendes & Soares-Pinto 2018" → 2019 (§4); (c) add `ollivier2005` "objective histories" as the configurational precursor (§4); (d) state the configurational→temporal transplant as an explicit open problem / candidate anti-claim (§3.1); (e) add the *multipartite ≠ redundant* distinction to Claim V (§3.2). These compound with the v0.3 candidates already in the roadmap (FIT citation, GR boundary, measure-registration, "many" specification).
2. **Ledger:** open CL-2026-007 ([[smith2020]]) and CL-2026-008 (distributed networks — [[covey2025]], [[fromonteil2025]], [[komar2014]]); the latter should declare **cross-probe mismatch** as its evaluating measure (§2) and would test whether the Claim-II-failure machinery generalises beyond two carriers (§3.4).
3. **Sail:** the reference apparatus is now corpus-backed; foreground the **co-authorship** finding in the external-circulation decision (§4).
4. **Methodological note(s):** the temporal-redundancy toy functional (Riedel-style, §2/§3.1) and a platform-general nuisance-discrimination kit (§3.3) are the two highest-value candidates.

---

## 6. Version history

| Version | Date | Notes |
| --- | --- | --- |
| v0.1 | 2026-05-26 | Initial synthesis over the 29-entry corpus. Claim-by-claim (§1), measure-by-measure (§2), gaps/falsifications (§3), lineage audit (§4), Phase-4 routing (§5). Central finding: the configurational→temporal transplant (Claim II redundancy) has no temporal exemplar in the corpus; the framework's multipartite-redundancy cell sits between QD (redundant-configurational) and clock networks (multipartite-anti-redundant) and is currently empty. Lineage audit confirms the `hartong2024` mis-attribution and the `mendes2019` year slip in the Coastline, and sharpens the Sail acknowledgement decision (Leibfried/Sanner are co-authors). |
| v0.1 — corrected 2026-05-26 | §4 acknowledgement bullet corrected: the steward reports **no relationship with C. Sanner**; the earlier "both close contacts" framing was an incorrect inference from the Sail. Genuine prior association is with Leibfried only. See [`../logbook.md`](../logbook.md). No other section affected. |

---

*Phase 3 synthesis under Local Stewardship. It interprets the corpus against Coastline v0.2 and does not itself revise any Coastline, Ledger, or Sail artefact — those edits are Phase 4, governed by the roadmap.*
