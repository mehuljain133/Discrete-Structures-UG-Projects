# Write a Program to store a function (polynomial/exponential), and then evaluate the polynomial. (For example store f(x) = 4n3 + 2n + 9 in an array and for a given value of n, sayn = 5, evaluate (i.e. compute the value of f(5)).

class Polynomial:
    def __init__(self, terms):
        """
        Initialize the polynomial with a list of (coefficient, exponent) pairs.
        For example, for the polynomial 4n^3 + 2n + 9, the terms would be [(4, 3), (2, 1), (9, 0)].
        """
        self.terms = terms
    
    def evaluate(self, n):
        """
        Evaluate the polynomial for a given value of n.
        The terms list contains (coefficient, exponent) pairs.
        """
        result = 0
        for coefficient, exponent in self.terms:
            result += coefficient * (n ** exponent)
        return result

# Main function to demonstrate usage
def main():
    # Define the polynomial 4n^3 + 2n + 9
    polynomial_terms = [(4, 3), (2, 1), (9, 0)]  # (coefficient, exponent)
    
    # Create a Polynomial object
    poly = Polynomial(polynomial_terms)
    
    # Given value of n
    n = 5
    
    # Evaluate the polynomial for n = 5
    result = poly.evaluate(n)
    
    # Display the result
    print(f"The value of the polynomial for n = {n} is: {result}")

if __name__ == "__main__":
    main()
