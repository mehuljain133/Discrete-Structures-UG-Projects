# Growth of Functions: asymptotic notations, summation formulas and properties, bounding summations, approximation by integrals.

import math
import sympy as sp

# --------------- ASYMPTOTIC NOTATIONS ------------------

# Big O (Upper Bound)
def big_o(f, g, x):
    return sp.limit(f / g, x, sp.oo)

# Big Omega (Lower Bound)
def big_omega(f, g, x):
    return sp.limit(f / g, x, sp.oo)

# Big Theta (Tight Bound)
def big_theta(f, g, x):
    upper_bound = sp.limit(f / g, x, sp.oo)
    lower_bound = sp.limit(g / f, x, sp.oo)
    return upper_bound, lower_bound

# Little o (Strictly Smaller)
def little_o(f, g, x):
    return sp.limit(f / g, x, sp.oo)

# Little omega (Strictly Greater)
def little_omega(f, g, x):
    return sp.limit(g / f, x, sp.oo)

# Example functions
x = sp.symbols('x')
f1 = x**2 + 3*x + 1  # A quadratic function
g1 = x**2  # Compare with a quadratic function

print("Big O of f1 and g1:", big_o(f1, g1, x))
print("Big Omega of f1 and g1:", big_omega(f1, g1, x))
print("Big Theta of f1 and g1:", big_theta(f1, g1, x))
print("Little o of f1 and g1:", little_o(f1, g1, x))
print("Little omega of f1 and g1:", little_omega(f1, g1, x))

# --------------- SUMMATION FORMULAS ------------------

# Sum of the first n natural numbers: S = n(n+1)/2
def sum_natural_numbers(n):
    return n * (n + 1) // 2

# Sum of squares of the first n natural numbers: S = n(n+1)(2n+1)/6
def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

# Sum of cubes of the first n natural numbers: S = (n(n+1)/2)^2
def sum_of_cubes(n):
    return (n * (n + 1) // 2) ** 2

# Sum of a geometric series: S = a * (1 - r^n) / (1 - r) for r != 1
def geometric_sum(a, r, n):
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)

# Example summations
n = 5
print(f"Sum of first {n} natural numbers: {sum_natural_numbers(n)}")
print(f"Sum of squares of first {n} natural numbers: {sum_of_squares(n)}")
print(f"Sum of cubes of first {n} natural numbers: {sum_of_cubes(n)}")

# Geometric sum example
a, r, n_geom = 1, 2, 5
print(f"Sum of geometric series with a={a}, r={r}, n={n_geom}: {geometric_sum(a, r, n_geom)}")

# --------------- BOUNDING SUMMATIONS ------------------

# Upper Bound for summations (bounding an arithmetic series)
def upper_bound_arithmetic_sum(n):
    return n * (n + 1) // 2

# Approximation of a sum using Big O bounds
def approximate_sum(n):
    return O(n**2, n)

# Example: Bounding summations and using approximations
print(f"Upper bound of the sum of first {n} natural numbers (bounding summation): {upper_bound_arithmetic_sum(n)}")

# --------------- APPROXIMATION BY INTEGRALS ------------------

# Integral approximation: Approximating the sum of a function using integrals
def integral_approximation(f, start, end):
    integral_value = sp.integrate(f, (x, start, end))
    return integral_value

# Example: Integral approximation of f(x) = x^2 from 0 to n
f_x = x**2
start, end = 0, n
approx_sum = integral_approximation(f_x, start, end)
print(f"Integral approximation of x^2 from {start} to {end}: {approx_sum}")
