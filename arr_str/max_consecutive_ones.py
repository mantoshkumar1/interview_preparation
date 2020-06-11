"""
Max Consecutive Ones

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip
at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you
can't store all numbers coming from the stream as it's too large to hold in memory.
Could you solve it efficiently?
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = zero = left = right = 0
        for n in nums:
            if n == 0:
                zero += 1
            
            if zero == 2:
                while nums[left] == 1:
                    left += 1
                left += 1
                zero -= 1
            
            ans = max(ans, right-left+1)
            right += 1
            
        return ans

a = Solution()
assert 0 == a.findMaxConsecutiveOnes([])
assert 2 == a.findMaxConsecutiveOnes([0, 0, 1])
assert 3 == a.findMaxConsecutiveOnes([1, 1, 1])
assert 5 == a.findMaxConsecutiveOnes([0, 1, 1, 0, 1, 1])
assert 4 == a.findMaxConsecutiveOnes([0, 1, 1, 0, 0, 1, 1, 1])
assert 4 == a.findMaxConsecutiveOnes([1, 0, 1, 0, 1, 1])