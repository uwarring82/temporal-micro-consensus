---
title: Breakwater Ledger
---

# Breakwater Ledger

The **Breakwater Claim Analysis Ledger** classifies external scientific claims against the current Coastline framework under a declared evaluating measure, with explicit *Discriminant Conditions* for upgrade or downgrade. Each entry is a versioned file; entries are not retroactively rewritten — supersession is recorded by issuing a new version.

All entries are anchored to **Coastline v0.4** ([*Consensus-Emergence of Classical Proper Time*](../coastlines/consensus-emergence-v0.4.md)). All three current entries sit at the same place: *theory-compatible, experimental-witness-underdetermined*.

## Current entries

| Entry | Subject | Classification | Anchors | Current file |
| --- | --- | --- | --- | --- |
| **CL-2026-006** | Sorci et al. (2026) — visibility witness of quantum proper-time dynamics in trapped optical ion clocks | **UNDERDETERMINED** | `I(C : M)` and `R_δ` (classification); `F[τ]` (resolution) | [v0.5.1](CL-2026-006-sorci-v0.5.1.md) |
| **CL-2026-007** | Smith & Ahmadi (2020) — quantum clocks observe classical and quantum time dilation | **UNDERDETERMINED** | `γ_Q⁻¹` (coherence-dependent quantum time dilation), Fisher `F[τ]` (resolution) | [v0.3](CL-2026-007-smith-ahmadi-v0.3.md) |
| **CL-2026-008** | Covey–Pikovski–Borregaard (2025) + Fromonteil et al. (2025) — distributed entanglement-enhanced clock networks | **UNDERDETERMINED** | Cross-probe mismatch `Δω` (classification); QFI / coherence-time budget (resolution) | [v0.2](CL-2026-008-clock-networks-v0.2.md) |

## Discriminant Conditions, in one sentence

The remaining gap for all three entries is at the **experimental-witness level**: an explicit nuisance-channel decomposition isolating the framework-relevant signal from technical decoherence. CL-2026-006's *theoretical* component of Discriminant D1 has been quantitatively grounded by the toolkit ([Module 3a — Sorci nuisance budget](../numerics/results/sorci_nuisance_budget_v0.1.json)); D2 / D3 remain experimental, as do the corresponding experimental discriminants for CL-2026-007 and CL-2026-008.

## What a "classification" is, and what it is not

A Ledger classification is *framework-relative*: it states how an external claim sits against the named Coastline under a declared measure, with explicit conditions for upgrade or downgrade. It does **not** assert that the external claim is correct or incorrect in the framework-independent sense. The verdict is a human-deliberated steward act (Lock-Key); numerical results from the toolkit *inform* it but do not auto-update it (toolkit Anti-Claim A5).

## Version history of this folder

Earlier versions of each entry are retained alongside the current version (e.g. `CL-2026-006-sorci-v0.4.md`, `v0.3.md`, `v0.2.md`, `v0.1.md`). Cite documents by version; never assume a citation to *v0.X* resolves to a later supersession.

For the broader context, see the [tutorial](../docs/tutorial.md), the [first Harbour View](../views/view-framework-overview-v0.1.md), or the [repository README](../README.md).
