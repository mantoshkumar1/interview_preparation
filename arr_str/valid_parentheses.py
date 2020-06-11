"""
Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sign_dict = { ')': '(', '}': '{', ']': '[' }
        
        arr_stack = []
        for c in s:
            if c in '{([':
                arr_stack.append(c)
                continue
            
            if len(arr_stack) == 0 or sign_dict[c] != arr_stack.pop():
                return False
        
        return False if len(arr_stack) else True


a = Solution()
assert True == a.isValid('')
assert True == a.isValid('()')
assert True == a.isValid('()[]{}')
assert False == a.isValid('(]')
assert False == a.isValid('([)]')
assert True == a.isValid('{[]}')

