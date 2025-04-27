# Write a Program to accept the truth values of variables x and y, and print the truth table of the following logical operations

def truth_table():
    # Loop through all possible combinations of x and y (True, False)
    print("x\ty\tAND\tOR\tXOR\tNAND\tNOR\tIMPLIES")
    for x in [False, True]:
        for y in [False, True]:
            # Calculate all logical operations
            and_op = x and y
            or_op = x or y
            xor_op = x != y
            nand_op = not (x and y)
            nor_op = not (x or y)
            implies_op = not x or y
            
            # Print the truth table row for the current x and y
            print(f"{x}\t{y}\t{and_op}\t{or_op}\t{xor_op}\t{nand_op}\t{nor_op}\t{implies_op}")

# Main function to call truth_table and display results
if __name__ == "__main__":
    truth_table()
