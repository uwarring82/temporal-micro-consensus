"""Classification anchor I(C:M) and resolution anchor F[τ] (Phase 2 contract §2).

`mutual_information` is a CLASSIFICATION anchor; `quantum_fisher` is the RESOLUTION
anchor and must NOT be read as a classifier (the CL-2026-007 v0.1 failure mode).
"""

from __future__ import annotations

import numpy as np
import qutip as qt


def _as_state(state) -> "qt.Qobj":
    fs = getattr(state, "final_state", None)
    rho = fs if fs is not None else state
    return rho * rho.dag() if rho.isket else rho


def _layout_of(state, layout):
    return layout if layout is not None else getattr(state, "layout", None)


def _resolve(group, layout):
    out = []
    for g in group:
        if isinstance(g, int):
            out.append(g)
        elif layout is not None:
            out.append(layout.index(g))
        else:
            raise ValueError("label-based partitions need a layout (pass an EvolutionResult or layout=)")
    return out


def mutual_information(state, partition, *, layout=None, base: str = "bits") -> float:
    """Quantum I(A:B) = S(ρ_A) + S(ρ_B) − S(ρ_AB) for a bipartition of layout subsystems."""
    rho = _as_state(state)
    lay = _layout_of(state, layout)
    group_a, group_b = partition
    ia, ib = _resolve(list(group_a), lay), _resolve(list(group_b), lay)
    if set(ia) & set(ib):
        raise ValueError("partition groups must be disjoint")
    b = 2 if base == "bits" else (np.e if base in ("nats", "e") else float(base))
    s_a = qt.entropy_vn(rho.ptrace(ia), base=b)
    s_b = qt.entropy_vn(rho.ptrace(ib), base=b)
    s_ab = qt.entropy_vn(rho.ptrace(sorted(ia + ib)), base=b)
    return float(s_a + s_b - s_ab)


def quantum_fisher(state, generator: "qt.Qobj") -> float:
    """QFI for ρ(τ) = e^{-iGτ} ρ e^{+iGτ}:  F = 2 Σ_{i,j} (λ_i−λ_j)²/(λ_i+λ_j) |⟨i|G|j⟩|².

    Dimensionful ([τ]⁻²). Reduces to 4·Var(G) for a pure state.
    """
    rho = _as_state(state)
    evals, evecs = rho.eigenstates()
    gv = [generator * evecs[j] for j in range(len(evals))]
    f = 0.0
    for i in range(len(evals)):
        for j in range(len(evals)):
            s = evals[i] + evals[j]
            if s <= 1e-15:
                continue
            gij = evecs[i].overlap(gv[j])
            f += 2.0 * (evals[i] - evals[j]) ** 2 / s * abs(gij) ** 2
    return float(f)
