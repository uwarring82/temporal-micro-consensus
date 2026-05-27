"""Typed exceptions for the tmc_numerics core layer (Phase 1 contract §6/§7)."""

from __future__ import annotations


class TmcNumericsError(Exception):
    """Base class for tmc_numerics errors."""


class LayoutMismatchError(TmcNumericsError):
    """A Qobj's dims do not match the SystemLayout."""


class NonHermitianHamiltonianError(TmcNumericsError):
    """The assembled Hamiltonian is not Hermitian."""


class SolverConvergenceError(TmcNumericsError):
    """The master-equation solver failed, or the trace drifted out of tolerance."""
