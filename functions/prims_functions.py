def cost(graph, e):
    return graph.edges[e]['weight']


def valid_incident_edges(G, T):
    edges = []

    for e in G.edges():
        if e[0] in T.nodes() or e[1] in T.nodes():
            edges.append(e)

    valid_edges = []

    for e in edges:
        if any(p not in T.nodes() for p in e[:2]):
            valid_edges.append(e)

    return valid_edges


def min_prims_edge(G, T):
    edges = valid_incident_edges(G, T)
    min_e = edges[0]

    for e in edges:
        if cost(G, e) < cost(G, min_e):
            min_e = e

    return min_e
