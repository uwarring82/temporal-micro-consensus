"""System layout: subsystems, tensor order, Hilbert-space dimensions.

Phase 1 API contract §2. Tensor order == subsystem sequence order.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Sequence

import qutip as qt

from .exceptions import LayoutMismatchError


class SubsystemKind(Enum):
    TWO_LEVEL = "two_level"        # dim hard-validated == 2 (qudits -> future FINITE_LEVEL)
    BOSONIC_MODE = "bosonic_mode"  # dim = Fock cutoff = n_max + 1


@dataclass(frozen=True)
class Subsystem:
    label: str
    kind: SubsystemKind
    dim: int

    def __post_init__(self) -> None:
        if self.kind is SubsystemKind.TWO_LEVEL and self.dim != 2:
            raise ValueError(
                f"TWO_LEVEL subsystem {self.label!r} must have dim 2, got {self.dim}"
            )
        if self.kind is SubsystemKind.BOSONIC_MODE and self.dim < 2:
            raise ValueError(
                f"BOSONIC_MODE subsystem {self.label!r} must have dim >= 2, got {self.dim}"
            )


@dataclass(frozen=True)
class SystemLayout:
    subsystems: tuple[Subsystem, ...]

    def __post_init__(self) -> None:
        if not self.subsystems:
            raise ValueError("SystemLayout must contain at least one subsystem")
        labels = [s.label for s in self.subsystems]
        if len(labels) != len(set(labels)):
            raise ValueError(f"Subsystem labels must be unique, got {labels}")

    @classmethod
    def clock_and_modes(
        cls, n_modes: int, mode_cutoffs: int | Sequence[int]
    ) -> "SystemLayout":
        """clock(2) ⊗ M1 ⊗ … ⊗ M_n  (the Sorci convention)."""
        if isinstance(mode_cutoffs, int):
            cutoffs = [mode_cutoffs] * n_modes
        else:
            cutoffs = list(mode_cutoffs)
            if len(cutoffs) != n_modes:
                raise ValueError(
                    f"mode_cutoffs length {len(cutoffs)} != n_modes {n_modes}"
                )
        subs = [Subsystem("clock", SubsystemKind.TWO_LEVEL, 2)]
        for k in range(n_modes):
            subs.append(Subsystem(f"M{k + 1}", SubsystemKind.BOSONIC_MODE, cutoffs[k]))
        return cls(tuple(subs))

    @classmethod
    def carriers(cls, n: int) -> "SystemLayout":
        """carrier_00 ⊗ carrier_01 ⊗ … (the open-temporal-instrument convention)."""
        subs = [
            Subsystem(f"carrier_{k:02d}", SubsystemKind.TWO_LEVEL, 2) for k in range(n)
        ]
        return cls(tuple(subs))

    def labels(self) -> list[str]:
        return [s.label for s in self.subsystems]

    def index(self, label: str) -> int:
        for i, s in enumerate(self.subsystems):
            if s.label == label:
                return i
        raise KeyError(f"No subsystem labelled {label!r} in layout {self.labels()}")

    def subsystem(self, label: str) -> Subsystem:
        return self.subsystems[self.index(label)]

    def dims(self) -> list[int]:
        return [s.dim for s in self.subsystems]

    def validate_state(self, state: "qt.Qobj") -> None:
        expected = self.dims()
        got = state.dims[0]
        if got != expected:
            raise LayoutMismatchError(
                f"State dims {got} do not match layout dims {expected}"
            )
