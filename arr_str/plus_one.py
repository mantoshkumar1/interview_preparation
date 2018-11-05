"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and
each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return digits

        digits[-1] += 1
        carry = digits[-1] // 10
        digits[-1] = digits[-1] % 10

        for i in range(len(digits) - 2, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] = digits[i] % 10

        if carry:
            digits.insert(0, carry)

        return digits


a = Solution()

assert [] == a.plusOne([])
assert [1, 3] == a.plusOne([1, 2])
assert [1] == a.plusOne([0])
assert [1, 0, 0] == a.plusOne([9, 9])
