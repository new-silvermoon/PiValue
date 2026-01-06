"""Tests for the Mandelbrot algorithm."""

import math
from pivalue.algorithms import mandelbrot


def test_mandelbrot_basic() -> None:
    """Test basic Mandelbrot calculation."""
    result = mandelbrot.calculate(digits=3)

    assert "pi" in result
    assert "iterations" in result
    assert "time_seconds" in result
    assert "method" in result

    # Check that result is close to pi (within 10% for low precision)
    pi_value = float(result["pi"])
    assert abs(pi_value - math.pi) < 0.5


def test_mandelbrot_higher_precision() -> None:
    """Test Mandelbrot with higher precision."""
    result = mandelbrot.calculate(digits=5)

    pi_value = float(result["pi"])
    # Should be more accurate with more digits
    assert abs(pi_value - math.pi) < 0.01


def test_mandelbrot_result_structure() -> None:
    """Test that result has expected structure."""
    result = mandelbrot.calculate()

    assert isinstance(result, dict)
    assert result["method"] == "Mandelbrot Set"
    assert isinstance(result["iterations"], int)
    assert isinstance(result["time_seconds"], float)
    assert result["time_seconds"] >= 0
