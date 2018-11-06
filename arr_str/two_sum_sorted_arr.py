"""
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that
they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you
may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index=2
"""


class Solution:
    def twoSum(self, numbers, target):
        """
        Time complexity: O(n)
        Space complexity: O(1)

        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            num_sum = numbers[left] + numbers[right]
            if num_sum == target:
                return [left + 1, right + 1]

            if num_sum < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]

    def twoSum_approach2(self, numbers, target):
        """
        Time and space complexity: O(n)

        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # num_dict = {num: (target_num-num, index_num)}
        num_dict = dict()

        for index, num in enumerate(numbers):
            rest_num = target - num

            if num_dict.get(rest_num):
                return [num_dict[rest_num][1] + 1, index + 1]

            num_dict[num] = (rest_num, index)

        return [-1, -1]


a = Solution()

assert [1, 2] == a.twoSum([1, 3, 5, 8], 4)
assert [3, 4] == a.twoSum([1, 3, 5, 8], 13)
assert [2, 3] == a.twoSum([1, 3, 5, 8], 8)
