"""
Command-line interface for PiValue.
"""

import argparse
import sys
from typing import Optional
from pivalue import __version__
from pivalue.benchmark import (
    run_all_algorithms,
    run_single_algorithm,
    print_comparison_table,
    export_results,
    ALGORITHMS,
)


def main() -> int:
    """
    Main entry point for the CLI.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    parser = argparse.ArgumentParser(
        description="Calculate Pi using various mathematical algorithms",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  pivalue run mandelbrot          # Run Mandelbrot algorithm
  pivalue run-all                 # Run all algorithms
  pivalue benchmark               # Run all and show comparison
  pivalue benchmark --export      # Run all and export to JSON
        """,
    )

    parser.add_argument("--version", action="version", version=f"PiValue {__version__}")

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Run single algorithm
    run_parser = subparsers.add_parser("run", help="Run a single algorithm")
    run_parser.add_argument(
        "algorithm",
        choices=list(ALGORITHMS.keys()),
        help="Algorithm to run",
    )
    run_parser.add_argument(
        "--iterations",
        type=int,
        help="Number of iterations (for applicable algorithms)",
    )
    run_parser.add_argument(
        "--digits",
        type=int,
        help="Number of digits (for Mandelbrot)",
    )

    # Run all algorithms
    subparsers.add_parser("run-all", help="Run all algorithms")

    # Benchmark
    benchmark_parser = subparsers.add_parser(
        "benchmark", help="Run all algorithms and compare results"
    )
    benchmark_parser.add_argument(
        "--export",
        action="store_true",
        help="Export results to JSON file",
    )
    benchmark_parser.add_argument(
        "--output",
        type=str,
        default="results.json",
        help="Output filename for export (default: results.json)",
    )

    # List algorithms
    subparsers.add_parser("list", help="List all available algorithms")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    if args.command == "list":
        print("Available algorithms:")
        for name in ALGORITHMS.keys():
            print(f"  - {name}")
        return 0

    elif args.command == "run":
        kwargs = {}
        if args.iterations is not None:
            kwargs["num_iterations"] = args.iterations
        if args.digits is not None:
            kwargs["digits"] = args.digits

        result = run_single_algorithm(args.algorithm, **kwargs)
        if result is None:
            return 1

        print(f"\n{'=' * 60}")
        print(f"Method: {result['method']}")
        print(f"{'=' * 60}")
        print(f"Pi ≈ {result['pi']}")
        if isinstance(result.get("iterations"), int):
            print(f"Iterations: {result['iterations']}")
        print(f"Time: {result['time_seconds']:.6f} seconds")
        print(f"Platform: {result['platform']}")
        print(f"{'=' * 60}\n")
        return 0

    elif args.command == "run-all":
        results = run_all_algorithms()
        print("\nResults:")
        print("-" * 60)
        for result in results:
            print(f"{result['method']}: {result['pi']}")
        print("-" * 60)
        return 0

    elif args.command == "benchmark":
        results = run_all_algorithms()
        print_comparison_table(results)

        if args.export:
            export_results(results, args.output)

        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
