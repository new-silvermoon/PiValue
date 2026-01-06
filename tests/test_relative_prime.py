"""Tests for the Relative Prime Probability algorithm."""

import math
from pivalue.algorithms import relative_prime


def test_relative_prime_basic() -> None:
    """Test basic relative prime calculation."""
    result = relative_prime.calculate(num_pairs=10000)

    assert "pi" in result
    assert "iterations" in result
    assert "time_seconds" in result
    assert "method" in result
    assert "probability" in result

    # This is a probabilistic method, so allow larger error
    pi_value = result["pi"]
    assert abs(pi_value - math.pi) < 0.5


def test_relative_prime_result_structure() -> None:
    """Test that result has expected structure."""
    result = relative_prime.calculate()

    assert isinstance(result, dict)
    assert result["method"] == "Relative Prime Probability"
    assert isinstance(result["iterations"], int)
    assert isinstance(result["time_seconds"], float)
    assert isinstance(result["pi"], float)
    assert isinstance(result["probability"], float)
    assert 0 < result["probability"] < 1
