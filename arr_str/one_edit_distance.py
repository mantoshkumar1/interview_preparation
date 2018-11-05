"""
One Edit Distance

Given two strings s and t, determine if they are both one edit distance apart.

Note:

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
"""


class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False
        
        if abs(len(s) - len(t)) > 1:
            return False
        
        return self.is_replaceable(s, t) or self.is_updateable(s, t)
    
    def is_updateable(self, s, t):  # for insert and delete
        # len(s) must be not equal to len(t)
        if len(s) == len(t):
            return False
        
        update_count = 0
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                update_count += 1
                if len(s) < len(t):
                    j += 1
                else:
                    i += 1
            else:
                i += 1
                j += 1
            
            if update_count == 2:
                return False
        
        return True
    
    def is_replaceable(self, s, t):
        # means s and t should be of same length
        if len(s) != len(t):
            return False
        
        replace_count = 0
        
        for i in range(len(s)):
            if s[i] != t[i]:
                replace_count += 1
            if replace_count == 2:
                return False
        
        return True


a = Solution()
assert False == a.isOneEditDistance("", "")
assert False == a.isOneEditDistance("c", "c")
assert True == a.isOneEditDistance("a", "A")
assert False == a.isOneEditDistance("ab", "ba")
