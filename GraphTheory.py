#Graph Theory: basic terminology, models and types, multi-graphs and weighted graphs, graph
#representation, graph isomorphism, connectivity, Euler and Hamiltonian Paths and Circuits,
#planar graphs, graph coloring, Trees, basic terminology and properties of Trees, introduction to
#spanning trees. 

import networkx as nx
import matplotlib.pyplot as plt

# --------------- BASIC TERMINOLOGY ---------------
# Create a graph and display basic terminology

# Creating an undirected graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

# Show basic properties
print("Vertices:", G.nodes)
print("Edges:", G.edges)
print("Degree of each vertex:", G.degree)

# --------------- MODELS AND TYPES OF GRAPHS ---------------
# Example of a weighted graph
G_weighted = nx.Graph()
G_weighted.add_weighted_edges_from([(1, 2, 5), (2, 3, 7), (3, 4, 10), (4, 5, 1)])

# Display edges with weights
print("Weighted Edges:", G_weighted.edges(data=True))

# Multi-graph (graph with multiple edges between nodes)
G_multigraph = nx.MultiGraph()
G_multigraph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 2)])

# --------------- GRAPH REPRESENTATION ---------------
# Adjacency matrix representation
adj_matrix = nx.adjacency_matrix(G_weighted).todense()
print("Adjacency Matrix of weighted graph:\n", adj_matrix)

# Adjacency list representation
adj_list = nx.to_dict_of_lists(G_weighted)
print("Adjacency List of weighted graph:", adj_list)

# --------------- GRAPH ISOMORPHISM ---------------
# Create two isomorphic graphs
G1 = nx.Graph()
G2 = nx.Graph()

G1.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
G2.add_edges_from([(5, 6), (6, 7), (7, 8), (8, 5)])

# Check if G1 and G2 are isomorphic
isomorphic = nx.is_isomorphic(G1, G2)
print("Are G1 and G2 isomorphic?", isomorphic)

# --------------- CONNECTIVITY ---------------
# Check if a graph is connected
is_connected = nx.is_connected(G)
print("Is G connected?", is_connected)

# --------------- EULERIAN AND HAMILTONIAN PATHS ---------------

# Eulerian Path/Circuit: A graph has an Eulerian path if it has exactly 0 or 2 vertices with an odd degree.
def eulerian_path(graph):
    return nx.has_eulerian_path(graph)

def eulerian_circuit(graph):
    return nx.has_eulerian_circuit(graph)

# Example Graph (Eulerian Circuit)
G_euler = nx.Graph()
G_euler.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

print("Does G_euler have an Eulerian Circuit?", eulerian_circuit(G_euler))

# Hamiltonian Path/Circuit: Check if a graph has a Hamiltonian Path (all vertices once) or Circuit (start and end same)
def hamiltonian_path(graph):
    # Check if the graph has a Hamiltonian path
    for path in nx.all_paths(graph, source=1, target=4):
        if len(path) == len(graph.nodes):
            return True
    return False

print("Does G have a Hamiltonian Path?", hamiltonian_path(G))

# --------------- PLANAR GRAPH ---------------
# Check if a graph is planar
def is_planar(graph):
    return nx.check_planarity(graph)[0]

# Example Graph (Planar check)
G_planar = nx.Graph()
G_planar.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])
print("Is G_planar planar?", is_planar(G_planar))

# --------------- GRAPH COLORING ---------------
# Color a graph using a greedy algorithm
coloring = nx.coloring.greedy_color(G, strategy="largest_first")
print("Greedy Coloring of G:", coloring)

# --------------- TREES ---------------
# Basic tree properties
T = nx.tree.Graph()
T.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5)])

# Tree properties: height, number of edges, number of vertices
print("Vertices in Tree T:", T.nodes)
print("Edges in Tree T:", T.edges)
print("Number of edges in T:", len(T.edges))
print("Number of vertices in T:", len(T.nodes))

# --------------- SPANNING TREES ---------------
# Find a spanning tree for the graph
spanning_tree = nx.minimum_spanning_tree(G_weighted)
print("Minimum Spanning Tree Edges:", spanning_tree.edges)

# --------------- VISUALIZATION ---------------
# Visualize graphs
plt.figure(figsize=(8, 8))

# Visualizing basic graph
plt.subplot(231)
nx.draw(G, with_labels=True, node_color='lightblue', node_size=700, font_size=12)
plt.title("Basic Graph")

# Visualizing weighted graph
plt.subplot(232)
nx.draw(G_weighted, with_labels=True, node_color='lightgreen', node_size=700, font_size=12, edge_labels=nx.get_edge_attributes(G_weighted, 'weight'))
plt.title("Weighted Graph")

# Visualizing multi-graph
plt.subplot(233)
nx.draw(G_multigraph, with_labels=True, node_color='salmon', node_size=700, font_size=12)
plt.title("Multi-Graph")

# Visualizing spanning tree
plt.subplot(234)
nx.draw(spanning_tree, with_labels=True, node_color='lightpink', node_size=700, font_size=12)
plt.title("Spanning Tree")

# Visualizing tree
plt.subplot(235)
nx.draw(T, with_labels=True, node_color='lightyellow', node_size=700, font_size=12)
plt.title("Tree")

# Display all plots
plt.tight_layout()
plt.show()
