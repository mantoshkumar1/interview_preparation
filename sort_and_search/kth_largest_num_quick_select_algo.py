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


# https://www.geeksforgeeks.org/quickselect-algorithm/
# This is example of Quickselect algorithm
class Solution:
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
    
    def partition(self, nums, i, j):
        p = i
        while i < j:
            while i < j and nums[i] <= nums[p]:
                i += 1
            while i <= j and nums[j] >= nums[p]:
                j -= 1
            if i < j:
                self.swap(nums, i, j)
        
        self.swap(nums, p, j)
        return j
    
    def find_kthelement(self, nums, i, j, k):
        p = self.partition(nums, i, j)
        if p == k:
            return nums[p]
        if p < k:
            i = p + 1
        else:
            j = p - 1
        
        return self.find_kthelement(nums, i, j, k)
    
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_len = len(nums)
        k = nums_len - k
        return self.find_kthelement(nums, 0, nums_len - 1, k)


a = Solution()
assert 5 == a.findKthLargest([3, 2, 1, 5, 6, 4], 2)
assert 4 == a.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
