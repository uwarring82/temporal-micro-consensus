# Task Card — Draft the First Harbour View

**Card ID:** HV-DRAFT-001
**Companion to:** *Harbour View — Structural Deliberation Note v0.6* (the locked spec; this card does not restate it, it points to it).
**Assignee:** [drafter]   **Steward / reviewer:** U. Warring (Guardian stance held by steward).

---

## Objective

Draft the **first Harbour View**: one externally-readable, citable presentation of the Temporal Micro Consensus work — framework + methodology + one worked exemplar. It is a *window onto* the work, not a new piece of it.

## You are given

- **The spec (v0.6).** Your rulebook. Read first: §6 (structure + figure plan), §8 (anti-claims), and rules Q10b, Q11b, Q12.
- **The sources to present, at pinned versions:** Coastline v0.4, MN v0.3, Ledger CL-2026-006 v0.5, toolkit Module 3a + 3b results (pinned commit, from the steward).

## Deliverable

One markdown file `view-framework-overview-v0.1.md` — five sections + reference apparatus (spec §6):

1. **Executive overview** (≤1 p) — question-driven entry; headline finding; one sentence on what this document is; one schematic figure.
2. **Framework** (~3 p) — what the Coastline claims and what it does *not*; seven anti-claims preserved; one schematic figure.
3. **Methodology** (~3 p) — the temporal-redundancy functional; einselection caveat preserved; one signal-to-noise figure showing **both** favourable and noise-dominated regions.
4. **Worked exemplar** (~3 p) — Module 3a + 3b results; model-conditionality preserved; one parameter-sweep figure + one live Colab link to the pinned notebook.
5. **Open problems + invitations** (~2 p) — what is open; how to cite, reproduce, and contact the steward.

**Reference apparatus:** commented bibliography (anchor + role + constraint-only marker, Q11); version-pinning appendix; Toolkit Provenance; Figure Provenance; acknowledgements & COI (separate from citations — Leibfried acknowledged, Sanner not).

## Five hard rules (a violation blocks acceptance)

1. **No new claims.** Present only what the pinned artefacts already say. If drafting surfaces a needed new definition, caveat, or claim — stop and route it to the steward; do not write it into the View. *(Q1)*
2. **Every operating-point figure shows both the sweet and the anti-sweet region.** A figure that shows only where the method works is rejected. *(Q10b / A7)*
3. **Every "consistent with X" claim about external physics cites a Ledger entry or Coastline section.** No anchor → delete the sentence. *(Q11b)*
4. **Externally readable.** Define each specialist term on first use; keep Harbour-only shorthand out of the body text (it belongs in the apparatus). The executive overview must be followable by a foundations-metrology physicist with no Harbour background. *(Q12)*
5. **If any sentence reads more confidently than the source artefact it presents, it is wrong.** *(A7)*

## Done when

- Five sections within their page caps; apparatus complete (all four provenance/bibliography blocks populated).
- One external foundations-metrology physicist, outside the Freiburg–NIST orbit, has read the executive overview and framework section; feedback incorporated.
- Steward + Guardian two-pass review clean (figure-honesty, bibliography, readability checks).

## Do not

- Edit any Coastline / Ledger / MN / Sail. This is presentation, not framework work.
- Add or drop a section without steward + Guardian sign-off.
- Teach the formalism from first principles — it is not a tutorial *(A8)*.
- Try to improve the spec. It is locked. Spec questions go to the steward, not into the draft.

## First move

Draft the **table of contents + a bullet outline per section** (with the §6 figure plan) and return it to the steward for sign-off **before writing any prose.**

---

*One card, one View. Build it; refine from contact with the task, not from re-reading the spec.*
