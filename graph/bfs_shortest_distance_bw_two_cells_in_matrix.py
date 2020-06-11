"""
Question: A int matrix of size MxN is given, where each grid is represented by
an integer. The accessible grid is denoted by 1, while inaccessible grid is
denoted by 0. The destination grid is denoted by 9.

The starting grid is always top-left corner of matrix which is always
accessible.

Find the shortest distance between starting and destination grid. If no path
exists between these two grids then return -1.
"""

"""
This approach uses BFS to calculate the distance between src and dst cell.

NOTE: For unweighted graph or a graph having edges with same weight, use BFS to
calculate the distance between two cells.
"""

from queue import Queue


def get_neighbour_list(r, c, i, j):
    neighbours = []
    
    # up : i - 1, j
    if 0 <= i-1 < r and 0 <= j < c:
        neighbours.append((i-1, j))

    # down : i + 1, j
    if 0 <= i+1 < r and 0 <= j < c:
        neighbours.append((i+1, j))
        
    # left : i, j - 1
    if 0 <= i < r and 0 <= j-1 < c:
        neighbours.append((i, j-1))
        
    # right : i, j + 1
    if 0 <= i < r and 0 <= j+1 < c:
        neighbours.append((i, j+1))
    
    return neighbours
    
    
def minimumDistance(numRows, numColumns, area):
    visited = [[False for _ in range(numColumns)] for _ in range(numRows)]
    q = Queue()  # [r, c, d]
    q.put((0, 0, 0))
    
    while not q.empty():
        curr = q.get()
        r = curr[0]
        c = curr[1]
        d = curr[2]
        visited[r][c] = True
        
        if area[r][c] == 9:
            return d
        
        neighbours = get_neighbour_list(numRows, numColumns, r, c)
        for n in neighbours:
            r = n[0]
            c = n[1]
            if area[r][c] == 0 or visited[r][c]:
                continue
                
            q.put((n[0], n[1], d+1))
    
    return -1


assert -1 == minimumDistance(3, 3, [[1, 0, 0], [1, 0, 0], [1, 0, 0]])
assert -1 == minimumDistance(3, 3, [[1, 0, 0], [1, 0, 0], [1, 0, 9]])
assert 4 == minimumDistance(3, 3, [[1, 1, 1], [1, 0, 1], [1, 1, 9]])
assert 4 == minimumDistance(3, 3, [[1, 0, 0], [1, 1, 1], [1, 1, 9]])
assert 2 == minimumDistance(3, 4, [[1, 1, 1, 1], [1, 1, 1, 1], [9, 0, 0, 1]])
