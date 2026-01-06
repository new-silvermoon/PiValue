"""Tests for the Leibniz algorithm."""

import math
from pivalue.algorithms import leibniz


def test_leibniz_basic() -> None:
    """Test basic Leibniz calculation."""
    result = leibniz.calculate(num_iterations=10000)

    assert "pi" in result
    assert "iterations" in result
    assert "time_seconds" in result
    assert "method" in result

    # Leibniz converges slowly, so allow larger error
    pi_value = result["pi"]
    assert abs(pi_value - math.pi) < 0.01


def test_leibniz_more_iterations() -> None:
    """Test Leibniz with more iterations for better accuracy."""
    result = leibniz.calculate(num_iterations=100000)

    pi_value = result["pi"]
    # More iterations should give better accuracy
    assert abs(pi_value - math.pi) < 0.001


def test_leibniz_result_structure() -> None:
    """Test that result has expected structure."""
    result = leibniz.calculate()

    assert isinstance(result, dict)
    assert result["method"] == "Madhava-Leibniz Formula"
    assert isinstance(result["iterations"], int)
    assert isinstance(result["time_seconds"], float)
    assert isinstance(result["pi"], float)
