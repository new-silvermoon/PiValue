# PiValue

A comprehensive Python package implementing **8 different mathematical algorithms** to calculate the value of Pi (π). Perfect for benchmarking computational performance and comparing mathematical approaches.

## 🚀 Features

- **8 Algorithms**: Mandelbrot Set, Leibniz Formula, Liu Hui's Method, Euler Convergence, Bailey-Borwein-Plouffe, Relative Prime Probability, Machin's Formula, and Ramanujan's Formula
- **Modern Python**: Built with Python 3.10+ standards, type hints, and best practices
- **CLI Interface**: Easy-to-use command-line interface
- **Benchmarking**: Compare performance and accuracy across all algorithms
- **Comprehensive Tests**: Full test coverage for all algorithms
- **Export Results**: Save results to JSON format

## 📋 Requirements

- Python 3.10 or higher

## 🔧 Installation

### From Source

```bash
# Clone the repository
cd /Users/sagardas/Code/Python/PiValue

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package in development mode
pip install -e .
```

### Install Development Dependencies

```bash
pip install -r requirements.txt
```

## 📖 Usage

### Command-Line Interface

#### List Available Algorithms

```bash
pivalue list
```

#### Run a Single Algorithm

```bash
# Run Mandelbrot algorithm
pivalue run mandelbrot

# Run with custom parameters
pivalue run mandelbrot --digits 7
pivalue run leibniz --iterations 500000
```

#### Run All Algorithms

```bash
pivalue run-all
```

#### Benchmark All Algorithms

```bash
# Run all and display comparison table
pivalue benchmark

# Run all and export results to JSON
pivalue benchmark --export
pivalue benchmark --export --output my_results.json
```

### Python API

```python
from pivalue.algorithms import mandelbrot, leibniz, ramanujan

# Calculate Pi using Mandelbrot method
result = mandelbrot.calculate(digits=5)
print(f"Pi ≈ {result['pi']}")
print(f"Time: {result['time_seconds']:.6f} seconds")

# Calculate using Ramanujan's formula (very fast convergence)
result = ramanujan.calculate(num_iterations=10)
print(f"Pi ≈ {result['pi']}")

# Compare multiple algorithms
from pivalue.benchmark import run_all_algorithms, print_comparison_table

results = run_all_algorithms()
print_comparison_table(results)
```

## 🧮 Algorithms

### 1. Mandelbrot Set Approach
Uses the Mandelbrot set equation f(z) = z² + c to calculate Pi by counting iterations until divergence.

### 2. Madhava-Leibniz Formula
Classic infinite series: π/4 = 1 - 1/3 + 1/5 - 1/7 + ...

### 3. Liu Hui's Algorithm
Ancient Chinese algorithm using polygon approximation with nested square roots.

### 4. Euler Convergence
Factorial-based series with improved convergence properties.

### 5. Bailey-Borwein-Plouffe (BBP) Formula
Modern formula allowing calculation of arbitrary hexadecimal digits of π.

### 6. Relative Prime Probability
Probabilistic approach using P((m,n) = 1) = 6/π².

### 7. Machin's Formula
Highly efficient formula: π/4 = 4·arctan(1/5) - arctan(1/239)

### 8. Ramanujan's Formula
Extremely fast-converging series discovered by Srinivasa Ramanujan, producing ~8 digits per iteration.

## 🧪 Testing

Run the test suite:

```bash
pytest tests/ -v
```

Run tests with coverage:

```bash
pytest tests/ --cov=pivalue --cov-report=html
```

## 📁 Project Structure

```
PiValue/
├── src/pivalue/
│   ├── __init__.py
│   ├── cli.py                    # Command-line interface
│   ├── benchmark.py              # Benchmarking utilities
│   └── algorithms/
│       ├── __init__.py
│       ├── mandelbrot.py
│       ├── leibniz.py
│       ├── liu_hui.py
│       ├── euler.py
│       ├── bailey.py
│       ├── relative_prime.py
│       ├── machin.py
│       └── ramanujan.py
├── tests/                        # Comprehensive test suite
├── pyproject.toml               # Modern Python project config
├── requirements.txt             # Development dependencies
└── README.md
```

## 🎯 Benchmarking

The package includes built-in benchmarking to compare:
- **Accuracy**: Error from true value of π
- **Performance**: Execution time
- **Convergence**: Iterations required

Example output:

```
====================================================================================================
Method                              Pi Value             Error           Time (s)       
====================================================================================================
Mandelbrot Set                      3.1415926535897      1.23e-10        0.002341
Madhava-Leibniz Formula             3.1415926535897      8.97e-06        0.145678
Liu Hui's Algorithm                 3.1415926535897      4.56e-11        0.000123
Euler Convergence                   3.1415926535897      2.34e-12        0.234567
Bailey-Borwein-Plouffe (BBP)        3.1415926535897      5.67e-13        0.012345
Relative Prime Probability          3.1415926535897      1.23e-02        0.567890
Machin's Formula                    3.1415926535897      0.00e+00        0.000045
Ramanujan's Formula                 3.1415926535897      0.00e+00        0.001234
====================================================================================================
```

## 📚 References

- [Leibniz Formula](https://en.wikipedia.org/wiki/Leibniz_formula_for_π)
- [Liu Hui's Algorithm](https://en.wikipedia.org/wiki/Liu_Hui%27s_π_algorithm)
- [Bailey-Borwein-Plouffe Formula](https://en.wikipedia.org/wiki/Bailey–Borwein–Plouffe_formula)
- [Machin-like Formulas](https://en.wikipedia.org/wiki/Machin-like_formula)
- [Ramanujan-Sato Series](https://en.wikipedia.org/wiki/Ramanujan–Sato_series)
- [Relatively Prime Numbers](https://mathworld.wolfram.com/RelativelyPrime.html)
- [Euler Convergence Improvement](http://mathworld.wolfram.com/ConvergenceImprovement.html)

## 🔄 Version History

### Version 2.0.0 (2026)
- Complete modernization to Python 3.10+
- Added CLI interface
- Added benchmarking tools
- Completed Ramanujan implementation
- Fixed bugs in Machin formula
- Added comprehensive test suite
- Replaced deprecated `time.clock()` with `time.perf_counter()`
- Added type hints throughout

### Version 1.0.0 (Original)
- Initial implementation with 7 algorithms
- Python 3.6 compatibility

## 📄 License

MIT License

## 👤 Author

Sagar Das






