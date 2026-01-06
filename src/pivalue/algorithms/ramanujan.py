"""
Ramanujan's formula for calculating Pi.

Srinivasa Ramanujan discovered several rapidly converging infinite series for π.
One of his most famous formulas is:

1/π = (2√2/9801) × Σ(k=0 to ∞) [(4k)!(1103 + 26390k)] / [(k!)^4 × 396^(4k)]

This formula converges extremely rapidly, producing about 8 additional correct
digits of π per term.

For more information, visit:
https://en.wikipedia.org/wiki/Ramanujan%E2%80%93Sato_series
"""

import math
import platform
import time
from decimal import Decimal, getcontext
from typing import Dict, Any


def factorial(n: int) -> int:
    """
    Calculate factorial of n.

    Args:
        n: The number to calculate factorial for.

    Returns:
        The factorial of n.
    """
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def calculate(num_iterations: int = 10, precision: int = 100) -> Dict[str, Any]:
    """
    Calculate Pi using Ramanujan's formula.

    Args:
        num_iterations: Number of iterations to perform (default: 10).
        precision: Decimal precision to use (default: 100).

    Returns:
        Dictionary containing:
            - pi: The calculated value of Pi (as string for precision)
            - iterations: Number of iterations performed
            - time_seconds: Time taken in seconds
            - method: Name of the method
            - platform: Platform information
    """
    start_time = time.perf_counter()

    # Set decimal precision
    getcontext().prec = precision

    # Constants
    sqrt2 = Decimal(2).sqrt()
    constant = (Decimal(2) * sqrt2) / Decimal(9801)

    # Calculate the sum
    total = Decimal(0)
    for k in range(num_iterations):
        numerator = Decimal(factorial(4 * k)) * Decimal(1103 + 26390 * k)
        denominator = Decimal(factorial(k) ** 4) * Decimal(396 ** (4 * k))
        total += numerator / denominator

    # Calculate 1/π and then π
    one_over_pi = constant * total
    pi = Decimal(1) / one_over_pi

    elapsed_time = time.perf_counter() - start_time

    return {
        "pi": str(pi),
        "iterations": num_iterations,
        "time_seconds": elapsed_time,
        "method": "Ramanujan's Formula",
        "platform": platform.platform(),
        "precision": precision,
    }


if __name__ == "__main__":
    result = calculate()
    print(f"Method: {result['method']}")
    print(f"Platform: {result['platform']}")
    print(f"Pi ≈ {result['pi']}")
    print(f"Iterations: {result['iterations']}")
    print(f"Precision: {result['precision']} digits")
    print(f"Time: {result['time_seconds']:.6f} seconds")
