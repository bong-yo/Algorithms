import networkx as nx
import matplotlib.pyplot as plt
import random
from random import randint
from BFS import BFS


random.seed(111)


# Generate random graph.
rndm_g = [
    (x, y)
    for (x, y) in [(randint(0, 20), (randint(0, 20))) for i in range(30)]
    if x != y
]
G = nx.Graph()
G.add_edges_from(rndm_g)
nx.draw(G, with_labels=True, font_weight='bold')

# Run BFS algo.
bfs = BFS(graph=G)
bfs.bfsearch(start_node=10)
print(sum(list(G.nodes())))
print(bfs.sum)


plt.show()
