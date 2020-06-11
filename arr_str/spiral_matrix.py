"""
Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return matrix

        RIGHT = LEFT = UP = DOWN = True
        op = []

        row = len(matrix)
        col = len(matrix[0])

        count = row * col

        # spiral means cycle (RIGHT - DOWN - LEFT - UP)
        RIGHT = True
        r = 0
        c = -1
        while count > 0:
            if RIGHT:
                c += 1

                # means row will be constant and col will be increasing
                for i in range(c, col):
                    if matrix[r][i] is None:
                        c = i - 1
                        break
                    op.append(matrix[r][i])
                    matrix[r][i] = None
                else:
                    c = i

                RIGHT = False
                DOWN = True

            elif DOWN:
                # means col will be constant and row will be increasing
                r += 1
                for i in range(r, row):
                    if matrix[i][c] is None:
                        r = i - 1
                        break

                    op.append(matrix[i][c])
                    matrix[i][c] = None
                else:
                    r = i

                DOWN = False
                LEFT = True

            elif LEFT:
                # means row will be constant and col will be decreasing
                c -= 1
                for i in range(c, -1, -1):
                    if matrix[r][i] is None:
                        c = i + 1
                        break

                    op.append(matrix[r][i])
                    matrix[r][i] = None
                else:
                    c = i

                LEFT = False
                UP = True

            elif UP:
                # means col will be constant and row will be decreasing
                r -= 1
                for i in range(r, -1, -1):
                    if matrix[i][c] is None:
                        r = i + 1
                        break

                    op.append(matrix[i][c])
                    matrix[i][c] = None
                else:
                    r = i

                UP = False
                RIGHT = True

            count -= 1

        return op


a = Solution()
assert [1, 2, 3, 6, 9, 8, 7, 4, 5] == a.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
assert [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7] == a.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
assert [] == a.spiralOrder([])

