"""
Google likes to test your ability to think at large scale by asking variation of
problems represented in data stream model. For example, instead of giving you an integer array,
you are given a stream of integers and all integers are too large to be fit in memory. A great
example of such problem which can be represented in data stream model
(https://en.wikipedia.org/wiki/Streaming_algorithm#Data_stream_model)
is Longest Substring with At Most K Distinct Characters.

https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/submissions/


Question Statement:
Given a string, find the length of the longest substring T that contains at most k "distinct" characters.

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
        max_len = 0
        min_index = 0

        ch_dict = dict()

        for index, ch in enumerate(s):
            ch_dict[ch] = index
            if len(ch_dict) > k:
                # find the ch with min_index in ch_dict
                key = s[min(ch_dict.values())]
                ch_dict.pop(key)
                min_index += 1

            max_len = max(max_len, index-min_index+1)

        return max_len


a = Solution()
assert 2 == a.lengthOfLongestSubstringKDistinct("aa", 2)
assert 1 == a.lengthOfLongestSubstringKDistinct("a", 1)
assert 1 == a.lengthOfLongestSubstringKDistinct("a", 2)
assert 3 == a.lengthOfLongestSubstringKDistinct("bacc", 2)
assert 3 == a.lengthOfLongestSubstringKDistinct("eceba", 2)
assert 0 == a.lengthOfLongestSubstringKDistinct("", 0)
