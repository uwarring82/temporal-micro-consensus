# Harbour View — Structural Deliberation Note

**Document type:** Deliberation note (not a Harbour View itself; a design document for the artefact category).
**Version:** v0.6 (lock candidate, 2026-05-27).
**Endorsement Marker:** Local Stewardship (Ulrich Warring, Physikalisches Institut, Albert-Ludwigs-Universität Freiburg). Authority from use, not endorsement.
**Status:** Lock candidate. All architectural questions resolved; all open decisions (O1–O12) carry recommendations awaiting explicit steward confirmation at a single lock call. No item blocks lockability. v0.6 adds language boundaries and readability discipline (Q12), the rule that holds a View to its externally-readable purpose.
**Lineage:** Discovery deliberation (2026-05-27 prior turn) → consolidated-write-up proposal → v0.1 → Guardian pass → structural pass → v0.2 → Scout pass → structural-pass approval → v0.3 → steward-initiated figure/notebook expansion → Guardian ADM-EC pass → v0.4 → Scout + structural + Architect passes → steward query on external-reference anchoring → v0.5 → steward-initiated language-boundary addition → Guardian pass → v0.6 (this version).

-----

## §1 — Purpose of this note

To work through, before drafting prose, the architectural questions that will determine what a Harbour View is, what it is not, and how it sits within the existing Harbour artefact taxonomy. This is a Lock-Key step: deliberate the structure → lock it → then draft. The note is not a Harbour View; it is the design specification for the artefact category.

**Two-layer structure.** This note contains both *category-level* rules that will bind every Harbour View and *first-instance* design choices that apply only to the initial framework-overview View. The two layers are distinguished where relevant: §§2–4, §§7–8, the eight anti-claims, and the version-pinning, snapshot, citation-locator, supersession, erratum, figure-taxonomy, interactive-notebook, external-reference-anchoring, and language-boundary rules are category-level; §§5–6 and decisions O3–O5, O8 are first-instance. Future Views inherit the category rules and make their own first-instance choices.

-----

## §2 — Why a new artefact category is needed

The Harbour currently has: **Coastlines** (frameworks), **Sails** (commentaries/essays), **Breakwater Ledger** (claim classifications), **Methodological Notes** (instruments), **Handbooks** (interfaces), and **Work Plans** (instruments for stewardship). None of these are the right vessel for a *consolidated, externally-readable, citable presentation of a body of work*. The gap is real.

Possible fits and why each is wrong:

- A *Sail* is wrong because it is commentary on one work, not a presentation of a body of work.
- A *Coastline* is wrong because it is a framework, not a presentation.
- An *MN* is wrong because it is methodological, focused on one instrument.
- A *Handbook* is wrong because it is an interface specification.
- A *Work Plan* is wrong because it is a plan, not a presentation of completed work.

The new artefact category is for: *consolidated presentation of a body of work, citable, externally-readable, derived from but not authoritative over the underlying framework artefacts.*

**Minimal entry condition (category-level discriminant).** A Harbour View is justified only when it must synthesise or present more than one underlying artefact family, or one artefact family together with a worked exemplar / toolkit result. A single-artefact presentation does not qualify; that work belongs in a Sail or in the artefact’s own README. This discriminant prevents any long Sail from being relabelled as a View.

-----

## §3 — Name: Harbour View

**Canonical type name:** `Harbour View`. Single token in citation strings, repository taxonomy, and internal references.

**External subtitle convention:** `Harbour View: Report on [topic]`. Used in external-facing contexts (arXiv categorisation, library cataloguing, first-encounter explanations) to give outsiders the technical-report cognate without binding the category permanently to “report” language.

Example: `Harbour View: Report on Temporal Redundancy and Emergent Proper Time`.

- **View** carries the right metaphor: a vantage point that surveys the work from a particular position. Not the territory itself; a map of it, taken from a stated standpoint. The View is a *window, not a door* — readers can see the work from outside without entering the steward’s vocabulary, but cannot modify the framework through the View.
- Distinguishes cleanly from *Coastline* (the territory’s terrain) and *Sail* (a particular journey).

Alternatives considered and rejected:

- “Harbour Report” — too narrowly procedural; loses the vantage-point metaphor.
- “Harbour Survey” — confusable with literature-review work.
- “Consolidated Stewardship Document” — verbose; not a Harbour-native term.

-----

## §4 — Architectural questions

### Q1. Authoritative vs presentational? *(category-level)*

**Resolution:** Presentational, not authoritative. The Coastline, Ledger, MN, Sail remain the authoritative versions of their content. A View *presents* adapted content with cross-references to the authoritative sources.

**Strengthened prohibition (load-bearing).** A View may not introduce new definitions, new anti-claims, new classification statuses, or new success criteria except by quoting or citing an already-versioned underlying artefact. If drafting the View surfaces a needed change to a framework artefact, the change routes through the relevant artefact’s next version, not the View. This preserves the Lock-Key separation: the View is a key (interpretation), the underlying artefacts are the lock (concepts), and the View cannot evolve the framework by stealth in summary prose.

### Q2. Audience? *(first-instance for the first View; category guidance below)*

**Category-level guidance:** Every View states its primary audience explicitly on its first page. Secondary audiences may be acknowledged but are not co-equal readers.

**First-instance resolution for the first View:** Primary audience: physicists working at the interface of foundations and metrology. Secondary audiences (philosophers of physics; methodologists) acknowledged as future-View candidates, not co-equal readers of the first View. (This is open decision O8; the steward confirms at the lock call.)

**Consequence:** vocabulary explanations included; cross-references explicit; jargon defined on first use; the artefact taxonomy itself briefly explained in an early section — but pitched at the primary audience’s background, not at a generic external reader.

### Q3. Scope — fixed snapshot or living document? *(category-level)*

Two options:

- **(a) Fixed snapshot.** Each View is byte-frozen on issue and gets its own citation locator; updates produce new Views (v0.2, v0.3) rather than editing the existing one. Consistent with the Coastline / Ledger / MN no-retro-edit convention.
- **(b) Living document.** A single View that evolves with the framework; snapshotted at major versions.

**Resolution: (a) fixed snapshot.** Discipline-consistent with the rest of the Harbour. Updates as new versions; old versions retained per the supersession rule at Q9. Citation-locator semantics are specified at Q3-DOI below.

**Q3-DOI — Citation regime (O6 resolution).** Three options were considered:

- **(i) Repository-release DOI only.** Each tagged release of the views repository mints one Zenodo version DOI; the View is cited via that release DOI alone. Coarse but simple; the View is identified by the release containing it. **Rejected:** insufficient for multi-View repositories.
- **(ii) Version DOI + file-path citation.** Each tagged release mints one Zenodo version DOI; the View is cited as “{version DOI} / {file path within release}”. Combines snapshot immutability with per-View specificity at no additional Zenodo overhead. **Recommended.**
- **(iii) Separate per-View Zenodo record.** Each View deposited as its own Zenodo record with its own concept DOI and version DOIs. Maximum per-View clarity; maximum maintenance burden; requires deliberate deposition workflow distinct from the existing repository-release pipeline. **Rejected for now;** deferred unless external citation practice proves regime (ii) insufficient.

**Final lock wording for O6 (recommended):**

> *Each issued Harbour View is cited by the Zenodo version DOI of the tagged repository release plus the exact file path of the View within that release. The repository release DOI guarantees immutability; the file path identifies the View within the release. Separate per-View Zenodo records are deferred unless external citation practice proves regime (ii) insufficient.*

**Registered future improvement (Scout EC-1; see §10).** File paths can change across repository reorganisations. If citation fragility manifests in practice, the category may migrate to a manifest-slug locator: a `views/manifest.json` per release mapping stable slugs (e.g. `view:framework-overview`) to the file paths within that release. The citation locator would then become `{version DOI} / view:{slug}`, decoupling citation from directory structure. Migration is backward-compatible in principle: manifests can be added to historical release records as supplementary metadata where permitted. Deferred under the discipline of minimum viable structure first.

### Q4. Relationship to the toolkit? *(category-level)*

A View citing toolkit results must pin the toolkit version explicitly (commit hash, results-file version, notebook version). Toolkit-derived content in a View inherits the toolkit’s anti-claims (A1–A5 of the toolkit work plan).

**Placement rule (Scout EC-6).** Inherited toolkit anti-claims must appear in a dedicated **Toolkit Provenance** subsection of the View’s reference apparatus. Inheritance honoured in spirit but invisible to the reader is not honouring it. The Toolkit Provenance subsection reproduces or cites by version the inherited anti-claims and pins the toolkit commit hash, results-file version, and notebook version used.

### Q5. Multiple coexisting Views? *(category-level)*

**Resolution: yes, allowed.** Different Views can present the same body of work from different vantage points — one for physicists, one for philosophers of physics, one focused on the methodological contribution, one toolkit-focused, etc. Each is a separate artefact with its own citation locator.

**Risks (explicitly registered).**

- **(i) Maintenance burden.** Under the no-retro-edit rule, View count multiplies the stewardship load: each View has its own version-pinned sources, its own citation locator, and possibly its own Pages entry.
- **(ii) Divergence-readable-as-contradiction.** External readers encountering two Views with different emphases on the same body of work may read the divergence as the framework contradicting itself.
- **(iii) Fragmentation.** Multiple Views may fragment the body of work in readers’ minds rather than illuminating it from complementary angles.

**Mitigations.**

- Each View declares its vantage-point in its first page.
- Each View carries a “related Views” cross-reference table at issue.
- The steward commits to maintaining no more Views than can be kept synchronised to current artefact versions.
- **Concordance paragraph (Scout EC-4).** Every View that has any predecessor or sibling View on the same body of work includes a mandatory concordance paragraph — a single, brief narrative paragraph, written at the same time as the View, that explicitly addresses how the new View relates to existing Views. The concordance paragraph is more than a cross-reference table; it is a structural mitigation against divergence-readable-as-contradiction. Placement: end of the executive overview, and **exempt from the executive overview's page cap** as a mandatory appendage — it does not consume the ≤1 page budget and does not force the overview to shrink.

**Collision rule (load-bearing).** Coexisting Views may differ in emphasis and audience framing, but they may not contradict the version-pinned underlying artefacts. If two Views appear to conflict, the cited source artefacts override both. This preserves the hierarchy: artefacts are the lock, Views are keys, and no key can be louder than the lock.

### Q6. Versioning convention? *(category-level)*

`view-{slug}-v0.x.md` — e.g. `view-framework-overview-v0.1.md`. The slug identifies the vantage-point; `v0.x` is the version. Repository placement is open decision O2.

### Q7. Endorsement Marker scope? *(category-level)*

Local Stewardship, same as all current Harbour artefacts. Views do not seek broader endorsement. A View may *cite* externally endorsed coastlines (Standard Model, GR, thermodynamics) as constraints, but the View itself remains under Local Stewardship.

### Q8. Lock-Key discipline within a View? *(category-level)*

A View MUST cite its underlying artefacts by version. If the underlying artefact evolves after the View is issued, the View remains anchored to the version it cited at issue; a later View can re-anchor. This prevents silent drift between View content and current framework state.

**Erratum clause.** If a factual error is discovered in an issued View after release, the only correction path is reissue at the next version. No retro-edits, consistent with the Harbour no-retro-edit discipline. The reissue changelog must explicitly note the error and the correction.

### Q9. Superseded View discoverability *(category-level — Scout EC-2)*

When a new version of a View supersedes an earlier version of the same View (e.g. v0.2 supersedes v0.1), or when a new View on the same body of work from the same vantage point supersedes an earlier View, three rules apply:

- **(a) Archive immutability.** All prior Zenodo version DOIs remain resolvable and immutable. Citation strings to old versions never break.
- **(b) Pages canonicality.** The Pages canonical URL for the View slug (e.g. `/views/framework-overview/`) always points to the most recent version. Pages entries for prior versions remain reachable at versioned URLs (e.g. `/views/framework-overview/v0.1/`) but carry a top-of-page **supersession banner** identifying the current canonical version and linking to it. *Implementation caveat:* the versioned-subpath structure is not produced by a default Jekyll setup without explicit collection or folder configuration. A one-time Pages configuration update may be required before the first View is released; a pre-issuance technical check is registered in §12.
- **(c) Supersession changelog.** The new version’s version-history entry explicitly states what was superseded and why (substantive update vs. erratum vs. vantage-point refinement).

Supersession is distinct from erratum (Q8): an erratum corrects a factual error within a presentation; supersession replaces the presentation as the current canonical version. Both produce a new version; only supersession requires the banner and the canonicality change.

### Q10. Figure taxonomy and interactive-notebook integration *(category-level menu; first-instance plan in §6)*

**Scope note.** Interactive notebook integration was deferred in v0.1–v0.3 (§10, "a separate discovery action"). v0.4 brings it into the artefact-category spec as an *explicit, steward-initiated scope expansion*, not silent creep. The §10 scope-creep mitigation is satisfied: this inclusion is deliberate and audit-marked.

**Q10a — Figure taxonomy (three types, offered as a category menu).** A View need not contain figures at all; Q10 applies only when figures or interactive notebooks are included. When figures are used, a View may draw on any of three figure types; the taxonomy is a shared vocabulary, not a blanket mandate. The three form a natural orientation hierarchy:

- **Type (a) — Schematic / illustrational.** Conceptual diagrams that orient the reader: apparatus layouts, framework-structure diagrams, comparison-geometry schematics (e.g. L_source / L_apparatus / L_comparison separation), coupling diagrams. Purpose: orientation.
- **Type (b) — Signal-to-noise at dedicated parameter spots (sweet and anti-sweet).** Figures that localise the operating points: where in parameter space the signal-to-noise of the observable is favourable (sweet spots) and where it is dominated by a noise contribution (anti-sweet spots). Purpose: honest localisation of where the method works and where it does not.
- **Type (c) — Parameter-space sweeps (landscapes).** Heatmaps, contour plots, or multi-trace sweeps showing how the observable varies across parameter space, with the sweet and anti-sweet regions of type (b) shown in their full landscape context. Purpose: situating the operating points.

**Q10b — Sweet-AND-anti-sweet rule (load-bearing, A7 enforcement).** The obligation attaches to *any figure that displays operating points*, regardless of figure type. A figure that displays operating points MUST show both the favourable (sweet) and the noise-dominated (anti-sweet) regions; a figure that displays only sweet spots — only where the method works — is an A7 violation ("reads more confidently than the underlying artefacts"). This binds type (b) by definition, and binds type (c) whenever a sweep is used to display operating points: a type (c) landscape that surfaces operating points must explicitly demarcate the anti-sweet regions, not only the favourable ones. A type (a) schematic that carries no operating-point claim is unaffected. The anti-sweet region is the visual analogue of honest limitation-reporting and is mandatory whenever operating points are shown. This is the visual form of the Uncertainty Atlas principle: selective display reduces apparent variance without increasing robustness; only showing the contrast (the kernel rotation) is honest.

**Q10c — Static-render-from-pinned-notebook rule (immutability preservation, load-bearing).** Every figure in a View is a static render generated by a version-pinned notebook. The generating notebook's commit hash, the parameter values or ranges used, and any fixed parameters are recorded in the Figure Provenance subsection (Q10f). The View's figures are reproducible from the pin regardless of any later change to a live notebook. This preserves the snapshot immutability that grounds the citation regime (Q3, Q9): a citation never resolves to drifted figure content.

**Q10d — Live notebook link as convenience layer (not the citable artefact).** A View may include in-text links to live Google Colab notebooks so visitors can make their own visualisation choices. These links are a *convenience/discovery layer*, never the citable artefact. Rules:

- The live link should, where technically possible, open the notebook *at the pinned commit* used to generate the View's static figures (Colab supports GitHub-commit-pinned opens), so the interactive starting state matches the published figures. Where the platform cannot honour a commit-pinned open, the pinned commit and the fallback statement remain the binding record.
- A broken or unavailable live link does not invalidate the View. The View remains fully citable and reproducible from the pin. Each live link carries a documented fallback: "if this link is unavailable, the notebook at {commit} reproduces all figures."
- The live link is best-effort under the steward's maintenance commitment (Q5 risk (i)); link rot is expected over long horizons and does not constitute a View erratum.

**Q10e — Accessible-parameter-regime guardrails.** Interactive widgets must be bounded to model-valid parameter regimes. The slider/widget ranges encode the model's validity bounds, and the relevant caveat (einselection, model-conditionality, the toolkit anti-claims A1–A5) is surfaced inline within the notebook so a visitor cannot silently wander into regions where the model breaks down. "Accessible regime" means: the visitor explores freely *within* the bounds where the figures and the underlying artefacts remain valid.

**Q10f — Figure Provenance (reference-apparatus requirement, parallel to Toolkit Provenance).** Every View carrying figures includes a Figure Provenance subsection in its reference apparatus, recording for each figure: figure type (a/b/c); the generating notebook, its **repository URL**, and its pinned commit hash; whether the notebook is toolkit-resident or views-resident (and, if toolkit-resident, whether its commit is identical to or linked with the Q4 toolkit pin); the recorded **environment dependencies** (a pinned `requirements.txt` or an explicit list of package versions) alongside the commit hash, so the live notebook's functional lifespan survives runtime drift as far as practicable; parameter values or swept ranges and fixed parameters; for any figure displaying operating points, explicit labelling of which regions are sweet and which anti-sweet (Q10b); the live-link fallback statement. Figure inheritance of toolkit anti-claims is cross-referenced to the Toolkit Provenance subsection (Q4).

**A8 boundary clarification for notebooks.** Interactive parameter exploration is *reproduction and exploration* (permitted: it lets a reader do something with the work), not *pedagogical onboarding* (not permitted: teaching prerequisite physics). A notebook that lets a reader sweep a validated parameter is within scope; a notebook that teaches the underlying formalism from first principles is a tutorial and belongs outside the View per A8.

### Q11. External-reference anchoring and commented bibliography *(category-level)*

The View anchors its internal and computational sources rigorously — underlying artefacts by version (Q8), toolkit by commit (Q4), figures and notebooks by commit and environment (Q10f). External references must be anchored with parallel discipline so that the View's epistemic posture (A4, Q7) remains auditable. A bare reference list is insufficient.

**Q11a — Commented bibliography (reference-apparatus requirement).** Every View includes a commented bibliography in its reference apparatus. Each external reference records:

- **Anchor:** a stable identifier — DOI for papers; canonical citation (with edition where applicable) for externally-endorsed coastlines (Standard Model, GR, thermodynamics) and textbook sources; a permanent URL or archived snapshot for external software or data.
- **Role annotation (the "comment"):** exactly one role from a controlled vocabulary —
  - *external-constraint* — an externally-endorsed coastline the framework must respect as a boundary condition;
  - *prior-art* — work the framework builds on or situates itself against;
  - *method-source* — a technique, instrument, or dataset adopted;
  - *contrast-contested* — work the framework explicitly diverges from, or that contests a cited constraint.
- **Endorsement-scope marker (for external-constraint entries only):** an explicit constraint-only / no-parity note, mirroring A4 and Q7. The citation establishes that the framework respects the external coastline as a boundary condition; it does not claim parity with, or endorsement by, the externally-validated body of work.

**Q11b — Relationship-claim anchoring (load-bearing, ties to Q1 / A7).** Any assertion in a View about the framework's *relationship* to an external constraint — "consistent with general relativity", "compatible with the second law", and the like — is a claim, and Q1 forbids the View from originating claims. Every such assertion must cite the Breakwater Ledger entry (with its COMPATIBLE / UNDERDETERMINED / INCONSISTENT classification) or the Coastline section that already establishes the relationship. A relationship claim with no Ledger or Coastline anchor is an A7 violation (the View asserting more than the underlying artefacts support) and is impermissible.

**Q11c — Acknowledgement vs citation separation.** The commented bibliography is for cited works. Acknowledgements (personal and institutional associations, e.g. Leibfried for the NIST 2010–2012 association) live in the separate acknowledgements-and-COI block (§6) and are never conflated with citations. A person or body acknowledged is not thereby claimed as endorsing the View (cf. the 2026-05-26 Sanner correction).

### Q12. Language boundaries and readability discipline *(category-level)*

A Harbour View is an externally readable presentation document. Its language must therefore minimise local shorthand and avoid unnecessary jargon. The goal is not simplification of the work's content, but reduction of avoidable linguistic barriers.

Rules:

1. **Avoid unexplained abbreviations.** Abbreviations are avoided where possible. If an abbreviation is necessary, it is written out on first use and used consistently thereafter. Local Harbour abbreviations are especially restricted.
1. **Prefer descriptive phrases over internal labels.** Use simple descriptive wording before internal taxonomy terms. For example, write "a presentational overview of several artefacts" before relying on "Harbour View." (Consistent with the first-page artefact-type declaration, §11 recommendation 1: declare the descriptive meaning, then introduce the term.)
1. **Use short, declarative sentences where possible.** Sentences should carry one main idea unless a more complex structure is needed for precision.
1. **Define specialist terms at first use.** Terms from physics, philosophy, methodology, or Harbour vocabulary are briefly anchored when first introduced. Definitions should be concise, not tutorial-like (consistent with A8).
1. **Avoid performative jargon.** Words that signal sophistication but do not add precision should be removed. A View should sound exact, not inflated.
1. **Preserve technical accuracy.** Simpler wording must not erase uncertainty, model-dependence, scope limits, or anti-claims. This rule is subordinate to A7: where readability and accuracy conflict, accuracy wins, and the more precise wording is kept.
1. **Audience test.** A reader in the declared primary audience should be able to follow the executive overview without prior knowledge of the Harbour taxonomy. The pilot-reader review (§5) operationalises this test: the pilot reader *is* the audience test, performed by an actual person rather than the drafter's imagination.

**Load-bearing formulation.** If a sentence is only understandable to readers already fluent in the Harbour vocabulary, it must either be rewritten descriptively or moved to a provenance/reference apparatus section.

**Two-register clarification (Guardian).** Q12 governs the body text and externally-facing sections of a View. The reference apparatus (commented bibliography, Toolkit and Figure Provenance, version-pinning appendix) is the permitted home for necessary technical density and version-pinning shorthand; Q4, Q10f, and Q11 deliberately require precision there. The load-bearing formulation routes Harbour-fluent-only content to that apparatus rather than forbidding it outright. The two registers are intentional: the body speaks to the declared primary audience; the apparatus speaks to the steward and the reproducing expert. Q12 does not relax the provenance rules; it confines their register to the apparatus.

-----

## §5 — Structural options for the first View *(first-instance)*

Four candidate structures, organised by reader-engagement model:

### Option A — Sequential narrative

Framework → methodology → exemplar → discussion. Mirrors how the work was actually developed.

*Pros:* Natural narrative arc; clear progression.
*Cons:* Buries the headline finding deep in the document; external readers may not reach it.

### Option B — Layered presentation

Executive summary (~1 page) → readable middle (~5 pages) → reference depth (~10 pages). Allows multiple reading depths.

*Pros:* Respects the reader’s time budget; lowest activation energy for skim-readers.
*Cons:* Layered documents are harder to write coherently; require deliberate redundancy across layers.

### Option C — Use-case driven

Organised by what the reader can do: cite the work, reproduce a result, try a variation, contribute. Each section answers a specific use-case.

*Pros:* Directly addresses the discovery problem of use. Lowest friction from “I am curious” to “I have done something.”
*Cons:* The framework’s conceptual content gets fragmented across use cases.

### Option D — Question-driven

Organised by the open questions the work addresses: “is classical proper time emergent?”, “what does redundancy mean for time?”, “how do we test it?”. Each section addresses one question and shows where the work stands.

*Pros:* Honest about open problems; consistent with anti-claim discipline; engages readers’ existing curiosity.
*Cons:* Risks emphasising open problems over completed work.

### Recommendation for the first View

**Hybrid: Option B layered + Option D question-driven entry.** The executive summary structured along Option D’s question-driven lines; the deeper sections structured along Option A’s sequential narrative. This pattern:

- Engages the external reader’s existing curiosity (Option D’s strength) in the executive summary.
- Allows skim-reading at the executive level (Option B’s strength).
- Preserves narrative coherence at the deeper level (Option A’s strength).
- Defers the use-case-driven framing (Option C) to either a separate Use-Focused View or to README-style ancillary documentation.

### Pilot-reader requirement

**Category-level rule (softened from v0.2 per structural pass).** Before issuance, every externally facing View should receive at least one pilot-reader pass matching its declared primary audience. If the pilot-reader review is omitted, the omission must be noted in the release checklist with explicit justification. This makes pilot-reader review the default discipline while admitting that minor Views or internal-facing Views may warrant exceptions documented at issue.

**First-instance requirement (mandatory for the first View).** The first View’s executive summary must be reviewed by at least one external physicist working at the foundations-metrology interface, outside the steward’s immediate Freiburg-NIST orbit, with feedback incorporated before the tagged release. No omission permitted for the first View.

**Pilot-reader timing and scope-creep interaction (Scout EC-5).** Pilot-reader review occurs after the executive summary and the framework section are drafted but before deeper sections are completed. If pilot-reader feedback identifies a needed section-level change (a missing section, a fundamentally mis-scoped section, an unworkable ordering), this is a recognised trigger for TOC revision rather than a scope-creep violation. TOC revision still requires steward + Guardian sign-off per §10, but pilot-reader feedback is an explicitly admissible reason. Pilot-reader feedback that only affects within-section content does not require TOC revision.

-----

## §6 — Structural cap

### First-View structural cap *(first-instance)*

**Five sections + reference apparatus.** Hard cap for the first View only, to prevent scope creep.

1. **Executive overview** (≤1 page). Question-driven entry; headline finding; the artefact category briefly explained. Concordance paragraph appended if applicable (Q5). Figure: one type (a) schematic orienting the framework.
1. **Framework** (~3 pages). What the Coastline claims and what it does not. The seven anti-claims preserved. Figure: one type (a) schematic of the comparison geometry / framework structure.
1. **Methodology** (~3 pages). The temporal-redundancy functional; what it measures; the einselection caveat preserved. Figure: one type (b) sweet/anti-sweet signal-to-noise figure for the redundancy functional, showing both favourable and noise-dominated operating points (Q10b mandatory).
1. **Worked exemplar** (~3 pages). The toolkit’s Module 3a and 3b results, with the model-conditionality preserved. Figures: one type (c) parameter-space sweep (landscape) situating the type (b) operating points in context, plus an in-text live Colab link (Q10d) opening the pinned notebook for visitor exploration within accessible regimes (Q10e).
1. **Open problems, invitations to engage** (~2 pages). What remains open; how to cite; how to reproduce; how to contact the steward; what kinds of engagement are not yet supported.

**First-View figure plan:** all three figure types used (a in §§1–2, b in §3, c in §4), with one live Colab link in §4. The type (b) figure must show both sweet and anti-sweet spots per Q10b.

**Reference apparatus** (no fixed page limit): **commented bibliography** with anchor, role annotation, and endorsement-scope markers for every external reference (Q11); appendix with version-pinning of all cited artefacts (Coastline v0.4, MN v0.3, CL-2026-006 v0.5, etc.); **Toolkit Provenance subsection** with inherited anti-claims and version pins (Q4); **Figure Provenance subsection** with per-figure type, generating notebook repository URL and commit, environment dependencies, parameter ranges, sweet/anti-sweet labelling, and live-link fallback (Q10f); acknowledgements and COI, kept separate from citations (Leibfried acknowledged; Sanner explicitly not); citation-metadata block.

**First-View notebook residency.** The first View's figure-generating notebooks are toolkit-resident: they live in the toolkit repository and are pinned to the same commit recorded in the Toolkit Provenance subsection (Q4), with the repository URL stated explicitly in Figure Provenance (Q10f). No separate views-resident notebook is introduced for the first View.

**Total expected length:** ~12–15 pages markdown source, rendering to a similar PDF page-count if PDF rendering is later added.

### Category-wide rule on structural caps *(category-level)*

The five-section cap is **not** category-wide. Some future Views may legitimately need a different structure. The category-wide rule is weaker but binding: **every View must declare its own structural cap before drafting prose**, and the cap must appear in the View’s table of contents at the time the TOC is locked. This preserves the discipline of pre-drafting structural lock without forcing future Views into the first View’s shape.

-----

## §7 — Format

**Markdown source**, consistent with the rest of the Harbour. Pages renders to HTML automatically via the existing Jekyll setup. The Zenodo archive includes the markdown via the repository ZIP.

**PDF rendering** is not part of the category definition. It may be part of the publication/discovery layer for externally facing Views (some external physicists prefer downloadable PDFs over Pages-rendered HTML). Defer the PDF-rendering question to a separate decision per View; default to markdown-only at v0.1.

-----

## §8 — Anti-claims for the Harbour View artefact category

What a View is NOT:

- **A1.** Not a peer-reviewed publication.
- **A2.** Not the authoritative version of any framework artefact it presents.
- **A3.** Not a substitute for the underlying Coastline / Ledger / MN / Sail.
- **A4.** Not seeking endorsement beyond Local Stewardship.
- **A5.** Not a freeze of the underlying framework; only a frozen snapshot of one presentation at one time.
- **A6.** Not a venue for new framework claims; sharpening routes through the Coastline first.
- **A7.** Not a promotional document. The View’s purpose is to make the work *findable and citable* by readers who would benefit from it; this is distinct from advocacy. Honest representation of open problems, limitations, and anti-claims is mandatory. **If the View reads more confidently than the underlying artefacts, the View has failed.** This extends to figures: any type (b) signal-to-noise figure must show both sweet and anti-sweet spots (Q10b); a figure displaying only where the method works is an A7 violation.
- **A8.** Not a teaching document in its primary function. Brief explanatory scaffolding — artefact-taxonomy glossary, jargon-on-first-use definitions, one-sentence concept anchors — is permitted within the executive overview, capped at approximately one page. Sustained pedagogical content (worked tutorials, methodological onboarding, conceptual introductions) is not. Readers needing pedagogical onboarding are pointed to underlying tutorials, reviews, or external resources. Interactive notebooks (Q10d) support reproduction and exploration, not pedagogical onboarding; a notebook that teaches the formalism from first principles is a tutorial and belongs outside the View. A View is also not a jargon-gated internal memo: its language must be externally readable according to Q12.

These anti-claims apply to every Harbour View, regardless of vantage-point or scope.

-----

## §9 — Open architectural decisions (registered for steward lock call)

Twelve decisions await explicit steward confirmation at a single lock call. None blocks lockability; O6 carries a recommended lock wording. The **Weight** column flags operational burden: *light* = a naming/format/placement decision settled once; *medium* = a per-View drafting/review discipline; *heavy* = an ongoing maintenance or infrastructure commitment. The steward should note that the heavy decisions (O9, O10, and partly O11) commit to recurring work per View, not a one-time choice.

| O | Item | Layer | Weight | Recommendation | Status |
|---|---|---|---|---|---|
| O1 | Type name | Category | Light | Canonical: “Harbour View”. External subtitle: “Report on [topic]”. | Recommend confirm |
| O2 | Placement | Category | Light | `views/` at repo root, alongside `coastlines/`, `sails/`, `ledger/`, `workplans/`, `numerics/`. | Recommend confirm |
| O3 | Structural cap for first View | First-instance | Light | 5 sections + reference apparatus (hard limit). | Recommend confirm |
| O4 | First View structure | First-instance | Light | Hybrid: Option B layered + Option D question-driven entry. | Recommend confirm |
| O5 | First View scope | First-instance | Light | Framework-overview combining Coastline + MN + toolkit worked exemplar. Other Views deferred. | Recommend confirm |
| O6 | Citation locator | Category | Light | Regime (ii): `{Zenodo version DOI} / {file path within release}`. Manifest-slug locator deferred per §10. | Recommend confirm (lock wording in §4 Q3) |
| O7 | Cap generality | Category | Light | Five-section cap applies to first View only. Category-wide rule: every View declares its own cap at TOC lock. | Recommend confirm |
| O8 | Primary audience for first View | First-instance | Light | Physicists at the foundations-metrology interface. Secondary audiences acknowledged as future-View candidates. | Recommend confirm |
| O9 | Figure taxonomy adoption | Category | Heavy | Three-type menu per Q10a; sweet-AND-anti-sweet mandatory for any operating-point figure under Q10b; static-render-from-pinned-notebook per Q10c; Figure Provenance per Q10f. First View uses all three types. | Recommend confirm |
| O10 | Interactive-notebook integration | Category | Heavy | In-scope as a convenience/discovery layer (Q10d): live Colab links open the pinned commit where possible; pinned static figures are the citable artefact; accessible-regime guardrails per Q10e; environment-pinning per Q10f; link rot is not an erratum. Commits the steward to recurring notebook-pinning, figure-generation, widget-bounding, and best-effort link maintenance per View. | Recommend confirm |
| O11 | External-reference anchoring | Category | Medium | Commented bibliography per Q11: anchor + role annotation + endorsement-scope marker for every external reference; relationship claims to external constraints anchored to a Ledger entry or Coastline section (Q11b). | Recommend confirm |
| O12 | Language boundaries | Category | Light | Add Q12: avoid unexplained abbreviations; prefer descriptive phrasing over internal shorthand; define specialist terms at first use; preserve accuracy (subordinate to A7); require the executive overview to be readable by the declared primary audience without prior Harbour fluency. Load-bearing: a Harbour-fluent-only sentence is rewritten descriptively or moved to the reference apparatus. | Recommend confirm |

Five architectural questions (Q3 snapshot rule; Q5 multiple Views including the collision rule and concordance-paragraph requirement; Q9 supersession discoverability; Q11 external-reference anchoring and commented bibliography, with its load-bearing Q11b relationship-claim rule; Q12 language boundaries, with its load-bearing readability formulation) and the figure/notebook integration (Q10, with its load-bearing Q10b operating-point honesty rule and Q10c immutability rule) carry resolutions in §4 above and warrant explicit steward confirmation at the same call.

-----

## §10 — Out of scope for this note

Decisions deliberately deferred to separate deliberations:

- Discovery campaign sequencing (arXiv-post timing, direct outreach scope, Pages landing-page rewrite).
- Second Zenodo DOI snapshotting framework-plus-toolkit state (a procedural action, separate from the View artefact-category design).
- Public issue tracker workflow (held until external engagement warrants).
- PDF rendering pipeline (deferred per §7).

**Scope change (v0.4, steward-initiated).** Binder/Colab integration for the toolkit example notebooks was out of scope in v0.1–v0.3 ("a separate discovery action"). v0.4 brings it in scope as a convenience/discovery layer under Q10d–Q10f, by explicit steward decision. This is recorded here as a deliberate inclusion so the audit trail distinguishes it from silent scope creep. The notebooks integrated are the existing toolkit example notebooks (already version-pinned under Q4), not a new artefact.

**Registered future improvement — manifest-slug citation locator (Scout EC-1).** The current citation regime (O6, regime (ii)) couples the locator to a file path. If repository reorganisation causes file-path changes that fragment external citations, the category may migrate to a manifest-slug locator: a `views/manifest.json` per release mapping stable slugs (`view:framework-overview`) to file paths within that release. Citation becomes `{version DOI} / view:{slug}`, stable across reorganisations. Migration is backward-compatible in principle: manifests can be added to historical release records as supplementary metadata where permitted. Trigger for migration: first external citation that breaks across a repository reorganisation, or steward judgement that pre-emptive migration is warranted.

**Scope-creep mitigation during drafting.** Once the first View’s TOC is locked, any addition or deletion of a section requires explicit steward + Guardian sign-off before prose drafting resumes. Section-level deliverables fixed at TOC lock; mid-draft scope changes are out of scope by default. Pilot-reader feedback identifying a needed section-level change is a recognised admissible trigger for TOC revision (§5).

-----

## §11 — Guardian recommendations carried forward

From the consolidated deliberation (v0.1 → v0.6 passes), the following recommendation areas apply to every Harbour View. Items 1–9 are distinct recommendations; item 10 is a deliberate "integrity bucket" grouping the smaller release-discipline rules, cited collectively as recommendation 10 rather than individually.

1. **Declare artefact-type explicitly** in the document’s first page (“This document is a Harbour View — neither a peer-reviewed paper nor a Coastline; a presentational vantage-point document under Local Stewardship”).
1. **Declare primary audience explicitly** on the first page; secondary audiences acknowledged but not co-equal.
1. **Lock the table of contents** before drafting prose.
1. **Anti-claims preserved** (the Coastline’s seven anti-claims and the MN’s einselection caveat appear verbatim or with explicit cross-reference; the eight Harbour View anti-claims A1–A8 from §8 apply additionally to the View itself).
1. **Lock-Key discipline for content reuse** (presentational, not authoritative; sharpening routes through the underlying artefact; no new definitions, anti-claims, classifications, or success criteria within a View).
1. **Invitation-to-engage clarity** (cite via the agreed citation locator; reproduce via notebooks; contact steward directly; *not yet* a public-issue-tracker collaboration model).
1. **External-reference discipline** (commented bibliography with anchor, role annotation, and constraint-only / no-parity markers per Q11; relationship claims to external constraints anchored to a Ledger entry or Coastline section per Q11b; citations kept separate from acknowledgements).
1. **Figure honesty** (any figure displaying operating points shows both sweet and anti-sweet regions per Q10b; figures are static renders from a pinned notebook per Q10c; interactive notebooks are a convenience layer over the pinned, citable figures per Q10d).
1. **Language discipline** (avoid unexplained abbreviations; prefer descriptive phrasing over internal shorthand; define specialist terms concisely at first use; remove performative jargon; preserve accuracy over simplicity where they conflict; test the executive overview against the declared primary audience per Q12, with the pilot reader as the operational test).
1. **Release-discipline integrity bucket** (single document, single citation locator, single Pages entry per View; acknowledgements and COI kept separate from citations, with Leibfried acknowledged and Sanner explicitly not, per the 2026-05-26 correction; mandatory pilot reader for the first View, recommended-default for subsequent Views with documented omission justification; reissue-only erratum policy; supersession discoverability per Q9).

-----

## §12 — Next concrete moves

1. Steward review of this v0.6 lock candidate.
1. Single lock call: confirm O1–O12 and Q3 / Q5 / Q9 / Q10 / Q11 / Q12 resolutions. With confirmation, v0.6 becomes the locked category specification.
1. Draft the first View’s table of contents (Section 1 → Section 5, with section-level deliverables and the figure plan from §6) as a separate document, observing the structural cap declared at TOC lock.
1. Steward review of the table of contents before any prose is drafted.
1. Pre-issuance technical check (Scout EC-5): verify the Jekyll/Pages configuration supports versioned subpaths (Q9b); apply a one-time configuration update if required before the first View is released.
1. Pin the figure-generating notebook(s) at a fixed commit; record the repository URL and environment dependencies (Q10f); generate the static figures (type a schematics, type b sweet/anti-sweet S:N, type c parameter sweep); verify every operating-point figure shows both sweet and anti-sweet regions (Q10b); set the Colab live links to open the pinned commit where possible and bound the widgets to accessible regimes (Q10d–Q10e).
1. Assemble the commented bibliography (Q11): anchor and role-annotate every external reference; mark external-constraint citations constraint-only / no-parity; anchor any relationship claim to a Ledger entry or Coastline section (Q11b).
1. Executive-summary and Framework-section prose drafting.
1. Pilot-reader review of the executive summary and Framework section (per §5; one external physicist at the foundations-metrology interface, outside the immediate Freiburg-NIST orbit). TOC revision admissible if pilot-reader feedback identifies a section-level need.
1. Remaining-section prose drafting.
1. Two-pass review (steward + Guardian) before issuance, including a figure-honesty check against A7 / Q10b, a bibliography audit against Q11, and a language/readability audit against Q12 (executive overview readable by the declared primary audience without prior Harbour fluency; no Harbour-fluent-only sentences left in the body text).
1. Tagged release; citation locator per O6 regime (ii); Pages canonical URL surfaced; commented bibliography, Toolkit Provenance, and Figure Provenance subsections populated; concordance paragraph included if applicable; live Colab links verified against the pinned commit.

-----

## §13 — Version history

- **v0.1** (2026-05-27): Initial deliberation note. Purpose, gap analysis identifying the Harbour artefact-category gap, proposed name (Harbour View / Report), eight architectural questions Q1–Q8 (six resolved-as-proposed, two recommended-but-explicit-confirmation-warranted), four structural options with recommendation for the first View (Option B + D hybrid), structural cap (5 sections + apparatus), format proposal (markdown source, PDF deferred), seven Harbour View anti-claims, seven Guardian recommendations carried forward, six open decisions registered, out-of-scope items declared, next concrete moves enumerated.

- **v0.2** (2026-05-27): Eleven patches folded in from the consolidated Guardian + structural deliberation. §1 two-layer structure declared explicitly. §2 minimal entry condition added. §3 canonical name lock with external subtitle convention. §4 Q1 strengthened prohibition. §4 Q2 audience scoping with first-instance recommendation (O8). §4 Q3 DOI regime articulated as three options with recommendation (ii). §4 Q5 explicit risks paragraph and mitigations; load-bearing collision rule registered. §4 Q8 erratum clause added. §5 pilot-reader requirement as category-level rule applied to first instance. §6 cap explicitly first-instance-only; category-wide rule added. §8 A5 reworded, A7 sharpened, A8 added. §9 open decisions table extended to O1–O8 with O6 elevated to lockability blocker. §10 scope-creep mitigation paragraph added. §11 recommendation list extended from seven to eight. §12 pilot-reader review inserted before steward+Guardian review.

- **v0.3** (2026-05-27): Lock candidate. Patches folded in from the Scout pass (six error-correction items, three Horizon Signals) and the structural-pass approval (two minor edits and O6 lock wording). §1 status changed to lock candidate. §3 section heading simplified (“Name” not “Proposed name”). §4 Q3 O6 elevated from “blocks lockability” to “recommend confirm with lock wording”; final lock wording added in blockquote; rejected regimes (i) and (iii) made explicit. §4 Q4 Toolkit Provenance placement rule added (Scout EC-6). §4 Q5 concordance-paragraph requirement added to mitigations (Scout EC-4); risks-paragraph references updated to “citation locator” throughout. §4 added Q9 superseded View discoverability (Scout EC-2): archive immutability, Pages canonicality, supersession changelog. §5 pilot-reader requirement softened to category-level default with first-View mandatory carve-out (structural pass); pilot-reader timing and scope-creep interaction clarified as admissible TOC-revision trigger (Scout EC-5). §6 Toolkit Provenance subsection added to reference apparatus structure; concordance paragraph noted in executive overview. §8 A8 reworded with page-budget clarification: “Not a teaching document in its primary function; brief explanatory scaffolding capped at ~1 page within the executive overview” (structural pass + Scout EC-3). §9 open decisions table: O6 status changed from “Refine before lock — blocks lockability” to “Recommend confirm (lock wording in §4 Q3)”; Q9 added to confirmation items. §10 manifest-slug locator registered as future improvement (Scout EC-1) with explicit migration trigger; pilot-reader-feedback-as-admissible-TOC-trigger noted. §11 item 6: “handle” → “locator” (structural pass minor edit 1); item 8 updated to reflect softened pilot-reader requirement and Q9 supersession discoverability. §12 next moves updated: lock call covers Q9; pilot-reader review timing clarified.

  Horizon-clear items preserved from Scout pass without modification: two-layer structure, minimal entry condition, strengthened prohibition (Q1), collision rule (Q5), five-section cap discipline, anti-claim set overall, Endorsement Marker scope.

- **v0.4** (2026-05-27): Lock candidate. Steward-initiated figure/notebook expansion folded in via a Guardian ADM-EC pass. §1 two-layer structure extended to list figure-taxonomy and interactive-notebook rules as category-level. §4 added Q10 (figure taxonomy and interactive-notebook integration): Q10a three-type menu (schematic / sweet-anti-sweet signal-to-noise / parameter-space sweep); Q10b load-bearing sweet-AND-anti-sweet rule enforcing A7 at the visual layer; Q10c load-bearing static-render-from-pinned-notebook rule preserving snapshot immutability; Q10d live-notebook link as convenience layer with pinned-commit opening and documented fallback; Q10e accessible-parameter-regime guardrails; Q10f Figure Provenance reference-apparatus requirement; A8 boundary clarification distinguishing reproduction/exploration from pedagogical onboarding. §6 first-View figure plan added (all three types; type b in Methodology, type c plus live Colab link in Worked Exemplar); Figure Provenance subsection added to reference apparatus. §8 A7 extended with the type (b) figure-honesty rule cross-referenced to Q10b; A8 extended with the notebook reproduction-vs-teaching boundary. §9 open decisions table extended to O1–O10 (O9 figure taxonomy adoption; O10 interactive-notebook integration); confirmation items extended to Q10. §10 Binder/Colab integration moved from out-of-scope to in-scope under an explicit steward-initiated scope-change marker; manifest-slug locator remains the sole registered future improvement. §12 next moves: notebook-pinning and figure-generation step inserted before prose drafting; figure-honesty check added to the two-pass review; live-link verification added to issuance.

  Load-bearing additions for steward attention: Q10b (sweet-AND-anti-sweet mandatory; only-sweet is an A7 violation) and Q10c (figures are static renders from a pinned notebook; the live link is never the citable artefact). These two rules together resolve the immutability tension that a naive live-notebook dependency would otherwise introduce.

- **v0.5** (2026-05-27): Lock candidate. External-reference anchoring added in response to a steward query, plus the Scout, structural, and Architect passes of v0.4 folded in. §1 two-layer structure extended to list external-reference-anchoring as category-level. §4 added Q11 (external-reference anchoring and commented bibliography): Q11a commented-bibliography requirement (anchor + role annotation from a controlled vocabulary + endorsement-scope marker for external constraints); Q11b load-bearing relationship-claim anchoring tying any assertion about the framework's relationship to an external constraint to a Ledger entry or Coastline section (Q1 / A7 enforcement); Q11c acknowledgement-vs-citation separation. §4 Q10a clarified that a View need not contain figures (structural pass). §4 Q10b enforcement gap closed (Scout EC-1): the sweet-AND-anti-sweet obligation now attaches to any figure displaying operating points, binding type (c) sweeps, not only type (b). §4 Q10d live-link wording softened to "where technically possible" (structural pass). §4 Q10f extended with generating-notebook repository URL, toolkit-vs-views residency, and environment-dependency pinning / requirements.txt (Scout EC-2, Architect). §4 Q5 concordance paragraph marked exempt from the executive-overview page cap (Scout EC-3). §4 Q9b Jekyll versioned-subpath implementation caveat added with pre-issuance check (Scout EC-5). §6 commented bibliography added to reference apparatus; first-View notebook residency specified as toolkit-resident. §9 open decisions table gains a Weight column (light/medium/heavy) flagging O9/O10 as recurring maintenance commitments (Scout EC-6); O11 external-reference anchoring added; confirmation items extended to Q11. §10 manifest-slug "one-way-easy" wording replaced with "backward-compatible in principle" (structural pass); stale v0.3 reference corrected. §11 intro reframed from "eight recommendations" to "recommendation areas" with item 9 marked an integrity bucket (Scout EC-4); external-reference discipline and figure honesty split into distinct recommendations. §12 the §12-item-1 "v0.3" → "v0.5" textual error corrected (structural pass); Jekyll pre-issuance check and commented-bibliography assembly steps added; lock-call coverage extended to O1–O11 and Q11; bibliography audit added to the two-pass review.

  Load-bearing addition for steward attention: Q11b (any relationship claim to an external constraint must be anchored to a Ledger entry or Coastline section; an unanchored relationship claim is an A7 violation). This closes the asymmetry whereby internal and computational sources were rigorously pinned while external references were not, and prevents the View from implying parity with externally-validated physics (A4) through loose citation.

  Horizon-clear items preserved from the Scout v0.4 pass without modification: two-layer structure, minimal entry condition, strengthened prohibition (Q1), collision rule (Q5), five-section cap discipline, anti-claim set overall, Endorsement Marker scope, supersession discoverability (Q9), concordance paragraph requirement, Toolkit Provenance placement, pilot-reader timing discipline, manifest-slug future improvement, Q10b and Q10c load-bearing rules.

- **v0.6** (2026-05-27): Lock candidate. Language boundaries and readability discipline added by explicit steward decision. §1 two-layer structure extended to list language-boundary rules as category-level. §4 added Q12 (language boundaries and readability discipline): seven rules (avoid unexplained abbreviations; prefer descriptive phrases over internal labels; short declarative sentences; define specialist terms concisely at first use; avoid performative jargon; preserve technical accuracy, made explicitly subordinate to A7 by Guardian; audience test cross-linked to the §5 pilot reader); the load-bearing formulation preserved verbatim (a Harbour-fluent-only sentence is rewritten descriptively or moved to the reference apparatus); a Guardian two-register clarification distinguishing the externally-readable body from the technically-dense reference apparatus, so Q12 does not read as in tension with the Q4 / Q10f / Q11 provenance rules. §8 A8 extended: "A View is also not a jargon-gated internal memo; its language must be externally readable according to Q12." §9 open decisions table gains O12 (language boundaries, Light weight); Weight-column legend extended with a "medium" tier; intro count updated to twelve; confirmation items extended to Q12. §11 intro recount (items 1–9 distinct, item 10 the integrity bucket); a distinct Language-discipline recommendation inserted. §12 lock-call coverage extended to O1–O12 and Q12; a language/readability audit added to the two-pass review.

  Load-bearing addition for steward attention: Q12's readability formulation (a sentence understandable only to Harbour-fluent readers must be rewritten descriptively or moved to the reference apparatus). Together with the two-register clarification, this holds the View to its externally-readable purpose without weakening the provenance rules, which retain their technical density in the apparatus. Guardian note: Q12 rule 6 is subordinate to A7 — where readability and accuracy conflict, accuracy wins.

-----

*End of Harbour View — Structural Deliberation Note v0.6 (lock candidate).*
