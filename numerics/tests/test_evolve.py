"""Phase 1 contract §6/§7 — evolve contract, closed system, diagnostics, failures."""

import numpy as np
import pytest

from tmc_numerics import (
    ChannelKind, HamiltonianTerm, LayoutMismatchError, LindbladChannel, LocalOp,
    MasterEquationSystem, ObservableSpec, Op, SolverOptions, Subsystem,
    SubsystemKind, SystemLayout, clock_superposition, fock_mode,
)


def test_closed_system_preserves_trace_and_purity():
    layout = SystemLayout.carriers(1)
    omega = 2 * np.pi
    sysm = MasterEquationSystem(layout, [HamiltonianTerm(omega / 2, {"carrier_00": LocalOp(Op.SIGMA_Z)})])
    res = sysm.evolve(clock_superposition(), np.linspace(0, 1, 11))
    assert res.converged
    for st in res.states:
        assert np.isclose(complex(st.tr()).real, 1.0, atol=1e-8)
        assert np.isclose(complex((st * st).tr()).real, 1.0, atol=1e-6)


def test_layout_mismatch_on_evolve():
    layout = SystemLayout.clock_and_modes(1, 5)
    sysm = MasterEquationSystem(layout, [])
    with pytest.raises(LayoutMismatchError):
        sysm.evolve(clock_superposition(), [0.0, 1.0])  # dims [2] vs layout [2, 5]


def test_truncation_diagnostic_flags_overflow():
    dim = 4  # deliberately tiny
    layout = SystemLayout((Subsystem("M", SubsystemKind.BOSONIC_MODE, dim),))
    sysm = MasterEquationSystem(layout, [], channels=[LindbladChannel("M", ChannelKind.HEATING, 2.0)])
    res = sysm.evolve(fock_mode(dim=dim, n=0), np.linspace(0, 3, 16))
    assert res.diagnostics.truncation_ok is False
    assert res.diagnostics.max_fock_population["M"] > 1e-6


def test_truncation_ok_when_well_truncated():
    dim = 40
    layout = SystemLayout((Subsystem("M", SubsystemKind.BOSONIC_MODE, dim),))
    sysm = MasterEquationSystem(layout, [], channels=[LindbladChannel("M", ChannelKind.HEATING, 1.0)])
    res = sysm.evolve(fock_mode(dim=dim, n=0), np.linspace(0, 2, 11))
    assert res.diagnostics.truncation_ok is True


def test_expectation_only_mode():
    layout = SystemLayout.carriers(1)
    sysm = MasterEquationSystem(layout, [HamiltonianTerm(1.0, {"carrier_00": LocalOp(Op.SIGMA_Z)})])
    res = sysm.evolve(
        clock_superposition(), np.linspace(0, 1, 5),
        e_ops={"sx": ObservableSpec({"carrier_00": LocalOp(Op.SIGMA_X)})},
        store_states=False,
    )
    assert res.states is None
    assert res.final_state is not None
    assert "sx" in res.expect and len(res.expect["sx"]) == 5


def test_mcsolve_not_selectable():
    layout = SystemLayout.carriers(1)
    sysm = MasterEquationSystem(layout, [])
    opts = SolverOptions()
    object.__setattr__(opts, "solver", "mcsolve")  # force an unsupported selection
    with pytest.raises(NotImplementedError):
        sysm.evolve(clock_superposition(), [0.0, 1.0], options=opts)
