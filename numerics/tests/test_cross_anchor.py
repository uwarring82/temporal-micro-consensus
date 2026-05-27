"""Cross-anchor invariants — the resolution/classification split (Phase 2 contract §5).

The resolution anchor F[τ] is NOT a classifier (the CL-2026-007 v0.1 failure mode); the
load-bearing invariant is its ANTI-CORRELATION with the classification anchor R_δ:
toward the anti-redundant pole, F[τ] rises (∝ N²) while R_δ falls (→ 1).
"""

import numpy as np
import pytest
import qutip as qt

from tmc_numerics import SystemLayout
from tmc_numerics.anchors import (
    InfoMode, TemporalRecordEnsemble, quantum_fisher, temporal_redundancy,
)

_PLUS = (qt.basis(2, 0) + qt.basis(2, 1)).unit()


def _collective_sz_half(n):
    terms = []
    for k in range(n):
        ops = [qt.qeye(2)] * n
        ops[k] = qt.sigmaz()
        terms.append(qt.tensor(ops))
    return sum(terms) / 2


def _product_plus(n):
    return qt.tensor([_PLUS] * n)


def _ghz_ket(n):
    return (qt.tensor([qt.basis(2, 0)] * n) + qt.tensor([qt.basis(2, 1)] * n)).unit()


def _carrier(e, t):
    return (1 - e) * qt.fock_dm(2, t) + e * qt.fock_dm(2, 1 - t)


def _product_ensemble(e, n=64):
    return TemporalRecordEnsemble.iid({0: _carrier(e, 0), 1: _carrier(e, 1)}, n)


@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_fisher_is_extensive_in_independent_carriers(n):
    """F_τ(m) = m · F_1 — additive over independent carriers (resolution anchor)."""
    qfi = quantum_fisher(_product_plus(n), _collective_sz_half(n))
    assert qfi == pytest.approx(float(n), abs=1e-9)


def test_fisher_and_redundancy_anticorrelate():
    """Toward the anti-redundant pole: F[τ] rises (N² vs N) while R_δ falls (1 vs ≫1)."""
    n = 4
    qfi_ghz = quantum_fisher(_ghz_ket(n), _collective_sz_half(n))       # N² = 16
    qfi_product = quantum_fisher(_product_plus(n), _collective_sz_half(n))  # N = 4
    assert qfi_ghz > qfi_product

    rd_ghz = temporal_redundancy(
        TemporalRecordEnsemble.from_evolution(
            {0: _ghz_ket(n) * _ghz_ket(n).dag(),
             1: (lambda k: k * k.dag())(
                 (qt.tensor([qt.basis(2, 0)] * n) - qt.tensor([qt.basis(2, 1)] * n)).unit())},
            SystemLayout.carriers(n)),
        0.10, mode=InfoMode.HOLEVO).R_delta
    rd_product = temporal_redundancy(_product_ensemble(0.20, n=64), 0.10).R_delta

    assert rd_ghz == pytest.approx(1.0)
    assert rd_product is not None and rd_product > rd_ghz
    # the anti-correlation: higher Fisher  <-> lower redundancy
    assert (qfi_ghz > qfi_product) and (rd_ghz < rd_product)


def test_per_carrier_nuisance_collapses_plateau_without_entanglement():
    """Raising the per-carrier flip e lowers R_δ with NO change in (product) entanglement."""
    r = [temporal_redundancy(_product_ensemble(e), 0.10).R_delta for e in (0.10, 0.20, 0.30)]
    assert r[0] > r[1] > r[2]  # 16.0 > 7.1 > 2.9, all unentangled product records
