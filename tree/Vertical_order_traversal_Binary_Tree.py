"""
Vertical Order traversal of Binary Tree
------------------------------------------
Given a binary tree, return a 2-D array with vertical order traversal of it.
Go through the example and image for more details.

Example :
Given binary tree:

      6
    /   \
   3     7
  / \     \
 2   5     9
returns

[
    [2],
    [3],
    [6 5],
    [7],
    [9]
]
"""

from collections import defaultdict
from queue import Queue


class Node:
    def __init__(self, val):
        self.left = self.right = None
        self.val = val

    def __repr__(self):
        return "{}".format(self.val)


class Solution:

    def utils(self, node):
        index_val_dict = defaultdict(lambda: [])

        index = 0
        q = Queue()
        q.put((node, index))

        while not q.empty():
            item = q.get()
            node = item[0]
            index = item[1]

            index_val_dict[index].append(node.val)

            if node.left:
                q.put((node.left, index - 1))

            if node.right:
                q.put((node.right, index + 1))

        return index_val_dict

    def verticalOrderTraversal(self, root: Node):
        if not root:
            return []

        index_val_dict = self.utils(root)
        vals = sorted(index_val_dict.items(), key=lambda x: x[0])
        result = list(map(lambda x: x[1], vals))
        return result


s = Solution()

# Test case 1
"""
		 1
		/ \ 
	   2   3
		  /
		 4
		  \
		   5
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.left.right = Node(5)
assert [[2], [1, 4], [3, 5]] == s.verticalOrderTraversal(root)

# [0,1,null,null,2,6,3,null,null,null,4,null,5]

# Test case 2
"""
    0
  /   \
 1     2
      /  \
     6    3
            \
              4
                \  
                  5     
"""
root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.right.left = Node(6)
root.right.right = Node(3)
root.right.right.right = Node(4)
root.right.right.right.right = Node(5)
assert [[1], [0, 6], [2], [3], [4], [5]] == s.verticalOrderTraversal(root)

# Test case 3
"""
    0
  /  
 1     
   \
     2
   /   \
 6      3
         \
          4
           \    
            5
"""
root = Node(0)
root.left = Node(1)
root.left.right = Node(2)
root.left.right.left = Node(6)
root.left.right.right = Node(3)
root.left.right.right.right = Node(4)
root.left.right.right.right.right = Node(5)
assert [[1, 6], [0, 2], [3], [4], [5]] == s.verticalOrderTraversal(root)

# Test case 4
"""
            0
              \
               1
             / 
            2
          /
         3
        /
       4          
"""

root = Node(0)
root.right = Node(1)
root.right.left = Node(2)
root.right.left.left = Node(3)
root.right.left.left.left = Node(4)
assert [[4], [3], [0, 2], [1]] == s.verticalOrderTraversal(root)
