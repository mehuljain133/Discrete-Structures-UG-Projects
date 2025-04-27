# Write a Program to accept a directed graph G and compute the in-degree and out-degree of each vertex

import numpy as np

class DirectedGraph:
    def __init__(self, vertices):
        """
        Initialize the directed graph with a given number of vertices.
        The adjacency matrix will be of size vertices x vertices, initially set to 0.
        """
        self.vertices = vertices
        self.adj_matrix = np.zeros((vertices, vertices), dtype=int)
    
    def add_edge(self, u, v):
        """
        Add a directed edge from vertex u to vertex v.
        """
        if u < self.vertices and v < self.vertices:
            self.adj_matrix[u][v] = 1
    
    def compute_degrees(self):
        """
        Compute and return the in-degree and out-degree of each vertex.
        - In-degree of a vertex is the number of edges directed towards the vertex.
        - Out-degree of a vertex is the number of edges originating from the vertex.
        """
        in_degrees = np.sum(self.adj_matrix, axis=0)  # Sum along columns for in-degree
        out_degrees = np.sum(self.adj_matrix, axis=1)  # Sum along rows for out-degree
        return in_degrees, out_degrees
    
    def print_graph(self):
        """Print the adjacency matrix of the directed graph."""
        print("Adjacency Matrix (Directed Graph):")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))
    
    def print_degrees(self, in_degrees, out_degrees):
        """Print the in-degree and out-degree of each vertex."""
        for i in range(self.vertices):
            print(f"Vertex {i}: In-degree = {in_degrees[i]}, Out-degree = {out_degrees[i]}")

# Main function to demonstrate the usage
def main():
    # Input: Number of vertices
    vertices = int(input("Enter the number of vertices: "))
    
    # Create a Directed Graph object
    graph = DirectedGraph(vertices)
    
    # Input: Add edges (u, v)
    edges_count = int(input(f"Enter the number of directed edges for the graph: "))
    for _ in range(edges_count):
        u, v = map(int, input("Enter a directed edge (u v): ").split())
        graph.add_edge(u, v)
    
    # Print the adjacency matrix
    graph.print_graph()
    
    # Compute in-degree and out-degree
    in_degrees, out_degrees = graph.compute_degrees()
    
    # Print the degrees
    graph.print_degrees(in_degrees, out_degrees)

if __name__ == "__main__":
    main()
