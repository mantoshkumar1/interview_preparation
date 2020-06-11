"""
A minimum spanning tree describes a path that contains the smallest number
of edges that are needed to visit every node in the graph.

1. Sort all the edges in non-decreasing order of their weight.

2. Pick the smallest edge. Check if it forms a cycle with the spanning tree
formed so far. If cycle is not formed, include this edge. Else, discard it.

3. Repeat step#2 until there are (V-1) edges in the spanning tree.

https://blog.csdn.net/kenden23/article/details/26821635
"""
from collections import defaultdict
from queue import PriorityQueue


class Graph:
    def __init__(self, V):
        self.graph = defaultdict(lambda: set())
        self.V = V

    def add_edge(self, u, v, w):
        self.graph[u].add((w, v))

    def get_minimum_edge(self):
        if len(self.graph) == 0:
            return -1, -1, -1

        edges = set()
        for i in self.graph:
            for entry in self.graph[i]:
                edges.add(entry)

        weight, dst = min(edges)

        for src in self.graph:
            if (weight, dst) in self.graph[src]:
                return weight, src, dst

    def print_min_spanning_tree(self):
        visited = [False] * self.V

        pq = PriorityQueue()  # priority (would be weight), r, c

        # edge of minimum weight
        weight, src, dst = self.get_minimum_edge()
        if weight == -1 and src == -1 and dst == -1:
            return

        pq.put((weight, src, dst))

        while not pq.empty():
            weight, src, dst = pq.get()
            visited[src] = True
            print(str(src) + "--" + str(dst))

            if src in self.graph:
                neighbours = self.graph[src]
                for n in neighbours:
                    weight = n[0]
                    dst = n[1]
                    if visited[src] == False:
                        pq.put((weight,) + (src, dst))

            if dst in self.graph:
                src = dst
                neighbours = self.graph[src]
                for n in neighbours:
                    weight = n[0]
                    dst = n[1]
                    if visited[src] == False:
                        pq.put((weight,) + (src, dst))


g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 4, 1)
g.add_edge(2, 3, 9)
g.add_edge(4, 3, 8)

g.print_min_spanning_tree()
