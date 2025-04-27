# For any number n, write a program to list all the solutions of the equation x1 + x2 + x3 +…+ xn = C, where C is a constant (C<=10) and x1, x2,x3,…,xn are nonnegative integersusing brute force strategy

import itertools

def find_solutions(n, C):
    """
    Find all solutions to the equation x1 + x2 + ... + xn = C where
    x1, x2, ..., xn are non-negative integers and C is the constant sum.
    """
    # Create a range of values for each xi from 0 to C
    # The Cartesian product generates all possible combinations of non-negative integers
    # whose sum will be equal to C
    solutions = []
    
    # Generate all combinations of n elements where each element is between 0 and C
    for comb in itertools.product(range(C + 1), repeat=n):
        if sum(comb) == C:
            solutions.append(comb)
    
    return solutions

def main():
    n = int(input("Enter the number of variables (n): "))
    C = int(input("Enter the constant sum (C <= 10): "))
    
    if C > 10:
        print("C must be less than or equal to 10.")
        return
    
    # Find all solutions to the equation
    solutions = find_solutions(n, C)
    
    # Print the solutions
    print(f"All solutions for x1 + x2 + ... + xn = {C} are:")
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
