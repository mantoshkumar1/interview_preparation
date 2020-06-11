"""
we can use DFS to detect cycle in an undirected graph in O(V+E) time. We do a
DFS traversal of the given graph. For every visited vertex ‘v’, if there is an
adjacent ‘u’ such that u is already visited and u is not parent of v, then
there is a cycle in graph. If we don’t find such an adjacent for any vertex,
we say that there is no cycle. The assumption of this approach is that there
 are no parallel edges between any two vertices.
"""
from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        #self.graph = defaultdict(lambda : []) # works
        self.graph = defaultdict(lambda: list())
        #self.graph = defaultdict(list) # works
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def isCyclicUtil(self, visited, v, parent):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == True and v != parent:
                return True
            
            return self.isCyclicUtil(visited, i, v)
        
        return False
    
    def isCyclic(self):
        visited = [False for _ in range(self.V)]
        
        # Call the recursive helper function to detect cycle in different DFS trees
        for i in range(self.V):
            if visited[i] == True:
                continue
            
            if self.isCyclicUtil(visited, i, -1) == True:
                return True
            
        return False
        
# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)

if g.isCyclic():
    print
    "Graph contains cycle"
else:
    print
    "Graph does not contain cycle "
g1 = Graph(3)
g1.addEdge(0, 1)
g1.addEdge(1, 2)

if g1.isCyclic():
    print
    "Graph contains cycle"
else:
    print
    "Graph does not contain cycle "
