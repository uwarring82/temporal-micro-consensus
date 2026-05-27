"""Anchor measures I(C:M) and F[τ] (Phase 2 contract §2)."""

import numpy as np
import pytest
import qutip as qt

from tmc_numerics.anchors import mutual_information, quantum_fisher

_PLUS = (qt.basis(2, 0) + qt.basis(2, 1)).unit()
_BELL = (qt.tensor(qt.basis(2, 0), qt.basis(2, 0)) + qt.tensor(qt.basis(2, 1), qt.basis(2, 1))).unit()


def test_mutual_information_bell_is_two_bits():
    assert mutual_information(_BELL, ([0], [1])) == pytest.approx(2.0, abs=1e-9)


def test_mutual_information_product_is_zero():
    rho = qt.tensor(_PLUS, qt.basis(2, 0))
    assert mutual_information(rho, ([0], [1])) == pytest.approx(0.0, abs=1e-9)


def test_mutual_information_partition_must_be_disjoint():
    with pytest.raises(ValueError):
        mutual_information(_BELL, ([0], [0]))


def test_qfi_pure_state_is_four_variance():
    # |+>, G = σ_z/2 : QFI = 4 Var(G) = 4·(1/4) = 1
    assert quantum_fisher(_PLUS, qt.sigmaz() / 2) == pytest.approx(1.0, abs=1e-9)


def test_qfi_ghz_heisenberg_vs_product_shot_noise():
    G = (qt.tensor(qt.sigmaz(), qt.qeye(2)) + qt.tensor(qt.qeye(2), qt.sigmaz())) / 2
    assert quantum_fisher(_BELL, G) == pytest.approx(4.0, abs=1e-9)               # N² (Heisenberg)
    assert quantum_fisher(qt.tensor(_PLUS, _PLUS), G) == pytest.approx(2.0, abs=1e-9)  # N (shot noise)
