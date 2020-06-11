"""
https://www.geeksforgeeks.org/zigzag-tree-traversal/

Write a function to print ZigZag order traversal of a binary tree. For the
below binary tree the zigzag order traversal will be 1 3 2 7 6 5 4
               1
               
        2              3
        
    7       6       5     4
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        
        
class Tree:
    def __init__(self):
        self.root = None
        
    def create_tree(self):
        self.root = Node(1)
        
        self.root.left = Node(2)
        self.root.left.left = Node(7)
        self.root.left.right = Node(6)
        
        self.root.right = Node(3)
        self.root.right.left = Node(5)
        self.root.right.right = Node(4)
    
    def print_zigzag(self):
        # Base Case
        if self.root is None:
            return

        # if lr is true push nodes from left to right
        # otherwise from right to left
        lr = 1
        
        # Create two stacks to store current and next level
        curr_level = []
        next_level = []

        # append root to curr_level stack
        curr_level.append(self.root)

        # Check if stack is empty
        while curr_level:
            # pop from stack
            node = curr_level.pop(-1)
            # print the data
            print(node.val, end=" ")
            if lr:
                # if ltr is true push left before right
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            else:
                # else push right before left
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
            
            if len(curr_level) == 0:
                # reverse lr to push node in opposite order
                lr = lr ^ 1
                # swapping of stacks
                curr_level, next_level = next_level, curr_level


a = Tree()
a.create_tree()

a.print_zigzag()
