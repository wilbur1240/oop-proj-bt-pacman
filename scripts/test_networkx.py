import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import time
import os
import sys

# create a nx graph
def test_create_graph():
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2, 3])
    G.add_edge(1, 2)
    G.add_edges_from([(1, 3), (2, 3)])
    nx.draw(G)
    plt.show()

def test_create_graph_from_adj_matrix():
    A = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    G = nx.from_numpy_matrix(A)
    nx.draw(G)
    plt.show()

def test_create_graph_from_adj_list():
    G = nx.Graph()
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    nx.draw(G)
    plt.show()

def test_add_value_to_node_edge():
    G = nx.Graph()
    G.add_edge(1, 2, weight=4.7)
    G.add_edges_from([(3, 4), (4, 5)], color='red')
    G.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])
    G[1][2]['weight'] = 4.7
    G.edges[1, 2]['weight'] = 4
    nx.draw(G)
    plt.show()

def test_create_graph_from_customized_class_as_node():
    class Node:
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return self.name
    G = nx.Graph()
    G.add_node(Node('foo'))
    G.add_nodes_from([Node('bar'), Node('baz')])
    nx.draw(G)
    plt.show()
