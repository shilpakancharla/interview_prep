"""
    Given an array of integers of size 'n', calculate the maximum sum of 'k'
    consecutive elements in the array.

    @param arr: array of numbers that we pass in
    @param k: number of consecutive integers
    @return sum of k consecutive integers found
"""
def max_sum(arr, k):
    n = len(arr) # Length of array
    # n should be greater than k
    if n < k:
        print("Invalid.")
        return -1
    
    window_sum = sum(arr[:k]) # Compute the sum of first window of size k
    max_sum = window_sum # First sum available

    # Compute the sums of the remaining windows by removing first element of previous window
    # and adding last element of the current window
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
    
    return max_sum