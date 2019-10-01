"""
Binary Tree Maximum Path Sum
------------------------------
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
import math


class Node:
    def __init__(self, val):
        self.left = self.right = None
        self.val = val


class Solution:
    def utils(self, node, ans):
        if not node:
            return 0

        l_s = self.utils(node.left, ans)
        r_s = self.utils(node.right, ans)
        m = max(node.val, node.val + l_s, node.val + r_s)

        ans[0] = max(ans[0], m, node.val + l_s + r_s)

        return m

    def maxPathSum(self, root) -> int:
        ans = [-math.inf]
        self.utils(root, ans)
        return ans[0]


s = Solution()

root = Node(2)
root.left = Node(-1)
2 == s.maxPathSum(root)
