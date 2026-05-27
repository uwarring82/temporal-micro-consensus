# Project Logbook

*A chronological, append-only record of substantive activities, decisions, and corrections in the Temporal Micro Consensus repository. It exists for **provenance and reproducibility** (the "R" of FAIR): each entry says what was done, when, by whom, why, and which artefacts/commits resulted.*

| Field | Value |
| --- | --- |
| Purpose | Provenance / audit trail (FAIR-Reusable) |
| Convention | **Append-only.** Entries are added chronologically (oldest first); existing entries are not rewritten. Corrections are logged as new entries that reference the earlier one. |
| Actors | **Steward** = U. Warring (decisions, authorship). **Agent** = Claude Code (execution under steward direction). |
| Scope | Decisions, version issuances, phase transitions, factual corrections. Routine edits are captured by the Git history, not duplicated here. |

---

## 2026-05-23 — Repository origin

- **Actor:** Steward. **Commit:** `c18af36` (Initial repository scaffold).
- Repository scaffolded under Local Stewardship: Coastline *Consensus-Emergence of Classical Proper Time* (v0.1 → v0.2), Ledger CL-2026-006 (v0.1 → v0.2), Sail *Visibility, the Right Witness* (v0.1 → v0.2), roadmap v0.1, split licensing (MIT / CC-BY-SA-4.0 / CC-BY-NC-SA-4.0).

## 2026-05-26 — Public remote established

- **Actor:** Steward (executed via Agent assistance). 
- Public GitHub remote created at `github.com/uwarring82/temporal-micro-consensus` and `main` pushed. Resolved the roadmap's "public visibility of repository" stewardship decision.

## 2026-05-26 — Literature review opened (plan v0.2, Phase 0)

- **Actor:** Steward (decisions) / Agent (drafting). **Commits:** `2030399`, `bc5ddce`.
- Established [`literature-review-plan.md`](literature-review-plan.md) (v0.2 after a Guardian-stance review): comprehensive broad-sweep field map, seven clusters, five phases, Tier-1 scope cap, CCUF-bridge lock, source-handling policy (PDFs local-only, git-ignored). Phase 0 scaffolding under [`literature/`](literature/) landed in a second commit for an auditable boundary.

## 2026-05-26 — Phase 1: corpus verified

- **Actor:** Agent (under steward direction). **Commit:** `d059320`.
- All corpus entries verified against Crossref / arXiv / ADS / publisher; `VERIFY` flags cleared; placeholders resolved (incl. `sorci2026`, `hartong2024`, `covey2025`, `fromonteil2025`, `fit2026`). Lineage flags recorded for later audit.

## 2026-05-26 — Phase 1/2: sources acquired, extraction notes

- **Actor:** Steward (PDF acquisition) / Agent (extraction). **Commits:** `932e6ea`, `78d3653`.
- 29 PDFs acquired into local-only `sources/`, renamed to citekeys; one findings note per paper (own-words summaries — copyright). `zych2019` added as the composite-system-action source behind `sorci2026`.

## 2026-05-26 — Phase 2: Tier-1 fixed at 13, full annotation

- **Actor:** Steward (down-tiering call) / Agent (annotation). **Commit:** `53127f5`.
- Tier 1 reduced 18 → 13; six papers down-tiered with rationale. The 13 Tier-1 notes upgraded to the full per-claim Phase-2 template. Structural-finding evaluation recorded (`hartong2024`: no v0.3 *plan* revision required; artefact-level fix logged).

## 2026-05-26 — Phase 3: synthesis

- **Actor:** Agent (under steward direction). **Commit:** `d6f00c3`.
- [`literature/synthesis-v0.1.md`](literature/synthesis-v0.1.md) committed: claim-by-claim, measure-by-measure, gaps/falsifications, lineage audit. **Headline finding:** the configurational→temporal transplant (Claim II redundancy) has no temporal exemplar in the corpus.

## 2026-05-26 — Coastline v0.3 issued

- **Actor:** Steward (explicit go) / Agent (drafting). **Commit:** `a2d037f`.
- [`coastlines/consensus-emergence-v0.3.md`](../coastlines/consensus-emergence-v0.3.md) issued (v0.2 frozen). Lineage fixes (Hartong removed, Mendes 2018→2019, Ollivier–Poulin–Zurek precursor added); transplant gap registered (Claim II paragraph, Anti-Claim #6, Deferred priority); "multipartite ≠ redundant" added; Claim III softened. FIT / GR-boundary / measure-registration deferred.

## 2026-05-26 — FAIR principles adopted; logbook established

- **Actor:** Steward (direction) / Agent (execution). **Commit:** *(this change).*
- Adopted FAIR principles (see [README §FAIR](../README.md)): added machine-readable citation metadata ([`CITATION.cff`](../CITATION.cff)) and established this logbook. Next step toward full *Findability* is a tagged release minted to a Zenodo DOI (requires steward action: connect Zenodo to the GitHub repo, then publish a release; optionally add the steward's ORCID to `CITATION.cff`).

## 2026-05-26 — Correction: no steward relationship with C. Sanner

- **Actor:** Steward (factual correction). **Commit:** *(this change).*
- The steward reports having **never met or directly interacted with C. Sanner**. This corrects an earlier inference (logged 2026-05-26, Phase 3) that treated both Leibfried and Sanner as "close contacts" of the steward.
- **Effect:** The Sail's Acknowledgements (`sails/sorci-commentary-v0.2.md`) state "ongoing exchanges" with C. Sanner — this is **factually inaccurate** and is flagged for correction. The genuine prior association is with **D. Leibfried** (discussions at NIST Boulder, 2010–2012). Both Leibfried and Sanner are co-authors of the subject paper (Sorci et al.); the independence-of-commentary consideration for any external circulation therefore concerns the steward's prior association with **Leibfried** alone.
- **Propagated:** `literature/synthesis-v0.1.md` §4 and `roadmap.md` (external-circulation item) corrected. **Pending:** the Sail acknowledgement itself awaits the steward's decision on correction (remove the Sanner clause / reformulate / handle in the Phase-4 Sail pass).

## 2026-05-26 — Sail v0.3 issued (Sanner acknowledgement removed)

- **Actor:** Steward (decision: minimal factual correction) / Agent (drafting). **Commit:** *(this change).*
- Resolves the "Pending" item in the entry above. [`sails/sorci-commentary-v0.3.md`](../sails/sorci-commentary-v0.3.md) issued (v0.2 frozen); the only changes versus v0.2 are the metadata block, the removal of the C. Sanner acknowledgement clause (the steward has no relationship with Sanner), and the version-history row. The D. Leibfried acknowledgement is retained.
- **Deliberately *not* changed:** anchoring remains Coastline **v0.2** / Ledger CL-2026-006 v0.2 (re-anchoring to Coastline v0.3 is a substantive change), and the broader acknowledgement decision (retain / reformulate / remove) remains open — both deferred to the Phase-4 Sail pass.

## 2026-05-26 — Phase 4 step 1: Ledger CL-2026-007 opened

- **Actor:** Steward (direction: "go step by step" through Phase 4) / Agent (drafting). **Commit:** *(this change).*
- [`ledger/CL-2026-007-smith-ahmadi-v0.1.md`](../ledger/CL-2026-007-smith-ahmadi-v0.1.md) issued (v0.1), classifying Smith & Ahmadi (2020) **UNDERDETERMINED** against **Coastline v0.3**. Declared measure: Fisher information F[τ] (deliberately distinct from CL-2026-006's mutual information, road-testing measure pluralism). Crux/discriminant: whether the quantum time-dilation correction is coherence-dependent (superposition ≠ classical mixture) — the coherence-sensitive test it lacks is what the Sorci visibility witness (CL-2026-006) provides.
- Roadmap "possible future Ledger entries" updated (CL-2026-007 → opened); README Ledger mention + structure tree updated. **Next steps (Phase 4):** CL-2026-008 (distributed networks); Sail re-anchor to v0.3; methodological notes.

## 2026-05-26 — CL-2026-007 corrected to v0.2 (Verifier catch)

- **Actor:** Verifier review (catch) / Steward (decision) / Agent (correction + source re-read). **Commit:** *(this change).*
- A Verifier-stance review flagged that CL-2026-007 v0.1's central rationale was **physically wrong**: v0.1 claimed Smith & Ahmadi do not settle whether the quantum time-dilation correction is coherence-dependent. Re-reading the source PDF (Eqs. 22–25, Figs. 1–2) confirmed the Verifier: `γ_C⁻¹` (Eq. 24) is explicitly the classical *statistical-mixture* value and `γ_Q⁻¹` (Eq. 25) is the *coherence-dependent* quantum term that vanishes for a mixture (θ ∈ {0,π/2} or p̄_A = p̄'_A). The theoretical superposition-vs-mixture distinction is therefore established by the paper; v0.1 had the compressibility backwards.
- **Correction:** [`ledger/CL-2026-007-smith-ahmadi-v0.2.md`](../ledger/CL-2026-007-smith-ahmadi-v0.2.md) issued (v0.1 frozen). Classification unchanged (UNDERDETERMINED) but the crux is **relocated** from the theoretical level to the **experimental-witness** level (isolating γ_Q⁻¹ from preparation/dephasing/verification nuisances) — the same location as CL-2026-006. Discriminant conditions rewritten as experimental nuisance-isolation tests; the "Fisher stable across anchors" overclaim was withdrawn (Fisher retained only as the registered resolution anchor, with a caveat that the coherence content lives in the cross-probe γ_Q⁻¹).
- **Lesson logged:** classify framework-relative claims only after reading the source's defining equations, not from the abstract-level note alone. README "most recent Ledger entry" line and the roadmap crux description corrected.

## 2026-05-26 — Design note captured: resolution anchor vs classification anchor

- **Actor:** Verifier review (insight) / Agent (capture). **Commit:** *(this change).*
- Forward-looking refinement for the deferred Claim IV **measure-registration protocol** (roadmap): distinguish a *resolution anchor* (bounds what must be resolved — e.g. Fisher F[τ]) from a *classification anchor* (carries the structural content classified — e.g. cross-probe γ_Q⁻¹ or mutual information). Conflating them was the CL-2026-007 v0.1 failure mode. Recorded in the roadmap's measure-registration item so it informs the protocol when written; no Coastline change made now.

## 2026-05-26 — Phase 4 step 2: Ledger CL-2026-008 opened (clock networks)

- **Actor:** Steward (direction + guardrails) / Agent (source reads + drafting). **Commit:** *(this change).*
- Per the steward's guardrails, read the defining equations in *both* PDFs first (Covey Eqs. 2–11 incl. Δω Eq. 10; Fromonteil Eqs. 1–7 incl. the redshift Hamiltonian and τ_dec) before drafting. [`ledger/CL-2026-008-clock-networks-v0.1.md`](../ledger/CL-2026-008-clock-networks-v0.1.md) issued (v0.1), classifying the **class** of distributed entanglement-enhanced clock-network proposals (Covey 2025; Fromonteil 2025) **UNDERDETERMINED** against Coastline v0.3.
- **Framing decision (per guardrail):** class claim, not single-paper — the two diverge (Covey: curvature via 3-node W; Fromonteil: redshift/decoherence via N-atom ensembles) while sharing the entanglement-enhanced/anti-redundant structure.
- **Firsts:** classification anchor = cross-probe mismatch (Δω), resolution anchor = QFI/coherence budget (the resolution/classification distinction applied); first exercise of v0.3 "multipartite ≠ redundant" (anti-redundancy noted but **not** held against C2, which does not claim redundancy — per guardrail); first entry to show the **GR-boundary item is load-bearing** (D1), feeding back to the roadmap (item elevated to a prerequisite).
- **Next steps (Phase 4):** Sail re-anchor to Coastline v0.3; methodological notes (temporal-redundancy toy functional; nuisance-discrimination kit). The GR-boundary statement is now a candidate next Coastline action in its own right.
- **Rev. 2026-05-26 (Verifier wording fix):** CL-2026-008 v0.1 corrected *in place* (current/unsuperseded version; wording-only, no load-bearing change). The GR-boundary subsection said Covey's curvature residual is "beyond the Newtonian/weak-field regime" — physically imprecise: Δω is a higher-order *post-Newtonian* term but still **weak-field**. Corrected to "outside the Coastline's written SR/inertial-worldline scope," matching the roadmap. Recorded in the entry's version-history row.

## 2026-05-26 — Phase 4 step 3: Coastline v0.4 (GR-regime boundary)

- **Actor:** Steward (decision: "follow your suggestion" — take the GR boundary before the Sail re-anchor) / Agent (drafting). **Commit:** *(this change).*
- [`coastlines/consensus-emergence-v0.4.md`](../coastlines/consensus-emergence-v0.4.md) issued (v0.3 frozen). Writes the GR-regime boundary statement that CL-2026-008 D1 made load-bearing.
- **Design decision — extend, not bound.** The framework's scope is *extended* to the SR-and-weak-field (post-Newtonian) regime rather than capped at SR, because its own machinery already accommodates it: a spacetime-curvature signal is a Claim IV cross-probe mismatch / Claim II.3 incompressible residual (as CL-2026-008 showed via Covey's Δω). Strong-field and quantum-gravity remain out of scope (Anti-Claim #7).
- **Changes (diff vs v0.3 = exactly these):** External Constraints item 5 (GR, weak-field/post-Newtonian); new *Regime of Validity* section (scope; comparison-protocol proviso; curvature-as-incompressible-residual; exclusions); Anti-Claim #7; a curvature clause on the Claim IV cross-probe anchor; a Deferred strong-field-extension item; version self-references v0.3→v0.4. No claim retired; Load-Bearing Sentence unchanged.
- **Consequence:** satisfies the *framework-side* condition of CL-2026-008 D1 (its experimental D2 still stands); CL-2026-008 may now be re-evaluated against v0.4 — flagged, not done.
- **Next steps (Phase 4):** Sail re-anchor to Coastline v0.4 (now cleaner — the Sail §2 non-inertial-regime paragraph is what the Regime-of-Validity section makes rigorous); methodological notes. Optionally, re-anchor/re-evaluate CL-2026-008 against v0.4.

## 2026-05-26 — Phase 4 step 4: Sail re-anchored to Coastline v0.4

- **Actor:** Steward (decision + scope) / Agent (drafting). **Commit:** *(this change).*
- [`sails/sorci-commentary-v0.4.md`](../sails/sorci-commentary-v0.4.md) issued (v0.3 frozen). Re-anchored the **Coastline** reference v0.2 → **v0.4**; diff vs v0.3 is metadata, three §2 paragraphs, the two Anchoring-Frameworks bullets, and the version-history row only — **no change to the scientific argument**.
- §2 aligned to v0.4: the Claim II triad now flags *many vs redundant* (the two-carrier protocol minimally engages but does not *satisfy* redundancy) and the *transplant gap* (so the reading is a structural alignment, not a satisfied-criterion claim); the distributed-network paragraph notes such entanglement-enhanced networks are *multipartite but anti-redundant* (Claim V; CL-2026-008); the accelerated-worldline caveat rewritten on v0.4's *Regime of Validity* (Anti-Claim #7 for the strong-field exclusion).
- **Ledger anchor kept at CL-2026-006 v0.2** (per scope), with a mixed-anchor note: the v0.2→v0.4 Coastline changes are refinements consistent with the Ledger's UNDERDETERMINED verdict; CL-2026-006's own re-anchor is a separate pending step.
- **Bookkeeping (per steward note):** stale roadmap headings normalised — "Coastline v0.3 — issued" → "Coastline — issued revisions & remaining candidates"; "Sail v0.3 candidates" → "Sail — pending decisions & candidates" (+ fixed the cross-reference). README current-Sail pointer/tree → v0.4.
- **Remaining Phase 4:** methodological notes (temporal-redundancy toy functional; nuisance-discrimination kit). Pending separate steps: re-anchor CL-2026-006 → v0.4; re-evaluate CL-2026-008 against v0.4.

## 2026-05-26 — Version-consistency loop: CL-2026-006 v0.3, CL-2026-008 v0.2

- **Actor:** Steward (direction: "the cheap consistency loop") / Agent (drafting). **Commit:** *(this change).*
- Also fixed a bookkeeping miss the steward caught: README item 3 still described the Sail as anchored to Coastline v0.2 — corrected to v0.4 (mixed anchor).
- **CL-2026-006 → v0.3** (v0.2 frozen): re-anchored Coastline v0.2 → v0.4. **No verdict or discriminant change** — UNDERDETERMINED, I(C : M), D1–D3/D−1 all stand. The v0.2→v0.4 changes are refinements the entry already anticipated ("two carriers, not many"); added a note that the trapped-ion setting falls within v0.4's *Regime of Validity*.
- **CL-2026-008 → v0.2** (v0.1 frozen): re-anchored v0.3 → v0.4 **and re-evaluated**. Coastline v0.4 wrote the GR boundary that v0.1's **D1** demanded, so the **framework-side gap is closed** (D1 ✓ satisfied); classification **stays UNDERDETERMINED**, now resting on **D2** (experimental discriminability) alone. Verdict, Classification, D1, and the roadmap-feedback note rewritten; the CL-006/007/008 set now all sit at the experimental-witness level.
- **Mixed-anchor residue (flagged, not actioned):** Sail v0.4 still cites CL-2026-006 as v0.2 — valid (no verdict/discriminant change), and a pointer bump to v0.3 can ride the next Sail revision rather than forcing a Sail v0.5 now.
- **PAUSE here** (per steward): the next item — the temporal-redundancy toy functional — is research work, not bookkeeping. Holding before it.

## 2026-05-26 — Cleanup: CL-2026-007 v0.3 re-anchor + roadmap normalisation

- **Actor:** Verifier review (catch) / Agent (cleanup). **Commit:** *(this change).*
- Verifier caught that the "all three entries anchored to v0.4" claim was not literally true — **CL-2026-007 was still on Coastline v0.3**. Re-anchored: **CL-2026-007 → v0.3** ([entry](../ledger/CL-2026-007-smith-ahmadi-v0.3.md); v0.2 frozen), a pure re-anchor to Coastline v0.4 with **no verdict/discriminant change** (v0.4's only addition over v0.3 — the GR boundary — is irrelevant to this bipartite SR/weak-field case). All three Ledger entries are now literally anchored to Coastline v0.4.
- Normalised the stale roadmap **active** section: "Possible future Ledger entries" → "Ledger entries opened from candidates", with both bullets refreshed to current versions (007 v0.3, 008 v0.2) and current verdicts. README ledger tree → CL-2026-007 v0.3 (current).
- **PAUSE holds:** next is the temporal-redundancy toy functional (research). Nothing further actioned.

## 2026-05-26 — Tutorial drafted and integrated

- **Actor:** Steward (review) / Agent (drafting + integration). **Commit:** *(this change).*
- [`docs/tutorial.md`](tutorial.md) v0.1 issued — a guided on-ramp covering Harbour architecture, the five Claims, Ledger system, literature-review methodology, synthesis headline, regime of validity, reading order, open problems, and key distinctions. Reviewed by the steward: praised as "genuinely strong," "accurate and version-current," with five identified issues (three substantive, two integration). Issues #1–#3 fixed in place (007 anchor framing softened; Sail mixed-anchor nuance added; mutual-information notation I(S:F) → I(C:M)). Issue #4 resolved: README structure tree updated (tutorial added, docs/ licence clarified as CC BY-SA 4.0), README reading order updated (tutorial as step 0), tutorial metadata licence field set to CC BY-SA 4.0. Issue #5 acknowledged (tutorial-level glosses not in Coastline) — no change required.
- **Status:** tutorial committed and tracked. Next research step remains the temporal-redundancy toy functional (research, not bookkeeping).

## 2026-05-26 — Public website: GitHub Pages

- **Actor:** Steward (direction) / Agent (setup). **Commit:** *(this change).*
- Stood up a dedicated GitHub Pages site presenting the **most recent version** of each artefact. Added `_config.yml` (Jekyll, `jekyll-theme-cayman`, served from `main` root) and a curated landing page [`index.md`](../index.md) linking to the current Coastline (v0.4), Sail (v0.4), Ledger entries (006 v0.3 / 007 v0.3 / 008 v0.2), tutorial, and synthesis. Verified beforehand that no tracked `.md` contained Liquid template delimiters (double-brace variable tags or brace-percent block tags), so the whole-repo Jekyll build is safe. `.gitignore` updated for local Jekyll build artefacts.
- **Outward-facing publish step:** enabling Pages is a *Create Public Surface* action (like the original public-repo creation). If the Pages API call is permission-gated, the site files are nonetheless committed and the steward can enable it in **Settings → Pages → Deploy from a branch → `main` / `(root)`**. Expected URL: `https://uwarring82.github.io/temporal-micro-consensus/`.

## 2026-05-26 — Pages build fix (self-inflicted Liquid error)

- **Actor:** Steward (report: "error building") / Agent (diagnosis + fix). **Commit:** *(this change).*
- The first Pages build (commit `3da95dc`) **failed**. Root cause, from the build log: a Liquid syntax error in `docs/logbook.md` — the entry above, while *describing* the pre-build safety check, included a literal pair of Liquid variable delimiters in its prose, and Jekyll tried to parse them as a template variable. The pre-check itself had been truthful: it ran before that sentence was written.
- **Fix:** (1) reworded that line to name the delimiters in words rather than print them; (2) added `liquid: error_mode: lax` to `_config.yml` so the documentation site renders incidental brace sequences literally instead of failing the whole build — appropriate here because the repo never uses Liquid templating, while the physics notes and logbook routinely contain braces. Re-verified that no other tracked `.md` carries the delimiters.

## 2026-05-27 — Phase 4 research step: temporal-redundancy functional drafted (v0.1)

- **Actor:** Steward (decision: cross the held pause line; Verifier-stance review) / Agent (drafting + computation). **Commit:** *(this change).*
- Crossed the repeatedly-logged PAUSE (the toy functional is research, not bookkeeping). Drafted [`docs/notes/temporal-redundancy-functional-v0.1.md`](notes/temporal-redundancy-functional-v0.1.md): a Riedel-style temporal-redundancy functional `R_δ[τ]` on a finite temporal pointer, with a *computed* partial-information plot and redundancy count. **Headline:** the redundant (product) pole gives `R_{0.10} = 7.1` (plateau reached at `m_δ = 9` of `N = 64`); the anti-redundant (GHZ-shadow) pole gives `R_δ = 1` (zero information in every proper fragment) — "multipartite ≠ redundant" as a number. Maps onto the Sorci case (CL-2026-006) and its D1–D3; argues the bounded-vs-extensive basis for the resolution/classification-anchor split. The Appendix-A script (MIT) regenerates every number; independently re-run and confirmed.
- **Lock-Key held:** the note edits **no** Coastline/Ledger/Sail and explicitly does **not** close the principal open problem (Anti-Claim #6) — the product pole is a *candidate toy exemplar* gated by four stated idealisations; a non-toy (continuous-`τ`, many-carrier, dynamically einselected) instance is carried forward.
- **Steward review (Verifier-stance), two High findings corrected in place before integration:** (1) the GHZ phase realisation `e^{iNθ}` aliased the binary pointer for `N = 64` (both bins map to the same phase) — replaced by the abstract cat encoding `(|0…0⟩ + (−1)^T|1…1⟩)/√2`; (2) the headline `R_δ = 1` did not follow from the stated threshold definition (`I(N) = 1 − h₂(e) < 0.9` bit ⇒ `m_δ` undefined) — resolved by taking the anti-redundant pole's global read-out as ideal (`I(N) = H_T`, `m_δ = N`, `R_δ = 1`), which also removed a per-pole ambiguity in the noise parameter `e`. Further fixes: the Sorci `N = 2` scaling softened to directional/signature (not a fitted `R_δ(r)` curve); `R_δ` reworded as an *effective ratio* (`⌊N/m_δ⌋` the integer count); "`T` is einselected" softened to "treated as the pointer variable (assumed)".
- **Decisions:** licence confirmed (note text CC BY-SA 4.0; Appendix-A code MIT). A formal `MN-2026-xxx` methodological-note ID scheme **deferred** — one note does not justify the taxonomy. Roadmap bumped to v0.3; README structure tree and `index.md` updated to surface `docs/notes/`.

## 2026-05-27 — Documentation weave: temporal-redundancy finding surfaced

- **Actor:** Steward (direction: "weave the toy-example findings into the web page and other relevant spots") / Agent (execution). **Commit:** *(this change).*
- Surfaced the temporal-redundancy functional result (commit `8451bde`) into the public/communication layer:
  - **`index.md` (Pages landing page):** new *A first computed instrument* section with the `R_{0.10} = 7.1` (redundant) vs `1` (anti-redundant) headline table, the resolution/classification-anchor point, the Sorci map, and the toy/open-problem caveat; the earlier Supporting-material bullet folded into it.
  - **`docs/tutorial.md` → v0.2:** §10 rewritten (the toy functional is now drafted, with the headline result and the residual non-toy open problem); the §4 *multipartite ≠ redundant* caveat and the §11 key-distinctions row now cross-reference the computed result. The five-Claim exposition is unchanged.
- **Deliberately left unchanged (Lock-Key):** the Coastline, the three Ledger entries, and the Sail — folding the toy result into the framework itself would be a Coastline-version decision (flagged in the note's §7), not a documentation weave; and the dated Phase-3 snapshot `synthesis-v0.1.md` is frozen by its own scope statement.

## 2026-05-27 — MN v0.2: temporal-redundancy functional (Guardian-review revision)

- **Actor:** Steward (Guardian-stance review, prioritised change list) / Agent (revision + verification). **Commit:** *(this change).*
- Issued [`docs/notes/temporal-redundancy-functional-v0.2.md`](notes/temporal-redundancy-functional-v0.2.md) (v0.1 frozen, retained). Five surgical changes from the review, none touching the load-bearing §4 argument or the refusal to close Anti-Claim #6:
  1. **§1.1** — the *einselection* of the temporal pointer reframed as the central assumption/deferral (the hardest part of Anti-Claim #6); redundancy is computed *conditional on* it. Correctly sizes the contribution as "an instrument that would read redundancy if a temporal pointer were einselected."
  2. **§2 + new Appendix B** — the anti-redundant (zero-in-every-proper-fragment) result is derived from the Schmidt structure of the cat state (reduced fragment is `T`-independent ⇒ *no* measurement carries `T`), measurement-independent; the v0.1 parity model is retained as one explicit read-out channel.
  3. **§3** — Sorci `N = 2` softened: it *exemplifies* the anti-redundant pole but, taking values in `{undefined, 1, 2}`, gives a single transition, not a quantitative `R_δ(r)` curve or a test.
  4. **§4** — anchor-split argument confined to the binary-pointer / continuous-`τ` regime (Fisher extensive/unbounded vs MI bounded); Heisenberg `∝ N²` demoted to a non-load-bearing illustration.
  5. **§5** — the `r`-scan discrimination acknowledged as *conditional* on an unsupplied infidelity-scaling model (inherited from CL-2026-006 D3).
- **External grounding (verified):** the Guardian-flagged preprint **arXiv:2509.17775** (*Functional Information in Quantum Darwinism*, submitted 2025-09, published 2026-02) was confirmed via web search to define `FI(δ) = log₂ R_δ` and compute `R_δ` for a heterogeneous pure-dephasing model — **configurational**. It is now cited as the operational configurational measure this note transplants, used to make the "first computed" claim corpus-relative, and positioned as the configurational counterpart of the open *temporal* instrument (§6c). Flagged as a candidate corpus addition (§7); **not** added to `references.bib` in this step (a literature-review action).
- **Pointer cascade (the three downstream artefacts were public, so versioned):** tutorial → **v0.3** (citations re-pointed to v0.2; content unchanged), roadmap → **v0.4** (references re-pointed; item status unchanged), README structure tree + `index.md` link updated to v0.2. v0.1 left byte-for-byte (matching the repo's no-retro-edit freeze convention — cf. Coastline v0.3 still reads "Successor (none yet)").
- **Lock-Key held:** no Coastline/Ledger/Sail edited. The instrument-vs-fitting architectural question and the Sail-citation coupling are registered (note §7) for steward decision.
