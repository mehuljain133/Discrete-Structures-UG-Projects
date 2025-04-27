# Create a class RELATION, use Matrix notation to represent a relation. Include functionsto check if the relation is Reflexive, Symmetric, Anti-symmetric and Transitive. Write aProgram to use this class.check whether the given relation is:a) Equivalent, orb) Partial Order relation, orc) None

class RELATION:
    def __init__(self, matrix: list):
        """
        Initializes the RELATION object with a matrix representation of the relation.
        
        :param matrix: A square matrix where matrix[i][j] = 1 means there is a relation from element i to j
        """
        self.matrix = matrix
        self.size = len(matrix)  # Assuming the matrix is square

    def is_reflexive(self) -> bool:
        """
        Checks if the relation is reflexive. The relation is reflexive if all diagonal elements are 1.
        
        :return: True if reflexive, False otherwise
        """
        for i in range(self.size):
            if self.matrix[i][i] != 1:
                return False
        return True
    
    def is_symmetric(self) -> bool:
        """
        Checks if the relation is symmetric. The relation is symmetric if M[i][j] == M[j][i] for all i, j.
        
        :return: True if symmetric, False otherwise
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True
    
    def is_antisymmetric(self) -> bool:
        """
        Checks if the relation is anti-symmetric. The relation is anti-symmetric if M[i][j] == 1 and M[j][i] == 1
        implies i == j for all i, j.
        
        :return: True if anti-symmetric, False otherwise
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] == 1 and self.matrix[j][i] == 1 and i != j:
                    return False
        return True
    
    def is_transitive(self) -> bool:
        """
        Checks if the relation is transitive. The relation is transitive if for all i, j, k:
        If M[i][j] = 1 and M[j][k] = 1, then M[i][k] = 1.
        
        :return: True if transitive, False otherwise
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] == 1:  # If there is a relation from i to j
                    for k in range(self.size):
                        if self.matrix[j][k] == 1:  # If there is a relation from j to k
                            if self.matrix[i][k] != 1:  # Then there must be a relation from i to k
                                return False
        return True
    
    def is_equivalent(self) -> bool:
        """
        Checks if the relation is an Equivalent relation. 
        An equivalent relation must be reflexive, symmetric, and transitive.
        
        :return: True if equivalent, False otherwise
        """
        return self.is_reflexive() and self.is_symmetric() and self.is_transitive()
    
    def is_partial_order(self) -> bool:
        """
        Checks if the relation is a Partial Order. 
        A partial order must be reflexive, antisymmetric, and transitive.
        
        :return: True if partial order, False otherwise
        """
        return self.is_reflexive() and self.is_antisymmetric() and self.is_transitive()
    
    def display_matrix(self):
        """Displays the relation matrix."""
        for row in self.matrix:
            print(row)

# Main function to demonstrate the RELATION class functionality
def main():
    try:
        # Input matrix for relation representation
        print("Enter the relation matrix (square matrix, each row space-separated):")
        matrix = []
        n = int(input("Enter the size of the matrix (n x n): "))
        print(f"Enter {n} rows of the matrix (each row should have {n} space-separated values 0 or 1):")
        
        for i in range(n):
            row = list(map(int, input().split()))
            if len(row) != n:
                raise ValueError("Each row must have exactly n elements.")
            matrix.append(row)
        
        # Create RELATION object
        relation = RELATION(matrix)
        
        # Display the matrix
        print("\nThe Relation Matrix is:")
        relation.display_matrix()
        
        # Check if the relation is reflexive, symmetric, antisymmetric, and transitive
        print("\nChecking the properties of the relation:")
        print(f"Is Reflexive? {'Yes' if relation.is_reflexive() else 'No'}")
        print(f"Is Symmetric? {'Yes' if relation.is_symmetric() else 'No'}")
        print(f"Is Anti-symmetric? {'Yes' if relation.is_antisymmetric() else 'No'}")
        print(f"Is Transitive? {'Yes' if relation.is_transitive() else 'No'}")
        
        # Check the type of relation (Equivalent or Partial Order)
        if relation.is_equivalent():
            print("The relation is an Equivalent Relation.")
        elif relation.is_partial_order():
            print("The relation is a Partial Order Relation.")
        else:
            print("The relation is neither Equivalent nor Partial Order.")
    
    except ValueError as e:
        print(f"Error: {e}")

# Run the main function
if __name__ == "__main__":
    main()
