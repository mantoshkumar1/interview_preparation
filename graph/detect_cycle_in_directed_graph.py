# Python program to detect cycle in a graph
"""
Depth First Traversal can be used to detect a cycle in a Graph. DFS for a
connected graph produces a tree. There is a cycle in a graph only if there is
a back edge present in the graph. A back edge is an edge that is from a node
to itself (self-loop) or one of its ancestor in the tree produced by DFS.
In the following graph, there are 3 back edges, marked with a cross sign.
We can observe that these 3 back edges indicate 3 cycles present in the graph.

For a disconnected graph, we get the DFS forest as output. To detect cycle,
we can check for a cycle in individual trees by checking back edges.

To detect a back edge, we can keep track of vertices currently in recursion
stack of function for DFS traversal. If we reach a vertex that is already
in the recursion stack, then there is a cycle in the tree. The edge that
connects current vertex to the vertex in the recursion stack is a back edge.
We have used recStack[] array to keep track of vertices in the recursion stack.
"""

from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def isCyclicUtil(self, v, visited, recStack):
        
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
        
        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
        
        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        return False
    
    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.isCyclic() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")

# Thanks to Divyanshu Mehta for contributing this code
