"""
First Unique Character in a String:

Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

from collections import defaultdict


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch_dict = {}  # count, index
        for index, c in enumerate(s):
            if c not in ch_dict:
                ch_dict[c] = [1, index]
            else:
                ch_dict[c][0] += 1
        
        for c in s:  # note here we are traversing input str
            if ch_dict[c][0] == 1:
                return ch_dict[c][1]
            
        return -1


a = Solution()
a.firstUniqChar("leetcode")
