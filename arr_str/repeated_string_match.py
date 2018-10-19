"""
Repeated String Match:

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""
import math


class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        times = math.ceil(len(B) / len(A))
        
        # if times = 1, ans is either 1 or 2
        # else: ans is either times or times + 1
        
        temp_a = A
        
        A = temp_a * times
        
        if B in A:
            return times
        
        A = A + temp_a
        
        if B in A:
            return times + 1
        
        return -1


a = Solution()

assert 3 == a.repeatedStringMatch(A="abcd", B="cdabcdab")

assert 1 == a.repeatedStringMatch(A="aaaaaab", B="ab")
assert 2 == a.repeatedStringMatch(A="aaaaaab", B="ba")

