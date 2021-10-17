"""
    Given an array of distinct elements, the task is to find triplets
    in the array whose sum is zero.
"""

# Function to print triplet with zero sum
def find_triplets(arr, n):
    found = False
    # Sort array elements
    arr.sort()
    for i in range(0, n - 1):
        # Initialize left and right pointer
        l = i + 1
        r = n - 1
        x = arr[i]
        while (l < r):
            if (x + arr[l] + arr[r] == 0):
                # Print elements if it's the sum of zero
                print(x, arr[l], arr[r])
                l += 1
                r -= 1
                found = True
            elif (x + arr[l] + arr[r] < 0):
                # If the sum of the three elements is less than
                # zero then increment in the left
                l += 1
            else:
                # If the sum is greater than zero then decrement on right side
                r -= 1
    if (found == False):
        print("No triplet found.")

# Driver code
arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)