# Recurrence: recurrence relations, generating functions, linear recurrence relations with constant coefficients and their solution, recursion trees, Master Theorem

import sympy as sp
import math
import numpy as np
import matplotlib.pyplot as plt

# --------------- RECURRENCE RELATIONS ---------------
# Example of a simple recurrence: Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Linear Recurrence Relation with constant coefficients: T(n) = aT(n/b) + f(n)
# For example, T(n) = 2T(n/2) + n
def recurrence_example(n):
    if n <= 1:
        return 1
    return 2 * recurrence_example(n // 2) + n

# --------------- GENERATING FUNCTIONS ---------------
# Generating Function for Fibonacci sequence: F(x) = x / (1 - x - x^2)
def generating_function_fibonacci(x):
    return x / (1 - x - x**2)

# --------------- LINEAR RECURRENCE RELATIONS WITH CONSTANT COEFFICIENTS ---------------

# Solve a linear recurrence relation with constant coefficients using the characteristic equation
def solve_linear_recurrence(a, b, c, n):
    """
    Solves the recurrence relation of the form:
    T(n) = a*T(n-1) + b*T(n-2) + c (constant)
    """
    # Solving recurrence with characteristic equation approach
    characteristic_eq = sp.symbols('r')
    characteristic_polynomial = a * characteristic_eq**2 - characteristic_eq + b
    roots = sp.solve(characteristic_polynomial, characteristic_eq)
    return roots

# Example linear recurrence relation: T(n) = 2*T(n-1) - T(n-2)
# We solve it using the characteristic equation
a, b = 2, -1
c = 0  # constant term is zero for this example
n = 10
print("Roots of the characteristic equation:", solve_linear_recurrence(a, b, c, n))

# --------------- RECURSION TREES ------------------

# Recursion tree for T(n) = 2T(n/2) + n
def recursion_tree(n):
    if n <= 1:
        return 1
    return 2 * recursion_tree(n // 2) + n

# Visualize recursion tree (for n=16) using Matplotlib
def plot_recursion_tree(n):
    levels = []
    current_level = [n]
    while n > 1:
        n = n // 2
        current_level = [n] * 2
        levels.append(current_level)
    print("Levels of recursion tree:", levels)

plot_recursion_tree(16)

# --------------- MASTER THEOREM ------------------

# Master Theorem for Divide-and-Conquer Recurrences:
# T(n) = aT(n/b) + f(n) has the following solution:
# - If f(n) = O(n^d) and log_b(a) < d, T(n) = O(n^d)
# - If log_b(a) = d, T(n) = O(n^d log n)
# - If log_b(a) > d, T(n) = O(n^log_b(a))

def master_theorem(a, b, d):
    log_b_a = math.log(a, b)
    if log_b_a < d:
        return f"O(n^{d})"
    elif log_b_a == d:
        return f"O(n^{d} * log n)"
    else:
        return f"O(n^{log_b_a})"

# Example: T(n) = 2T(n/2) + n
a = 2  # Number of subproblems
b = 2  # Factor by which the problem size is reduced
d = 1  # Growth rate of the cost of work at each level

# Applying Master Theorem for this recurrence
print("Master Theorem Solution for T(n) = 2T(n/2) + n:", master_theorem(a, b, d))

# --------------- VISUALIZING RECURSION TREES ------------------

# Plotting a simple example of recursion tree for T(n) = 2T(n/2) + n
def plot_recursion_tree_example(n):
    def helper(n, level, data):
        if n <= 1:
            return
        data[level] += 1
        helper(n // 2, level + 1, data)
        helper(n // 2, level + 1, data)

    data = {i: 0 for i in range(int(math.log2(n)) + 1)}
    helper(n, 0, data)
    levels = list(data.keys())
    counts = list(data.values())
    
    plt.bar(levels, counts)
    plt.xlabel('Recursion Level')
    plt.ylabel('Number of Calls')
    plt.title(f'Recursion Tree for T(n) = 2T(n/2) + n')
    plt.show()

plot_recursion_tree_example(16)

