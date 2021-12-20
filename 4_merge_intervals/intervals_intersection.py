"""
    Given a set of time intervals in any order, mege all overlapping intervals into one and output the result which should have 
    only mutually exclusive intervals. Let the intervals be represented as pairs of integers for simplicity. For example, let the
    given set be {{1, 3}, {2, 4}, {5, 7}, {6, 8}}. The intervals {1, 3} and {2, 4} should be come {1, 4}, and {5, 7} and {6, 8}
    should become {5, 8}. Write a function that produces the set of merged intervals for the given set of intervals.
"""

def merge_intervals(array):
    # Sort based on the increasing order of the start intervals
    array.sort(key = lambda x: x[0])

    # Array to hold the merged intervals
    m = []
    s = -10000
    max = -100000
    for i in range(len(array)):
        a = arr[i]
        if a[0] > max:
            if i != 0: # If we are not looking at the first element in the list
                m.append([s, max])
            max = a[1]
            s = a[0]
        else: 
            if a[1] >= max:
                max = a[1]
    
    # 'max' value gives the last points of that particular interval
    # 's' gives the starting pint of that interval
    # 'm' array contains the list of all merged intervals

    if max != -100000 and [s, max] not in m:
        m.append([s, max])
    print("The merged intervals are :", end = " ")
    for i in range(len(m)):
        print(m[i], end = " ")

# Driver code
array = [[6, 8], [1, 9], [2, 4], [4, 7]]
merge_intervals(array)