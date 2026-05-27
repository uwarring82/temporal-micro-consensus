"""Phase 2 anchor-measure layer for tmc_numerics.

Kept in a submodule so the Phase-1 core (``import tmc_numerics``) stays import-clean
and the firewall test remains meaningful. Import explicitly:

    from tmc_numerics.anchors import mutual_information, quantum_fisher, temporal_redundancy
"""

from __future__ import annotations

from .ensemble import (
    InfoMode, TemporalPointer, TemporalRecordEnsemble, partial_information,
)
from .info import mutual_information, quantum_fisher
from .redundancy import RedundancyResult, temporal_redundancy

__all__ = [
    "InfoMode", "TemporalPointer", "TemporalRecordEnsemble", "partial_information",
    "mutual_information", "quantum_fisher",
    "RedundancyResult", "temporal_redundancy",
]
