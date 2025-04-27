# Write a Program to calculate Permutation and Combination for an input value n and r using recursive formula of nCr and nPr

class PermutationCombination:
    
    def combination(self, n, r):
        """
        Calculate nCr using recursive formula.
        """
        # Base cases
        if r == 0 or r == n:
            return 1
        # Recursive formula: nCr = (n-1)Cr-1 + (n-1)Cr
        return self.combination(n-1, r-1) + self.combination(n-1, r)
    
    def permutation(self, n, r):
        """
        Calculate nPr using recursive formula.
        """
        # Base case
        if r == 0:
            return 1
        # Recursive formula: nPr = n * (n-1)Pr-1
        return n * self.permutation(n-1, r-1)

# Main program to take input and calculate nCr and nPr
def main():
    n = int(input("Enter value of n: "))
    r = int(input("Enter value of r: "))
    
    pc = PermutationCombination()
    
    # Calculate nCr and nPr
    nCr = pc.combination(n, r)
    nPr = pc.permutation(n, r)
    
    # Display results
    print(f"Combination (nCr) for n = {n} and r = {r} is: {nCr}")
    print(f"Permutation (nPr) for n = {n} and r = {r} is: {nPr}")

# Execute the program
if __name__ == "__main__":
    main()
