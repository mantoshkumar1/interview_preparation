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

        # ch_dict = {'a': [unique_status, index]}
        ch_dict = defaultdict(lambda: [1, 0])

        for index, ch in enumerate(s):
            if ch in ch_dict:
                ch_dict[ch][0] = 0
            else:
                ch_dict[ch][1] = index

        return sorted(ch_dict.values(), key=lambda x: (-x[0], x[1]))[0][1]

a = Solution()
a.firstUniqChar("leetcode")