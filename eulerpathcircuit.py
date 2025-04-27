# Given an adjacency matrix of a graph, write a program to check whether a given set of vertices {v1,v2,v3.....,vk} forms an Euler path / Euler Circuit (for circuit assume vk=v1).

import numpy as np

class Graph:
    def __init__(self, vertices, adj_matrix):
        self.vertices = vertices
        self.adj_matrix = np.array(adj_matrix)
    
    def degree(self, vertex):
        """Calculate the degree of a vertex (number of edges connected to it)."""
        return np.sum(self.adj_matrix[vertex])

    def check_euler_path_or_circuit(self, vertex_set):
        """
        Check if the given set of vertices forms an Euler Path or Euler Circuit.
        Euler Circuit: All vertices in the set have an even degree.
        Euler Path: Exactly two vertices in the set have an odd degree.
        """
        odd_degree_count = 0
        
        for vertex in vertex_set:
            deg = self.degree(vertex)
            if deg % 2 != 0:
                odd_degree_count += 1
        
        if odd_degree_count == 0:
            print("The set of vertices forms an Euler Circuit.")
        elif odd_degree_count == 2:
            print("The set of vertices forms an Euler Path.")
        else:
            print("The set of vertices does not form an Euler Path or Euler Circuit.")

    def is_connected(self, vertex_set):
        """
        Check if the graph formed by the given set of vertices is connected.
        We will use Depth First Search (DFS) to check connectivity.
        """
        visited = [False] * self.vertices
        self.dfs(vertex_set[0], visited, vertex_set)
        
        # Check if all vertices in the set are visited
        for vertex in vertex_set:
            if not visited[vertex]:
                return False
        return True
    
    def dfs(self, vertex, visited, vertex_set):
        """Perform DFS to visit all vertices in the vertex set."""
        visited[vertex] = True
        for i in range(self.vertices):
            if self.adj_matrix[vertex][i] == 1 and i in vertex_set and not visited[i]:
                self.dfs(i, visited, vertex_set)

def main():
    # Input: Number of vertices and the adjacency matrix
    vertices = int(input("Enter the number of vertices in the graph: "))
    adj_matrix = []
    print("Enter the adjacency matrix (use 0 for no edge and 1 for edge):")
    for i in range(vertices):
        row = list(map(int, input().split()))
        adj_matrix.append(row)
    
    # Create the Graph object
    graph = Graph(vertices, adj_matrix)
    
    # Input: Set of vertices to check for Euler path/circuit
    vertex_set = list(map(int, input("Enter the set of vertices (space separated): ").split()))
    
    # Check if the set of vertices forms an Euler Path or Circuit
    graph.check_euler_path_or_circuit(vertex_set)
    
    # Check if the graph formed by the set of vertices is connected (for Euler circuit)
    if graph.is_connected(vertex_set):
        print("The graph formed by the set of vertices is connected.")
    else:
        print("The graph formed by the set of vertices is not connected.")

if __name__ == "__main__":
    main()
