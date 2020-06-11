"""
LRU Cache
---------
Design and implement a data structure for Least Recently Used (LRU) cache. It should support
the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present. When the cache
reached its capacity, it should invalidate the least recently used item before inserting a
new item.

Follow up:
----------
Could you do both operations in O(1) time complexity?
"""

import heapq
from datetime import datetime
from itertools import count

class Item:
    # _counter = count() # this will also work
    
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.valid = True
        # self.counter = next(Item._counter)
        self.counter = datetime.now()
    
    def __eq__(self, other):
        return self.counter == other.counter
    
    def __nq__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return self.counter < other.counter
    
    def __le__(self, other):
        return self.counter <= other.counter
    
    def __gt__(self, other):
        return self.counter > other.counter
    
    def __ge__(self, other):
        return not self.__lt__(other)


class LRUCache:
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.valid_key_item_dict = dict()
        self.hq = []
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # if key is not in valid_key_item_dict:
        #       return -1
        # else:
        #       get ref of item through valid_key_item_dict
        #       set ref.valid to false
        #       create new item with same value
        #       insert new item into heapq
        #       insert key: item_ref to valid_key_item_dict
        #       return value
        #       End
        item = self.valid_key_item_dict.get(key)
        if item is None:
            return -1
        
        item.valid = False
        
        new_item = Item(item.key, item.val)
        heapq.heappush(self.hq, new_item)
        self.valid_key_item_dict[key] = new_item
        
        return item.val
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # if key is not in valid_key_item_dict:
        #       if remaining capacity = 0:
        #              # delete least recent item
        #                   delete until one of active item is deleted
        #                   capacity += 1
        #                   delete reference of popped item from valid_key_item_dict
        #
        #              # insert new item
        #                   capacity -= 1
        #
        #                   create new item with given value
        #                   insert new item into heapq
        #                   insert key: item_ref to valid_key_item_dict
        #                   End
        #        else:
        #              # insert new item
        #                   capacity -= 1
        #
        #                   create new item with given value
        #                   insert new item into heapq
        #                   insert key: item_ref to valid_key_item_dict
        #                   End
        #
        # else:
        #       # update new item
        #             get ref of item through valid_key_item_dict
        #             set ref.valid to false
        #
        #             create new item with given value
        #             insert new item into heapq
        #             insert key: item_ref to valid_key_item_dict
        #             End
        
        if key not in self.valid_key_item_dict:
            if self.capacity == 0:
                while True:
                    item = heapq.heappop(self.hq)
                    if item.valid:
                        break
                
                self.capacity += 1
                self.valid_key_item_dict.pop(item.key)
            
            self.capacity -= 1
        
        else:
            item = self.valid_key_item_dict[key]
            item.valid = False
        
        item = Item(key, value)
        heapq.heappush(self.hq, item)
        self.valid_key_item_dict[key] = item


# Your LRUCache object will be instantiated and called as such:

if __name__ == "__main__":
    cache = LRUCache(capacity=2)
    
    cache.put('a', 1)
    cache.put('b', 2)
    
    assert 1 == cache.get('a')  # returns 1
    
    cache.put('c', 3)  # evicts key 'b'
    
    assert -1 == cache.get('b')  # returns -1 (not found)
    
    cache.put('d', 4)  # evicts key 'a
    
    assert -1 == cache.get('a')  # returns -1 (not found)
    assert 3 == cache.get('c')  # returns 3
    assert 4 == cache.get('d')  # returns 4
