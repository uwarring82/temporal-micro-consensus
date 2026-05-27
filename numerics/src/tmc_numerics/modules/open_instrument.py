"""Module 3b — open temporal instrument (Phase 3).

Contract: ``workplans/toolkit-module3b-open-instrument-contract-v0.1.md`` (D6-locked).

Dynamical bridge: a single-carrier pure-dephasing master equation (Phase-1 ``evolve``) sets the
per-carrier distinguishability ``ε(γ_φ, t) = (1 − e^{−γ_φ t})/2``; the Phase-2 ``iid`` ensemble +
``temporal_redundancy`` then give ``R_δ(N, ε)`` — the candidate worked exemplar for Anti-Claim #6
**within the assumed-einselection regime** (contract §4). Anti-Claim #6 remains open.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np
import qutip as qt

from ..anchors import RedundancyResult, TemporalRecordEnsemble, temporal_redundancy
from ..channels import ChannelKind, LindbladChannel
from ..layout import SystemLayout
from ..prep import clock_superposition
from ..system import MasterEquationSystem


@dataclass(frozen=True)
class OpenInstrumentParams:
    gamma_phi: float
    t: float
    n_carriers: int
    deficit: float = 0.10


def single_carrier_coherence(gamma_phi: float, t: float) -> float:
    """``c = 2|ρ₀₁|`` of ``|+⟩`` evolved under ``DEPHASING(γ_φ)`` for ``t`` (= e^{−γ_φ t})."""
    layout = SystemLayout.carriers(1)
    sysm = MasterEquationSystem(
        layout, [], channels=[LindbladChannel("carrier_00", ChannelKind.DEPHASING, gamma_phi)]
    )
    res = sysm.evolve(clock_superposition(), np.asarray([0.0, t]), store_states=True)
    return float(2.0 * abs(res.final_state.full()[0, 1]))


def carrier_distinguishability(gamma_phi: float, t: float) -> float:
    """``ε = (1 − c)/2`` (trace-distance / Helstrom / phase-bin projective — all coincide)."""
    return (1.0 - single_carrier_coherence(gamma_phi, t)) / 2.0


def carrier_conditional_states(eps: float) -> "dict[int, qt.Qobj]":
    """Computational-basis MN §2 product-pole states (Hadamard image of ½(I ± c σ_x))."""
    return {
        0: (1 - eps) * qt.fock_dm(2, 0) + eps * qt.fock_dm(2, 1),
        1: (1 - eps) * qt.fock_dm(2, 1) + eps * qt.fock_dm(2, 0),
    }


def redundancy_at(params: OpenInstrumentParams) -> RedundancyResult:
    eps = carrier_distinguishability(params.gamma_phi, params.t)
    ens = TemporalRecordEnsemble.iid(carrier_conditional_states(eps), params.n_carriers)
    return temporal_redundancy(ens, params.deficit)


def redundancy_curve(*, gamma_phi: float, t_values: Sequence[float], n_values: Sequence[int],
                     deficit: float = 0.10) -> dict:
    """R_δ(N, γ_φ t) grid + the undefined boundary (first t where the threshold stops being reached)."""
    eps_of_t = {float(t): carrier_distinguishability(gamma_phi, t) for t in t_values}
    grid: dict = {}
    boundary: dict = {}
    for n in n_values:
        row = []
        crit = None
        for t in t_values:
            eps = eps_of_t[float(t)]
            ens = TemporalRecordEnsemble.iid(carrier_conditional_states(eps), n)
            r = temporal_redundancy(ens, deficit)
            row.append((float(t), eps, r.R_delta))
            if r.R_delta is None and crit is None:
                crit = float(t)
        grid[int(n)] = row
        boundary[int(n)] = crit
    return {"gamma_phi": gamma_phi, "deficit": deficit, "grid": grid, "undefined_boundary": boundary}
