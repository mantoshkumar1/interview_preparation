"""
References:
-----------
[1]. http://keithschwarz.com/interesting/code/find-duplicate/FindDuplicate.python.html
[2]. https://www.jasondavies.com/duplicates/

Find the Duplicate Number
-------------------------
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate
number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = len(nums) - 1
        while True:
            slow = nums[slow] - 1
            fast = nums[nums[fast] - 1] - 1
            if slow == fast:
                break
        
        finder = len(nums) - 1
        while slow != finder:
            slow = nums[slow] - 1
            finder = nums[finder] - 1
        
        return finder + 1
        
        """
        slow = fast = len(nums)
        while True:
            slow = nums[slow-1] - 1
            fast = nums[nums[fast] - 1] - 1
            if slow == fast:
                break
        
        finder = len(nums)
        while slow != finder:
            slow = nums[slow-1] -1
            finder = nums[finder-1] -1
        
        return finder
        """


a = Solution()
assert 1 == a.findDuplicate([1, 1, 2, 3, 4])
assert 4 == a.findDuplicate([1, 2, 3, 4, 4])
assert 1 == a.findDuplicate([4, 3, 2, 1, 1])
assert 4 == a.findDuplicate([4, 4, 3, 2, 1])
