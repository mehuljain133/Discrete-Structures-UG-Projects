# Given a graph G, write a Program to find the number of paths of length n between the source and destination entered by the user

import numpy as np

class Graph:
    def __init__(self, vertices):
        """Initialize the graph with a given number of vertices."""
        self.vertices = vertices
        self.adj_matrix = np.zeros((vertices, vertices), dtype=int)
    
    def add_edge(self, u, v):
        """Add a directed edge from vertex u to vertex v."""
        if u < self.vertices and v < self.vertices:
            self.adj_matrix[u][v] = 1
    
    def matrix_multiply(self, A, B):
        """Matrix multiplication of two matrices A and B."""
        return np.dot(A, B)
    
    def matrix_exponentiate(self, A, power):
        """Exponentiate the adjacency matrix A to the given power."""
        result = np.identity(self.vertices, dtype=int)  # Identity matrix
        base = A
        
        while power > 0:
            if power % 2 == 1:
                result = self.matrix_multiply(result, base)
            base = self.matrix_multiply(base, base)
            power //= 2
        return result
    
    def find_paths(self, source, destination, length):
        """Find the number of paths of given length from source to destination."""
        # Get the adjacency matrix raised to the power of 'length'
        exp_matrix = self.matrix_exponentiate(self.adj_matrix, length)
        
        # Return the number of paths from source to destination
        return exp_matrix[source][destination]
    
    def print_graph(self):
        """Print the adjacency matrix."""
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))


# Main function to demonstrate the usage
def main():
    # Input: Number of vertices
    vertices = int(input("Enter the number of vertices: "))
    
    # Create the Graph object
    graph = Graph(vertices)
    
    # Input: Add edges (u, v)
    edges_count = int(input(f"Enter the number of edges for the graph: "))
    for _ in range(edges_count):
        u, v = map(int, input("Enter an edge (u v): ").split())
        graph.add_edge(u, v)
    
    # Print the adjacency matrix
    graph.print_graph()
    
    # Input: Source, Destination, and Path Length
    source = int(input("Enter the source vertex: "))
    destination = int(input("Enter the destination vertex: "))
    length = int(input("Enter the path length: "))
    
    # Find and display the number of paths of the given length
    number_of_paths = graph.find_paths(source, destination, length)
    print(f"The number of paths of length {length} from vertex {source} to vertex {destination} is: {number_of_paths}")


if __name__ == "__main__":
    main()
