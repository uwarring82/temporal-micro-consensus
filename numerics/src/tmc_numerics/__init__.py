"""Temporal Micro Consensus — numerical toolkit (``tmc_numerics``).

Phase 1 core layer: master-equation simulation of clock-plus-carrier systems.
Public API per ``workplans/toolkit-phase1-api-contract-v0.1.md`` (D6-locked).

The Phase-2 anchor-measure layer (``I(C:M)``, ``F[tau]``, ``R_delta``, the
``TemporalRecordEnsemble``) and the Module-3b factorised backend (Phase 3) are
intentionally absent here — see the firewall test.
"""

from __future__ import annotations

from .channels import (
    ChannelKind, DriveNoise, LindbladChannel, NoiseModel, ReadoutModel,
)
from .exceptions import (
    LayoutMismatchError, NonHermitianHamiltonianError, SolverConvergenceError,
    TmcNumericsError,
)
from .layout import Subsystem, SubsystemKind, SystemLayout
from .operators import HamiltonianTerm, LocalOp, ObservableSpec, Op
from .prep import (
    clock_superposition, coherent_mode, fock_mode, product_state, squeezed_mode,
    thermal_mode, two_level_state,
)
from .system import (
    EvolutionDiagnostics, EvolutionResult, MasterEquationSystem, SolverOptions,
)

__version__ = "0.1.0.dev0"

__all__ = [
    "__version__",
    # layout
    "SubsystemKind", "Subsystem", "SystemLayout",
    # operators
    "Op", "LocalOp", "HamiltonianTerm", "ObservableSpec",
    # channels / nuisance specs
    "ChannelKind", "LindbladChannel", "NoiseModel", "DriveNoise", "ReadoutModel",
    # system / evolution
    "MasterEquationSystem", "SolverOptions", "EvolutionResult", "EvolutionDiagnostics",
    # preparation primitives
    "clock_superposition", "two_level_state", "squeezed_mode", "coherent_mode",
    "thermal_mode", "fock_mode", "product_state",
    # exceptions
    "TmcNumericsError", "LayoutMismatchError", "NonHermitianHamiltonianError",
    "SolverConvergenceError",
]
