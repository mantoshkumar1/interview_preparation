"""
Implement Trie (Prefix Tree)
-----------------------------
https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


class Node:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        self.root.is_end = True

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            return

        root = self.root

        for ch in word:
            index = ord(ch) - ord('a')
            if root.children[index] is None:
                root.children[index] = Node()

            root = root.children[index]

        root.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root

        for ch in word:
            index = ord(ch) - ord('a')
            if root.children[index] is None:
                return False

            root = root.children[index]

        return root.is_end

    def is_node_childless(self, node):
        for i in range(26):
            if node.children[i] is not None:
                return False

        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root

        for ch in prefix:
            index = ord(ch) - ord('a')
            if root.children[index] is None:
                return False

            root = root.children[index]

        return True
        # return root.is_end or not self.is_node_childless(root) # (This also works)

    def find_all_words(self, root, word=''):
        w_list = []

        if not root:
            return w_list

        if root.is_end and word:
            w_list.append(word)

        children = root.children
        for index, c_node in enumerate(children):
            if c_node is None:
                continue

            ch = chr(index + ord('a'))
            w_list += self.find_all_words(c_node, word + ch)

        return w_list


# Test case 1
t = Trie()
t.insert("apple")
assert t.search("apple") is True
assert t.search("app") is False
assert t.startsWith("app") is True
t.insert("app")
assert t.search("app") is True

# Test case 2
t = Trie()
t.insert("a")
assert True == t.search("a")
assert True == t.startsWith("a")

# Test case 3
t = Trie()
t.insert('a')
t.insert('aa')
t.insert('aaa')
t.insert('baaa')
assert t.search("aaaaa") is False
assert ['a', 'aa', 'aaa', 'baaa'] == t.find_all_words(t.root)
