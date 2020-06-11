"""
Min Stack
---------

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""


class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []  # [ (val, min) ]
    
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        min_val = min(self.arr[-1][1], x) if self.arr else x
        self.arr.append((x, min_val))
    
    def pop(self):
        """
        :rtype: void
        """
        self.arr.pop()
    
    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1][0]
    
    def getMin(self):
        """
        :rtype: int
        """
        return self.arr[-1][1]


# Your MinStack object will be instantiated and called as such:

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
assert -3 == minStack.getMin()
minStack.pop()
0 == minStack.top()
-2 == minStack.getMin()
