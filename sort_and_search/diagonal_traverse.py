"""
Diagonal Traverse
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.



Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Note:

The total number of elements of the given matrix will not exceed 10,000.
"""


class Solution:
    def print_dir(self, matrix, n, i, j, direction):
        tmp = []
        
        while i > -1 and j < n:
            tmp.append(matrix[i][j])
            i -= 1
            j += 1
        
        if direction:
            return tmp
        
        tmp.reverse()
        return tmp
    
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return list()
        
        m = len(matrix)
        n = len(matrix[0])
        direction = 1
        ans = []
        
        for i in range(m):
            tmp = self.print_dir(matrix, n, i, 0, direction)
            direction ^= 1
            ans.extend(tmp)
        
        for j in range(1, n):
            tmp = self.print_dir(matrix, n, m - 1, j, direction)
            direction ^= 1
            ans.extend(tmp)
        
        return ans

a = Solution()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
assert [1,2,4,7,5,3,6,8,9] == a.findDiagonalOrder(matrix)