"""
    Recursive program for level order traversal of binary tree.
"""

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Iterative method to print the height of binary tree
def print_level_order_queue(root):
    # Base case
    if root in None:
        return
    
    # Create an empty queue for level order traversal
    queue = []

    # Enqueue root and initialize height
    queue.append(root)

    while (len(queue) > 0):
        # Print front of queue and remove it from queue
        print(queue[0].data)
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)
        
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

# Function to print level order traversal of tree
def print_level_order(root):
    h = height(root)
    for i in range(1, h + 1):
        print_current_level(root, i)

# Print nodes at current level
def print_current_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end = " ")
    elif level > 1:
        print_current_level(root.left, level - 1)
        print_current_level(root.right, level - 1)

"""
    Compute the height of a tree, the number of nodes along the
    longest path from the root node down to the farthest leaf node.
"""
def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        left_height = height(node.left)
        right_height = height(node.right)

        # Use the larger one
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1