"""Temporal-record ensemble and partial information (Phase 2 contract §1).

`R_δ` is `I(T : F_m)` between a classical pointer T and a fragment read-out — not a
state-intrinsic quantity. The ensemble composes Phase-1 evolved states + ReadoutModel
into the redundancy substrate, with two representations:

- iid:   a single-carrier conditional-state map + a count n. I(m) is the m-fold i.i.d.
         channel MI (binomial for binary T). Scales to any n; never builds a 2^n state.
- joint: a full carrier-joint state per pointer value (small n); fragments via ptrace.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from math import comb
from typing import Mapping, Sequence

import numpy as np
import qutip as qt


class InfoMode(Enum):
    PER_CARRIER = "per_carrier"  # classical MI of independent per-carrier POVM outcomes (default)
    HOLEVO = "holevo"            # Holevo χ; the ideal global read-out (MN §2); upper bound in general


@dataclass(frozen=True)
class TemporalPointer:
    dim: int = 2
    prior: tuple[float, ...] | None = None  # default uniform

    def probs(self) -> tuple[float, ...]:
        if self.prior is None:
            return tuple([1.0 / self.dim] * self.dim)
        if len(self.prior) != self.dim or abs(sum(self.prior) - 1.0) > 1e-12:
            raise ValueError("pointer prior must have length dim and sum to 1")
        return tuple(self.prior)

    def H_T_bits(self) -> float:
        p = np.array(self.probs())
        return float(-(p[p > 0] * np.log2(p[p > 0])).sum())


@dataclass(frozen=True)
class TemporalRecordEnsemble:
    pointer: TemporalPointer
    n_carriers: int
    iid_carrier_states: Mapping[int, "qt.Qobj"] | None = None
    joint_states: Mapping[int, "qt.Qobj"] | None = None
    joint_layout: object | None = None
    readout: object | None = None  # Phase-1 ReadoutModel (per-carrier detection layer)
    pointer_basis: str = "computational"

    def __post_init__(self) -> None:
        if (self.iid_carrier_states is None) == (self.joint_states is None):
            raise ValueError("provide exactly one of {iid_carrier_states, joint_states}")
        if self.pointer_basis != "computational":
            raise NotImplementedError("v0.1 supports only the computational pointer basis")

    @classmethod
    def iid(cls, conditional_carrier: Mapping[int, "qt.Qobj"], n_carriers: int,
            pointer: TemporalPointer | None = None, *, readout=None) -> "TemporalRecordEnsemble":
        return cls(pointer=pointer or TemporalPointer(), n_carriers=n_carriers,
                   iid_carrier_states=dict(conditional_carrier), readout=readout)

    @classmethod
    def from_evolution(cls, results: Mapping[int, object], joint_layout,
                       pointer: TemporalPointer | None = None, *, readout=None) -> "TemporalRecordEnsemble":
        states: dict = {}
        for t, r in results.items():
            fs = getattr(r, "final_state", None)
            states[t] = fs if fs is not None else r
        return cls(pointer=pointer or TemporalPointer(), n_carriers=len(joint_layout.subsystems),
                   joint_states=states, joint_layout=joint_layout, readout=readout)


# --- information helpers (bits) ---------------------------------------------

def _detection_eps(ensemble: TemporalRecordEnsemble) -> float:
    ro = ensemble.readout
    return float(getattr(ro, "detection_infidelity", 0.0)) if ro is not None else 0.0


def _classical_mi_bits(prior: Sequence[float], cond: np.ndarray) -> float:
    """cond[t, o] = P(outcome o | T=t); returns I(T:O) in bits."""
    prior = np.asarray(prior)
    p_o = (prior[:, None] * cond).sum(axis=0)
    mi = 0.0
    for t in range(cond.shape[0]):
        for o in range(cond.shape[1]):
            joint = prior[t] * cond[t, o]
            if joint > 0 and p_o[o] > 0:
                mi += joint * np.log2(cond[t, o] / p_o[o])
    return float(max(mi, 0.0))


def _iid_binary_counts_mi(p_read1: Sequence[float], prior: Sequence[float], m: int) -> float:
    """MI between T and the count of '1's over m i.i.d. binary carriers."""
    d = len(prior)
    cond = np.zeros((d, m + 1))
    for t in range(d):
        p = p_read1[t]
        for k in range(m + 1):
            cond[t, k] = comb(m, k) * (p ** k) * ((1.0 - p) ** (m - k))
    return _classical_mi_bits(prior, cond)


def _bitflip_matrix(m: int, eps: float) -> np.ndarray:
    F = np.array([[1.0 - eps, eps], [eps, 1.0 - eps]])
    M = np.array([[1.0]])
    for _ in range(m):
        M = np.kron(M, F)
    return M


def _holevo_bits(states: Sequence["qt.Qobj"], prior: Sequence[float]) -> float:
    rho_bar = sum(prior[t] * states[t] for t in range(len(prior)))
    chi = qt.entropy_vn(rho_bar, base=2)
    for t in range(len(prior)):
        chi -= prior[t] * qt.entropy_vn(states[t], base=2)
    return float(max(chi, 0.0))


def partial_information(ensemble: TemporalRecordEnsemble, fragment, *,
                        mode: InfoMode = InfoMode.PER_CARRIER) -> float:
    """I(T : F) in bits for a fragment (iid: int count; joint: carrier-index sequence)."""
    prior = ensemble.pointer.probs()
    d = ensemble.pointer.dim

    if ensemble.iid_carrier_states is not None:
        if d != 2:
            raise NotImplementedError("iid v0.1 supports a binary pointer only")
        m = int(fragment)
        eps = _detection_eps(ensemble)
        p_read1 = []
        for t in range(d):
            rho = ensemble.iid_carrier_states[t]
            if rho.shape[0] != 2:
                raise NotImplementedError("iid v0.1 supports two-level carriers only")
            if mode is InfoMode.HOLEVO and abs(rho.full()[0, 1]) > 1e-9:
                raise NotImplementedError(
                    "iid HOLEVO requires carriers diagonal in the pointer basis"
                )
            p1 = float(np.real(rho.full()[1, 1]))
            p_read1.append((1.0 - eps) * p1 + eps * (1.0 - p1))
        return _iid_binary_counts_mi(p_read1, prior, m)

    indices = list(fragment)
    reduced = [ensemble.joint_states[t].ptrace(indices) for t in range(d)]
    if mode is InfoMode.HOLEVO:
        return _holevo_bits(reduced, prior)
    # PER_CARRIER: outcome = computational bitstring; P(o|t) = diag(ρ_F^{(t)}) (+ per-carrier flips)
    m = len(indices)
    eps = _detection_eps(ensemble)
    cond = np.zeros((d, 2 ** m))
    flip = _bitflip_matrix(m, eps) if eps > 0 else None
    for t in range(d):
        diag = np.real(np.asarray(reduced[t].full()).diagonal()).copy()
        cond[t] = flip @ diag if flip is not None else diag
    return _classical_mi_bits(prior, cond)
