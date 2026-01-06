"""
Euler Convergence method for calculating Pi.

This method uses a factorial-based series to calculate Pi with improved convergence.

For more information, visit:
http://mathworld.wolfram.com/ConvergenceImprovement.html
"""

import platform
import time
from decimal import Decimal
from functools import lru_cache
from typing import Dict, Any


@lru_cache(maxsize=None)
def get_factorial(n: int) -> int:
    """
    Calculate factorial of n with memoization.

    Args:
        n: The number to calculate factorial for.

    Returns:
        The factorial of n.
    """
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def calculate(num_iterations: int = 2000) -> Dict[str, Any]:
    """
    Calculate Pi using Euler convergence method.

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

    val = Decimal("0.0")

    for i in range(0, num_iterations + 1):
        numerator = pow(2, i) * pow(get_factorial(i), 2)
        denominator = get_factorial(2 * i + 1)
        val += Decimal(numerator) / Decimal(denominator)

    pi = Decimal(2) * val
    elapsed_time = time.perf_counter() - start_time

    return {
        "pi": str(pi),
        "iterations": num_iterations,
        "time_seconds": elapsed_time,
        "method": "Euler Convergence",
        "platform": platform.platform(),
    }


if __name__ == "__main__":
    result = calculate()
    print(f"Method: {result['method']}")
    print(f"Platform: {result['platform']}")
    print(f"Pi ≈ {result['pi']}")
    print(f"Iterations: {result['iterations']}")
    print(f"Time: {result['time_seconds']:.6f} seconds")
