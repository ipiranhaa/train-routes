from collections import defaultdict


class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
        self.times = {}

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.times[(from_node, to_node)] = weight
        self.times[(to_node, from_node)] = weight

