#Create a class SET and take two sets as input from user to perform following SET Operations

from typing import List, Set, Union
import itertools

class SET:
    def __init__(self, elements: List[Union[int, str]]):
        """
        Initializes the SET object with unique elements. 
        The input list can contain repeated elements, which will be removed in the set.

        :param elements: List of elements to be added to the set
        """
        self.set_elements: Set[Union[int, str]] = set(elements)
    
    def display(self) -> Set[Union[int, str]]:
        """
        Displays the current set elements.
        
        :return: The set of elements
        """
        return self.set_elements
    
    def ismember(self, a: Union[int, str]) -> bool:
        """
        Checks if an element 'a' is a member of the set.
        
        :param a: Element to check for membership in the set
        :return: True if 'a' is in the set, False otherwise
        """
        return a in self.set_elements
    
    def union(self, other_set: 'SET') -> Set[Union[int, str]]:
        """
        Returns the union of two sets.
        
        :param other_set: Another SET object to perform the union operation with
        :return: The union of this set and the other set
        """
        return self.set_elements | other_set.set_elements
    
    def intersection(self, other_set: 'SET') -> Set[Union[int, str]]:
        """
        Returns the intersection of two sets.
        
        :param other_set: Another SET object to perform the intersection operation with
        :return: The intersection of this set and the other set
        """
        return self.set_elements & other_set.set_elements
    
    def difference(self, other_set: 'SET') -> Set[Union[int, str]]:
        """
        Returns the difference between two sets (elements in the current set but not in the other set).
        
        :param other_set: Another SET object to perform the difference operation with
        :return: The difference of this set and the other set
        """
        return self.set_elements - other_set.set_elements
    
    def symmetric_difference(self, other_set: 'SET') -> Set[Union[int, str]]:
        """
        Returns the symmetric difference between two sets (elements in either set, but not both).
        
        :param other_set: Another SET object to perform the symmetric difference operation with
        :return: The symmetric difference of this set and the other set
        """
        return self.set_elements ^ other_set.set_elements
    
    def cardinality(self) -> int:
        """
        Returns the cardinality (size) of the set.
        
        :return: The number of elements in the set
        """
        return len(self.set_elements)
    
    def power_set(self) -> Set[frozenset]:
        """
        Returns the power set of the current set. The power set is the set of all subsets.
        
        :return: The power set of the set as a set of frozensets (immutable sets)
        """
        power_set = set()
        for i in range(len(self.set_elements) + 1):
            # Generate all subsets using combinations
            for subset in itertools.combinations(self.set_elements, i):
                power_set.add(frozenset(subset))  # Use frozenset to ensure immutability of subsets
        return power_set
    
    def subset(self, other_set: 'SET') -> bool:
        """
        Check whether the current set is a subset of the other set.
        
        :param other_set: The other SET to check for the subset condition
        :return: True if the current set is a subset of the other set, False otherwise
        """
        return self.set_elements <= other_set.set_elements
    
    def complement(self, universal_set: 'SET') -> Set[Union[int, str]]:
        """
        Returns the complement of the current set relative to the universal set.
        
        :param universal_set: The universal set to compute the complement relative to
        :return: The complement of the current set
        """
        return universal_set.set_elements - self.set_elements
    
    def cartesian_product(self, other_set: 'SET') -> Set[tuple]:
        """
        Computes the Cartesian product of the current set and another set.
        
        :param other_set: Another SET object to compute the Cartesian product with
        :return: A set of tuples representing the Cartesian product
        """
        return {(x, y) for x in self.set_elements for y in other_set.set_elements}
    
    def __str__(self) -> str:
        """
        String representation of the set for easier printing.
        
        :return: String representation of the set
        """
        return f"SET({self.set_elements})"


# Main function to demonstrate the advanced SET operations
def main():
    # Error handling for user inputs
    try:
        # Take input for the first set from the user
        input1 = input("Enter the elements of the first set (separated by space): ").split()
        # Validate input for type (string or integer values)
        if not all(item.isdigit() or item.isalpha() for item in input1):
            raise ValueError("Input elements must be either strings or integers.")
        
        # Take input for the second set from the user
        input2 = input("Enter the elements of the second set (separated by space): ").split()
        # Validate input for type (string or integer values)
        if not all(item.isdigit() or item.isalpha() for item in input2):
            raise ValueError("Input elements must be either strings or integers.")
        
        # Take input for the universal set (the superset for complement operations)
        universal_input = input("Enter the elements of the universal set (separated by space): ").split()
        if not all(item.isdigit() or item.isalpha() for item in universal_input):
            raise ValueError("Input elements must be either strings or integers.")
        
        # Convert input to integers or leave as strings
        input1 = [int(x) if x.isdigit() else x for x in input1]
        input2 = [int(x) if x.isdigit() else x for x in input2]
        universal_input = [int(x) if x.isdigit() else x for x in universal_input]
        
        # Create SET objects for both sets and the universal set
        set1 = SET(input1)
        set2 = SET(input2)
        universal_set = SET(universal_input)
        
        # Display the sets
        print(f"Set 1: {set1}")
        print(f"Set 2: {set2}")
        print(f"Universal Set: {universal_set}")
        
        # Perform various set operations
        print(f"Union of Set 1 and Set 2: {set1.union(set2)}")
        print(f"Intersection of Set 1 and Set 2: {set1.intersection(set2)}")
        print(f"Difference of Set 1 and Set 2: {set1.difference(set2)}")
        print(f"Symmetric Difference of Set 1 and Set 2: {set1.symmetric_difference(set2)}")
        
        # Subset check
        print(f"Is Set 1 a subset of Set 2? {'Yes' if set1.subset(set2) else 'No'}")
        
        # Perform membership test
        element_to_check = input("Enter an element to check membership in Set 1: ")
        if element_to_check.isdigit():
            element_to_check = int(element_to_check)
        
        print(f"Is {element_to_check} a member of Set 1? {'Yes' if set1.ismember(element_to_check) else 'No'}")
        
        # Display cardinality
        print(f"Cardinality of Set 1: {set1.cardinality()}")
        print(f"Cardinality of Set 2: {set2.cardinality()}")
        
        # Display power set of Set 1
        print("Power Set of Set 1:")
        power_set1 = set1.power_set()
        for subset in power_set1:
            print(subset)
        
        # Complement of Set 1 with respect to the Universal Set
        print(f"Complement of Set 1 with respect to the Universal Set: {set1.complement(universal_set)}")
        
        # Cartesian Product of Set 1 and Set 2
        print(f"Cartesian Product of Set 1 and Set 2: {set1.cartesian_product(set2)}")
        
    except ValueError as e:
        print(f"Error: {e}")

# Run the main function
if __name__ == "__main__":
    main()
