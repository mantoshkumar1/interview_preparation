"""
Valid Palindrome:

Given a arr_str, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty arr_str as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


class Solution:
    def move(self, s, i, ltor=True):
        while len(s) > i > -1 and not s[i].isalnum():
            if ltor:
                i += 1
            else:
                i -= 1

        return i
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = -1
        end = len(s)
        
        while start < end:
            start = self.move(s, start+1)
            end = self.move(s, end-1, ltor=False)
            if start >= end:
                break

            if s[start].lower() != s[end].lower():
                return False

        return True


a = Solution()
assert True == a.isPalindrome(".,")
assert True == a.isPalindrome("1,")
assert True == a.isPalindrome("")
assert True == a.isPalindrome(" ")
assert True == a.isPalindrome("  ")
assert True == a.isPalindrome(",")
assert True == a.isPalindrome("A man, a plan, a canal: Panama")
assert False == a.isPalindrome("race a car")

