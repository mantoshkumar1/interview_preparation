"""
Implement a basic calculator to evaluate a simple expression arr_str.

The expression arr_str contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.

"""


class Calculator:
    def get_next_num(self, s, i):
        while s[i].isspace():
            i += 1
        
        n = 0
        while i < len(s) and s[i].isdigit():
            n = n*10 + int(s[i])
            i += 1
        
        return n, i
    
    def calculate(self, s):
        nums = []
        n, i = self.get_next_num(s, 0)
        nums.append(n)
        
        while i < len(s):
            if s[i].isspace():
                i += 1
                continue
            
            if s[i] == '+':
                n, i = self.get_next_num(s, i+1)
                nums.append(n)
                continue
            
            if s[i] == '-':
                n, i = self.get_next_num(s, i+1)
                nums.append(-n)
                continue
            
            if s[i] == '*':
                n, i = self.get_next_num(s, i+1)
                nums[-1] = nums[-1] * n
                continue
            
            if s[i] == '/':
                n, i = self.get_next_num(s, i+1)
                nums[-1] = nums[-1] / n if nums[-1] >= 0 else -(-nums[-1] / n)
                continue
        
        return sum(nums)


a = Calculator()
assert (1+3-2+111/1*2/4*187) == a.calculate(
    "  1 + 3 - 2     + 111 / 1 * 2  / 4  * 187    ")

