"""
Madhava-Leibniz formula for calculating Pi.

The Leibniz formula for π is an infinite series:
π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...

For more information, visit:
https://en.wikipedia.org/wiki/Leibniz_formula_for_π
"""

import platform
import time
from typing import Dict, Any


def calculate(num_iterations: int = 400000) -> Dict[str, Any]:
    """
    Calculate Pi using the Madhava-Leibniz formula.

    Args:
        num_iterations: Number of iterations to perform.

    Returns:
        Dictionary containing:
            - pi: The calculated value of Pi
            - iterations: Number of iterations performed
            - time_seconds: Time taken in seconds
            - method: Name of the method
            - platform: Platform information
    """
    start_time = time.perf_counter()

    pi_over_4 = 0.0
    for i in range(num_iterations + 1):
        denom = i * 2 + 1
        pi_over_4 = (pi_over_4 + (1 / denom)) if i % 2 == 0 else (pi_over_4 - (1 / denom))

    pi = pi_over_4 * 4
    elapsed_time = time.perf_counter() - start_time

    return {
        "pi": pi,
        "iterations": num_iterations,
        "time_seconds": elapsed_time,
        "method": "Madhava-Leibniz Formula",
        "platform": platform.platform(),
    }


if __name__ == "__main__":
    result = calculate()
    print(f"Method: {result['method']}")
    print(f"Platform: {result['platform']}")
    print(f"Pi ≈ {result['pi']}")
    print(f"Iterations: {result['iterations']}")
    print(f"Time: {result['time_seconds']:.6f} seconds")
