"""
Closest Binary Search Tree Value:

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None

class Solution:
    def __init__(self):
        self.root = None
        self.makeBST()
        
    def makeBST(self):
        self.root = TreeNode(4)
        self.root.left = TreeNode(2)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(3)
        self.root.right = TreeNode(5)

    def find_close(self, root, target, ans=[]):
        # ans = [dist, node_val]
        if root is None:
            return ans

        dist = abs(target - root.val)
        
        if not ans:
            ans.extend([dist, root.val])
            
        if dist == 0:
            return [dist, root.val]

        if dist < ans[0]:
            ans[0] = dist
            ans[1] = root.val
        #elif dist > ans[0]:
        #    return ans
        
        if target < root.val:
            return self.find_close(root.left, target, ans)
        else:
            return self.find_close(root.right, target, ans)
        
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        dist, val = self.find_close(root, target)
        return val


a = Solution()
assert 4 == a.closestValue(a.root, 3.714286)
#assert 3 == a.closestValue(a.root, [36,13,37,4,20,null,48,1,5,17,33,43,49,0,2,null,9,14,18,22,34,40,46,null,null,null,null,null,3,7,11,null,16,null,19,21,27,null,35,39,42,45,47,null,null,6,8,10,12,15,null,null,null,null,null,26,32,null,null,38,null,41,null,44,null,null,null,null,null,null,null,null,null,null,null,null,null,24,null,28,null,null,null,null,null,null,null,23,25,null,29,null,null,null,null,null,31,30]
#3.142857)