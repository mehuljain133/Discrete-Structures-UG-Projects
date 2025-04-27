# Given a full m-ary tree with i internal vertices, Write a Program to find the number of leaf nodes

def find_leaf_nodes(internal_nodes, m):
    """
    Given the number of internal nodes (i) and the branching factor (m), 
    this function calculates the number of leaf nodes in a full m-ary tree.
    
    Parameters:
    internal_nodes (int): Number of internal nodes in the tree.
    m (int): Number of children each internal node has (branching factor).
    
    Returns:
    int: Number of leaf nodes.
    """
    # The number of leaf nodes in a full m-ary tree
    leaf_nodes = m * internal_nodes + 1
    return leaf_nodes


# Main function
def main():
    # Input: Number of internal nodes and branching factor (m)
    internal_nodes = int(input("Enter the number of internal nodes: "))
    m = int(input("Enter the branching factor (m): "))
    
    # Calculate the number of leaf nodes
    leaf_nodes = find_leaf_nodes(internal_nodes, m)
    
    # Output the result
    print(f"The number of leaf nodes in the full m-ary tree is: {leaf_nodes}")


if __name__ == "__main__":
    main()
