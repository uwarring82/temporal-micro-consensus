"""Phase-0 smoke test: verifies package import and CI plumbing.

Deliberately requires no heavy dependency (no QuTiP) — its only job is to confirm
the package is importable and the pytest/CI harness runs cleanly, which is the
Phase 0 -> Phase 1 gate condition (work plan §3, Phase 0).
"""

import tmc_numerics


def test_package_importable():
    assert tmc_numerics.__version__ == "0.1.0.dev0"


def test_version_is_string():
    assert isinstance(tmc_numerics.__version__, str)
