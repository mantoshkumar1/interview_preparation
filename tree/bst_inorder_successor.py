"""
Inorder Successor in BST

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

Example 1:

Input: root = [2,1,3], p = 1

  2
 / \
1   3

Output: 2
Example 2:

Input: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /
1

Output: null
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None


class Solution:
    def __init__(self):
        self.root = None
    
    def insert_bst(self, root, val):
        if root is None:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insert_bst(root.left, val)
        else:
            root.right = self.insert_bst(root.right, val)
        
        return root
    
    def destroy_bst(self, root):
        if root is None:
            return
        
        self.destroy_bst(root.left)
        self.destroy_bst(root.right)
        
        del root
        
    def construct_bst(self, arr):
        self.destroy_bst(self.root)
        self.root = None
        
        for i in arr:
            self.root = self.insert_bst(self.root, i)
    
    def find_min_in_right_child(self, node):
        if node is None:
            return node
        
        if node.left is None:
            return node
        
        return self.find_min_in_right_child(node.left)
    
    def find_just_big_parent_of_target(self, node, target, parent=None):
        if target is node:
            return parent
            
        if target.val < node.val:
            parent = node
            return self.find_just_big_parent_of_target(node.left, target, parent)
        
        return self.find_just_big_parent_of_target(node.right, target, parent)
        
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if p.right:
            return self.find_min_in_right_child(p.right)
        return self.find_just_big_parent_of_target(self.root, p)
    
a = Solution()
a.construct_bst([2,1,3])
#root = [2,1,3], p = 1, ans = 2
assert a.root == a.inorderSuccessor(a.root, a.root.left)

