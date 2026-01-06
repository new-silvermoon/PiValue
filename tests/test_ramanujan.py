"""Tests for the Ramanujan algorithm."""

import math
from pivalue.algorithms import ramanujan


def test_ramanujan_basic() -> None:
    """Test basic Ramanujan calculation."""
    result = ramanujan.calculate(num_iterations=5, precision=50)

    assert "pi" in result
    assert "iterations" in result
    assert "time_seconds" in result
    assert "method" in result
    assert "precision" in result

    pi_value = float(result["pi"])
    # Ramanujan's formula converges very rapidly
    assert abs(pi_value - math.pi) < 1e-10


def test_ramanujan_high_precision() -> None:
    """Test Ramanujan with high precision."""
    result = ramanujan.calculate(num_iterations=10, precision=100)

    pi_value = float(result["pi"])
    # Should be extremely accurate
    assert abs(pi_value - math.pi) < 1e-15


def test_ramanujan_result_structure() -> None:
    """Test that result has expected structure."""
    result = ramanujan.calculate()

    assert isinstance(result, dict)
    assert result["method"] == "Ramanujan's Formula"
    assert isinstance(result["iterations"], int)
    assert isinstance(result["time_seconds"], float)
    assert isinstance(result["precision"], int)
