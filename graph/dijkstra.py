"""
The algorithm uses the priority queue version of Dijkstra and return the
distance between the source node and the others nodes d(s,i).

https://www.hackerrank.com/topics/dijkstras-algorithm
http://code.activestate.com/recipes/578156-simple-dijkstra-algorithm/
"""
import heapq as hq

INF = float("inf")


def dijkstra(G, src):
    distance = [INF for _ in range(len(G))]
    distance[src] = 0
    
    pq = [(0, src)]  # priority queue
    
    while len(hq):
        weight, u = hq.heappop(pq)
        for v in G[u]:
            if distance[v] > distance[v] + G[u][v]:
                distance[v] = distance[v] + G[u][v]
                hq.heappush(pq, (distance[v], v))
    
    return distance
    
    

G = [\
        [0.0,  1.0,  3.0,  INF],\
        [1.0,  0.0,  1.0,  4.0],\
        [3.0,  1.0,  0.0,  2.0],\
        [INF,  4.0,  2.0,  0.0]]

d = dijkstra(G, 0)