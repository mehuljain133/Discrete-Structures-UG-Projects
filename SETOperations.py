#Create a class SET and take two sets as input from user to perform following SET Operations

class SET:
    def __init__(self, elements):
        # Initialize the set with the given elements (unique values)
        self.set_elements = set(elements)
    
    def display(self):
        # Display the set
        return self.set_elements
    
    def ismember(self, a):
        # Check if element 'a' is in the set
        return a in self.set_elements
    
    def union(self, other_set):
        # Union of two sets
        return self.set_elements | other_set.set_elements
    
    def intersection(self, other_set):
        # Intersection of two sets
        return self.set_elements & other_set.set_elements
    
    def difference(self, other_set):
        # Difference of two sets (elements in this set but not in the other)
        return self.set_elements - other_set.set_elements
    
    def symmetric_difference(self, other_set):
        # Symmetric Difference (elements in either set but not both)
        return self.set_elements ^ other_set.set_elements
    
    def cardinality(self):
        # Return the cardinality of the set (number of elements)
        return len(self.set_elements)
    
# Main function
def main():
    # Take input for the first set from the user
    input1 = input("Enter the elements of the first set (separated by space): ").split()
    # Take input for the second set from the user
    input2 = input("Enter the elements of the second set (separated by space): ").split()
    
    # Create SET objects for both sets
    set1 = SET(input1)
    set2 = SET(input2)
    
    # Display the sets
    print(f"Set 1: {set1.display()}")
    print(f"Set 2: {set2.display()}")
    
    # Perform various set operations
    print(f"Union of Set 1 and Set 2: {set1.union(set2)}")
    print(f"Intersection of Set 1 and Set 2: {set1.intersection(set2)}")
    print(f"Difference of Set 1 and Set 2: {set1.difference(set2)}")
    print(f"Symmetric Difference of Set 1 and Set 2: {set1.symmetric_difference(set2)}")
    
    # Perform membership test
    element_to_check = input("Enter an element to check membership in Set 1: ")
    print(f"Is {element_to_check} a member of Set 1? {'Yes' if set1.ismember(element_to_check) else 'No'}")
    
    # Display cardinality
    print(f"Cardinality of Set 1: {set1.cardinality()}")
    print(f"Cardinality of Set 2: {set2.cardinality()}")

# Run the main function
if __name__ == "__main__":
    main()
