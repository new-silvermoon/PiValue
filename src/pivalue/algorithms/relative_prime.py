"""
Relative Prime Probability approach to calculating Pi.

The probability that two integers m and n picked at random are relatively prime is:
P((m,n) = 1) = 6/π²

Therefore, π = sqrt(6 / P((m,n) = 1))

For more information, visit:
https://mathworld.wolfram.com/RelativelyPrime.html
"""

import platform
import time
from functools import reduce
from math import sqrt
from random import randint
from typing import Dict, Any, Set


def get_factors(num: int) -> Set[int]:
    """
    Get all factors of a number (excluding 1).

    Args:
        num: The number to find factors for.

    Returns:
        Set of factors (excluding 1).
    """
    factors_set = set(
        reduce(
            list.__add__,
            ([i, int(num / i)] for i in range(1, int(num**0.5) + 1) if num % i == 0),
        )
    )
    factors_set.discard(1)
    return factors_set


def has_common_factors(num1: int, num2: int) -> bool:
    """
    Check if two numbers have common factors.

    Args:
        num1: First number.
        num2: Second number.

    Returns:
        True if numbers have common factors, False otherwise.
    """
    return len(get_factors(num1).intersection(get_factors(num2))) > 0


def calculate(
    num_pairs: int = 100000, min_range: int = 10, max_range: int = 1000
) -> Dict[str, Any]:
    """
    Calculate Pi using the relative prime probability approach.

    Args:
        num_pairs: Number of random pairs to test.
        min_range: Minimum value for random numbers.
        max_range: Maximum value for random numbers.

    Returns:
        Dictionary containing:
            - pi: The calculated value of Pi
            - iterations: Number of pairs tested
            - time_seconds: Time taken in seconds
            - method: Name of the method
            - platform: Platform information
            - probability: Calculated probability of relative primality
    """
    start_time = time.perf_counter()

    common_count = 0

    for _ in range(num_pairs):
        if has_common_factors(randint(min_range, max_range), randint(min_range, max_range)):
            common_count += 1

    probability = 1 - common_count / num_pairs
    pi = sqrt(6 / probability)
    elapsed_time = time.perf_counter() - start_time

    return {
        "pi": pi,
        "iterations": num_pairs,
        "time_seconds": elapsed_time,
        "method": "Relative Prime Probability",
        "platform": platform.platform(),
        "probability": probability,
    }


if __name__ == "__main__":
    result = calculate()
    print(f"Method: {result['method']}")
    print(f"Platform: {result['platform']}")
    print(f"Pi ≈ {result['pi']}")
    print(f"Pairs tested: {result['iterations']}")
    print(f"Probability: {result['probability']:.6f}")
    print(f"Time: {result['time_seconds']:.6f} seconds")
