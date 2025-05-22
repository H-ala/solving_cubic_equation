# Cubic Equation Solver

This Python script solves a general **cubic equation** of the form:


It uses a combination of normalization, Cardano's method, and complex number handling to compute all three roots—real or complex.

## 📌 Features

- Accepts user input for coefficients `a`, `b`, `c`, and `d`.
- Automatically normalizes the equation if `a ≠ 1`.
- Eliminates the quadratic term using a substitution.
- Calculates the discriminant to determine the nature of roots.
- Handles:
  - One real and two complex roots.
  - Three real roots (distinct or repeated).

## 🧮 Methodology

The solver uses **Cardano's formula** for solving depressed cubic equations:

1. Normalize the equation to make the leading coefficient 1.
2. Substitute `x = y - p/3` to eliminate the `x²` term.
3. Reduce to the depressed form: `y³ + m·y + n = 0`
4. Solve based on the discriminant:
   - If Δ ≥ 0: one real and two complex roots.
   - If Δ < 0: three real roots.

## 🛠️ Requirements

- Python 3.x
- NumPy

Install NumPy if not available:

```bash
pip install numpy
