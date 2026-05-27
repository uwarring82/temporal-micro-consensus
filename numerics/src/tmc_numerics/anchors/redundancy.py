"""Temporal-redundancy functional R_δ (Phase 2 contract §2).

R_δ = n / m_δ, m_δ = min{ m : I(m) ≥ (1−δ)·H_T }; R_δ undefined (None) if never reached.
The None ("undefined") case is distinct from R_δ == 1 (threshold reached only by the whole set).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .ensemble import InfoMode, TemporalRecordEnsemble, partial_information


@dataclass
class RedundancyResult:
    R_delta: float | None
    m_delta: int | None
    deficit: float
    H_T: float
    info_curve: list
    mode: str


def temporal_redundancy(ensemble: TemporalRecordEnsemble, deficit: float, *,
                        mode: InfoMode = InfoMode.PER_CARRIER, fragment_order=None) -> RedundancyResult:
    n = ensemble.n_carriers
    H_T = ensemble.pointer.H_T_bits()
    threshold = (1.0 - deficit) * H_T
    order = list(range(n)) if fragment_order is None else list(fragment_order)

    curve: list = []
    m_delta = None
    for m in range(1, n + 1):
        fragment = m if ensemble.iid_carrier_states is not None else order[:m]
        info = partial_information(ensemble, fragment, mode=mode)
        curve.append((m, info))
        if info >= threshold - 1e-12:
            m_delta = m
            break

    R = (n / m_delta) if m_delta is not None else None
    return RedundancyResult(
        R_delta=R, m_delta=m_delta, deficit=deficit, H_T=float(H_T),
        info_curve=curve, mode=mode.value,
    )
