"""
Kth Largest Element in an Array:

Find the kth largest element in an unsorted array. Note that it is the kth largest element in
the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
    
    def __repr__(self):
        return "{}".format(self.val)


class Solution:
    def __init__(self):
        self.root = None
    
    def insert(self, root, n):
        if root is None:
            return Node(n)
        if n <= root.val:
            root.left = self.insert(root.left, n)
        else:
            root.right = self.insert(root.right, n)
        
        return root
    
    def create_bst(self, nums):
        for n in nums:
            self.root = self.insert(self.root, n)
    
    def size_of_subtree(self, root):
        if root is None:
            return 0
        
        return 1 + self.size_of_subtree(root.left) + self.size_of_subtree(root.right)
    
    def find_kth_node(self, root, k):
        # print(root)
        left_subtee_size = self.size_of_subtree(root.left)
        # print(left_subtee_size)
        if left_subtee_size == k - 1:
            return root.val
        elif left_subtee_size >= k:
            return self.find_kth_node(root.left, k)
        
        return self.find_kth_node(root.right, k - left_subtee_size - 1)
    
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # for reusing it without making new class instance
        self.root = None

        self.create_bst(nums)
        
        nums_len = len(nums)
        k = nums_len - k + 1
        return self.find_kth_node(self.root, k)


a = Solution()
assert 1 == a.findKthLargest([2, 1], 2)
assert 1 == a.findKthLargest([2, 1, 1], 2)
