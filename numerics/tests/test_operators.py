"""Phase 1 contract §3/§4 — operators, embedding, Hamiltonian assembly."""

import numpy as np
import pytest
import qutip as qt

from tmc_numerics import (
    HamiltonianTerm, LocalOp, NonHermitianHamiltonianError, Op, SystemLayout,
)
from tmc_numerics.operators import assemble_hamiltonian, embed_operators


def test_embed_places_on_correct_subsystem():
    layout = SystemLayout.clock_and_modes(1, 4)
    got = embed_operators({"clock": LocalOp(Op.SIGMA_Z)}, layout)
    expected = qt.tensor(qt.sigmaz(), qt.qeye(4))
    assert (got - expected).norm() < 1e-12


def test_assemble_hermitian_total():
    layout = SystemLayout.clock_and_modes(1, 4)
    terms = [
        HamiltonianTerm(0.5, {"clock": LocalOp(Op.SIGMA_Z)}, "clock free"),
        HamiltonianTerm(1.0, {"M1": LocalOp(Op.NUM)}, "mode free"),
    ]
    H = assemble_hamiltonian(terms, layout)
    assert (H - H.dag()).norm() < 1e-10


def test_non_hermitian_total_raises():
    layout = SystemLayout.carriers(1)
    terms = [HamiltonianTerm(1.0, {"carrier_00": LocalOp(Op.SIGMA_PLUS)})]
    with pytest.raises(NonHermitianHamiltonianError):
        assemble_hamiltonian(terms, layout)


def test_unknown_target_raises():
    layout = SystemLayout.carriers(1)
    with pytest.raises(KeyError):
        embed_operators({"nonexistent": LocalOp(Op.SIGMA_Z)}, layout)


def test_p_quad_power_two():
    layout = SystemLayout.clock_and_modes(1, 6)
    got = embed_operators({"M1": LocalOp(Op.P_QUAD, power=2)}, layout)
    a = qt.destroy(6)
    p = (a - a.dag()) / (1j * np.sqrt(2))
    expected = qt.tensor(qt.qeye(2), p ** 2)
    assert (got - expected).norm() < 1e-10


def test_localop_requires_exactly_one():
    with pytest.raises(ValueError):
        LocalOp()  # neither op nor qobj
    with pytest.raises(ValueError):
        LocalOp(op=Op.SIGMA_Z, qobj=qt.sigmaz())  # both


def test_wrong_kind_op_rejected():
    layout = SystemLayout.carriers(1)
    with pytest.raises(ValueError):
        embed_operators({"carrier_00": LocalOp(Op.NUM)}, layout)  # bosonic op on two-level
