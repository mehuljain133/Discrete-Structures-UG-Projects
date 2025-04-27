# Introduction: Sets - finite and infinite sets, uncountable infinite sets; functions, relations,
# properties of binary relations, closure, partial ordering relations; counting - Pigeonhole Principle,
# permutation and combination; mathematical induction, Principle of Inclusion and Exclusion. 

import itertools
import math

# --------------- SET THEORY ---------------
# Finite Set
finite_set = {1, 2, 3, 4, 5}

# Infinite Set (Conceptual representation)
def infinite_set_example():
    return "This represents an infinite set (e.g., natural numbers, Z)."

# Uncountable Infinite Set (Conceptual example with real numbers between 0 and 1)
def uncountable_infinite_set():
    return "This represents an uncountable set (e.g., real numbers between 0 and 1)."

# Set Operations: Union, Intersection, Difference, Symmetric Difference
def set_operations(set_A, set_B):
    union = set_A.union(set_B)
    intersection = set_A.intersection(set_B)
    difference = set_A.difference(set_B)
    symmetric_difference = set_A.symmetric_difference(set_B)
    return {
        'union': union,
        'intersection': intersection,
        'difference': difference,
        'symmetric_difference': symmetric_difference
    }

# Power Set: All subsets of a given set
def power_set(set_A):
    return [set(x) for x in itertools.chain.from_iterable(itertools.combinations(set_A, r) for r in range(len(set_A)+1))]

# ------------ RELATIONS -------------
# Example of binary relation: "less than"
relation = lambda x, y: x < y

# Checking Reflexive, Symmetric, Transitive properties
def is_reflexive(relation, set_elements):
    return all(relation(x, x) for x in set_elements)

def is_symmetric(relation, set_elements):
    return all(relation(x, y) == relation(y, x) for x in set_elements for y in set_elements)

def is_transitive(relation, set_elements):
    return all(relation(x, y) and relation(y, z) <= relation(x, z) for x in set_elements for y in set_elements for z in set_elements)

# Example of Equivalence Relation (Reflexive, Symmetric, and Transitive)
def equivalence_relation(set_elements):
    return { (x, x) for x in set_elements }  # Reflexive pairs

# Partial Ordering example: "Less than or equal to"
partial_order = lambda x, y: x <= y

# ----------- COUNTING PRINCIPLES -----------

# Pigeonhole Principle (Generalized version)
def pigeonhole_principle(n, m):
    if n > m:
        return "At least one pigeonhole contains more than one pigeon."
    return "Pigeonholes can be empty."

# Factorial Calculation for n!
def factorial(n):
    return math.factorial(n)

# Permutations and Combinations (Generalized)
def permutations_example(n, r):
    return list(itertools.permutations(range(1, n + 1), r))

def combinations_example(n, r):
    return list(itertools.combinations(range(1, n + 1), r))

# Stirling numbers of the second kind (Partitioning set of size n into k non-empty subsets)
def stirling_second_kind(n, k):
    if k == 0 or k > n:
        return 0
    if k == 1 or k == n:
        return 1
    table = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        table[i][0] = 0
    for i in range(k + 1):
        table[0][i] = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            table[i][j] = j * table[i - 1][j] + table[i - 1][j - 1]
    return table[n][k]

# Binomial Coefficients: n choose r
def binomial_coefficient(n, r):
    return math.comb(n, r)

# ----------- MATHEMATICAL INDUCTION ---------------

# Weak Induction: Prove that P(n) is true for all n >= 1
def weak_induction(base_case_fn, inductive_step_fn, n_max):
    # Base case
    if not base_case_fn(1):  # Base case: P(1) must be true
        return False
    
    # Inductive step
    for n in range(2, n_max + 1):
        if not inductive_step_fn(n):
            return False
    
    return True

# Strong Induction: Prove that P(n) is true for all n >= 1
def strong_induction(base_case_fn, inductive_step_fn, n_max):
    # Base case
    if not base_case_fn(1):  # Base case: P(1) must be true
        return False
    
    # Inductive step
    for n in range(2, n_max + 1):
        if not inductive_step_fn(n, n_max):
            return False
    
    return True

# ----------- PRINCIPLE OF INCLUSION-EXCLUSION ---------------

# Inclusion-Exclusion Principle (PIE) for two sets
def inclusion_exclusion(set_A, set_B):
    intersection = set_A.intersection(set_B)
    union = set_A.union(set_B)
    
    # PIE formula: |A ∪ B| = |A| + |B| - |A ∩ B|
    return len(set_A) + len(set_B) - len(intersection)

# Advanced Inclusion-Exclusion for multiple sets (generalized version)
def generalized_inclusion_exclusion(sets):
    n = len(sets)
    total = 0
    
    # Iterate over all subsets of the sets
    for r in range(1, n+1):
        for subset in itertools.combinations(sets, r):
            intersection = set.intersection(*subset)
            total += (-1)**(r+1) * len(intersection)
    
    return total

# Example usage:
# Testing permutation and combination
print("Permutations of 3 elements taken 2 at a time:", permutations_example(3, 2))
print("Combinations of 3 elements taken 2 at a time:", combinations_example(3, 2))

# Testing Stirling numbers (partitioning)
print("Stirling number of the second kind for partitioning 5 elements into 3 non-empty subsets:", stirling_second_kind(5, 3))

# Testing inclusion-exclusion with two sets
set_A = {1, 2, 3}
set_B = {2, 3, 4}
print("Inclusion-Exclusion of Set A and Set B:", inclusion_exclusion(set_A, set_B))

# Testing generalized Inclusion-Exclusion with 3 sets
set_C = {3, 4, 5}
sets = [set_A, set_B, set_C]
print("Generalized Inclusion-Exclusion for sets A, B, C:", generalized_inclusion_exclusion(sets))

# Induction example: Prove that 1+2+...+n = n*(n+1)/2 using induction
def base_case_fn(n):
    return n * (n + 1) // 2 == sum(range(1, n+1))

def inductive_step_fn(n):
    return (n * (n + 1)) // 2 == sum(range(1, n + 1))

print("Induction for sum formula valid for n = 10:", weak_induction(base_case_fn, inductive_step_fn, 10))

# Strong Induction example: Prove that any integer n >= 2 can be factored into primes
def base_case_fn_strong(n):
    return n == 2 or n == 3  # Base case: 2 and 3 are prime numbers

def inductive_step_fn_strong(n, n_max):
    if n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)):
        return True
    return False

print("Strong Induction for prime factorization valid for n = 10:", strong_induction(base_case_fn_strong, inductive_step_fn_strong, 10))

