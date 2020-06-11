"""
Find Median from Data Stream
-----------------------------
Median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""

import heapq


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        if not self.min_heap:
            heapq.heappush(self.min_heap, num)
            return

        if num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        if len(self.max_heap) + 2 == len(self.min_heap):
            n = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -n)

        elif len(self.max_heap) == len(self.min_heap) + 2:
            n = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -n)

    def findMedian(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0

        if len(self.max_heap) + 1 == len(self.min_heap):
            return self.min_heap[0]

        return -self.max_heap[0]


# test case 1
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
assert 1.5 == obj.findMedian()
obj.addNum(3)
assert 2 == obj.findMedian()

# test case 2
obj = MedianFinder()
obj.addNum(1)
assert 1 == obj.findMedian()

# test case 3
obj = MedianFinder()
obj.addNum(-1)
assert -1 == obj.findMedian()
obj.addNum(-2)
assert -1.5 == obj.findMedian()
obj.addNum(-3)
assert -2 == obj.findMedian()
obj.addNum(-4)
assert -2.5 == obj.findMedian()
obj.addNum(-5)
assert -3 == obj.findMedian()
