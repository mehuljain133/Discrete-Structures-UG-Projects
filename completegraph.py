# Write a Program to represent Graphs using the Adjacency Matrices and check if it is a complete graph.

import numpy as np

class Graph:
    def __init__(self, vertices):
        """
        Initialize the graph with a given number of vertices.
        The adjacency matrix will be of size vertices x vertices, initially set to 0.
        """
        self.vertices = vertices
        self.adj_matrix = np.zeros((vertices, vertices), dtype=int)
    
    def add_edge(self, u, v):
        """
        Add an edge between vertex u and vertex v.
        Since the graph is undirected, we update both adj_matrix[u][v] and adj_matrix[v][u].
        """
        if u < self.vertices and v < self.vertices:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
    
    def is_complete_graph(self):
        """
        Check if the graph is complete.
        A graph is complete if all off-diagonal elements in the adjacency matrix are 1.
        The diagonal elements should be 0 (no self-loops).
        """
        for i in range(self.vertices):
            for j in range(self.vertices):
                # Ignore diagonal elements (self-loops)
                if i != j:
                    if self.adj_matrix[i][j] == 0:
                        return False
        return True
    
    def print_graph(self):
        """Print the adjacency matrix of the graph."""
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

# Main function to demonstrate the usage
def main():
    # Input: Number of vertices
    vertices = int(input("Enter the number of vertices: "))
    
    # Create a Graph object
    graph = Graph(vertices)
    
    # Input: Add edges (u, v)
    edges_count = int(input(f"Enter the number of edges for the graph: "))
    for _ in range(edges_count):
        u, v = map(int, input("Enter an edge (u v): ").split())
        graph.add_edge(u, v)
    
    # Print the adjacency matrix
    graph.print_graph()
    
    # Check if the graph is a complete graph
    if graph.is_complete_graph():
        print("The graph is a complete graph.")
    else:
        print("The graph is not a complete graph.")

if __name__ == "__main__":
    main()
