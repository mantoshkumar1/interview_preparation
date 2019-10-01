"""
The algorithm uses the priority queue version of Dijkstra and return the
distance between the source node and the others nodes d(s,i).

https://www.hackerrank.com/topics/dijkstras-algorithm
http://code.activestate.com/recipes/578156-simple-dijkstra-algorithm/
"""
import heapq as hq
import math

# INF = float("inf")
INF = math.inf


def dijkstra(G, src):
    distance = [INF for _ in range(len(G))]
    distance[src] = 0

    visited = [False] * len(G)

    pq = [(0, src)]  # priority queue (distance_from_source, node)

    while len(pq):
        distance_from_src, u = hq.heappop(pq)
        for v, w in enumerate(G[u]):
            if visited[v]:
                continue

            if distance[v] > distance_from_src + w:
                distance[v] = distance_from_src + w
                hq.heappush(pq, (distance[v], v))

        visited[u] = True
    
    return distance
    
    

G = [\
        [0.0,  1.0,  3.0,  INF],\
        [1.0,  0.0,  1.0,  4.0],\
        [3.0,  1.0,  0.0,  2.0],\
        [INF,  4.0,  2.0,  0.0]]

d = dijkstra(G, 0)
print(d)