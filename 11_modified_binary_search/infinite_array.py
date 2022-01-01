"""
    Demonstrate working of an algorithm that finds an element in an 
    array of infinite size. 
"""

# Binary search algorithm implementation
def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - 1) // 2

        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        return binary_search(arr, mid + 1, r, x)

# Function takes an infinite size array and a key to be searched and returns its position
# if found else -1. We don't know size of a[] and we can assume size to be infinite in this function.
def find_pos(a, key):
    l, h, val = 0, 1, arr[0]

    # Find h to do binary search
    while val < key:
        l = h # Store previous high
        h = 2 * h # Double high index
        val = arr[h] # Update new val

    # At this point we have updated low and high indices, thus use binary search between them
    return binary_search(a, l, h, key)