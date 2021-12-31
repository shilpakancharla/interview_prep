"""
    Print all paths with sum k.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Utility function to print contents of a vector from index i
# to its end
def print_vector(v, i):
    for j in range(i, len(v)):
        print(v[j], end = " ")
    print()

def print_k_path_util(root, path, k):
    # Empty node
    if not root:
        return

    # Add current node to the path
    path.append(root.data)

    # Check if there's any k sum path in the left sub-tree
    print_k_path_util(root.left, path, k)

    # Check if there's any k sum path in the right sub-tree
    print_k_path_util(root.right, path, k)

    # Check if there's any k sum path that terminates at this node
    # Traverse the entire path as there can be negative elements too
    f = 0
    for j in range(len(path) - 1, -1, -1):
        f += path[j]

        # If path sum is k, print the path
        if (f == k):
            print_vector(path, j)
    
    # Remove the current element from the path
    path.pop(-1)

# Wrapper over print_k_path_util()
def print_k_path(root, k):
    path = []
    print_k_path_util(root, path, k)