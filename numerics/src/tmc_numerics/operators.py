"""Operator specifiers, Hamiltonian terms, observables, full-space embedding.

Phase 1 API contract §3, §4, and the ObservableSpec of §7.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping, Sequence

import numpy as np
import qutip as qt

from .exceptions import NonHermitianHamiltonianError
from .layout import SubsystemKind, SystemLayout


class Op(Enum):
    IDENTITY = "identity"
    SIGMA_X = "sigma_x"
    SIGMA_Y = "sigma_y"
    SIGMA_Z = "sigma_z"
    SIGMA_PLUS = "sigma_plus"
    SIGMA_MINUS = "sigma_minus"
    NUM = "num"
    DESTROY = "destroy"
    CREATE = "create"
    X_QUAD = "x_quad"
    P_QUAD = "p_quad"


_TWO_LEVEL_OPS = {
    Op.IDENTITY, Op.SIGMA_X, Op.SIGMA_Y, Op.SIGMA_Z, Op.SIGMA_PLUS, Op.SIGMA_MINUS,
}
_BOSONIC_OPS = {Op.IDENTITY, Op.NUM, Op.DESTROY, Op.CREATE, Op.X_QUAD, Op.P_QUAD}


@dataclass(frozen=True)
class LocalOp:
    op: Op | None = None
    power: int = 1
    qobj: "qt.Qobj | None" = None

    def __post_init__(self) -> None:
        if (self.op is None) == (self.qobj is None):
            raise ValueError("LocalOp requires exactly one of {op, qobj}")
        if self.power < 1:
            raise ValueError("LocalOp.power must be >= 1")


def _two_level_op(op: Op) -> "qt.Qobj":
    return {
        Op.IDENTITY: qt.qeye(2),
        Op.SIGMA_X: qt.sigmax(),
        Op.SIGMA_Y: qt.sigmay(),
        Op.SIGMA_Z: qt.sigmaz(),
        Op.SIGMA_PLUS: qt.sigmap(),
        Op.SIGMA_MINUS: qt.sigmam(),
    }[op]


def _bosonic_op(op: Op, dim: int) -> "qt.Qobj":
    a = qt.destroy(dim)
    if op is Op.IDENTITY:
        return qt.qeye(dim)
    if op is Op.NUM:
        return qt.num(dim)
    if op is Op.DESTROY:
        return a
    if op is Op.CREATE:
        return a.dag()
    if op is Op.X_QUAD:
        return (a + a.dag()) / np.sqrt(2)
    if op is Op.P_QUAD:
        return (a - a.dag()) / (1j * np.sqrt(2))
    raise ValueError(f"Unhandled bosonic op {op}")


def local_qobj(local: LocalOp, kind: SubsystemKind, dim: int) -> "qt.Qobj":
    """Build the local operator on a single subsystem's Hilbert space."""
    if local.qobj is not None:
        if local.qobj.dims != [[dim], [dim]]:
            raise ValueError(f"LocalOp.qobj dims {local.qobj.dims} != [[{dim}], [{dim}]]")
        base = local.qobj
    elif kind is SubsystemKind.TWO_LEVEL:
        if local.op not in _TWO_LEVEL_OPS:
            raise ValueError(f"Op {local.op} is not valid on a TWO_LEVEL subsystem")
        base = _two_level_op(local.op)
    else:
        if local.op not in _BOSONIC_OPS:
            raise ValueError(f"Op {local.op} is not valid on a BOSONIC_MODE subsystem")
        base = _bosonic_op(local.op, dim)
    return base if local.power == 1 else base ** local.power


def embed_operators(operators: Mapping[str, LocalOp], layout: SystemLayout) -> "qt.Qobj":
    """Tensor local operators into the full space (absent labels => identity)."""
    unknown = set(operators) - set(layout.labels())
    if unknown:
        raise KeyError(f"Operator targets {sorted(unknown)} not in layout {layout.labels()}")
    factors = []
    for sub in layout.subsystems:
        if sub.label in operators:
            factors.append(local_qobj(operators[sub.label], sub.kind, sub.dim))
        else:
            factors.append(qt.qeye(sub.dim))
    return qt.tensor(factors)


@dataclass(frozen=True)
class HamiltonianTerm:
    coefficient: float
    operators: Mapping[str, LocalOp]
    label: str = ""


@dataclass(frozen=True)
class ObservableSpec:
    operators: Mapping[str, LocalOp]
    coefficient: float = 1.0


def assemble_hamiltonian(
    terms: Sequence[HamiltonianTerm], layout: SystemLayout, *, atol: float = 1e-10
) -> "qt.Qobj":
    """Sum the Hamiltonian terms; raise if the total is not Hermitian."""
    total = 0.0 * embed_operators({}, layout)
    for term in terms:
        total = total + term.coefficient * embed_operators(term.operators, layout)
    nonherm = (total - total.dag()).norm()
    if nonherm > atol:
        raise NonHermitianHamiltonianError(
            f"Assembled Hamiltonian is not Hermitian (||H - H†|| = {nonherm:.3e})"
        )
    return total


def build_observable(spec, layout: SystemLayout) -> "qt.Qobj":
    """An observable from an ObservableSpec (or a raw full-space Qobj)."""
    if isinstance(spec, qt.Qobj):
        return spec
    return spec.coefficient * embed_operators(spec.operators, layout)
