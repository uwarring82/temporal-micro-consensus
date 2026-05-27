"""Preparation primitives (Phase 1 API contract §8).

Local primitives return LOCAL density matrices; `product_state` tensors them into
the full-space state on a SystemLayout. Preparation infidelity is LOCAL (symmetric
depolarising toward the local maximally mixed state).
"""

from __future__ import annotations

from typing import Mapping

import numpy as np
import qutip as qt

from .exceptions import LayoutMismatchError
from .layout import SystemLayout


def _depolarize(rho: "qt.Qobj", eps: float, dim: int) -> "qt.Qobj":
    if not 0.0 <= eps <= 1.0:
        raise ValueError(f"prep_infidelity must be in [0, 1], got {eps}")
    if eps == 0.0:
        return rho
    return (1.0 - eps) * rho + eps * qt.qeye(dim) / dim


def clock_superposition(*, relative_phase: float = 0.0, prep_infidelity: float = 0.0) -> "qt.Qobj":
    ket = (qt.basis(2, 0) + np.exp(1j * relative_phase) * qt.basis(2, 1)).unit()
    return _depolarize(ket * ket.dag(), prep_infidelity, 2)


def two_level_state(*, ket: "qt.Qobj", prep_infidelity: float = 0.0) -> "qt.Qobj":
    if ket.dims[0] != [2]:
        raise LayoutMismatchError(f"two_level_state ket dims {ket.dims} not a 2-level ket")
    ket = ket.unit()
    return _depolarize(ket * ket.dag(), prep_infidelity, 2)


def squeezed_mode(
    *, dim: int, r: float, theta: float = 0.0, n_thermal: float = 0.0, prep_infidelity: float = 0.0
) -> "qt.Qobj":
    """Squeezed (thermal) motional state; ⟨n⟩ = sinh²r at n_thermal = 0."""
    S = qt.squeeze(dim, r * np.exp(1j * theta))
    if n_thermal <= 0.0:
        psi = S * qt.basis(dim, 0)
        rho = psi * psi.dag()
    else:
        rho = S * qt.thermal_dm(dim, n_thermal) * S.dag()
    return _depolarize(rho, prep_infidelity, dim)


def coherent_mode(*, dim: int, alpha: complex, prep_infidelity: float = 0.0) -> "qt.Qobj":
    return _depolarize(qt.coherent_dm(dim, alpha), prep_infidelity, dim)


def thermal_mode(*, dim: int, n_thermal: float, prep_infidelity: float = 0.0) -> "qt.Qobj":
    return _depolarize(qt.thermal_dm(dim, n_thermal), prep_infidelity, dim)


def fock_mode(*, dim: int, n: int, prep_infidelity: float = 0.0) -> "qt.Qobj":
    return _depolarize(qt.fock_dm(dim, n), prep_infidelity, dim)


def product_state(layout: SystemLayout, parts: Mapping[str, "qt.Qobj"]) -> "qt.Qobj":
    """Tensor the per-subsystem LOCAL states in layout order.

    Unspecified subsystems default to ground (TWO_LEVEL) / vacuum (BOSONIC_MODE).
    """
    unknown = set(parts) - set(layout.labels())
    if unknown:
        raise KeyError(f"product_state parts {sorted(unknown)} not in layout {layout.labels()}")
    factors = []
    for sub in layout.subsystems:
        if sub.label in parts:
            local = parts[sub.label]
            if local.isket:
                local = local * local.dag()
            if local.dims[0] != [sub.dim]:
                raise LayoutMismatchError(
                    f"part {sub.label!r} dims {local.dims[0]} != [{sub.dim}]"
                )
            factors.append(local)
        else:
            factors.append(qt.fock_dm(sub.dim, 0))
    return qt.tensor(factors)
