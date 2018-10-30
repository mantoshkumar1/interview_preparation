"""
First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


a = Solution()
assert 4 == a.firstMissingPositive([1, 2, 3])
assert 3 == a.firstMissingPositive([0, 2, 2, 1, 1])
assert 2 == a.firstMissingPositive([1,1000])
assert 4 == a.firstMissingPositive()
assert 4 == a.firstMissingPositive()