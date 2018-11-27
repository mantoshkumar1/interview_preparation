"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until
the first non-whitespace character is found. Then, starting from this
character, takes an optional initial plus or minus sign followed by as many
numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the
integral number, which are ignored and have no effect on the behavior of
this function.

If the first sequence of non-whitespace characters in str is not a valid
integral number, or if no such sequence exists because either str is empty
or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical
value is out of the range of representable values, INT_MAX (231 − 1) or
INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus
sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a
numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a
numerical
             digit or a +/- sign. Therefore no valid conversion could be
             performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit
signed integer.
             Thefore INT_MIN (−231) is returned.

"""
import math

INT_MAX = int(math.pow(2, 31)) - 1
INT_MIN = -int(math.pow(2, 31))


class ListIsCoveredException(Exception):
    pass


class Solution:
    def get_sign(self, str):
        '''returns sign and next index'''
        i = 0
        
        while i < len(str) and str[i].isspace():
            i += 1
        
        if i == len(str):
            return 1, i
            
        if str[i] == '-':
            return -1, i+1
        elif str[i] == '+':
            return 1, i+1
        
        return 1, i
    
    def get_next_digit(self, str, index):
        while index < len(str) and not str[index].isdigit():
            index += 1
        if index == len(str):
            raise ListIsCoveredException
        
        return str[index], index+1
    
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign, index = self.get_sign(str)
        
        num = 0
        while index < len(str):
            try:
                n, index = self.get_next_digit(str, index)
            except ListIsCoveredException:
                break
            
            num = 10*num + int(n)
            
        return sign * num


a = Solution()
assert 42 == a.myAtoi("42")
assert 0 == a.myAtoi("+")
assert 0 == a.myAtoi("     ")
assert 0 == a.myAtoi("    0000000000000   ")
assert -2147483647 == a.myAtoi("-2147483647")
assert -2147483647 == a.myAtoi("-   2147   483  647")