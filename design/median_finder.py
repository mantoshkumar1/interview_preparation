"""
Find Median from Data Stream
------------------------------
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


class MedianFinderWithTwoHeaps:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []  # left: contains -ve values
        self.min_heap = []  # right: contains +ve values
    
    def balance_heaps(self):
        if len(self.max_heap) == len(self.min_heap) + 2:
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -val)
        else:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
    
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.min_heap:
            heapq.heappush(self.min_heap, num)
            return
        
        # For min heap, if we insert value which is greater then min value then propagation will
        # take less time. On the other hand, for max heap, insertion of value which is less than
        # max value will take less propagation.
        
        if num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        self.balance_heaps()
    
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        
        return -self.max_heap[0]


class MedianFinder(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.n = 0
    
    def find_insert_pos(self, i, j, val):
        if i > j:
            return i
        
        mid = (i + j) // 2
        if val == self.arr[mid]:
            return mid
        
        if val < self.arr[mid]:
            return self.find_insert_pos(i, mid - 1, val)
        
        return self.find_insert_pos(mid + 1, j, val)
    
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        pos = self.find_insert_pos(0, self.n - 1, num)
        self.arr.insert(pos, num)
        self.n += 1
    
    def findMedian(self):
        """
        :rtype: float
        """
        mid = self.n // 2
        
        if self.n % 2 != 0:  # odd length
            return self.arr[mid]
        
        return (self.arr[mid] + self.arr[mid - 1]) / 2


# MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
assert 1.5 == obj.findMedian()
obj.addNum(3)
assert 2 == obj.findMedian()

# testing for another approach which uses two heaps
obj = MedianFinderWithTwoHeaps()
obj.addNum(1)
obj.addNum(2)
assert 1.5 == obj.findMedian()
obj.addNum(3)
assert 2 == obj.findMedian()
obj = MedianFinderWithTwoHeaps()
obj.addNum(1)
assert 1 == obj.findMedian()
