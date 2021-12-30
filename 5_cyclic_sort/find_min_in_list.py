"""
    Find the minimum element in a sorted and rotated array.
"""

# Method for unique elements
def find_min(arr, low, high):
    # This condition is needed to handle the case when array is not rotated at all
    if high < low:
        return arr[0]

    # If there is only one element left
    if high == low:
        return arr[low]

    # Find mid
    mid = int((low + high) / 2)

    # Check if element (mid + 1) is minimum element. 
    if mid < high and arr[mid + 1] < arr[mid]:
        return arr[mid + 1]
    
    # Check if mid itself is minimum element
    if mid > low and arr[mid] < arr[mid - 1]:
        return arr[mid]

    # Decide whether we need to go to left half or right half
    if arr[high] > arr[mid]:
        return find_min(arr, low, mid - 1)
    return find_min(arr, mid + 1, high)

# Method for duplicate elements
def find_min_duplicates(arr, low, high):
    while (low < high):
        mid = low + (high - low) // 2
        
        if (arr[mid] == arr[high]):
            high -= 1
        elif (arr[mid] > arr[high]):
            low = mid + 1
        else:
            high = mid
    return arr[high]