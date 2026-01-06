"""
Benchmarking utilities for comparing Pi calculation algorithms.
"""

import json
import math
from typing import Dict, List, Any, Optional
from pivalue.algorithms import (
    mandelbrot,
    leibniz,
    liu_hui,
    euler,
    bailey,
    relative_prime,
    machin,
    ramanujan,
)


# Map of algorithm names to their modules
ALGORITHMS = {
    "mandelbrot": mandelbrot,
    "leibniz": leibniz,
    "liu_hui": liu_hui,
    "euler": euler,
    "bailey": bailey,
    "relative_prime": relative_prime,
    "machin": machin,
    "ramanujan": ramanujan,
}


def run_all_algorithms() -> List[Dict[str, Any]]:
    """
    Run all available Pi calculation algorithms.

    Returns:
        List of result dictionaries from each algorithm.
    """
    results = []

    print("Running all algorithms...\n")

    # Mandelbrot
    print("1/8 Running Mandelbrot Set...")
    results.append(mandelbrot.calculate())

    # Leibniz
    print("2/8 Running Leibniz Formula...")
    results.append(leibniz.calculate())

    # Liu Hui
    print("3/8 Running Liu Hui's Algorithm...")
    results.append(liu_hui.calculate())

    # Euler
    print("4/8 Running Euler Convergence...")
    results.append(euler.calculate())

    # Bailey
    print("5/8 Running Bailey-Borwein-Plouffe...")
    results.append(bailey.calculate())

    # Relative Prime
    print("6/8 Running Relative Prime Probability...")
    results.append(relative_prime.calculate())

    # Machin
    print("7/8 Running Machin's Formula...")
    results.append(machin.calculate())

    # Ramanujan
    print("8/8 Running Ramanujan's Formula...")
    results.append(ramanujan.calculate())

    print("\nAll algorithms completed!\n")

    return results


def calculate_accuracy(pi_value: Any) -> float:
    """
    Calculate the accuracy of a Pi approximation.

    Args:
        pi_value: The calculated Pi value (can be string, float, or Decimal).

    Returns:
        The absolute error from the true value of Pi.
    """
    true_pi = math.pi
    calculated_pi = float(str(pi_value))
    return abs(true_pi - calculated_pi)


def print_comparison_table(results: List[Dict[str, Any]]) -> None:
    """
    Print a formatted comparison table of all results.

    Args:
        results: List of result dictionaries from algorithms.
    """
    print("=" * 100)
    print(f"{'Method':<35} {'Pi Value':<20} {'Error':<15} {'Time (s)':<15}")
    print("=" * 100)

    for result in results:
        method = result["method"]
        pi_val = str(result["pi"])[:18]  # Truncate for display
        error = calculate_accuracy(result["pi"])
        time_sec = result["time_seconds"]

        print(f"{method:<35} {pi_val:<20} {error:<15.2e} {time_sec:<15.6f}")

    print("=" * 100)


def export_results(results: List[Dict[str, Any]], filename: str = "results.json") -> None:
    """
    Export results to a JSON file.

    Args:
        results: List of result dictionaries from algorithms.
        filename: Output filename (default: results.json).
    """
    # Add accuracy to each result
    for result in results:
        result["accuracy_error"] = calculate_accuracy(result["pi"])

    with open(filename, "w") as f:
        json.dump(results, f, indent=2, default=str)

    print(f"\nResults exported to {filename}")


def run_single_algorithm(name: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
    """
    Run a single algorithm by name.

    Args:
        name: Name of the algorithm to run.
        **kwargs: Additional arguments to pass to the algorithm.

    Returns:
        Result dictionary from the algorithm, or None if algorithm not found.
    """
    if name not in ALGORITHMS:
        print(f"Error: Algorithm '{name}' not found.")
        print(f"Available algorithms: {', '.join(ALGORITHMS.keys())}")
        return None

    algorithm = ALGORITHMS[name]
    return algorithm.calculate(**kwargs)
