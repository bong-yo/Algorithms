import sys
import networkx as nx
from utils import Paths
sys.path.append(Paths.QUEUE_DIR)
from my_queue import Queue


class BFS(Queue):
    def __init__(self, graph: nx.Graph):
        super(BFS, self).__init__()
        self.visited_nodes = {n: False for n in graph.nodes}
        self.graph = graph
        self.sum = 0

    def bfsearch(self, start_node):
        self.enqueue(start_node)
        self.mark_as_visited(start_node)

        while not self.is_empty():
            node = self.dequeue()
            self.sum += node

            for x in self.graph.neighbors(node):
                if not self.graph.nodes[x].get('bfs_visited', False):
                    self.enqueue(x)
                    self.mark_as_visited(x)

    def mark_as_visited(self, node):
        nx.set_node_attributes(self.graph, {node: True}, 'bfs_visited')
