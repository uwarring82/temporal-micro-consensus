"""Phase 1/Phase 2 firewall (contract §0.3, §12).

Phase 1 must expose NO temporal-pointer / fragment / R_δ / I(C:M) / F[τ] symbol.
"""

import tmc_numerics

_FORBIDDEN = [
    "temporal_redundancy", "TemporalRecordEnsemble", "TemporalPointer", "Fragment",
    "mutual_information", "quantum_fisher", "R_delta", "Rdelta", "fisher",
]


def test_no_phase2_symbols_in_namespace():
    names = set(dir(tmc_numerics))
    leaked = sorted(n for n in names if any(f.lower() in n.lower() for f in _FORBIDDEN))
    assert not leaked, f"Phase-2 symbols leaked into Phase 1: {leaked}"
