"""
Liu Hui's algorithm for calculating Pi.

Liu Hui's π algorithm uses polygon approximation to estimate Pi.
It involves iteratively refining the approximation using nested square roots.

For more information, visit:
https://en.wikipedia.org/wiki/Liu_Hui%27s_π_algorithm
"""

import math
import platform
import time
from typing import Dict, Any


def calculate(iterations: int = 7) -> Dict[str, Any]:
    """
    Calculate Pi using Liu Hui's algorithm.

    Args:
        iterations: Number of iterations to perform (default: 7).

    Returns:
        Dictionary containing:
            - pi: The calculated value of Pi
            - iterations: Number of iterations performed
            - time_seconds: Time taken in seconds
            - method: Name of the method
            - platform: Platform information
    """
    start_time = time.perf_counter()

    init = math.sqrt(2 + 1)

    for _ in range(1, iterations + 1):
        init = math.sqrt(2 + init)

    pi = 768 * math.sqrt(2 - init)
    elapsed_time = time.perf_counter() - start_time

    return {
        "pi": pi,
        "iterations": iterations,
        "time_seconds": elapsed_time,
        "method": "Liu Hui's Algorithm",
        "platform": platform.platform(),
    }


if __name__ == "__main__":
    result = calculate()
    print(f"Method: {result['method']}")
    print(f"Platform: {result['platform']}")
    print(f"Pi ≈ {result['pi']}")
    print(f"Iterations: {result['iterations']}")
    print(f"Time: {result['time_seconds']:.6f} seconds")
