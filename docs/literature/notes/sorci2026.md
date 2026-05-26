# sorci2026 — Quantum Signatures of Proper Time in Optical Ion Clocks

| Field | Value |
| --- | --- |
| Reference | G. Sorci, J. Foo, D. Leibfried, C. Sanner, I. Pikovski, *Quantum Signatures of Proper Time in Optical Ion Clocks*, Phys. Rev. Lett. **136**, 163602 (2026). |
| DOI / arXiv | 10.1103/qhj9-pc2b · arXiv:2509.09573 · CC BY 4.0 · Editors' Suggestion · publ. 20 Apr 2026 |
| Cluster · Tier | C · 1 |
| Source PDF | `sources/sorci2026.pdf` — 9 pp. ✅ complete |
| Extracted | 2026-05-26 |

## Summary

Develops a Hamiltonian formalism for harmonically trapped clock atoms/ions in which the proper time is promoted to an operator τ̂(x̂,p̂), and shows that beyond the classical second-order Doppler shift (SODS) there arise genuinely quantum proper-time effects. The central prediction is that **time-dilation-induced entanglement between the motional and internal-clock degrees of freedom produces an observable reduction of interferometric visibility** — a witness of *non-classical* proper-time evolution — reachable with state-of-the-art ²⁷Al⁺ ion clocks when the motion is squeezed.

## Key points

- Clock–motion coupling Hamiltonian `Ĥ = Ĥc + ℏω(n̂+½) − (ℏω/2mc²)Ĥc P̂²`, derived from the composite-system action of [[zych2019]] (their Ref. 21); the last term entangles clock and motion.
- **vSODS** (vacuum-induced): `Δν/ν = −εm/4 = −ℏω/4mc²`, present even in the motional ground state (finite momentum spread of the vacuum); ~5×10⁻¹⁹ in a MHz trap — potentially observable.
- **sqSODS / visibility loss**: motional squeezing (r = 2.26, already demonstrated in ion traps) gives a visibility `V ≈ 0.93` for a ²⁷Al⁺ clock (267 nm, 20 MHz trap, t ≈ 1 s) — this visibility drop is the experimental witness.
- Crucially distinguishes effects reproducible by a *semiclassical* ⟨τ⟩ (the frequency shifts) from those that are **not** (the entanglement/visibility loss). The latter is the genuine quantum-proper-time signature.
- **qSODS** (~10⁻¹⁰ rad) is currently unobservable.

## Relevance to the framework

- **Subject of Ledger CL-2026-006.** The visibility-loss witness is the prime candidate for a Claim III "breakdown of a classical temporal-consensus variable." The paper's own separation of semiclassically-reproducible shifts from irreducibly-quantum entanglement effects maps directly onto the Coastline's **Claim III nuisance-discrimination** requirement and onto **Claim IV** (interferometric visibility as the operational measure).
- **Acknowledgement decision (Sail):** D. Leibfried (NIST) and C. Sanner (Colorado State) are **co-authors** of this paper, not third parties. This reframes the roadmap's pending proximity-signal decision for the Sorci commentary.
- **Lineage:** confirms the Cluster-E "high-traffic" claim — the Hamiltonian descends from the Zych–Rudnicki–Pikovski composite-system action ([[zych2019]]).

## In-corpus citation chain

Cites: [[zych2011]] (13), [[pikovski2015]] (15), [[zych2019]] (21), [[martinezlahuerta2022]] (22), [[hartong2024]] (23), [[smith2020]] (25), [[covey2025]] (34), [[fromonteil2025]] (35), [[yudin2018]] (37), [[margalit2015]] (48). Dense overlap with the corpus — a backbone for the Phase 3 lineage audit.

## Flags

- `file` reported "1 page" — **false**; the PDF is the full 9-page article. (`file`'s page counts proved unreliable for several APS/arXiv PDFs.)
- Title casing: published form is title-case "Quantum **S**ignatures…"; `references.bib` uses sentence case. Harmonise at typesetting, not now.
