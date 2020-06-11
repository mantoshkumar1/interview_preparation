"""
Serialization is the process of converting a data structure or object into a sequence of bits so that
it can be stored in a file or memory buffer, or transmitted across a network connection link to be
reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can
be serialized to a string and this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not
necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize
algorithms should be stateless.

https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""

from queue import Queue


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        s = ""
        delimiter = ','

        q = Queue()
        q.put(root)

        while not q.empty():
            node = q.get()
            if node:
                q.put(node.left)
                q.put(node.right)
                s = s + delimiter + str(node.val)
                continue

            s = s + delimiter + 'None'

        return s[1:]

    def createNode(self, s):
        if s == 'None':
            return None

        return TreeNode(int(s))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        strs = data.split(',')

        i = 0
        root = TreeNode(int(strs[0]))

        leaf_nodes = Queue()
        leaf_nodes.put(root)

        while not leaf_nodes.empty():
            node = leaf_nodes.get()
            left = self.createNode(strs[i + 1])
            right = self.createNode(strs[i + 2])
            i += 2

            node.left = left
            node.right = right

            if left:
                leaf_nodes.put(left)
            if right:
                leaf_nodes.put(right)

        return root


def create_sample_tree():
    """
    1
   / \
  2   3
     / \
    4   5
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    return root


def is_dup_tree(root1, root2):
    if not (root1 or root2):  # equivalent to (not root1 and not root2) or (root1 is None and root2 is None)
        return True

    if not (root1 and root2 and root1.val == root2.val):
        return False

    return True and is_dup_tree(root1.left, root2.left) and is_dup_tree(root1.right, root2.right)


# Test cases for is_dup_tree
assert is_dup_tree(None, None)
assert not is_dup_tree(None, TreeNode(1))
assert is_dup_tree(TreeNode(1), TreeNode(1))
assert not is_dup_tree(TreeNode(1), TreeNode(2))

# Test cases for given problem
root = create_sample_tree()

codec = Codec()

assert is_dup_tree(
    root, codec.deserialize(codec.serialize(root))
)

assert is_dup_tree(
    None, codec.deserialize(codec.serialize(None))
)
