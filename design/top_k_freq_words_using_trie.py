"""
692. Top K Frequent Words
-----------------------------------
https://leetcode.com/problems/top-k-frequent-words/

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""


class Node:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = Node()
        self.root.is_end = True

    def add(self, word):
        root = self.root

        for ch in word:
            index = ord(ch) - ord('a')
            if root.children[index] is None:
                root.children[index] = Node()

            root = root.children[index]

        root.is_end = True

    def find_words(self, root, words, k, w=''):
        if not root:
            return k

        if k == 0:
            return k

        if root.is_end and w:
            words.append(w)
            k -= 1

        for index, node in enumerate(root.children):
            if not node:
                continue

            ch = chr(index + ord('a'))
            k = self.find_words(node, words, k, w + ch)

        return k


class Solution:
    def topKFrequent(self, words, k):
        d = dict()
        max_freq = -1
        for w in words:
            if w not in d:
                d[w] = 0
            d[w] += 1
            max_freq = max(max_freq, d[w])

        freq = [None] * (max_freq + 1)

        # adding words in trie at their freq position
        for w, f in d.items():
            if freq[f] is None:
                freq[f] = Trie()

            trie = freq[f]
            trie.add(w)

        ans = []

        for trie in freq[::-1]:
            if k == 0:
                break

            if not trie:
                continue

            k = trie.find_words(trie.root, ans, k)

        return ans


s = Solution()

words = ["a", "aa", "aaa"]
assert ["a", "aa"] == s.topKFrequent(words, k=2)

words = ["i", "love", "i"]
assert ["i"] == s.topKFrequent(words, k=1)

words = ["i", "love", "leetcode", "i", "love", "coding"]
assert ["i", "love"] == s.topKFrequent(words, k=2)

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
assert ["the", "is", "sunny", "day"] == s.topKFrequent(words, k=4)
