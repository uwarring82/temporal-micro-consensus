"""Module 3b — open temporal instrument (Phase 3). Contract §6."""

import numpy as np
import pytest

from tmc_numerics.modules.open_instrument import (
    OpenInstrumentParams, carrier_distinguishability, redundancy_at, redundancy_curve,
    single_carrier_coherence,
)

_LN53 = np.log(5 / 3)  # γ_φ·t giving ε = 0.20 (c = 0.6)


def test_single_carrier_bridge():
    assert single_carrier_coherence(2.0, 0.5) == pytest.approx(np.exp(-1.0), abs=1e-6)
    assert carrier_distinguishability(1.0, _LN53) == pytest.approx(0.20, abs=1e-9)


def test_d5_cross_link_lands_on_analytic_pole():
    # the dynamical path must reproduce the validated MN §2 pole — to the D5 standard
    r = redundancy_at(OpenInstrumentParams(1.0, _LN53, 64, 0.10))
    assert r.m_delta == 9
    assert r.R_delta == pytest.approx(64 / 9, abs=1e-9)


def test_redundancy_collapses_with_dephasing_time():
    # per-carrier nuisance collapses the plateau with NO change in (product) entanglement (MN §5)
    rs = [redundancy_at(OpenInstrumentParams(1.0, t, 64, 0.10)).R_delta for t in (0.2, 0.5, 0.8, 1.2)]
    assert all(a > b for a, b in zip(rs, rs[1:]))


def test_redundancy_rises_with_N_at_fixed_epsilon():
    rs = [redundancy_at(OpenInstrumentParams(1.0, _LN53, n, 0.10)).R_delta for n in (16, 64, 256)]
    assert all(a < b for a, b in zip(rs, rs[1:]))


def test_eps_crit_rises_with_N():
    t_hi = -np.log(0.16)  # ε ≈ 0.42
    assert carrier_distinguishability(1.0, t_hi) == pytest.approx(0.42, abs=1e-9)
    assert redundancy_at(OpenInstrumentParams(1.0, t_hi, 64, 0.10)).R_delta is None     # undefined at small N
    big = redundancy_at(OpenInstrumentParams(1.0, t_hi, 256, 0.10))
    assert big.R_delta is not None and big.R_delta > 1.0                                # defined at large N


def test_redundancy_curve_grid_and_boundary():
    out = redundancy_curve(gamma_phi=1.0, t_values=[0.2, 0.8, 1.6], n_values=[16, 64], deficit=0.10)
    assert set(out["grid"]) == {16, 64}
    assert len(out["grid"][64]) == 3
    assert out["undefined_boundary"][64] == pytest.approx(1.6)  # R_δ undefined by γ_φ t = 1.6 at N=64
