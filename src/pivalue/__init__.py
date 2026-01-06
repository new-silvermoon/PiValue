"""
PiValue - Mathematical approaches to calculate Pi.

This package provides multiple algorithms for calculating the value of Pi,
useful for benchmarking computational performance and comparing mathematical approaches.
"""

__version__ = "2.0.0"
__author__ = "Sagar Das"

from pivalue.algorithms import (
    bailey,
    euler,
    leibniz,
    liu_hui,
    machin,
    mandelbrot,
    ramanujan,
    relative_prime,
)

__all__ = [
    "bailey",
    "euler",
    "leibniz",
    "liu_hui",
    "machin",
    "mandelbrot",
    "ramanujan",
    "relative_prime",
]
