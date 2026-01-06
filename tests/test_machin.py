"""Tests for the Machin algorithm."""

import math
from pivalue.algorithms import machin


def test_machin_basic() -> None:
    """Test basic Machin calculation."""
    result = machin.calculate()

    assert "pi" in result
    assert "time_seconds" in result
    assert "method" in result

    pi_value = result["pi"]
    # Machin's formula is very accurate
    assert abs(pi_value - math.pi) < 1e-10


def test_machin_result_structure() -> None:
    """Test that result has expected structure."""
    result = machin.calculate()

    assert isinstance(result, dict)
    assert result["method"] == "Machin's Formula"
    assert isinstance(result["time_seconds"], float)
    assert isinstance(result["pi"], float)


def test_machin_like_formula() -> None:
    """Test the generalized Machin-like formula."""
    # Test with Machin's original formula parameters
    # π/4 = 4·arctan(1/5) - arctan(1/239)
    pi = machin.machin_like_formula([1, 1], [5, 239], [4, -1])

    assert abs(pi - math.pi) < 1e-10
