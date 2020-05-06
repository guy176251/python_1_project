import networkx as nx
from algorithms.prims import prims_algorithm

G = nx.read_weighted_edgelist('data/G3.txt', nodetype=int)
T = prims_algorithm(G, 5, True, True)
