"""
Maximum Frequency Stack
---------------------------
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.


Example 1:

Input:
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].


Note:

Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
The total number of FreqStack.push calls will not exceed 10000 in a single test case.
The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.
"""

import heapq
import itertools


class Item:
    _counter = itertools.count()

    def __init__(self, val, freq):
        self.freq = -1 * freq
        self.counter = -1 * next(Item._counter)
        self.val = val

    def __eq__(self, other):
        return (self.freq, self.counter) == (other.freq, other.counter)

    def __ne__(self, other):
        return (self.freq, self.counter) != (other.freq, other.counter)

    def __lt__(self, other):
        return (self.freq, self.counter) < (other.freq, other.counter)

    def __le__(self, other):
        return (self.freq, self.counter) <= (other.freq, other.counter)

    def __gt__(self, other):
        return (self.freq, self.counter) > (other.freq, other.counter)

    def __ge__(self, other):
        return (self.freq, self.counter) >= (other.freq, other.counter)


class FreqStack:

    def __init__(self):
        self.arr = []
        self.item_freq = {}

    def push(self, x: int) -> None:
        if x not in self.item_freq:
            freq = 0
        else:
            freq = self.item_freq[x]

        freq += 1

        item = Item(x, freq)
        heapq.heappush(self.arr, item)
        self.item_freq[x] = freq

    def pop(self) -> int:
        item = heapq.heappop(self.arr)
        val = item.val

        self.item_freq[val] -= 1
        if self.item_freq[val] == 0:
            self.item_freq.pop(val)

        return val


f = FreqStack()
f.push(4)
f.push(0)
f.push(9)
f.push(3)
f.push(4)
f.push(2)
assert 4 == f.pop()
f.push(6)
assert 6 == f.pop()
f.push(1)
assert 1 == f.pop()
f.push(1)
assert 1 == f.pop()
f.push(4)
assert 4 == f.pop()
assert 2 == f.pop()
assert 3 == f.pop()
assert 9 == f.pop()
assert 0 == f.pop()
assert 4 == f.pop()
