import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def draw_subtree(G, T):
    pos = nx.planar_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G,
                                 pos,
                                 edge_labels = labels,)
    nx.draw_networkx_edges(G, pos,
                            edgelist=T.edges(),
                            width=8, alpha=0.5,
                            edge_color='r',)
    nx.draw_networkx_nodes(G,
                           pos,
                           nodelist=T.nodes(),
                           node_color='r',
                           node_size=500,
                           alpha=0.8)
    plt.show()
