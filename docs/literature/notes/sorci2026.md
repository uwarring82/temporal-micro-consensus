# sorci2026 — Quantum Signatures of Proper Time in Optical Ion Clocks

| Field | Value |
| --- | --- |
| Reference | G. Sorci, J. Foo, D. Leibfried, C. Sanner, I. Pikovski, *Quantum Signatures of Proper Time in Optical Ion Clocks*, Phys. Rev. Lett. **136**, 163602 (2026). |
| DOI / arXiv | 10.1103/qhj9-pc2b · arXiv:2509.09573 · CC BY 4.0 · Editors' Suggestion · publ. 20 Apr 2026 |
| Cluster · Tier | C · 1 |
| Source PDF | `sources/sorci2026.pdf` — 9 pp. ✅ complete |
| Annotated | 2026-05-26 (Phase 2) |

## Core claim

Trapped-ion optical clocks can reach a regime where proper time must be treated quantum-mechanically: time-dilation-induced **entanglement between the ion's motion and its internal clock** produces an observable **loss of interferometric visibility** that no semiclassical single-⟨τ⟩ description can reproduce. This visibility drop is a witness of genuinely quantum proper-time evolution, reachable with motionally squeezed ²⁷Al⁺ clocks using existing technology.

## Method

Hamiltonian formalism for a harmonically trapped two-level clock with proper time promoted to an operator τ̂(x̂,p̂). The clock–motion coupling `−(ℏω/2mc²)Ĥc P̂²` (Eq. 1) descends from the composite-system action of [[zych2019]]. The unitary is decomposed via clock-dependent squeezing/rotation operators; the reduced clock coherence `2ρ_eg = ⟨e^{−iω′_c(n̂)t}⟩` and visibility `V = 2|ρ_eg|` are computed for thermal, ground, and squeezed motional states, yielding four shifts: SODS, vacuum-induced vSODS, squeezing-induced sqSODS, and quantum qSODS.

## Relation to the five Coastline claims

- **Claim I — emergent proper time / temporal record:** **Strongly supports.** The clock's internal coherence is an explicit temporal record, and the paper's central distinction — a fixed semiclassical parameter `⟨τ⟩ ≈ t(1 − ⟨v²⟩/2c²)` versus the operator τ̂(x̂,p̂) — is exactly Claim I's "classical proper time is not the expectation value of a microscopic time variable." Proper time acquires operational meaning only at the level of the clock observable.
- **Claim II — redundancy / stability / compressibility:** **Largely silent / boundary case.** This is a *bipartite* clock⊗motion system (one ion), not a multi-carrier redundancy demonstration. It touches compressibility only implicitly: it maps exactly where a single effective τ_cl *suffices* (the frequency shifts, reproducible semiclassically) versus where it does not (the entanglement regime). No redundancy across many carriers is exercised.
- **Claim III — failure mode / nuisance-discrimination:** **Central — the paper's spine.** It explicitly separates effects reproducible by a semiclassical ⟨τ⟩ (SODS, vSODS — frequency shifts that, despite being quantum in origin, do *not* witness non-classical proper time) from the **entanglement-induced visibility loss that cannot be so reproduced**. That is precisely Claim III's requirement to discriminate a structural failure of the classical temporal-consensus variable from ordinary nuisance shifts. The visibility loss is the witness; the SODS/vSODS are the discriminate-against channel.
- **Claim IV — operational anchors:** Instantiates **interferometric visibility** `V = 2|ρ_eg|` (a coherence measure) as the operational anchor — `V ≈ 0.93` for ²⁷Al⁺ at r = 2.26 squeezing, 20 MHz trap, t ≈ 1 s. Not Fisher-framed, but visibility is a legitimate Claim IV candidate; an open question is whether a Fisher-information anchor would be sharper here.
- **Claim V — positioning:** The minimal **L₀** case — a single clock plus a single motional mode, i.e. a bipartite-correlation effect nearer the Page–Wootters picture than to multipartite redundancy. It marks the boundary at which multipartite redundancy is *not yet* present; the framework would say a classical τ_cl for this ion fails precisely in the strongly-squeezed regime.

## Bearing on Ledger / Sail

**Subject of Ledger CL-2026-006.** The visibility-loss witness is the discriminant the framework classifies as a (partial) failure of the classical temporal-consensus variable, discriminable from SODS/vSODS nuisance — a textbook instance of the Claim III + Claim IV machinery. **Sail:** the Sorci commentary is on this paper; D. **Leibfried** (NIST) and C. **Sanner** (Colorado State) are **co-authors**, which reframes the roadmap's pending acknowledgement / proximity-signal decision (they are authors of the work being commented on, not third parties).

## Lineage & citation chain

Builds on [[zych2019]] (Hamiltonian / composite-system action), [[zych2011]] and [[pikovski2015]] (time-dilation-induced entanglement & decoherence). In-corpus citations: [[smith2020]], [[martinezlahuerta2022]], [[hartong2024]], [[yudin2018]], [[margalit2015]], [[covey2025]], [[fromonteil2025]]. Dense overlap — a backbone for the Phase-3 lineage audit.

## Open questions / flags

- Single-ion / bipartite: the framework's multipartite-redundancy condition (Claim II) is untested here; natural extension to multi-ion crystals (the paper notes two-ion ²⁷Al⁺ and a prospective ¹⁰B⁺ clock at 1119 THz, V ∼ 0.76).
- Open: visibility vs a Fisher-information measure as the better Claim IV anchor for this case.
- `file` reported "1 page" — false; full 9-page article. Title casing: published title-case vs sentence case in `references.bib` (harmonise at typesetting).
