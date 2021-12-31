"""
    Given a binary tree, where every node value is a digit from 1-9. Find
    the sum of all the numbers which are formed from root to leaf paths.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Returns sum of all root and leaf paths. The first parameter is root of current subtree,
# the second parameter is value of the number formed by nodes from root to this node.
def tree_path_sum_util(root, val):
    # Base case
    if root is None:
        return 0
    
    # Update val
    val = (val * 10 + root.data)

    # If current node is leaf, return the current value of val
    if root.left is None and root.right is None:
        return value

    # Recur sum of values for left and right subtree
    return (tree_path_sum_util(root.left, val) +
            tree_path_sum_util(root.right, val)) 

# A wrapper function over tree_path_sum_util()
def tree_path_sum(root):
    # Pass the initial value as 0 as there is nothing above the root
    return tree_path_sum_util(root, 0)