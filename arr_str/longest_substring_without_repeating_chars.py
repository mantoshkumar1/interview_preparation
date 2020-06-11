"""
Longest Substring Without Repeating Characters
-------------------------------------------------
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def update_left_index_and_char_set(self, s, left, dup_char, ch_set):
        """
        1. find the index of dup char in s[left: right+1].
        2.1. if index of dup char == s[left] then no need to add s[right] in ch_set.
        2.2. if index of dup char != s[left] then ch_set should only have chars which is in s[index of dup char: right+1].
        """
        while dup_char != s[left]:
            ch_set.remove(s[left])
            left += 1

        return left + 1

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        if s_len <= 1:
            return s_len

        ch_set = set()
        ch_set.add(s[0])

        max_len = 1

        left = 0
        right = 1

        while right < s_len:
            ch = s[right]

            if ch not in ch_set:
                ch_set.add(ch)
                max_len = max(max_len, right - left + 1)
                right += 1
                continue

            left = self.update_left_index_and_char_set(s, left, ch, ch_set)
            right += 1

        return max_len


s = Solution()

assert 5 == s.lengthOfLongestSubstring("tmmzuxt")
assert 3 == s.lengthOfLongestSubstring("pwwkew")
assert 5 == s.lengthOfLongestSubstring("tvqnkvovks")
