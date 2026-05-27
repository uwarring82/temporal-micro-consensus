"""Phase 1/Phase 2 firewall (contract §0.3, §12; Phase 2 §0.3).

The Phase-1 core namespace (`import tmc_numerics`) must stay clean of anchor symbols;
the Phase-2 anchor layer lives in the `tmc_numerics.anchors` submodule.
"""

import tmc_numerics
import tmc_numerics.anchors as anchors

_FORBIDDEN_SUBSTRINGS = ["temporal_redundancy", "temporalrecord", "mutual_information",
                         "quantum_fisher", "r_delta", "redundancy", "fisher", "holevo"]


def test_core_namespace_stays_clean():
    names = set(dir(tmc_numerics))
    leaked = sorted(n for n in names if any(f in n.lower() for f in _FORBIDDEN_SUBSTRINGS))
    assert not leaked, f"Phase-2 symbols leaked into the Phase-1 core namespace: {leaked}"


def test_anchor_layer_lives_in_submodule():
    for name in ("mutual_information", "quantum_fisher", "temporal_redundancy",
                 "partial_information", "TemporalRecordEnsemble", "RedundancyResult", "InfoMode"):
        assert hasattr(anchors, name), f"{name} missing from tmc_numerics.anchors"
