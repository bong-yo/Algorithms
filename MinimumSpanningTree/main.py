import networkx as nx
import matplotlib.pyplot as plt
import random
from random import randint
from MinSpanTree import MinSpanTree_UnionFind
random.seed(111)


def draw_graph(G, G1, mst):
    mst_edges = set([str(x.attributes) for x in mst])
    print(mst_edges)
    edges_color = []
    for edge in G.edges:
        edg = str(edge[:2])
        if edg in mst_edges:
            edges_color.append('red')
        else:
            edges_color.append('grey')

    pos = nx.spring_layout(G1)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10)
    nx.draw_networkx_labels(G, pos, font_size=10)
    nx.draw(G, pos, edges=G.edges, edge_color=edges_color, node_size=10)
    plt.show()


# Generate random graph.
rndm_weighted_g = [
    (x, y, randint(0, 10))
    for (x, y) in [(randint(0, 20), (randint(0, 20))) for i in range(50)]
    if x != y
]
G = nx.Graph()
G.add_weighted_edges_from(rndm_weighted_g)


mst = MinSpanTree_UnionFind(graph=G)
mst.run()

G1 = nx.Graph()
G1.add_edges_from([x.attributes for x in mst.mst])

draw_graph(G, G1, mst.mst)
print(0)
