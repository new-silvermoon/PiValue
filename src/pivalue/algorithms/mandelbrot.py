"""
Mandelbrot Set approach to calculating Pi.

The Mandelbrot set is the set of complex numbers c for which the function f(z)=z^2+c
does not diverge when iterated from z=0, i.e., for which the sequence f(0), f(f(0)),
etc., remains bounded in absolute value.

The value lies within a Mandelbrot set if f(z) <= 2. Considering the equation
f(z)=z^2+c, the value of c at the cusp of Mandelbrot set is 0.25. Now, if we add
a slight increment (e) to the value and apply it to the above equation, eventually
the value of f(z) will exceed 2.

The number of iterations required for f(z) to exceed the value of 2 will give us
the value of Pi (provided we place the decimal point at the correct place).
"""

import platform
import time
from decimal import Decimal
from typing import Dict, Any


def calculate(digits: int = 5) -> Dict[str, Any]:
    """
    Calculate Pi using the Mandelbrot set approach.

    Args:
        digits: Number of digits of precision to calculate.

    Returns:
        Dictionary containing:
            - pi: The calculated value of Pi (as string for precision)
            - iterations: Number of iterations performed
            - time_seconds: Time taken in seconds
            - method: Name of the method
            - platform: Platform information
    """
    start_time = time.perf_counter()

    c = Decimal("0.25")
    e = Decimal(1.0 / (100**digits - 1))
    c += e
    z = Decimal("0.0")
    iterations = 0

    while z < 2:
        z = z * z + c
        iterations += 1

    elapsed_time = time.perf_counter() - start_time

    return {
        "pi": str(iterations / (10**digits)),
        "iterations": iterations,
        "time_seconds": elapsed_time,
        "method": "Mandelbrot Set",
        "platform": platform.platform(),
        "digits": digits,
    }


if __name__ == "__main__":
    result = calculate()
    print(f"Method: {result['method']}")
    print(f"Platform: {result['platform']}")
    print(f"Digits: {result['digits']}")
    print(f"Pi ≈ {result['pi']}")
    print(f"Iterations: {result['iterations']}")
    print(f"Time: {result['time_seconds']:.6f} seconds")
