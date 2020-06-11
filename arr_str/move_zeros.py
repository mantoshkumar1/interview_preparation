"""
Move Zeroes:

Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.
"""
from functools import cmp_to_key


class Solution:
    def my_cmp(self, a, b):
        if a == 0 and b != 0:
            return 1  # move a to right side
        if a != 0 and b == 0:
            return -1  # keep a to left side

        return 0  # do not change position of a

    def another_approach_using_sort(self, nums):
        nums.sort(key=cmp_to_key(self.my_cmp))

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_len = len(nums)
        c_index = 0
        for _ in range(num_len):
            if nums[c_index] == 0:
                nums.pop(c_index)
                nums.append(0)
            else:
                c_index += 1


a = Solution()
assert "0000" == a.moveZeroes("0000")
assert "123000" == a.moveZeroes("012030")
assert "123000" == a.moveZeroes("000123")
assert "123000" == a.moveZeroes("123000")
assert "" == a.moveZeroes("")


assert "0000" == a.another_approach_using_sort("0000")
assert "123000" == a.another_approach_using_sort("012030")
assert "123000" == a.another_approach_using_sort("000123")
assert "123000" == a.another_approach_using_sort("123000")
assert "" == a.another_approach_using_sort("")
