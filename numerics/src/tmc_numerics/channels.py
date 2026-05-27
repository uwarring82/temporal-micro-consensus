"""Lindblad channels, drive noise, readout model, collapse-operator construction.

Phase 1 API contract §5.2, §5.3, §5.4. Generators are pinned per ChannelKind so
each closed-form test has a single right answer (see the contract).
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import numpy as np
import qutip as qt

from .layout import SubsystemKind, SystemLayout
from .operators import LocalOp, local_qobj


class ChannelKind(Enum):
    HEATING = "heating"                        # ṅ·(D[a†]+D[a]); d⟨n⟩/dt = +ṅ (state-independent)
    THERMAL_RELAXATION = "thermal_relaxation"  # κ(n̄+1)D[a]+κn̄D[a†]; d⟨n⟩/dt = −κ(⟨n⟩−n̄)
    MOTIONAL_DEPHASING = "motional_dephasing"  # γ_φ·D[a†a]
    DEPHASING = "dephasing"                    # (γ_φ/2)·D[σ_z]; coherence ∝ e^{−γ_φ t}
    AMPLITUDE_DAMPING = "amplitude_damping"    # Γ·D[σ_−]


class NoiseModel(Enum):
    WHITE = "white"
    CORRELATED = "correlated"


@dataclass(frozen=True)
class LindbladChannel:
    target: str
    kind: ChannelKind
    rate: float
    n_thermal: float | None = None
    label: str = ""


@dataclass(frozen=True)
class DriveNoise:
    target: str
    operator: LocalOp
    model: NoiseModel
    effective_rate: float  # coherence-decay rate; WHITE adds (effective_rate/2)·D[operator]
    label: str = ""


@dataclass(frozen=True)
class ReadoutModel:
    target: str
    detection_infidelity: float = 0.0
    correlated_with: str | None = None
    label: str = ""
    # NOT consumed by evolve(); applied in Phase 2.


_BOSONIC_KINDS = {
    ChannelKind.HEATING, ChannelKind.THERMAL_RELAXATION, ChannelKind.MOTIONAL_DEPHASING,
}
_TWO_LEVEL_KINDS = {ChannelKind.DEPHASING, ChannelKind.AMPLITUDE_DAMPING}


def _embed_local(local: "qt.Qobj", target: str, layout: SystemLayout) -> "qt.Qobj":
    factors = [
        local if sub.label == target else qt.qeye(sub.dim) for sub in layout.subsystems
    ]
    return qt.tensor(factors)


def collapse_ops_for_channel(
    channel: LindbladChannel, layout: SystemLayout
) -> list["qt.Qobj"]:
    sub = layout.subsystem(channel.target)
    dim = sub.dim
    kind = channel.kind
    if kind in _BOSONIC_KINDS and sub.kind is not SubsystemKind.BOSONIC_MODE:
        raise ValueError(f"{kind} requires a BOSONIC_MODE target; {channel.target!r} is {sub.kind}")
    if kind in _TWO_LEVEL_KINDS and sub.kind is not SubsystemKind.TWO_LEVEL:
        raise ValueError(f"{kind} requires a TWO_LEVEL target; {channel.target!r} is {sub.kind}")
    r = channel.rate
    if r < 0:
        raise ValueError(f"channel rate must be >= 0, got {r}")

    if kind is ChannelKind.HEATING:
        a = qt.destroy(dim)
        locals_ = [np.sqrt(r) * a.dag(), np.sqrt(r) * a]
    elif kind is ChannelKind.THERMAL_RELAXATION:
        nbar = 0.0 if channel.n_thermal is None else float(channel.n_thermal)
        a = qt.destroy(dim)
        locals_ = [np.sqrt(r * (nbar + 1.0)) * a]
        if nbar > 0.0:
            locals_.append(np.sqrt(r * nbar) * a.dag())
    elif kind is ChannelKind.MOTIONAL_DEPHASING:
        locals_ = [np.sqrt(r) * qt.num(dim)]
    elif kind is ChannelKind.DEPHASING:
        locals_ = [np.sqrt(r / 2.0) * qt.sigmaz()]
    elif kind is ChannelKind.AMPLITUDE_DAMPING:
        locals_ = [np.sqrt(r) * qt.sigmam()]
    else:  # pragma: no cover
        raise ValueError(f"Unhandled channel kind {kind}")

    return [_embed_local(c, channel.target, layout) for c in locals_]


def collapse_ops_for_drive(drive: DriveNoise, layout: SystemLayout) -> list["qt.Qobj"]:
    if drive.model is NoiseModel.CORRELATED:
        raise NotImplementedError(
            "CORRELATED drive noise is deferred to v0.2 (trajectory ensemble)."
        )
    if drive.effective_rate < 0:
        raise ValueError(f"effective_rate must be >= 0, got {drive.effective_rate}")
    sub = layout.subsystem(drive.target)
    operator = local_qobj(drive.operator, sub.kind, sub.dim)
    c_local = np.sqrt(drive.effective_rate / 2.0) * operator
    return [_embed_local(c_local, drive.target, layout)]
