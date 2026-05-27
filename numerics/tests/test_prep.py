"""Phase 1 contract §8 — preparation primitives."""

import numpy as np
import pytest
import qutip as qt

from tmc_numerics import (
    LayoutMismatchError, SystemLayout, clock_superposition, fock_mode,
    product_state, squeezed_mode,
)


def test_squeezed_mean_occupation():
    dim, r = 40, 0.8
    rho = squeezed_mode(dim=dim, r=r)
    assert np.isclose(float(qt.expect(qt.num(dim), rho)), np.sinh(r) ** 2, atol=1e-3)


def test_squeezed_quadrature_below_vacuum():
    dim, r = 40, 0.6
    rho = squeezed_mode(dim=dim, r=r)
    a = qt.destroy(dim)
    x = (a + a.dag()) / np.sqrt(2)
    var_x = float(qt.expect(x * x, rho) - qt.expect(x, rho) ** 2)
    assert var_x < 0.5  # vacuum variance is 0.5


def test_product_state_dims_and_trace():
    layout = SystemLayout.clock_and_modes(1, 6)
    rho = product_state(layout, {"clock": clock_superposition(), "M1": squeezed_mode(dim=6, r=0.3)})
    assert rho.dims[0] == [2, 6]
    assert np.isclose(complex(rho.tr()).real, 1.0, atol=1e-9)


def test_product_state_defaults_to_ground_vacuum():
    layout = SystemLayout.clock_and_modes(1, 5)
    rho = product_state(layout, {})
    expected = qt.tensor(qt.fock_dm(2, 0), qt.fock_dm(5, 0))
    assert (rho - expected).norm() < 1e-12


def test_product_state_dim_mismatch_rejected():
    layout = SystemLayout.clock_and_modes(1, 6)
    with pytest.raises(LayoutMismatchError):
        product_state(layout, {"M1": fock_mode(dim=5, n=0)})  # 5 != layout's 6


def test_prep_infidelity_lowers_purity():
    eps = 0.2
    rho = clock_superposition(prep_infidelity=eps)
    purity = complex((rho * rho).tr()).real
    assert np.isclose(purity, 1.0 - eps + eps ** 2 / 2.0, atol=1e-9)  # depolarised pure qubit


def test_prep_infidelity_out_of_range():
    with pytest.raises(ValueError):
        clock_superposition(prep_infidelity=1.5)
