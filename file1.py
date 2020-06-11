def isSafe(i, j, visited, graph):
    """
    This function to check whether a given cell  (row, col) can be included in DFS or not
    :param i: current row number
    :param j: current column number
    :param visited: 2-d grid of visited nodes
    :param graph: given 2-d grid
    :return: bool
    """
    return (
            not visited[i][j]
            and graph[i][j]
    )


def get_neighbour_list(r, c, i, j):
    """
    :param r: max row
    :param c: max col
    :param i: current row
    :param j: current col
    :return: list of list
    """
    neighbours = []

    # up : i - 1, j
    if 0 <= i - 1 < r and 0 <= j < c:
        neighbours.append((i - 1, j))

    # down : i + 1, j
    if 0 <= i + 1 < r and 0 <= j < c:
        neighbours.append((i + 1, j))

    # left : i, j - 1
    if 0 <= i < r and 0 <= j - 1 < c:
        neighbours.append((i, j - 1))

    # right : i, j + 1
    if 0 <= i < r and 0 <= j + 1 < c:
        neighbours.append((i, j + 1))

    return neighbours


def DFS(r, c, i, j, visited, grid):
    # Mark this cell as visited
    visited[i][j] = True

    # Recur for all connected unvisited neighbours
    for nx, ny in get_neighbour_list(r, c, i, j):
        if not isSafe(nx, ny, visited, grid):
            continue
        DFS(r, c, nx, ny, visited, grid)


def numberAmazonTreasureTrucks(rows, column, grid):
    """
    To put simply, the problem is to count the number of connected components in an undirected graph.
    Or in other words, find the number of islands denoted by 1's.

    Now how do you define islands or connected components?
    It's a group of connected 1's. That's our solution.

    I am using DFS to solve this. But I could have also used BFS and this would have worked seamlessly too.
    Complexity:
    """
    visited = [[False for j in range(column)] for i in range(rows)]
    # Initialize count as 0 and traverse  through the all cells of given matrix
    count = 0

    for i in range(rows):
        for j in range(column):
            # If a cell with value 1 is not visited yet then new island is found
            if isSafe(i, j, visited, grid):
                # Visit all cells in this island and increment island count
                DFS(rows, column, i, j, visited, grid)

                count = count + 1

    return count


grid = [
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 1, 1],
    [1, 1, 1, 1]
]

assert 3 == numberAmazonTreasureTrucks(5, 4, grid)

# https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/
