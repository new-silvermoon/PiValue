"""
Bailey-Borwein-Plouffe (BBP) formula for calculating Pi.

In 1997, David H. Bailey, Peter Borwein and Simon Plouffe published a paper
on a new formula for π as an infinite series:

π = Σ(k=0 to ∞) [1/16^k × (4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6))]

This formula is notable for allowing the calculation of arbitrary hexadecimal
digits of π without calculating the preceding digits.
"""

import platform
import time
from decimal import Decimal
from typing import Dict, Any


def calculate(num_iterations: int = 100) -> Dict[str, Any]:
    """
    Calculate Pi using the Bailey-Borwein-Plouffe formula.

    Args:
        num_iterations: Number of iterations to perform.

    Returns:
        Dictionary containing:
            - pi: The calculated value of Pi (as string for precision)
            - iterations: Number of iterations performed
            - time_seconds: Time taken in seconds
            - method: Name of the method
            - platform: Platform information
    """
    start_time = time.perf_counter()

    pi = Decimal("0.0")

    for i in range(num_iterations + 1):
        term = (1 / 16**i) * (
            (4 / (8 * i + 1)) - (2 / (8 * i + 4)) - (1 / (8 * i + 5)) - (1 / (8 * i + 6))
        )
        pi += Decimal(term)

    elapsed_time = time.perf_counter() - start_time

    return {
        "pi": str(pi),
        "iterations": num_iterations,
        "time_seconds": elapsed_time,
        "method": "Bailey-Borwein-Plouffe (BBP)",
        "platform": platform.platform(),
    }


if __name__ == "__main__":
    result = calculate()
    print(f"Method: {result['method']}")
    print(f"Platform: {result['platform']}")
    print(f"Pi ≈ {result['pi']}")
    print(f"Iterations: {result['iterations']}")
    print(f"Time: {result['time_seconds']:.6f} seconds")
