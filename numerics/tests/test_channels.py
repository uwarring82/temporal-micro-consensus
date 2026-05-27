"""Phase 1 contract §5.2/§5.3 — Lindblad channels and WHITE drive noise (closed-form)."""

import numpy as np
import pytest

from tmc_numerics import (
    ChannelKind, DriveNoise, LindbladChannel, LocalOp, MasterEquationSystem,
    NoiseModel, ObservableSpec, Op, Subsystem, SubsystemKind, SystemLayout,
    clock_superposition, fock_mode,
)


def _mode_layout(dim):
    return SystemLayout((Subsystem("M", SubsystemKind.BOSONIC_MODE, dim),))


def _num_obs():
    return {"n": ObservableSpec({"M": LocalOp(Op.NUM)})}


def test_dephasing_coherence_decay():
    layout = SystemLayout.carriers(1)
    gamma = 1.0
    sysm = MasterEquationSystem(
        layout, [], channels=[LindbladChannel("carrier_00", ChannelKind.DEPHASING, gamma)]
    )
    times = np.linspace(0, 2, 21)
    res = sysm.evolve(clock_superposition(), times, store_states=True)
    for t, st in zip(times, res.states):
        assert np.isclose(abs(st.full()[0, 1]), 0.5 * np.exp(-gamma * t), atol=1e-3)


def test_heating_constant_rate():
    dim, ndot = 40, 1.0
    sysm = MasterEquationSystem(
        _mode_layout(dim), [], channels=[LindbladChannel("M", ChannelKind.HEATING, ndot)]
    )
    times = np.linspace(0, 3, 31)
    res = sysm.evolve(fock_mode(dim=dim, n=0), times, e_ops=_num_obs(), store_states=False)
    assert np.allclose(res.expect["n"].real, ndot * times, atol=2e-2)


def test_thermal_relaxation_cooling():
    dim, kappa = 30, 1.0
    sysm = MasterEquationSystem(
        _mode_layout(dim), [], channels=[LindbladChannel("M", ChannelKind.THERMAL_RELAXATION, kappa)]
    )
    times = np.linspace(0, 3, 31)
    res = sysm.evolve(fock_mode(dim=dim, n=3), times, e_ops=_num_obs(), store_states=False)
    assert np.allclose(res.expect["n"].real, 3.0 * np.exp(-kappa * times), atol=2e-2)


def test_thermal_relaxation_steady_state():
    dim, kappa, nbar = 30, 2.0, 1.5
    sysm = MasterEquationSystem(
        _mode_layout(dim), [],
        channels=[LindbladChannel("M", ChannelKind.THERMAL_RELAXATION, kappa, n_thermal=nbar)],
    )
    times = np.linspace(0, 6, 61)
    res = sysm.evolve(fock_mode(dim=dim, n=0), times, e_ops=_num_obs(), store_states=False)
    assert np.isclose(res.expect["n"].real[-1], nbar, atol=2e-2)


def test_white_drive_noise_equals_dephasing():
    """WHITE σ_z drive noise at effective_rate γ == a DEPHASING channel at γ_φ=γ."""
    layout = SystemLayout.carriers(1)
    gamma = 0.7
    drive = MasterEquationSystem(
        layout, [],
        drive_noise=[DriveNoise("carrier_00", LocalOp(Op.SIGMA_Z), NoiseModel.WHITE, gamma)],
    )
    times = np.linspace(0, 2, 11)
    res = drive.evolve(clock_superposition(), times, store_states=True)
    for t, st in zip(times, res.states):
        assert np.isclose(abs(st.full()[0, 1]), 0.5 * np.exp(-gamma * t), atol=1e-3)


def test_correlated_drive_noise_deferred():
    layout = SystemLayout.carriers(1)
    sysm = MasterEquationSystem(
        layout, [],
        drive_noise=[DriveNoise("carrier_00", LocalOp(Op.SIGMA_Z), NoiseModel.CORRELATED, 1.0)],
    )
    with pytest.raises(NotImplementedError):
        sysm.evolve(clock_superposition(), [0.0, 1.0])


def test_channel_kind_subsystem_mismatch():
    layout = SystemLayout.carriers(1)
    sysm = MasterEquationSystem(
        layout, [], channels=[LindbladChannel("carrier_00", ChannelKind.HEATING, 1.0)]
    )
    with pytest.raises(ValueError):
        sysm.evolve(clock_superposition(), [0.0, 1.0])
