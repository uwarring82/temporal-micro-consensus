"""Module 3a — Sorci protocol (Phase 3).

Contract: ``workplans/toolkit-module3a-sorci-contract-v0.1.md`` (D6-locked).

Rotating frame w.r.t. the free clock (exact: σ_z commutes with the coupling). Two models:
- secular dispersive ``H_sec = g_md σ_z n̂`` — the workhorse, valid for any t (n̂ conserved);
- full ``ω n̂ + g_md σ_z P̂²`` — scaled-parameter validation of the coefficient and RWA error.

``g_md = −ε_m ω_c / 4`` is DERIVED from Ĥ and the Phase-1 ``P_QUAD`` convention; the baseline
check VALIDATES that this reproduces Sorci Eq. (12)'s coefficient (1−V → λ² sinh²(2r)/16 as λ→0).
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Mapping, Sequence

import numpy as np

from ..anchors import mutual_information
from ..channels import ChannelKind, DriveNoise, LindbladChannel, NoiseModel, ReadoutModel
from ..layout import SystemLayout
from ..operators import HamiltonianTerm, LocalOp, Op
from ..prep import clock_superposition, product_state, squeezed_mode
from ..system import MasterEquationSystem

_NUISANCE = ("n_dot", "gamma_phi", "eps_prep", "drive_phase_rate", "eps_det")
_LAYER = {
    "n_dot": ("dynamical-Lindblad", "heating"),
    "gamma_phi": ("dynamical-Lindblad", "motional dephasing"),
    "eps_prep": ("initial-state", "prep infidelity"),
    "drive_phase_rate": ("stochastic-Hamiltonian", "drive-phase noise"),
    "eps_det": ("read-out", "detection infidelity"),
}


@dataclass(frozen=True)
class SorciParams:
    omega_c: float
    omega: float
    cutoff: int
    t: float
    eps_m: float
    r: float
    n_dot: float = 0.0
    gamma_phi: float = 0.0
    eps_prep: float = 0.0
    drive_phase_rate: float = 0.0
    eps_det: float = 0.0

    @property
    def g_md(self) -> float:
        return -(self.eps_m * self.omega_c) / 4.0

    @property
    def lam(self) -> float:  # the dimensionless control λ = ε_m ω_c t
        return self.eps_m * self.omega_c * self.t


def build_sorci_system(params: SorciParams, *, secular: bool = True,
                       include_nuisance: bool = True) -> MasterEquationSystem:
    layout = SystemLayout.clock_and_modes(1, params.cutoff)
    g = params.g_md
    if secular:
        H = [HamiltonianTerm(g, {"clock": LocalOp(Op.SIGMA_Z), "M1": LocalOp(Op.NUM)}, "secular dispersive")]
    else:
        H = [
            HamiltonianTerm(params.omega, {"M1": LocalOp(Op.NUM)}, "free mode"),
            HamiltonianTerm(g, {"clock": LocalOp(Op.SIGMA_Z), "M1": LocalOp(Op.P_QUAD, power=2)}, "mass-defect coupling"),
        ]
    channels, drive, readout = [], [], []
    if include_nuisance:
        if params.n_dot > 0:
            channels.append(LindbladChannel("M1", ChannelKind.HEATING, params.n_dot))
        if params.gamma_phi > 0:
            channels.append(LindbladChannel("M1", ChannelKind.MOTIONAL_DEPHASING, params.gamma_phi))
        if params.drive_phase_rate > 0:
            drive.append(DriveNoise("clock", LocalOp(Op.SIGMA_Z), NoiseModel.WHITE, params.drive_phase_rate))
        if params.eps_det > 0:
            readout.append(ReadoutModel("clock", detection_infidelity=params.eps_det))
    return MasterEquationSystem(layout, H, channels=channels, drive_noise=drive, readout=readout)


def sorci_initial_state(params: SorciParams):
    layout = SystemLayout.clock_and_modes(1, params.cutoff)
    return product_state(layout, {
        "clock": clock_superposition(),
        "M1": squeezed_mode(dim=params.cutoff, r=params.r, prep_infidelity=params.eps_prep),
    })


def _evolve(params, *, secular=True, include_nuisance=True, npts=40):
    sysm = build_sorci_system(params, secular=secular, include_nuisance=include_nuisance)
    times = np.linspace(0.0, params.t, npts)
    return sysm.evolve(sorci_initial_state(params), times, store_states=True)


def sorci_visibility(result) -> "np.ndarray":
    """Latent clock visibility V_state(t) = 2|ρ₀₁^clock| (read-out-invariant)."""
    return np.array([2.0 * abs(s.ptrace(0).full()[0, 1]) for s in result.states])


def sorci_observed_visibility(result, eps_det: float) -> "np.ndarray":
    """Observed visibility: V_state degraded by a symmetric clock-readout infidelity ε_det."""
    return (1.0 - 2.0 * eps_det) * sorci_visibility(result)


def clock_motion_mutual_information(result) -> "np.ndarray":
    """Latent I(C:M)(t) in bits (read-out-invariant)."""
    return np.array([mutual_information(s, ([0], [1])) for s in result.states])


def baseline_visibility_check(params: SorciParams, *, lambdas: Sequence[float] = (0.1, 0.05, 0.025),
                              secular: bool = True) -> dict:
    """Validate Sorci Eq. (12)'s coefficient: (1−V)/(λ² sinh²2r) → 1/16 as λ→0.

    Eq. (12) is leading-order in λ; this recovers its coefficient in the λ→0 limit, validating
    the derived g_md and the P_QUAD convention (a validation, not a fit).
    """
    sinh2 = np.sinh(2.0 * params.r) ** 2
    ratios = {}
    for lam in lambdas:
        t = lam / (params.eps_m * params.omega_c)
        res = _evolve(replace(params, t=t), secular=secular, include_nuisance=False)
        one_minus_V = 1.0 - sorci_visibility(res)[-1]
        ratios[float(lam)] = one_minus_V / (lam ** 2 * sinh2)
    return {"ratios": ratios, "target": 1.0 / 16.0, "limit_ratio": ratios[float(min(lambdas))]}


def rwa_error(params: SorciParams) -> float:
    """|V_full − V_secular| at the operating point (the RWA/secular error; → 0 as ωt → ∞)."""
    vf = sorci_visibility(_evolve(params, secular=False, include_nuisance=False))[-1]
    vs = sorci_visibility(_evolve(params, secular=True, include_nuisance=False))[-1]
    return float(abs(vf - vs))


@dataclass
class NuisanceBudget:
    rows: list            # (layer, channel, parameter, value, dI, dL_state, dL_obs)
    signal: tuple         # (I_sig, L_state_sig, L_obs_sig)
    full: tuple
    interaction_residual: tuple
    params: SorciParams
    model: str
    transfer: dict
    metadata: dict


def _observables(params, *, secular):
    res = _evolve(params, secular=secular, include_nuisance=True)
    i_cm = float(clock_motion_mutual_information(res)[-1])
    v_state = float(sorci_visibility(res)[-1])
    v_obs = (1.0 - 2.0 * params.eps_det) * v_state
    return i_cm, 1.0 - v_state, 1.0 - v_obs  # I(C:M), L_state, L_obs


def nuisance_budget(params: SorciParams, *, secular: bool = True,
                    sweep_ranges: "Mapping[str, Sequence[float]] | None" = None) -> NuisanceBudget:
    """Marginal-from-signal per-channel budget + full model + interaction residual.

    `sweep_ranges` (optional) is reserved for per-channel marginal curves; the v0.1 table uses
    each channel's operating value from `params`.
    """
    signal_params = replace(params, **{k: 0.0 for k in _NUISANCE})
    i_sig, ls_sig, lo_sig = _observables(signal_params, secular=secular)

    rows = []
    sum_di = sum_dls = sum_dlo = 0.0
    for k in _NUISANCE:
        value = getattr(params, k)
        if value == 0.0:
            continue
        marg_params = replace(signal_params, **{k: value})
        i_k, ls_k, lo_k = _observables(marg_params, secular=secular)
        di, dls, dlo = i_k - i_sig, ls_k - ls_sig, lo_k - lo_sig
        layer, channel = _LAYER[k]
        rows.append((layer, channel, k, value, di, dls, dlo))
        sum_di += di
        sum_dls += dls
        sum_dlo += dlo

    i_full, ls_full, lo_full = _observables(params, secular=secular)
    residual = (i_full - i_sig - sum_di, ls_full - ls_sig - sum_dls, lo_full - lo_sig - sum_dlo)

    return NuisanceBudget(
        rows=rows,
        signal=(i_sig, ls_sig, lo_sig),
        full=(i_full, ls_full, lo_full),
        interaction_residual=residual,
        params=params,
        model="secular" if secular else "full",
        transfer={"lambda": params.lam, "g_md_over_omega": abs(params.g_md) / params.omega if params.omega else float("inf"),
                  "omega_t": params.omega * params.t},
        metadata={"g_md": params.g_md, "sinh2_2r": float(np.sinh(2 * params.r) ** 2)},
    )
