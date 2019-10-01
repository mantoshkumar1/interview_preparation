"""
79. Word Search
------------------
https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution:
    def get_unvisited_neighbours(self, visited, m, n, x, y):
        neighbours = []

        if (0 <= x - 1 < m) and (0 <= y < n):
            neighbours.append([x - 1, y])

        if (0 <= x + 1 < m) and (0 <= y < n):
            neighbours.append([x + 1, y])

        if (0 <= x < m) and (0 <= y - 1 < n):
            neighbours.append([x, y - 1])

        if (0 <= x < m) and (0 <= y + 1 < n):
            neighbours.append([x, y + 1])

        neighbours = self.filter_neighbours(visited, neighbours)

        return neighbours

    def filter_neighbours(self, visited, neighbours):
        # return list(filter(lambda c: not visited[c[0]][c[1]], neighbours))

        unvisited_neighbours = []

        for x, y in neighbours:
            if not visited[x][y]:
                unvisited_neighbours.append([x, y])

        return unvisited_neighbours

    def utils(self, board, visited, m, n, x, y, word, curr_index=0):
        if curr_index == len(word) - 1 and word[curr_index] == board[x][y]:
            return True

        if word[curr_index] != board[x][y]:
            return False

        visited[x][y] = True
        neighbours = self.get_unvisited_neighbours(visited, m, n, x, y)

        status = False
        for xn, yn in neighbours:
            status = status or self.utils(board, visited, m, n, xn, yn, word, curr_index + 1)
            if status:
                return status

        visited[x][y] = False

        return status

    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] != word[0]:
                    continue

                if self.utils(board, visited, m, n, i, j, word):
                    return True

        return False


s = Solution()

board = [["a"]]
assert s.exist(board, "a") is True

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
assert s.exist(board, "ABCCED") is True
assert s.exist(board, "SEE") is True
assert s.exist(board, "ABCB") is False

board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
assert s.exist(board, "AAB") is True
