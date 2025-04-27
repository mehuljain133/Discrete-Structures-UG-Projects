#Write a Program to create a SET A and determine the cardinality of SET for an input
#array of elements (repetition allowed) and perform the following operations on the
#SET:a) ismember (a, A): check whether an element belongs to set or not and return value astrue/false.b) powerset(A): list all the elements of power set of A.

import itertools

# Function to check if an element is a member of the set
def ismember(a, A):
    return a in A

# Function to generate the power set of a set
def powerset(A):
    # Convert the set into a list to generate subsets using itertools
    A_list = list(A)
    power_set = []
    # Generate all combinations of subsets of A (including empty set)
    for r in range(len(A_list) + 1):
        subsets = itertools.combinations(A_list, r)
        power_set.extend(subsets)
    return power_set

# Main Function
def main():
    # Input array (with repetitions allowed)
    input_array = input("Enter the elements of the array separated by spaces: ").split()
    
    # Create the set A (this will automatically remove duplicates)
    A = set(input_array)
    
    # Display the set and its cardinality (size)
    print(f"Set A: {A}")
    print(f"Cardinality of Set A: {len(A)}")
    
    # Perform ismember operation
    element_to_check = input("Enter an element to check if it belongs to the set: ")
    if ismember(element_to_check, A):
        print(f"{element_to_check} is a member of the set.")
    else:
        print(f"{element_to_check} is not a member of the set.")
    
    # Generate the power set of A
    power_set = powerset(A)
    print("Power Set of A:")
    for subset in power_set:
        print(subset)

# Run the main function
if __name__ == "__main__":
    main()
