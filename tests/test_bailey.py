"""Tests for the Bailey-Borwein-Plouffe algorithm."""

import math
from pivalue.algorithms import bailey


def test_bailey_basic() -> None:
    """Test basic Bailey calculation."""
    result = bailey.calculate(num_iterations=50)

    assert "pi" in result
    assert "iterations" in result
    assert "time_seconds" in result
    assert "method" in result

    pi_value = float(result["pi"])
    assert abs(pi_value - math.pi) < 0.0001


def test_bailey_result_structure() -> None:
    """Test that result has expected structure."""
    result = bailey.calculate()

    assert isinstance(result, dict)
    assert result["method"] == "Bailey-Borwein-Plouffe (BBP)"
    assert isinstance(result["iterations"], int)
    assert isinstance(result["time_seconds"], float)
