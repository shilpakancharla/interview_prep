"""
    Write a function to print the zigzag (left to right to left, etc.) 
    traversal of a binary tree. 
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def zigzag_traversal(root):
    # Base case
    if root is None:
        return
    
    # Create two stacks to store current and next level 
    current_level = []
    next_level = []

    # If ltr is true push nodes from left to right otherwise
    # from right to left
    ltr = True

    # Append root to current level stack
    current_level.append(root)

    # Check if stack is empty
    while (len(current_level)) > 0:
        # Pop from stack
        temp = current_level.pop(-1)
        # Print the data
        print(temp.data, " ", end = "")

        if ltr:
            # If ltr is true push left before right
            if temp.left:
                next_level.append(temp.left)
            if temp.right:
                next_level.append(temp.right)

        else:
            # Else push right before left
            if temp.right:
                next_level.append(temp.right)
            if temp.left:
                next_level.append(temp.left)

        if (len(current_level)) == 0:
            # Reverse ltr to push node in opposite order
            ltr = not ltr
            # Swapping of stacks
            current_level, next_level = next_level, current_level