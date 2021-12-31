"""
    Find all subsets of given set. Any repeated subset is considered only 
    once in the output.
"""

def print_power_set(arr, n):
    # Function to fina all subsets of a given set.
    # Any repeated subset is considered only once in the output.
    _list = []

    # Run counter i from 000...0 to 111...1
    for i in range(2 ** n):
        subset = ""
        
        # Consider each element in the set
        for j in range(n):
            # Check if jth bit in the i is set
            # If the bit is set, we consider jth element from set
            if (i & (1 << j)) != 0:
                subset += str(arr[j]) + "|"

        # If subset is encountered for the first time
        # We use set<string>, we can directly insert
        if subset not in _list and len(subset) > 0:
            _list.append(subset)
        
    # Consider every subset
    for subset in _list:
        # Split the subset and print its elements
        arr = subset.split('|')
        for string in arr:
            print(string, end = " ")
        print()