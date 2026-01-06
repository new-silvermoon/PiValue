"""Tests for the Euler algorithm."""

import math
from pivalue.algorithms import euler


def test_euler_basic() -> None:
    """Test basic Euler calculation."""
    result = euler.calculate(num_iterations=100)

    assert "pi" in result
    assert "iterations" in result
    assert "time_seconds" in result
    assert "method" in result

    pi_value = float(result["pi"])
    assert abs(pi_value - math.pi) < 0.001


def test_euler_result_structure() -> None:
    """Test that result has expected structure."""
    result = euler.calculate()

    assert isinstance(result, dict)
    assert result["method"] == "Euler Convergence"
    assert isinstance(result["iterations"], int)
    assert isinstance(result["time_seconds"], float)
