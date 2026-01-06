"""Tests for the Liu Hui algorithm."""

import math
from pivalue.algorithms import liu_hui


def test_liu_hui_basic() -> None:
    """Test basic Liu Hui calculation."""
    result = liu_hui.calculate()

    assert "pi" in result
    assert "iterations" in result
    assert "time_seconds" in result
    assert "method" in result

    pi_value = result["pi"]
    assert abs(pi_value - math.pi) < 0.01


def test_liu_hui_result_structure() -> None:
    """Test that result has expected structure."""
    result = liu_hui.calculate(iterations=10)

    assert isinstance(result, dict)
    assert result["method"] == "Liu Hui's Algorithm"
    assert isinstance(result["iterations"], int)
    assert isinstance(result["time_seconds"], float)
    assert isinstance(result["pi"], float)
