# Write a Program that generates all the permutations of a given set of digits, with or without repetition. (For example, if the given set is {1,2}, the permutations are 12 and21). (One method is given in Liu)

import itertools

class Permutations:
    def __init__(self, digits):
        """
        Initialize with a set of digits (list or string)
        """
        self.digits = digits

    def permutations_without_repetition(self):
        """
        Generate permutations without repetition.
        """
        return list(itertools.permutations(self.digits))

    def permutations_with_repetition(self, length):
        """
        Generate permutations with repetition.
        The length of each permutation is specified by `length`.
        """
        return list(itertools.product(self.digits, repeat=length))

    def display_permutations(self, permutations):
        """
        Display the permutations in a readable format.
        """
        for perm in permutations:
            print(''.join(map(str, perm)))

# Example usage
def main():
    digits = input("Enter a set of digits (comma separated): ").split(',')
    digits = [digit.strip() for digit in digits]  # Clean up any extra spaces
    
    perm_obj = Permutations(digits)
    
    print("\nPermutations without repetition:")
    perms_no_repetition = perm_obj.permutations_without_repetition()
    perm_obj.display_permutations(perms_no_repetition)
    
    length = int(input("\nEnter the length of permutations with repetition: "))
    print("\nPermutations with repetition:")
    perms_with_repetition = perm_obj.permutations_with_repetition(length)
    perm_obj.display_permutations(perms_with_repetition)

if __name__ == "__main__":
    main()
