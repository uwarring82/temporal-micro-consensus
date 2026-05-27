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

## 2026-05-27 — Source archived + findings note: tank2025 (functional information in QD)

- **Actor:** Steward (direction: "download, archive locally, extract to md note") / Agent (acquisition + extraction). **Commit:** *(this change).*
- Archived **arXiv:2509.17775** — A. B. Tank, *Functional Information in Quantum Darwinism: An Operational Measure of Classical Objectivity* (single author, Yeditepe University; v1 2025-09-22, v3 2026-02-01; CC BY 4.0). PDF downloaded to `docs/literature/sources/tank2025.pdf` (11 pp.) — **local-only, git-ignored** per the source-handling policy (not committed; confirmed `git check-ignore`).
- Wrote the own-words findings note [`docs/literature/notes/tank2025.md`](literature/notes/tank2025.md): full per-claim analysis. **Why it matters:** this is the operational *configurational* functional-information measure `F_QD(δ) = log₂ R_δ` (onset-based `R_δ ≈ N/m*_δ`, Holevo-grounded) that MN v0.2 transplants onto a temporal pointer; its pure-dephasing *computed* `R_δ(t)` (early growth → capacity plateau `≲ log₂ N`) is the configurational counterpart of the MN's open temporal instrument (§6c). Its Holevo-over-QMI grounding answers the synthesis §2 "MI overcounts" limitation and is a candidate refinement of the Claim IV measure-registration anchor.
- **Registered per convention:** added a verified `references.bib` entry (`tank2025`, cluster-B) and a provisional row + a *Post-synthesis addition* note in the corpus tracker `index.md`.
- **Deliberately NOT done (flagged):** `synthesis-v0.1.md` is left untouched (frozen Phase-3 snapshot of the 29-entry corpus); the entry's **tier is provisional** (the "Tier-1 fixed at 13" decision predates it) and a synthesis refresh / formal tiering is a future literature-review action for the steward. No Coastline/Ledger/Sail edited (Lock-Key).

## 2026-05-27 — CL-2026-006 v0.4: R_δ added as a second classification anchor

- **Actor:** Steward (Guardian-stance decision: the next coupling work sits in the Ledger, not the Sail) / Agent (drafting). **Commit:** *(this change).*
- Issued [`ledger/CL-2026-006-sorci-v0.4.md`](../ledger/CL-2026-006-sorci-v0.4.md) (v0.3 frozen, retained). Adds the **temporal-redundancy functional R_δ** (MN v0.2) as a second declared **classification anchor** alongside I(C:M), and registers the **resolution-vs-classification split** (resolution anchor = Fisher/QFI F[τ]). New *Engagement under the R_δ anchor* subsection: the Sorci protocol is the minimum-multipartite (N=2) anti-redundant case; squeezing drives the reduced clock toward the anti-redundant pole (R_δ ↓ as V ↓) — the same Claim II.2 stability failure the I(C:M) reading records.
- **Verdict unchanged: UNDERDETERMINED**, now cross-consistent under both anchors (both locate the failure at II.2 and the crux at experimental discriminability), which strengthens its robustness. D1–D3 unchanged; the R_δ-specific quantitative discriminant `R_δ(r) ∼ sinh²(2r)` requires N≫2 and is registered as a forward target, not a condition on the two-carrier claim.
- **Venue rationale (Guardian decision 2026-05-27):** the MN is cited *internally by the Ledger*, **not** from the Sail — citing a methodological instrument from the Sail would, by co-mention, risk implying the Coastline's principal open problem (Anti-Claim #6) is nearer resolution than it is, and the Sail's argument is complete at Coastline v0.4 + this entry. Instrument-vs-fitting placement of MNs stays deferred (note §7) until a second MN forces it.
- **Operationally previews — does NOT commit — the Coastline v0.5 measure-registration protocol** (the split is exercised in the Ledger, its proper venue). **Cascade:** roadmap → v0.5; README ledger tree + reading-order + `index.md` Ledger row → v0.4. Tutorial's CL-2026-006 v0.3 citations left as valid (verdict unchanged); pointer bump optional. Lock-Key: no Coastline/Sail edited.

## 2026-05-27 — Zenodo DOI minted (FAIR-Findability complete)

- **Actor:** Steward (Zenodo↔GitHub integration + release) / Agent (CITATION.cff + README + diagnosis). **Commit:** *(this change).*
- The framework repository is archived at a persistent **Zenodo DOI: [10.5281/zenodo.20411120](https://doi.org/10.5281/zenodo.20411120)**, release tag `framework-status-2026.05.27`. This completes the FAIR *Findable* step the README had flagged as remaining.
- **Blocker resolved en route:** the first Zenodo attempt failed with *"Citation metadata load failed."* Diagnosed (via `cffconvert -f zenodo`, which emulates Zenodo's mapping) as the `CITATION.cff` `license:` **list** mapping to `license.id = [array]`, which Zenodo's deposition model rejects (it accepts a single SPDX id). Fixed by collapsing to the single headline licence **CC-BY-SA-4.0** (steward decision); the repository remains split-licensed (MIT / CC-BY-SA / CC-BY-NC-SA), governed per-file by the in-archive `LICENSE-*` files and documented in a `CITATION.cff` comment.
- **Wired in:** `CITATION.cff` now carries `doi: 10.5281/zenodo.20411120` and `date-released: 2026-05-27`; README gains a DOI row, a completed FAIR-Findable bullet, and a repository-level citation pointer. **Still open (steward):** the ORCID TODO in `CITATION.cff` — provide it to fully complete the author identifier.
- **Consequence:** the toolkit's DOI prerequisite (2026-05-27 Guardian pre-toolkit audit) is now satisfied; the remaining gate before a Toolkit Work Plan v0.1 is steward confirmation of the toolkit's scope.

## 2026-05-27 — ORCID added (author identifier complete)

- **Actor:** Steward (provided ORCID) / Agent (edit). **Commit:** *(this change).*
- Resolves the *"Still open (steward): ORCID TODO"* flagged in the Zenodo-DOI entry above. Added the steward's ORCID — **0000-0001-8081-9718** (checksum-verified, ISO 7064 MOD 11-2) — to `CITATION.cff`, replacing the placeholder. CFF re-validated against schema 1.2.0; the Zenodo creator mapping now carries the ORCID. With the DOI and the ORCID both in place, the FAIR *Findable* author/identifier metadata is complete.
- *Note:* the live Zenodo record was archived before this metadata update, so the ORCID will appear there only on the next published version (or via a manual edit in the Zenodo deposition form); `CITATION.cff` is authoritative for citation regardless.

## 2026-05-27 — Toolkit Work Plan v0.1 (numerical toolkit scope confirmed)

- **Actor:** Steward (scope confirmation + direction; in-IDE Endorsement-Marker edit) / Agent (drafting, review reconciliation, edits). **Commits:** `45b368f` (plan + rev. (a)); *(this change)* (rev. (b) + this entry + README cascade).
- Created [`workplans/toolkit-work-plan-v0.1.md`](../workplans/toolkit-work-plan-v0.1.md) — the **toolkit-scope confirmation** that was the remaining gate flagged in the Zenodo-DOI entry above (2026-05-27 Guardian pre-toolkit audit). New top-level `workplans/` family. Defines scope, locked decisions (D1–D6), gated phases (0–4), validation strategy, framework-artefact discharge mapping, and toolkit anti-claims (A1–A5) for a numerical toolkit (at `numerics/`) operationalising the anchor measures I(C:M), F[τ], R_δ.
- **Multi-pass review (rev. (a)):** steward + IDE reviewer + Claude, nine reconciled findings folded in place. Substantive corrections (not cosmetic): the `R_δ` post-processor re-based on an explicit `TemporalRecordEnsemble` read-out abstraction (R_δ is mutual information between a *classical* pointer and fragment read-outs per MN v0.2 §1.1, not a state-intrinsic quantum MI); the nuisance model split into four computational layers (only the dynamical-Lindblad layer is Liouvillian — preparation/drive-phase/detection errors are not); the impossible `R_δ(r)` curve at N=2 rewritten as a directional transition; the stray squeezing knob `r` dropped from the redundant-pole observable `R_δ(N, ε)`. Plus over-claim corrections (D1 = 1 of 3, not "satisfied"; "candidate exemplar within the assumed regime"; publication staging as proposal), explicit-invariant cross-anchor tests guarding the CL-2026-007 v0.1 failure mode, and CL-2026-005/CBG registration (Q5).
- **Guardian review (rev. (b)):** corrected the §3 Module 3a D1-mapping. CL-2026-006 D1 enumerates five *physical-channel* contributions (i)–(v); the toolkit's four *computational* layers are a distinct taxonomy (heating+dephasing share the dynamical layer, the signal sits in the Hamiltonian), and the sweep covers drive-phase noise + mode-mixing as channels from CL-2026-006's wider discriminability gap, outside D1's formal five — so the budget is a *superset* of the D1 decomposition. *(The Guardian's suggested fix placed drive-phase noise inside D1(i)–(v); verified against CL-2026-006 line 120, which does not list it — corrected accordingly.)*
- **Cascade:** README — new `workplans/` entry in the structure tree, a *What this repository contains* mention, and a CC BY-SA 4.0 licence note. **Lock-Key held:** no Coastline/Ledger/Sail/MN edited; the plan is an instrument, not a framework artefact. **Still open (steward):** Phase 0 kickoff (scaffold `numerics/`), which carries the deferred Q1 (CITATION placement) and Q2 (CI) decisions.

## 2026-05-27 — Toolkit Phase 0: numerics/ scaffold (first code commit)

- **Actor:** Steward (Phase 0 go-ahead; Q1/Q2 defaults accepted) / Agent (scaffold + verification). **Commit:** *(this change).*
- Scaffolded the **`numerics/` numerical toolkit** per work-plan Phase 0 — the first code in the repository. Package `tmc-numerics` (src-layout under `src/tmc_numerics/`, MIT-licensed per the split), `pyproject.toml` (authoritative deps: `qutip`≥5, `numpy`≥1.24, `scipy`≥1.10; extras test/viz/examples/progress), `requirements.txt` (minimum-version manifest, §4), and a QuTiP-free pytest smoke test (`tests/test_smoke.py`, 2 tests). Placeholder `examples/` and `results/` directories with READMEs (Phase 3 deliverables).
- **Decisions resolved:** **Q1** → code citation is an *appended comment section* in the root `CITATION.cff` (re-validated against CFF schema 1.2.0 via `cffconvert`), not a separate file. **Q2** → GitHub Actions CI enabled (`.github/workflows/numerics-ci.yml`; Python 3.10–3.12, path-filtered to `numerics/`). Root `.gitignore` extended for numerics scratch/cache (final results stay committed, per Q3).
- **Q5 still open (Phase 0 TODO):** reconcile with CL-2026-005 (the "CBG" pipeline) before building Module 3a — registered in `numerics/README.md`.
- **Gate to Phase 1:** scaffold committed; `pytest` passes locally (2 passed in 0.01 s). The "runs cleanly on a fresh clone with declared dependencies" half of the gate is confirmed by the CI run triggered on this push. **Lock-Key held:** no Coastline/Ledger/Sail/MN edited.

## 2026-05-27 — Toolkit Q5 resolved: CBG (CL-2026-005) reconciliation

- **Actor:** Steward (decision: QuTiP + CBG-as-optional-backend; flag the ledger note) / Agent (investigation across repos + drafting). **Commit:** *(this change).*
- **Located** CL-2026-005 — it is **not** in this repo; it lives in the separate `oqs-cbg-pipeline` repository. **CBG = Colla–Breuer–Gasbarri**, the minimal-dissipation effective-Hamiltonian construction for *non-Markovian* open quantum systems (two *Phys. Rev. A* 112, 2025 papers); CL-2026-005 v0.4 is its Council-cleared, immutable Breakwater dossier (Sail v0.5).
- **Finding (scope mismatch):** the CBG pipeline computes the coherent effective Hamiltonian `K(t)` and its recursive TCL expansion in the non-Markovian / strong-coupling regime — **not** the Markovian-Lindblad mutual-information nuisance budget that CL-2026-006 D1 requires. Hosting Module 3a inside CBG was rejected because (i) scope mismatch (`K(t)` ≠ MI/Lindblad budget; and toolkit D3 already commits the Sorci module to QuTiP), (ii) CBG's trapped-ion territory is *permanently stewardship-conflict-bound* (steward co-authors the cited Nat. Commun. experiment, CL-2026-005 Entry 6) under Council-clearance discipline, and (iii) different anchor chains / update cadences.
- **Resolution (recorded in the work plan §6/§8/§10 rev. (c) + `numerics/README.md`):** Module 3a is reimplemented in QuTiP (per D3); CBG is retained only as (a) an *optional* non-Markovian validation backend (its HEOM/pseudomode reference solvers, for later cross-checks of the Markovian approximation) and (b) a methodological template (its benchmark-card / frozen-parameter / cause-labelled failure-envelope / validity-envelope discipline).
- **Registered flag (not actioned — Lock-Key):** CL-2026-006's "Relation to other Ledger entries" note claims CBG "produces precisely the nuisance-channel decomposition required by D1"; this overstates the scope mismatch and is flagged for softening when **CL-2026-006 v0.5** is drafted (work-plan Phase 4). No Coastline/Ledger/Sail/MN edited; CL-2026-005 (immutable, other repo) untouched.

## 2026-05-27 — Toolkit Phase 1 API contract accepted (signatures locked, D6)

- **Actor:** Steward (two-review pass → accept after blocking fixes; directive "mirror + commit, pause before code") / Agent (drafting, fix, mirror). **Commit:** *(this change).*
- Created [`workplans/toolkit-phase1-api-contract-v0.1.md`](../workplans/toolkit-phase1-api-contract-v0.1.md) — the Phase 1 **core-layer API contract** (the D6-locked public surface: `SystemLayout`, `HamiltonianTerm`/`LocalOp`/`Op`, `LindbladChannel`/`ChannelKind`, `DriveNoise`, `ReadoutModel`, `MasterEquationSystem`/`evolve`, `ObservableSpec`/`SolverOptions`/`EvolutionResult`, prep primitives). **Design-only; no implementation written.**
- **Two-pass review reconciled:** one review accepted as-is; the other found 4 Blocking + 2 High + 2 Medium. The blocking findings were correct on the merits — including a genuine physics error the accepting review mis-scored as non-blocking: HEATING as `D[a†]` gives state-dependent `d⟨n⟩/dt = ṅ(⟨n⟩+1)`, not the constant `ṅ` its test asserts. All resolved (contract §13): **HEATING redefined** as `ṅ·(D[a†]+D[a])` (state-independent `d⟨n⟩/dt = ṅ`) with a new **`THERMAL_RELAXATION`** channel for steady-state behaviour; **prep made local** (primitives return local density matrices, `product_state` tensors, `prep_infidelity` per-primitive); **`ObservableSpec`** for `e_ops` (bare `LocalOp` had no target); explicit **full-Hilbert (Phase 1) / factorised (Phase 3) backend boundary** (D3); constructor `dim` args removed (`TWO_LEVEL`==2); `DriveNoise.effective_rate` (explicit Lindblad rate, no hidden PSD factor); `SolverOptions.solver` + `fock_population_warn_threshold`.
- **Steward calls O1–O7 recorded** (contract §11): SI/`ℏ=1`; `TWO_LEVEL`=2; bare `Qobj` + `validate_state`; local symmetric-depolarising prep infidelity; `WHITE`→explicit effective rate; `mesolve` only; `drive_noise`+`readout` carried on the system as declared specs.
- **Accepted by the steward** ("mirror + commit, pause before code"): the signatures are mirrored into [`numerics/README.md`](../numerics/README.md) (new *Phase 1 — core-layer API* section) and locked per D6. **Implementation deliberately NOT started** — the steward will review the README-form locked contract before a separate implementation go-ahead. **Lock-Key held:** no Coastline/Ledger/Sail/MN edited.

## 2026-05-27 — Phase 1 contract LOCKED (drive-noise factor fixed); implementation begins

- **Actor:** Steward (final review: one remaining blocker, then "Go") / Agent (fix + implementation). **Commit:** *(this change; implementation follows).*
- **Final blocker fixed:** the `DriveNoise.effective_rate` factor convention. The first rev. said WHITE noise adds `effective_rate·D[operator]` and called that "dephasing at effective_rate" — but `D[σ_z]` sends a coherence `ρ_01 → −2ρ_01`, so `rate·D[σ_z]` decays as `e^{−2·rate·t}`, inconsistent with `ChannelKind.DEPHASING`'s `(γ_φ/2)·D[σ_z] → e^{−γ_φ t}`. **Fixed (steward option 1):** `effective_rate` is the *coherence-decay rate*; WHITE adds `(effective_rate/2)·D[operator]`, so a σ_z WHITE drive noise is exactly a `DEPHASING` channel at `γ_φ = effective_rate` (contract §5.3 + README mirror).
- **Contract ACCEPTED + D6-LOCKED.** All four Blocking + two High + two Medium findings + this factor fix resolved across two review passes. Public signatures are stable from v0.1; Phase 1 implementation proceeds against them (next commit). **Lock-Key held.**

## 2026-05-27 — Toolkit Phase 1 core layer implemented (37 tests green)

- **Actor:** Steward ("Go" after the drive-noise fix) / Agent (implementation + local test run). **Commit:** *(this change).*
- Implemented the Phase 1 core layer in `numerics/src/tmc_numerics/` against the D6-locked contract: `layout.py` (`SystemLayout`/`Subsystem`/`SubsystemKind`), `operators.py` (`Op`/`LocalOp`/`HamiltonianTerm`/`ObservableSpec`, full-space embedding, Hermiticity-checked assembly), `channels.py` (`ChannelKind`/`LindbladChannel`/`NoiseModel`/`DriveNoise`/`ReadoutModel`, collapse-operator construction), `system.py` (`MasterEquationSystem`/`evolve` over QuTiP `mesolve`; `SolverOptions`/`EvolutionResult`/`EvolutionDiagnostics`), `prep.py` (local prep primitives + `product_state`), `exceptions.py`.
- **Closed-form validation (the contract §10 test list):** 37 tests pass locally on QuTiP 5.2.3. Verified — DEPHASING coherence `e^{−γ_φ t}`; HEATING constant `d⟨n⟩/dt = ṅ` (the symmetric-pair generator); THERMAL_RELAXATION cooling `e^{−κt}` and steady-state `n̄`; **WHITE σ_z drive noise == DEPHASING at `γ_φ=effective_rate`** (confirms the `/2` factor fix at runtime); squeezed `⟨n⟩=sinh²r` + sub-vacuum quadrature variance; closed-system trace/purity preservation; truncation diagnostic flags overflow at tiny cutoff; layout/Hermiticity/kind-mismatch/firewall guards.
- **Firewall test passes:** no `R_δ` / pointer / `I(C:M)` / `F[τ]` symbol in the Phase-1 public namespace. README status + API section updated to "implemented". **Lock-Key held:** no Coastline/Ledger/Sail/MN edited. **Next:** Phase 2 (anchor-measure layer) — and the D5 regression gate (reproduce MN v0.2 §2 analytic poles) before Phase 3.

## 2026-05-27 — Toolkit Phase 2 implemented: anchor-measure layer + D5 gate (68 tests green)

- **Actor:** Steward (lightweight Phase-2 contract requested; accepted after a two-review pass; "Go") / Agent (contract + implementation + local validation). **Commit:** *(this change).*
- Accepted + D6-locked the Phase-2 contract addendum [`workplans/toolkit-phase2-api-contract-v0.1.md`](../workplans/toolkit-phase2-api-contract-v0.1.md) (P1–P5 confirmed as recommended). Implemented the anchor layer in `numerics/src/tmc_numerics/anchors/`: `ensemble.py` (`TemporalPointer`/`InfoMode`/`TemporalRecordEnsemble` with `iid`+`from_evolution`, `partial_information`), `info.py` (`mutual_information` I(C:M), `quantum_fisher` F[τ]), `redundancy.py` (`RedundancyResult`, `temporal_redundancy` R_δ).
- **D5 gate MET** (architectural-integrity gate). The regression reproduces the MN v0.2 §2 analytic poles **exactly**: product (redundant) pole via the **iid** representation matches Appendix A to ≤1e-9 — `R_{0.10}=64/9≈7.1` at e=0.20, *undefined* at e≥0.40 — and never builds a 2⁶⁴ state; GHZ-shadow (anti-redundant) pole via the **joint** representation at small N gives `R_δ=1` under `HOLEVO`, with `test_ghz_per_carrier_reads_zero` the negative confirmation (per-carrier read-out sees `I(N)=0` — why the ideal-global/HOLEVO mode is required). The "multipartite ≠ redundant" contrast (7.1 vs 1) is a single test.
- **Design (per contract):** `TemporalRecordEnsemble` has two representations — **iid** (single-carrier state + count; binomial MI; scales to N=64 and is the Phase-3 Module-3b substrate per D3) and **joint** (small-N dense, fragments via `ptrace`). `InfoMode.HOLEVO` makes MN's "ideal global read-out" an explicit typed mode (= `PER_CARRIER` on the redundant pole). All information in bits; QFI dimensionful; pointer basis fixed computational/binary for v0.1.
- **Cross-anchor invariants implemented** (`tests/test_cross_anchor.py`): `F[τ]` extensive (`F_τ(m)=m·F_1`); the **anti-correlation** — GHZ has Heisenberg `F[τ]=N²` but `R_δ=1`, product has `F[τ]=N` but `R_δ≫1` (F rises where R_δ falls); per-carrier nuisance collapses the `R_δ` plateau with no entanglement change. This is the resolution/classification split (F[τ] is *not* a classifier — the CL-2026-007 v0.1 guard).
- **68 tests pass** locally (QuTiP 5.2.3). Firewall updated: the Phase-1 core (`import tmc_numerics`) stays clean; anchors live in `tmc_numerics.anchors`. **Lock-Key held:** no Coastline/Ledger/Sail/MN edited. **Next: Phase 3** — protocol modules (Module 3a Sorci nuisance budget; Module 3b open-temporal-instrument via the iid backend).

## 2026-05-27 — Toolkit Phase 3 Module 3a implemented: Sorci nuisance budget (79 tests green)

- **Actor:** Steward (lightweight Module-3a contract; accepted after a two-review pass; "Go") / Agent (contract fixes + implementation + local validation). **Commit:** *(this change).*
- Accepted + D6-locked the Module 3a contract [`workplans/toolkit-module3a-sorci-contract-v0.1.md`](../workplans/toolkit-module3a-sorci-contract-v0.1.md) (M1–M4 confirmed). Implemented `numerics/src/tmc_numerics/modules/sorci.py`: `SorciParams`, `build_sorci_system` (secular/full), `sorci_initial_state`, `sorci_visibility`/`sorci_observed_visibility`/`clock_motion_mutual_information`, `baseline_visibility_check`, `rwa_error`, `nuisance_budget`/`NuisanceBudget`.
- **Two-pass review reconciled** (one accept-as-is; one with 2 Blocking + 2 High + 1 Medium — all correct, all folded): **B1** latent/observed split — `I(C:M)`/`V_state` are read-out-invariant; detection acts only on `V_obs`, so the detection budget row has latent `ΔI = ΔL_state ≡ 0` (an executable invariant). **B2** M3 transfer conditions made explicit (`λ=ε_m ω_c t`, `r`, `γ_φ t`, `ṅ t`; secular hierarchy `|g_md|/ω ≪ 1`, `ωt ≫ 1`). **H1** `g_md = −ε_m ω_c/4` **derived** (the baseline *validates* Sorci Eq. (12)'s coefficient, not calibrates). **H2** sign tests are benchmark-specific diagnostics, not global invariants. **M** D1-minimal single-mode; mode-mixing deferred.
- **Physics validated (79 tests, QuTiP 5.2.3):** the secular model reproduces Sorci Eq. (12)'s coefficient (`(1−V)/(λ²sinh²2r) → 1/16` as λ→0 — the derived `g_md` pinned, not fitted); the full `σ_z P̂²` model agrees within the RWA error at `ωt=10`; the ²⁷Al⁺ secular extrapolation gives `V≈0.93` (matching Sorci); `I(C:M)>0` confirms the signal entanglement.
- **A genuine physics finding the harness surfaced:** in the secular dispersive model, **motional dephasing `D[n̂]` is invisible to the clock** (it leaves the Fock populations — and hence `⟨e^{-2i g_md t n̂}⟩` — unchanged), while heating, clock drive-phase, and prep infidelity do contribute. Concrete evidence for why sign tests must be benchmark-specific (review H2); the contribution would differ in the full `σ_z P̂²` model.
- **Budget:** marginal-from-signal per channel + full + interaction residual (honest non-additivity, A4), latent/observed columns; scaled headline + extrapolated ²⁷Al⁺ column. **Lock-Key held.** **Next: Module 3b** (open-temporal-instrument via the iid backend — derive `ε(γ_φ,ṅ,t)` from a single-carrier master equation; a short 3b addendum first), then Phase-4 feed-forward (CL-2026-006 v0.5 D1 grounding + the registered CBG-note softening).

## 2026-05-27 — Toolkit Phase 3 Module 3b implemented: open temporal instrument (85 tests green)

- **Actor:** Steward (lightweight 3b addendum; accepted after a two-review pass; "Go") / Agent (contract fixes + implementation + validation + committed results). **Commit:** *(this change).*
- Accepted + D6-locked the Module 3b addendum [`workplans/toolkit-module3b-open-instrument-contract-v0.1.md`](../workplans/toolkit-module3b-open-instrument-contract-v0.1.md) (B1–B3 confirmed). Implemented `numerics/src/tmc_numerics/modules/open_instrument.py`: `OpenInstrumentParams`, `single_carrier_coherence`, `carrier_distinguishability`, `carrier_conditional_states`, `redundancy_at`, `redundancy_curve`.
- **The dynamical bridge:** a single-carrier pure-dephasing `evolve` (`|+⟩` under `(γ_φ/2)D[σ_z]`) gives `c=e^{−γ_φ t}`; `ε(γ_φ,t)=(1−c)/2`, where the trace-distance/Helstrom, the phase-bin projective flip, and the Holevo information (`χ=1−h₂(ε)`) all agree — so MN Appendix A's hand-fixed `e` is now *derived*. The Phase-2 `iid` ensemble + `temporal_redundancy` give `R_δ(N, γ_φ t)` (any N, no 2ᴺ state).
- **Two-pass review reconciled** (1 Blocking + 1 High + 2 Medium, all folded): **B** the `σ_x` read-out renamed the *assumed temporal / phase-bin readout basis* (NOT "einselected" — the dephasing's physical pointer is σ_z; what is einselected for the temporal record is the §4 *assumption*). **H** Holevo `χ = 1 − h₂(ε)` (consistent with, not equal to, ε). **M** single-carrier label `carrier_00`; artifacts → `results/` + notebook.
- **D5 cross-link passes to the D5 standard:** at `γ_φ t = ln(5/3)` (`ε=0.20`) the dynamical path lands on `R_{0.10}=64/9` exactly (`m_δ=9`) — Module 3b inherits the Phase-2 exactness.
- **Results committed** (Q3): `numerics/results/open_instrument_redundancy_v0.1.json` (the `R_δ(N, γ_φ t)` grid + undefined boundary — **`γ_φt_crit` rises with N: 0.27 (N=4) → 1.83 (N=128)**, i.e. more independent carriers tolerate more per-carrier nuisance, MN §5) and `numerics/results/sorci_nuisance_budget_v0.1.json` (the Module 3a D1 budget; the detection row confirms latent `ΔI=ΔL_state=0`, observed `ΔL_obs≈0.099`; Al⁺ extrapolation `V=0.943`).
- **85 tests pass** (QuTiP 5.2.3). The **einselection caveat (§4) is verbatim-ready** for Phase-4 feed-forward; **Anti-Claim #6 stays open**. **Lock-Key held:** no Coastline/Ledger/Sail/MN edited. **Next: Phase 4** — CL-2026-006 v0.5 (D1 grounding + the registered CBG-note softening) and MN v0.3 (Module 3b curves), plus the Phase-3 example notebooks (both modules) to close the gate. All steward/Lock-Key.

## 2026-05-27 — Phase 3 formally closed: example notebooks (gate condition met)

- **Actor:** Steward (direction: close the gate before Phase 4) / Agent (notebooks). **Commit:** *(this change).*
- Added the two reproducible example notebooks (`numerics/examples/`), **executed end-to-end** (nbconvert, QuTiP 5.2.3, zero errors), regenerating the committed results from scratch:
  - [`sorci_module.ipynb`](../numerics/examples/sorci_module.ipynb) — Module 3a: baseline Eq. (12)-coefficient validation, the latent/observed D1 budget table (detection row latent `ΔI=ΔL_state≡0`), the ²⁷Al⁺ `V≈0.943` extrapolation; asserts a match to `results/sorci_nuisance_budget_v0.1.json`.
  - [`open_instrument_module.ipynb`](../numerics/examples/open_instrument_module.ipynb) — Module 3b: derives `ε=(1−e^{−γ_φ t})/2`, the D5 cross-link (`ε=0.20 → R_{0.10}=64/9` exactly), the `R_δ(N, γ_φ t)` curves (plot) + the undefined boundary rising with N; carries the **einselection caveat verbatim**; asserts a match to `results/open_instrument_redundancy_v0.1.json`.
- **Phase-3 gate condition MET** (work-plan §3): both protocol modules produce reproducible results stored as notebooks in `numerics/examples/` and documented results in `numerics/results/`. **Phase 3 is complete.** **Next: Phase 4 feed-forward** — CL-2026-006 v0.5 drafted first (Module 3a D1 grounding + the registered CBG-note softening; Lock-Key — the numerical results inform but do **not** auto-update the verdict, Anti-Claim A5). Lock-Key held.

## 2026-05-27 — Ledger CL-2026-006 v0.5 issued: D1 quantitatively grounded by the toolkit

- **Actor:** Steward (two-review pass → accept + issue after two text fixes) / Agent (draft + fixes + cascade). **Commit:** *(this change).*
- Issued [`ledger/CL-2026-006-sorci-v0.5.md`](../ledger/CL-2026-006-sorci-v0.5.md) (v0.4 frozen, retained) — the first Phase-4 framework feed-forward. tmc-numerics **Module 3a's D1 nuisance budget** (committed `numerics/results/sorci_nuisance_budget_v0.1.json`) is incorporated as quantitative grounding for Discriminant D1.
- **Verdict UNCHANGED — UNDERDETERMINED** (Lock-Key / Anti-Claim A5: numerics inform, do not auto-update). D1's *theoretical* decomposition is now produced and reproducible, but the budget shows it is **model-conditional**, so it *sharpens* D1 (a demand on controlled scaling + explicit channel models) rather than discharging it; D2/D3 remain experimental and unmet. Three honestly-reported findings: per-channel signs are non-uniform (heating/dephasing **reduce** I(C:M); the depolarising prep-infidelity model **raises** and dominates it); detection is **latent-invariant** (ΔI=ΔV_state=0, observed-only); motional dephasing is **visibility-invisible** in the secular model yet still lowers I(C:M) (channels non-additive).
- **CBG-note softened** (toolkit Q5): the v0.4 "CBG produces precisely the D1 decomposition" corrected — CL-2026-005 computes the coherent K(t) (non-Markovian), not the Markovian D1 budget; D1 is produced by tmc-numerics. **Module 3b** registered as a candidate Anti-Claim #6 exemplar under the **verbatim einselection caveat** (Anti-Claim #6 open).
- **Two review fixes folded before issuance:** (1) the toolkit grounding cites the committing commit `a6518a7` with "Zenodo update pending" — the existing DOI snapshot (`framework-status-2026.05.27`, tag → `d4ca52d`) **predates** the toolkit; (2) motional dephasing reworded "visibility-invisible (secular)" — it still lowers quantum I(C:M) — removing a draft self-contradiction.
- **Cascade:** README structure tree + reading-order → v0.5; `index.md` Ledger row → v0.5; roadmap → v0.6. **Toolkit-v0.2 refinement registered:** a physical squeezing-prep-infidelity model (r-jitter / thermal admixture) — the v0.1 symmetric-depolarising model is aggressive for a high-cutoff bosonic mode. **Next Phase-4:** MN v0.3 (Module 3b curves), then journal-paper integration. **Lock-Key held:** Coastline untouched; v0.4 frozen.

## 2026-05-27 — MN v0.3 issued: numerical companion (§8) to the temporal-redundancy functional

- **Actor:** Steward (two-review pass → accept + issue after two wording fixes) / Agent (draft + fixes + cascade). **Commit:** *(this change).*
- Issued [`docs/notes/temporal-redundancy-functional-v0.3.md`](notes/temporal-redundancy-functional-v0.3.md) (v0.2 frozen, retained). v0.3 **adds §8** — the open-temporal-instrument numerical companion (toolkit Module 3b) — and carries §1–§7 + Appendices A/B **verbatim**; §2's analytic poles are byte-identical (diff-verified).
- **§8 content:** the dynamical bridge `ε(γ_φ,t)=(1−e^{−γ_φ t})/2` derived from a single-carrier pure-dephasing master equation (the four-way trace-distance / Helstrom / projective / Holevo coincidence); the `R_δ(N, γ_φ t)` curves with the undefined-boundary table (first undefined sweep point, rising with N); the D5 cross-link validation (`ε=0.20, N=64 → R_{0.10}=64/9` exactly); the *redundancy-lost-without-entanglement* structural point (§8.4); and the **match to arXiv:2509.17775** (§8.5 — the temporal-side pure-dephasing `R_δ` now exists, matching the configurational computation in *structure*, not numerically — the asymmetry closed at the level of the computation).
- **Einselection caveat carried verbatim (§8.6)** — identical block to CL-2026-006 v0.5; **Anti-Claim #6 remains open** (§8 is a candidate exemplar within the assumed regime, not a resolution).
- **Two review fixes before issuance:** (1) the §8.2 boundary table relabelled "first undefined `γ_φ t` in the committed sweep" (grid-resolution-dependent), **not** the exact continuous `ε_crit` — with the distinction stated; (2) explicit artifact provenance added (`numerics/results/open_instrument_redundancy_v0.1.json`, `numerics/examples/open_instrument_module.ipynb`).
- **Cascade:** `index.md` / README structure tree / `docs/tutorial.md` (×2) MN pointers → v0.3; roadmap "Toy-model functional" item → v0.3 + roadmap → v0.7. v0.2 frozen; **Coastline untouched (Lock-Key).** **Next Phase-4 (final): journal-paper integration** (Coastline + MN v0.3 + the worked exemplar).
