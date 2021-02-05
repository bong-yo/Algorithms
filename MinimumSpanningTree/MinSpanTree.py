import sys
import networkx as nx
from utils import Paths
sys.path.append(Paths.QUEUE_DIR)
from my_priority_queue import Heap, Node
sys.path.append(Paths.UNIONFIND_DIR)
from my_union_find import UnionFind, Element


class MinSpanTree_PriorityQueue(Heap):
    '''
    Find Minimum Spanning Tree using Priority Queue based method.
    1 Get smallest edge from the queue
    2 Get vertices of that edge
    3 Add new edges connected to those vertices to the queue
    4 Repeat form 1 untill the queue is empty
    '''
    def __init__(self, graph: nx.Graph):
        super(MinSpanTree_PriorityQueue, self).__init__()
        self.graph = graph
        self.mst = []

    def run(self):
        next_smallest_edge = self.get_smallest_edge()
        vertices = next_smallest_edge[:2]
        weight = next_smallest_edge[2]['weight']
        next_smallest_edge = Node(weight, vertices)

        while next_smallest_edge is not None:
            verts = self.get_new_vertices(next_smallest_edge)  # If an edge is in the queue at least one of the 2 vertices should be already in the MST.
            if verts:
                self.mark_vertices_as_part_of_MST(verts)
                self.mst.append(next_smallest_edge)
                for edge in self.get_new_edges(verts):
                    vertices = edge[:2]
                    weight = edge[2]['weight']
                    self.enqueue(Node(weight, vertices))
            next_smallest_edge = self.dequeue()

    def get_new_vertices(self, edge: Node):
        return [x for x in edge.attributes if not self.already_in_MST(x)]

    def get_new_edges(self, vertices):
        return [
            edge
            for edge in self.get_edges(vertices)
            if not (self.already_in_MST(edge[0]) and self.already_in_MST(edge[1]))
        ]

    def get_next_smallest_edge(self):
        edge = self.dequeue()
        return edge.attributes

    def add_edges_to_queue(self, edges):
        for (v1, v2) in edges:
            if not (self.already_in_MST(v1) and self.already_in_MST(v2)):
                self.enqueue((v1, v2))

    def get_smallest_edge(self):
        return sorted(
            self.graph.edges(data=True), key=lambda x: x[2]['weight']
        )[0]

    def get_edges(self, vertices):
        return self.graph.edges(vertices, data=True)

    def mark_vertices_as_part_of_MST(self, vertices):
        if type(vertices) != list:
            vertices = [vertices]
        for vertex in vertices:
            nx.set_node_attributes(self.graph, {vertex: True}, 'already_in_MST')

    def already_in_MST(self, vertex):
        return self.graph.node[vertex].get("already_in_MST", False)


class MinSpanTree_UnionFind(UnionFind):
    def __init__(self, graph: nx.Graph):
        super(MinSpanTree_UnionFind, self).__init__()
        self.graph = graph
        self.mst = []

    def init_unionfind_elements(self):
        '''Initially assign each vertex to a different group'''
        for i, vertex in enumerate(self.graph.nodes):
            self.insert(elem=Element(name=vertex), group=i)

    def run(self):
        self.init_unionfind_elements()
        sorted_edges = \
            sorted(self.graph.edges(data=True), key=lambda x: x[2]['weight'])

        while sorted_edges:
            v1, v2, weight = sorted_edges.pop(0)
            if self.merge(Element(name=v1), Element(name=v2)):
                self.mst.append((v1, v2, weight))

