"""
Given a list of numbers, find indices of exactly two values from this list, which when
added produces a result that is less than or equal to a given target number but also
nearest to the target number.
"""


class Solution:
    def indices_of_values(self, target, nums):
        max_sum = -1
        result = []

        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(i + 1, len_nums):
                sum_two_values = nums[i] + nums[j]
                if sum_two_values > target:
                    continue

                if max_sum < sum_two_values:
                    max_sum = sum_two_values
                    result = [i, j]

        return result


s = Solution()

target = 60
nums = [1, 10, 25, 35, 60]
assert [2, 3] == s.indices_of_values(target, nums)
