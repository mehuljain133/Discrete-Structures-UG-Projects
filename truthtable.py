# Write a Program to accept the truth values of variables x and y, and print the truth table of the following logical operations

import numpy as np
import itertools

class LogicalOperations:
    def __init__(self, x_values, y_values):
        """
        Initialize with the list of truth values for x and y.
        """
        self.x_values = x_values
        self.y_values = y_values
        self.results = {}

    def and_op(self):
        """AND operation (x AND y)"""
        return np.logical_and(self.x_values, self.y_values)

    def or_op(self):
        """OR operation (x OR y)"""
        return np.logical_or(self.x_values, self.y_values)

    def xor_op(self):
        """XOR operation (x XOR y)"""
        return np.logical_xor(self.x_values, self.y_values)

    def nand_op(self):
        """NAND operation (not (x AND y))"""
        return np.logical_not(self.and_op())

    def nor_op(self):
        """NOR operation (not (x OR y))"""
        return np.logical_not(self.or_op())

    def implies_op(self):
        """Implies operation (x → y), equivalent to (not x OR y)"""
        return np.logical_or(np.logical_not(self.x_values), self.y_values)

    def biconditional_op(self):
        """Bi-Conditional operation (x ↔ y)"""
        return np.logical_xor(self.x_values, self.y_values) == False

    def xnor_op(self):
        """XNOR operation (not (x XOR y))"""
        return np.logical_not(self.xor_op())

    def print_truth_table(self):
        """Print the truth table for all operations"""
        header = ["x", "y", "AND", "OR", "XOR", "NAND", "NOR", "Implies", "Biconditional", "XNOR"]
        print("\t".join(header))
        
        # Generate the combinations of x and y (each combination is an array)
        for x, y in zip(self.x_values, self.y_values):
            row = [int(x), int(y), 
                   int(self.and_op()[0]), int(self.or_op()[0]), 
                   int(self.xor_op()[0]), int(self.nand_op()[0]), 
                   int(self.nor_op()[0]), int(self.implies_op()[0]), 
                   int(self.biconditional_op()[0]), int(self.xnor_op()[0])]
            print("\t".join(map(str, row)))

    def check_tautology(self):
        """Check if the expression is a tautology (always true)"""
        for operation in [self.and_op, self.or_op, self.xor_op, self.nand_op, self.nor_op, self.implies_op, self.biconditional_op, self.xnor_op]:
            if not np.all(operation()):  # If any result is False, it's not a tautology
                return False
        return True

    def check_contradiction(self):
        """Check if the expression is a contradiction (always false)"""
        for operation in [self.and_op, self.or_op, self.xor_op, self.nand_op, self.nor_op, self.implies_op, self.biconditional_op, self.xnor_op]:
            if np.any(operation()):  # If any result is True, it's not a contradiction
                return False
        return True


def main():
    # Possible truth values
    x_values = np.array([False, True])
    y_values = np.array([False, True])

    # Instantiate LogicalOperations class
    logic_ops = LogicalOperations(x_values, y_values)

    # Print the truth table
    logic_ops.print_truth_table()

    # Check if the operations form a tautology or contradiction
    if logic_ops.check_tautology():
        print("\nThe operations form a tautology (always true).")
    elif logic_ops.check_contradiction():
        print("\nThe operations form a contradiction (always false).")
    else:
        print("\nThe operations are neither a tautology nor a contradiction.")

if __name__ == "__main__":
    main()
