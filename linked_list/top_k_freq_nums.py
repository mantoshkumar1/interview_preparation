"""
347. Top K Frequent Elements
------------------------------
https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def insert(self, curr, prev, val):
        if curr is None or curr.val >= val:
            node = Node(val)
            node.next = curr
            prev.next = node
            return

        self.insert(curr.next, curr, val)

    def fill_freq_arr(self, freq, d):
        for num, index in d.items():
            if freq[index] is None:
                freq[index] = Node(None)

            self.insert(freq[index].next, freq[index], num)

    def getKElement(self, root, ans, k):
        if k == 0:
            return k

        if not root:
            return k

        ans.append(root.val)
        k = k - 1
        return self.getKElement(root.next, ans, k)

    def topKFrequent(self, nums, k):
        d = dict()  # val: freq
        max_freq = -1
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
            max_freq = max(max_freq, d[n])

        freq = [None] * (max_freq + 1)
        self.fill_freq_arr(freq, d)

        ans = []
        for node in freq[::-1]:
            if node is None:
                continue

            if k == 0:
                return ans

            k = self.getKElement(node.next, ans, k)

        return ans


s = Solution()

nums = [1, 1, 1, 2, 2, 3]
assert [1, 2] == s.topKFrequent(nums, k=2)

nums = [1]
assert [1] == s.topKFrequent(nums, k=1)
