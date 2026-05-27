"""Module 3a — Sorci protocol (Phase 3). Contract §6."""

import numpy as np
import pytest

from tmc_numerics.modules.sorci import (
    SorciParams, baseline_visibility_check, build_sorci_system, clock_motion_mutual_information,
    nuisance_budget, rwa_error, sorci_observed_visibility, sorci_visibility, _evolve,
)


def _scaled(**kw):
    base = dict(omega_c=1e3, omega=1e2, cutoff=80, t=0.1, eps_m=1e-3, r=1.0)
    base.update(kw)
    return SorciParams(**base)


# --- baseline: validate Sorci Eq. (12)'s coefficient (the DERIVED g_md), not a fit ---

def test_baseline_recovers_sorci_coefficient():
    chk = baseline_visibility_check(_scaled())
    assert chk["limit_ratio"] == pytest.approx(1 / 16, rel=0.02)   # (1-V)/(λ² sinh²2r) -> 1/16
    rs = chk["ratios"]
    assert rs[0.025] > rs[0.1]                                     # converges up toward 1/16 as λ→0


def test_full_model_agrees_with_secular_within_rwa():
    assert rwa_error(_scaled()) < 2e-3                             # small at ω t = 10


def test_signal_generates_clock_motion_entanglement():
    res = _evolve(_scaled(), secular=True, include_nuisance=False)
    assert clock_motion_mutual_information(res)[-1] > 0.0          # unitary signal => I(C:M) > 0


def test_al_plus_extrapolation_visibility():
    # secular workhorse at the experimental ²⁷Al⁺ point -> V ≈ 0.93
    p = SorciParams(omega_c=2 * np.pi * 1.1e15, omega=1.0, cutoff=200, t=1.0, eps_m=3.3e-18, r=2.26)
    V = sorci_visibility(_evolve(p, secular=True, include_nuisance=False, npts=30))[-1]
    assert 0.90 < V < 0.96


# --- the review-1 latent/observed split, as executable invariants ---

def test_detection_is_latent_invariant():
    r0 = _evolve(_scaled(eps_det=0.0))
    r1 = _evolve(_scaled(eps_det=0.1))
    assert sorci_visibility(r0)[-1] == pytest.approx(sorci_visibility(r1)[-1], abs=1e-12)
    assert clock_motion_mutual_information(r0)[-1] == pytest.approx(
        clock_motion_mutual_information(r1)[-1], abs=1e-12)
    v = sorci_visibility(r1)[-1]
    assert sorci_observed_visibility(r1, 0.1)[-1] == pytest.approx(0.8 * v)  # observed degrades


def test_detection_row_latent_zero_observed_nonzero():
    b = nuisance_budget(_scaled(eps_det=0.1))
    layer, channel, key, value, di, dls, dlo = next(r for r in b.rows if r[2] == "eps_det")
    assert di == pytest.approx(0.0, abs=1e-12)     # read-out cannot change quantum MI
    assert dls == pytest.approx(0.0, abs=1e-12)    # …nor the latent visibility
    assert abs(dlo) > 1e-6                          # …only the observed visibility


# --- sign diagnostics (benchmark-specific, NOT global invariants) ---

def test_clock_drive_phase_adds_visibility_loss():
    b = nuisance_budget(_scaled(drive_phase_rate=1.0))
    row = next(r for r in b.rows if r[2] == "drive_phase_rate")
    assert row[5] > 0   # clock dephasing unambiguously adds latent visibility loss


def test_motional_dephasing_is_secular_invisible():
    # The dispersive coupling σ_z n̂ is insensitive to number-basis dephasing (D[n̂] leaves the
    # Fock populations — and hence ⟨e^{-2i g_md t n̂}⟩ — unchanged). A benchmark-specific
    # diagnostic, NOT a global invariant: in the FULL σ_z P̂² model it would contribute.
    b = nuisance_budget(_scaled(gamma_phi=1.0), secular=True)
    deph = next(r for r in b.rows if r[2] == "gamma_phi")
    assert deph[5] == pytest.approx(0.0, abs=1e-8)


# --- budget bookkeeping + honest non-additivity ---

def test_budget_reconstruction_and_small_residual():
    b = nuisance_budget(_scaled(n_dot=0.5, gamma_phi=0.5, eps_prep=0.05))
    sum_dls = sum(r[5] for r in b.rows)
    assert b.full[1] - b.signal[1] == pytest.approx(sum_dls + b.interaction_residual[1], abs=1e-12)
    total = abs(b.full[1] - b.signal[1])
    assert abs(b.interaction_residual[1]) <= 0.3 * total + 1e-9   # interactions small in this regime


def test_transfer_conditions_recorded():
    b = nuisance_budget(_scaled())
    assert b.transfer["lambda"] == pytest.approx(0.1)
    assert b.transfer["g_md_over_omega"] < 1.0        # secular hierarchy |g_md|/ω << 1
    assert b.transfer["omega_t"] == pytest.approx(10.0)


def test_truncation_ok_at_operating_point():
    assert _evolve(_scaled(), secular=False).diagnostics.truncation_ok
