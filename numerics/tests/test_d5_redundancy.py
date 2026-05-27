"""D5 regression gate — reproduce the MN v0.2 §2 analytic poles (Phase 2 contract §3)."""

from math import comb, log2

import numpy as np
import pytest
import qutip as qt

from tmc_numerics import SystemLayout
from tmc_numerics.anchors import (
    InfoMode, TemporalRecordEnsemble, partial_information, temporal_redundancy,
)


# --- reference: MN v0.2 Appendix A (exact) ---------------------------------

def _h2(p):
    if p <= 0 or p >= 1:
        return 0.0
    return -p * log2(p) - (1 - p) * log2(1 - p)


def _I_product_ref(m, e):
    """MN Appendix A I_product(m, e): MI between binary T and m i.i.d. flip-e copies."""
    hcond = 0.0
    for k in range(m + 1):
        p0 = comb(m, k) * e ** k * (1 - e) ** (m - k)
        p1 = comb(m, k) * (1 - e) ** k * e ** (m - k)
        pk = 0.5 * p0 + 0.5 * p1
        if pk > 0:
            hcond += pk * _h2(0.5 * p1 / pk)
    return 1.0 - hcond


def _carrier(e, t):
    """Single-carrier conditional state ρ^{(t)} = (1−e)|t⟩⟨t| + e|1−t⟩⟨1−t|."""
    return (1 - e) * qt.fock_dm(2, t) + e * qt.fock_dm(2, 1 - t)


def _product_ensemble(e, n=64):
    return TemporalRecordEnsemble.iid({0: _carrier(e, 0), 1: _carrier(e, 1)}, n)


def _ghz_ensemble(n=4):
    k0 = (qt.tensor([qt.basis(2, 0)] * n) + qt.tensor([qt.basis(2, 1)] * n)).unit()
    k1 = (qt.tensor([qt.basis(2, 0)] * n) - qt.tensor([qt.basis(2, 1)] * n)).unit()
    return TemporalRecordEnsemble.from_evolution(
        {0: k0 * k0.dag(), 1: k1 * k1.dag()}, SystemLayout.carriers(n)
    )


# --- 3a: redundant (product) pole ------------------------------------------

@pytest.mark.parametrize("m", [1, 2, 4, 8, 16, 32, 48, 64])
def test_product_partial_information_matches_appendix_a(m):
    ens = _product_ensemble(0.20)
    assert abs(partial_information(ens, m) - _I_product_ref(m, 0.20)) <= 1e-9


@pytest.mark.parametrize(
    "e, m_delta, R",
    [(0.10, 4, 16.0), (0.20, 9, 64 / 9), (0.30, 22, 64 / 22)],
)
def test_product_redundancy_defined(e, m_delta, R):
    res = temporal_redundancy(_product_ensemble(e), 0.10)
    assert res.m_delta == m_delta
    assert res.R_delta == pytest.approx(R)


@pytest.mark.parametrize("e", [0.40, 0.45])
def test_product_redundancy_undefined(e):
    res = temporal_redundancy(_product_ensemble(e), 0.10)
    assert res.R_delta is None and res.m_delta is None


def test_per_carrier_equals_holevo_on_product_pole():
    ens = _product_ensemble(0.20)
    for m in (1, 4, 16, 64):
        assert partial_information(ens, m, mode=InfoMode.PER_CARRIER) == pytest.approx(
            partial_information(ens, m, mode=InfoMode.HOLEVO), abs=1e-12
        )


# --- 3b: anti-redundant (GHZ-shadow) pole ----------------------------------

def test_ghz_proper_fragments_carry_zero():
    ghz = _ghz_ensemble(4)
    for frag in ([0], [0, 1], [0, 1, 2]):
        assert partial_information(ghz, frag, mode=InfoMode.HOLEVO) == pytest.approx(0.0, abs=1e-12)


def test_ghz_full_set_carries_H_T():
    ghz = _ghz_ensemble(4)
    assert partial_information(ghz, [0, 1, 2, 3], mode=InfoMode.HOLEVO) == pytest.approx(1.0, abs=1e-12)


def test_ghz_redundancy_is_one_not_undefined():
    res = temporal_redundancy(_ghz_ensemble(4), 0.10, mode=InfoMode.HOLEVO)
    assert res.m_delta == 4
    assert res.R_delta == pytest.approx(1.0)


def test_ghz_per_carrier_reads_zero():
    """NEGATIVE confirmation, not a bug: a per-carrier computational read-out cannot see
    the cat's relative phase, so I(N)=0 — which is exactly why HOLEVO (ideal global) is
    required for the anti-redundant pole (MN §2)."""
    ghz = _ghz_ensemble(4)
    assert partial_information(ghz, [0, 1, 2, 3], mode=InfoMode.PER_CARRIER) == pytest.approx(0.0, abs=1e-12)


# --- the headline contrast: same N carriers, different R_δ -----------------

def test_multipartite_neq_redundant_headline():
    product = temporal_redundancy(_product_ensemble(0.20, n=64), 0.10)
    ghz = temporal_redundancy(_ghz_ensemble(4), 0.10, mode=InfoMode.HOLEVO)
    assert product.R_delta == pytest.approx(64 / 9)  # ≈ 7.1
    assert ghz.R_delta == pytest.approx(1.0)
    assert product.R_delta > ghz.R_delta
