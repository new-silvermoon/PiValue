"""
Machin-like formula for calculating Pi.

Machin's formula is one of the most efficient formulas for calculating π:
π/4 = 4·arctan(1/5) - arctan(1/239)

This formula was discovered by John Machin in 1706 and was used to calculate
π to 100 decimal places.

For more information, visit:
https://en.wikipedia.org/wiki/Machin-like_formula
"""

import math
import platform
import time
from typing import Dict, Any, List


def calculate() -> Dict[str, Any]:
    """
    Calculate Pi using Machin's formula.

    Returns:
        Dictionary containing:
            - pi: The calculated value of Pi
            - iterations: Number of iterations (N/A for this method)
            - time_seconds: Time taken in seconds
            - method: Name of the method
            - platform: Platform information
    """
    start_time = time.perf_counter()

    pi = 4 * ((4 * math.atan(1 / 5)) - math.atan(1 / 239))

    elapsed_time = time.perf_counter() - start_time

    return {
        "pi": pi,
        "iterations": "N/A",
        "time_seconds": elapsed_time,
        "method": "Machin's Formula",
        "platform": platform.platform(),
    }


def machin_like_formula(a_list: List[int], b_list: List[int], c_list: List[int]) -> float:
    """
    Calculate Pi using a generalized Machin-like formula.

    The formula is: π = 4 × Σ(c[i] × arctan(a[i] / b[i]))

    Args:
        a_list: List of numerators for arctan arguments.
        b_list: List of denominators for arctan arguments.
        c_list: List of coefficients for each term.

    Returns:
        The calculated value of Pi.

    Raises:
        AssertionError: If the lists have different lengths.
    """
    assert (
        len(a_list) == len(b_list) and len(b_list) == len(c_list)
    ), "Length of all three lists should match"

    total = 0.0
    for i in range(len(a_list)):
        total += c_list[i] * math.atan(a_list[i] / b_list[i])

    pi = 4 * total
    return pi


if __name__ == "__main__":
    result = calculate()
    print(f"Method: {result['method']}")
    print(f"Platform: {result['platform']}")
    print(f"Pi ≈ {result['pi']}")
    print(f"Time: {result['time_seconds']:.6f} seconds")
