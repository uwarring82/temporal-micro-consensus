# hartong2024 — A Coupling Prescription for Post-Newtonian Corrections in QM

| Field | Value |
| --- | --- |
| Reference | J. Hartong, E. Have, N. A. Obers, I. Pikovski, "A coupling prescription for post-Newtonian corrections in quantum mechanics", *SciPost Phys.* **16**, 088 (2024). DOI 10.21468/SciPostPhys.16.3.088, arXiv:2308.07373. |
| Cluster · Tier | A · 2 (down-tiered from 1 — methods/PN node, not relational-time) |
| Source PDF | `sources/hartong2024.pdf` — 40 pp. ✅ complete (read front matter, §1 intro, §5 discussion) |
| Extracted | 2026-05-26 |

## Summary
Develops a covariant, geometry-based prescription for adding post-Newtonian gravitational corrections to the Schrödinger equation, via a 1/c² expansion of Lorentzian geometry (non-Lorentzian / Newton–Cartan structure at each order) coupled to a 1/c² expansion of the complex Klein–Gordon field. The output is a quantum Hamiltonian on an arbitrary post-Newtonian background, worked out explicitly for a Kerr metric up to O(c⁻²) (yielding a generalized Lense–Thirring / Hartle–Thorne case). The authors stress this is *not* quantum gravity but a way to capture fixed-background GR effects on quantum systems.

## Key points
- Method: split g_{μν} = −c²T_μT_ν + Π_{μν}, expand T_μ, Π^{μν} in inverse even powers of c; LO geometry is Galilean (Newton–Cartan), subleading "gauge" fields encode gravity (time component of m_μ is the Newtonian potential).
- Gauge symmetries of the nonrelativistic geometry uniquely fix the form of the Schrödinger equation (up to non-minimal terms) order by order in 1/c²; same result reproduced by 1/c² expansion of the Klein–Gordon Lagrangian.
- Notes that the would-be wavefunctions inherit the (positive-frequency) Klein–Gordon inner product and need a field redefinition to recover the standard L²(ℝ³) Born norm.
- Final Kerr-background Hamiltonian (Eq. 154) includes a JL_z Lense–Thirring coupling plus novel O(J²) terms potentially measurable.
- Discussion flags composite/clock systems: delocalized systems "that keep track of time" experience time-dilation-induced entanglement between internal and external DOF (citing Zych/Pikovski-type work) — noted as future work, not developed here.

## Relevance to the framework
**LINEAGE FLAG — confirmed.** This is *not* a Page–Wootters or relational-time paper despite its Cluster-A placement. It is a post-Newtonian coupling-prescription / geometry paper producing gravitationally corrected single-particle Schrödinger Hamiltonians. It has no clock-conditioning, no conditional-probability time, and no temporal-record construction. Its only contact with the Coastline claims is indirect: it supplies the curved-background Hamiltonians whose mass–energy coupling underlies time-dilation effects (relevant to Claim I/III machinery downstream, e.g. as cited by sorci2026), but it does not itself bear on emergence, redundancy, or any Claim IV measure. Treat as a methods/lineage reference, not a relational-time source.

## Flags
- Reference-vs-content mismatch in *role*, not bibliography: the citation is correct, but its cluster-A (Page–Wootters/relational-time) framing is misleading. Recommend re-tagging as a post-Newtonian/coupling-prescription lineage node. (This matches the note's stated suspicion.)
- 40-pp. article; only front matter, introduction, and discussion read in full per the review-article rule. Body (§2–§4, appendices) is technical PN/Kerr derivation.
