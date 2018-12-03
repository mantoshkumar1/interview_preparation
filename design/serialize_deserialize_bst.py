"""
Serialize and Deserialize BST

Serialization is the process of converting a data structure or object into a sequence of bits so
that it can be stored in a file or memory buffer, or transmitted across a network connection
link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction
on how your serialization/deserialization algorithm should work. You just need to ensure that a
binary search tree can be serialized to a string and this string can be deserialized to the
original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and
deserialize algorithms should be stateless.
"""


class TreeNode:
    def __init__(self, val):
        self.left = self.right = None
        self.val = val


class Codec:
    def insert(self, root, val, side):
        if not root:
            return TreeNode(val)
        
        if side < 2:  # left or does not matter as values will be unique in bst
            if val <= root.val:
                root.left = self.insert(root.left, val, side)
            else:
                root.right = self.insert(root.right, val, side)
        else:
            if val < root.val:
                root.left = self.insert(root.left, val, side)
            else:
                root.right = self.insert(root.right, val, side)
        
        return root
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split("-")
        
        equal_val_storage_loc = int(data[0])
        root = None
        
        for val in data[1:]:
            if not val:  # for ''
                continue
            
            root = self.insert(root, int(val), equal_val_storage_loc)
        
        return root
    
    def get_nodes_val(self, root):
        if not root:
            return ""
        
        if root.left is None and root.right is None:
            return str(root.val)
        
        return "-".join(
            [str(root.val), self.get_nodes_val(root.left), self.get_nodes_val(root.right)])
    
    def side_where_equal_values_stored(self, root, side=1):
        """
                values of side stored in:
                0 : left
                1: does not matter (all values are anyway is then unique)
                2: right
        """
        if not root:
            return side
        
        if root.left and root.val == root.left.val:
            return 0
        
        if root.right and root.val == root.right.val:
            return 2
        
        l_side = self.side_where_equal_values_stored(root.left)
        if l_side != side:
            return l_side
        
        r_side = self.side_where_equal_values_stored(root.right)
        return r_side
    
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        equal_val_storage_loc = str(self.side_where_equal_values_stored(root))
        return "-".join([equal_val_storage_loc, self.get_nodes_val(root)])


def test_tree_equality(root1, root2):
    # only for testing purpose
    if root1 is None and root2 is None:
        return True
    
    if (root1 is None and root2 is not None) or (root1 is not None and root2 is None):
        return False
    
    if root1.val != root2.val:
        return False
    
    return test_tree_equality(root1.left, root2.left) and test_tree_equality(root1.right,
        root2.right)


a = Codec()

# Test 1
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
assert True == test_tree_equality(root, a.deserialize(a.serialize(root)))

# Test 2 where equal items are stored in left side
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(3)
assert True == test_tree_equality(root, a.deserialize(a.serialize(root)))

# Test 3 where equal items are stored in right side
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(2)
assert test_tree_equality(root, a.deserialize(a.serialize(root)))

# Test 4 edge case
root = None
assert test_tree_equality(root, a.deserialize(a.serialize(root)))
