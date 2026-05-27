"""MasterEquationSystem and evolve — the Phase-1 full-Hilbert QuTiP backend.

Phase 1 API contract §6, §7. This is the full-Hilbert `mesolve` engine (Module 3a
+ small-N validation); the Module-3b factorised N≫2 backend is a separate Phase-3
component (work-plan D3) and is not implemented here.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Mapping, Sequence

import numpy as np
import qutip as qt

from .channels import (
    DriveNoise, LindbladChannel, ReadoutModel,
    collapse_ops_for_channel, collapse_ops_for_drive,
)
from .exceptions import LayoutMismatchError, SolverConvergenceError
from .layout import SubsystemKind, SystemLayout
from .operators import HamiltonianTerm, assemble_hamiltonian, build_observable

_TRACE_TOL = 1e-6


@dataclass
class SolverOptions:
    solver: Literal["mesolve"] = "mesolve"
    method: str = "adams"
    atol: float = 1e-12
    rtol: float = 1e-10
    nsteps: int = 10_000
    fock_population_warn_threshold: float = 1e-6
    qutip_options: dict | None = None


@dataclass
class EvolutionDiagnostics:
    max_fock_population: dict
    trace_drift: float
    truncation_ok: bool


@dataclass
class EvolutionResult:
    times: "np.ndarray"
    states: "list | None"
    expect: dict
    final_state: "qt.Qobj"
    layout: SystemLayout
    solver: str
    converged: bool
    diagnostics: EvolutionDiagnostics


class MasterEquationSystem:
    def __init__(
        self,
        layout: SystemLayout,
        hamiltonian: Sequence[HamiltonianTerm],
        channels: Sequence[LindbladChannel] = (),
        drive_noise: Sequence[DriveNoise] = (),
        readout: Sequence[ReadoutModel] = (),
    ) -> None:
        self._layout = layout
        self._hamiltonian = tuple(hamiltonian)
        self._channels = tuple(channels)
        self._drive_noise = tuple(drive_noise)
        self._readout = tuple(readout)
        valid = set(layout.labels())
        for specs, name in (
            (self._channels, "channel"),
            (self._drive_noise, "drive_noise"),
            (self._readout, "readout"),
        ):
            for spec in specs:
                if spec.target not in valid:
                    raise KeyError(
                        f"{name} target {spec.target!r} not in layout {sorted(valid)}"
                    )

    @property
    def layout(self) -> SystemLayout:
        return self._layout

    @property
    def readout(self) -> tuple:
        return self._readout

    def hamiltonian_operator(self) -> "qt.Qobj":
        return assemble_hamiltonian(self._hamiltonian, self._layout)

    def collapse_operators(self) -> list["qt.Qobj"]:
        c_ops: list = []
        for ch in self._channels:
            c_ops.extend(collapse_ops_for_channel(ch, self._layout))
        for dn in self._drive_noise:
            c_ops.extend(collapse_ops_for_drive(dn, self._layout))
        return c_ops

    def evolve(
        self,
        state: "qt.Qobj",
        times,
        *,
        e_ops: Mapping | None = None,
        options: SolverOptions | None = None,
        store_states: bool = True,
    ) -> EvolutionResult:
        options = options or SolverOptions()
        if options.solver != "mesolve":
            raise NotImplementedError(
                f"solver={options.solver!r} not available in v0.1 (mesolve only)"
            )
        self._layout.validate_state(state)
        rho0 = state * state.dag() if state.isket else state
        H = self.hamiltonian_operator()
        c_ops = self.collapse_operators()
        times = np.asarray(times, dtype=float)

        e_labels = list(e_ops.keys()) if e_ops else []
        e_list = [build_observable(e_ops[k], self._layout) for k in e_labels]
        for lbl, eo in zip(e_labels, e_list):
            if eo.dims[0] != self._layout.dims():
                raise LayoutMismatchError(
                    f"Observable {lbl!r} dims {eo.dims[0]} != layout {self._layout.dims()}"
                )

        opts = {
            "store_states": store_states,
            "store_final_state": True,
            "atol": options.atol,
            "rtol": options.rtol,
            "nsteps": options.nsteps,
            "method": options.method,
            "progress_bar": False,
        }
        if options.qutip_options:
            opts.update(options.qutip_options)

        try:
            result = qt.mesolve(H, rho0, times, c_ops=c_ops, e_ops=e_list, options=opts)
        except Exception as exc:  # noqa: BLE001
            raise SolverConvergenceError(f"mesolve failed: {exc}") from exc

        states = list(result.states) if (store_states and result.states) else None
        final_state = getattr(result, "final_state", None)
        if final_state is None:
            final_state = states[-1] if states else rho0

        expect: dict = {}
        for i, lbl in enumerate(e_labels):
            expect[lbl] = np.asarray(result.expect[i])

        diag = self._diagnostics(states, final_state, options.fock_population_warn_threshold)
        if diag.trace_drift > _TRACE_TOL:
            raise SolverConvergenceError(
                f"Trace drifted by {diag.trace_drift:.3e} (> {_TRACE_TOL:.0e})"
            )

        return EvolutionResult(
            times=times,
            states=states,
            expect=expect,
            final_state=final_state,
            layout=self._layout,
            solver="mesolve",
            converged=True,
            diagnostics=diag,
        )

    def _diagnostics(self, states, final_state, threshold) -> EvolutionDiagnostics:
        sampled = states if states else [final_state]
        max_pop: dict = {}
        for i, sub in enumerate(self._layout.subsystems):
            if sub.kind is SubsystemKind.BOSONIC_MODE:
                top = 0.0
                for st in sampled:
                    reduced = st.ptrace(i) if len(self._layout.subsystems) > 1 else st
                    pops = np.real(reduced.diag())
                    top = max(top, float(pops[-1]))
                max_pop[sub.label] = top
        trace_drift = max(abs(complex(st.tr()) - 1.0) for st in sampled)
        truncation_ok = all(v < threshold for v in max_pop.values()) if max_pop else True
        return EvolutionDiagnostics(
            max_fock_population=max_pop,
            trace_drift=float(trace_drift),
            truncation_ok=truncation_ok,
        )
