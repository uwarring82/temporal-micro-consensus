"""Phase 1 contract §2 — SystemLayout / Subsystem."""

import pytest
import qutip as qt

from tmc_numerics import LayoutMismatchError, Subsystem, SubsystemKind, SystemLayout


def test_clock_and_modes_order_and_dims():
    layout = SystemLayout.clock_and_modes(n_modes=2, mode_cutoffs=[10, 8])
    assert layout.labels() == ["clock", "M1", "M2"]
    assert layout.dims() == [2, 10, 8]
    assert layout.index("M2") == 2
    assert layout.subsystem("M1").dim == 10


def test_clock_and_modes_scalar_cutoff():
    layout = SystemLayout.clock_and_modes(n_modes=3, mode_cutoffs=6)
    assert layout.dims() == [2, 6, 6, 6]


def test_carriers_order():
    layout = SystemLayout.carriers(3)
    assert layout.labels() == ["carrier_00", "carrier_01", "carrier_02"]
    assert layout.dims() == [2, 2, 2]


def test_two_level_dim_must_be_2():
    with pytest.raises(ValueError):
        Subsystem("clock", SubsystemKind.TWO_LEVEL, 3)


def test_bosonic_dim_min_2():
    with pytest.raises(ValueError):
        Subsystem("M", SubsystemKind.BOSONIC_MODE, 1)


def test_duplicate_labels_rejected():
    with pytest.raises(ValueError):
        SystemLayout((Subsystem("a", SubsystemKind.TWO_LEVEL, 2),
                      Subsystem("a", SubsystemKind.TWO_LEVEL, 2)))


def test_validate_state_mismatch():
    layout = SystemLayout.clock_and_modes(1, 5)
    bad = qt.fock_dm(2, 0)  # only the clock factor, missing the mode
    with pytest.raises(LayoutMismatchError):
        layout.validate_state(bad)
