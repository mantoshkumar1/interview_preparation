"""
Longest Substring with At Most K Distinct Characters:

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ch_dict = dict()
        min_index = 0
        ans = 0

        for index, ch in enumerate(s):
            ch_dict[ch] = index

            if len(ch_dict) > k:
                ch_dict_min_index = min(ch_dict.values())
                ch_dict_min_index_key = s[ch_dict_min_index]
                ch_dict.pop(ch_dict_min_index_key)

                min_index = ch_dict_min_index + 1

            ans = max(ans, index - min_index + 1)

        return ans


a = Solution()
assert 0 == a.lengthOfLongestSubstringKDistinct("", 0)
assert 0 == a.lengthOfLongestSubstringKDistinct("", 3)
assert 0 == a.lengthOfLongestSubstringKDistinct("a", 0)
assert 3 == a.lengthOfLongestSubstringKDistinct("eceba", 2)
assert 4 == a.lengthOfLongestSubstringKDistinct("aabavaacd", 2)
