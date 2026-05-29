# Memory Note — Analytical Route Towards Narrowing Anti-Claim #6

**Document type:** Memory note. A research-direction memorandum, not a Methodological Note, not a Coastline revision, not an instrument. Introduces no framework claim. Anchored *from* the framework (motivation), not *into* it (no artefact cites this memo).
**Status:** Pre-development. Captures a candidate analytical route surfaced during the 2026-05-28 Integrator-stance deliberation, parked for later pickup. Lock-Key held — no Coastline / MN / Ledger / Sail / View edited or anchored on the basis of this memo.
**Date:** 2026-05-28.
**Motivation anchors:** Coastline v0.4 Anti-Claim #6 (the framework's principal open problem); MN v0.3 §8.6 (einselection caveat); Harbour View v0.1 §2 anti-claim restatement.

---

## The question parked here

Can the configurational → temporal transplant be made into a *derivation* of temporal-pointer einselection, rather than an assumption? If so, Anti-Claim #6 narrows from *"redundant temporal records exhibited within an assumed-einselection regime"* to *"redundant temporal records exhibited under an explicit, physically located residual assumption"*. That is a narrowing, not a closure — see *What this would and would not establish* below.

## Why the naïve transplant stalls

In configurational quantum Darwinism the recorded object is a system *observable* Â_S; the pointer basis is the eigenbasis of the observable that commutes with the system–environment coupling, [H_int, Â_S] ≈ 0. Nondemolition is the engine — the observable is copied into many fragments without disturbance, so each fragment independently pins its value and R_δ → N. **Proper time is not an observable of this kind; it is a parameter.** That disanalogy is what "assume the temporal pointer is einselected" has been load-bearing for.

## The candidate route — relational temporal Darwinism

Define the criteria *relationally*, in the Page–Wootters picture. Take a clock C with a reading observable, and carriers F_k each coupling diagonally in the clock-reading basis:

> `H_int = Σ_k Ĝ_C ⊗ B̂_k,  Ĝ_C = ∫dτ g(τ) |τ⟩⟨τ|`

The clock-reading basis is conserved by the coupling — [H_int, |τ⟩⟨τ|] = 0 — and the joint state branches exactly as in configurational QD:

> `|Ψ⟩ = ∫ dτ ψ(τ) |τ⟩_C ⊗_k |ε_k(τ)⟩_F`

Each fragment holds a record |ε_k(τ)⟩ of the clock reading; if those records are bin-distinguishable, the reading is redundantly copied and R_δ → N. **The einselection of the clock-reading basis follows from the nondemolition condition; it is not posited.**

The temporal content cannot come from the recording alone (a sceptic would correctly say that is configurational QD with the position observable relabelled "time"); it must come from the clock condition. The recorded observable has to be a function of the clock's time observable T̂, conjugate to the clock Hamiltonian: [T̂, H_C] = iℏ. The compatibility that does the work: **[H_int, T̂] = 0 and [T̂, H_C] = iℏ are simultaneously satisfiable because H_int and H_C are different operators.** During a fast recording interaction the clock reading is copied nondemolition; under H_C between recordings the reading advances. This is a stroboscopic (repeated-nondemolition) structure — and it is exactly the repeated-interaction clock geometry the project's stroboscopic-travelling-waves work already lives in.

**Synthesis (one-line):** *Temporal QD = Page–Wootters relational time + nondemolition redundant recording of the clock observable.*

Under this construction the three criteria for temporal records become:

- **Redundancy** — many disjoint carrier-fragments each carry (1−δ)·H_T of the clock-reading record; R_δ = N / m_δ ≫ 1.
- **Stability (einselection), derived** — the clock-reading basis is selected as the pointer by [H_int, T̂] = 0; no longer an assumption.
- **Compressibility** — the partial-information plot saturates at H_T; carriers agree on a single proper-time labelling. Consensus.

Temporality is supplied by the clock condition; objectivity is supplied by the redundant nondemolition recording.

## Three residual difficulties — to be treated carefully, not glossed

1. **Finite clocks have no exact T̂.** [T̂, H_C] = iℏ is impossible in finite dimension (Pauli's theorem / trace obstruction). The projective-pointer derivation is an idealised limit. For real clocks the recorded object is a *covariant clock POVM*, and "redundancy of a POVM record" must be the right quantity — exactly the Holevo-grounded R_δ already adopted from Tank 2025 (MN v0.3 §8). The measure is POVM-ready; the theorem is exact only in the ideal-clock limit, with quantifiable corrections otherwise.

2. **Shared time versus which-time — the most fragile point.** Repeated recording gives fragment k a record of the reading at *its* interaction instant t_k. Redundancy of a single shared proper time (genuine consensus) is not automatic from this — it requires either near-synchronous recording, or, deeper, fragments recording the clock's *phase function / rate* so they agree on the parametrisation even when sampled at different points. The second is the real cash value of "consensus," and it is the part most exposed to hand-waving. **A careful definition here is the difference between a theorem and a slogan.** Develop this before any novelty claim.

3. **Non-ideal nondemolition = the anti-sweet structure already measured.** Exact nondemolition gives R_δ → N (the sweet pole). Real couplings deplete the clock and degrade the records — and that degradation is exactly the γ_φ·t_crit-rising-with-N boundary Module 3b found numerically (open-temporal-instrument curves, MN v0.3 §8). The analytical result would be the sweet-pole limit; the numerics already map the departure from it. Two ends of one axis — a cross-check between analytical and numerical sides of the same structure, not a duplication.

## What this would and would not establish

Even cleanly executed, this would close Anti-Claim #6 only *within the ideal-clock, exact-nondemolition model*. It narrows the residual assumption (from "einselection assumed" to "exact nondemolition of an ideal clock assumed") rather than eliminating it.

**Honest framing for any write-up:** *the einselection step is derivable in the idealised relational model; the residual assumption is now explicit and physically located.* Not *"Anti-Claim #6 resolved."*

## Pickup process

For whoever returns to this — possibly you, possibly later:

1. **VERIFY pass first.** Before any novelty claim: literature search for prior work on relational / temporal quantum Darwinism, covariant-POVM clock formulations (Smith–Ahmadi 2020 and descendants; any "objective time" or "temporal Darwinism" literature). The Phase-3 literature-review synthesis registered "no temporal exemplar in the corpus" — but absence-of-prior-art *for this specific construction* must be checked, not assumed.
2. **Develop the idealised model.** Clock + N nondemolition carriers; explicit branching state; partial-information plot; einselection derivation. Treat difficulty (2) — shared-vs-which-time — carefully, not as an afterthought. The sweet-pole limit should reproduce Module 3b's R_δ → N behaviour as a consistency check.
3. **Locate the residual assumption.** Where exactly does *ideal-clock + exact-nondemolition* do load-bearing work? That location is what the narrowed Anti-Claim #6 names. Be specific.
4. **Routing if it survives.** Up-channel to a new Methodological Note (MN v0.4 or a new ID series); if it then survives MN-level scrutiny, *then* it sharpens Coastline Claim II — under standard Lock-Key routing, not by direct edit. Does not touch the View; the View is a presentation of the current public framework, not a venue for emerging research.

## What this memo is not

- Not a Methodological Note. No instrument defined; no formal versioned object; no place in the artefact taxonomy.
- Not a Coastline revision. Coastline v0.4 stands; Claim II untouched.
- Not anchored from the View, the Ledger, or any Sail.
- Not a claim that Anti-Claim #6 has been resolved or even substantially narrowed; only that a candidate analytical route exists worth developing.
- Not under review discipline. A memorandum, not an artefact.

## Origin

Brainstormed during the 2026-05-28 Integrator-stance deliberation, following Harbour View v0.1 §1 + §2 publication and the discovery-campaign decision. The Guardian held the honesty line throughout (no claim that the route closes Anti-Claim #6; the three residual difficulties named explicitly). This memo captures the architecture for later pickup so the thread is not lost.

---

*End of memory note. To be picked up later.*
