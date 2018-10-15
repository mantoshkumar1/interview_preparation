"""
Valid Palindrome:

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


class Solution:
    def move_forward(self, s, i):
        while not s[i].isalnum():
            if i + 1 == len(s):
                return -1, -1
            i += 1
        return s[i].lower(), i
    
    def move_back(self, s, i):
        while not s[i].isalnum():
            if i == 0:
                return -1, -1
            i -= 1
        return s[i].lower(), i
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1
        
        while start < end:
            f, start = self.move_forward(s, start)
            b, end = self.move_back(s, end)
            if f != b:
                return False
            start += 1
            end -= 1
        
        return True


a = Solution()
assert True == a.isPalindrome(".,")
assert True == a.isPalindrome("1,")
assert True == a.isPalindrome("")
assert True == a.isPalindrome(",")
assert True == a.isPalindrome("A man, a plan, a canal: Panama")
assert False == a.isPalindrome("race a car")

