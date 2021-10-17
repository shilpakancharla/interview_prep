"""
    Search for all anagrams of a pattern in a text.
"""

MAX = 256

"""
    Returns true if contents of arr1 and arr2 are same, otherwise false.
"""
def compare(arr1, arr2):
    for i in range(MAX):
        if arr1[i] != arr2[i]:
            return False
    return True

"""
    Searches for all the permuations of a pattern in a text.
"""
def search(pattern, text):
    m = len(pattern)
    n = len(text)

    count_p = [0] * MAX # Store count of all characters of pattern
    count_tw = [0] * MAX # Store count of current window of text

    for i in range(m):
        (count_p[ord(pattern[i])]) += 1
        (count_tw[ord(text[i])]) += 1

    # Traverse through remaining characters of pattern
    for i in range(m, n):
        # Compare counts of current window of text with counts of pattern
        if compare(count_p, count_tw):
            print("Found at index ", (i - m))

        # Add current character to current window
        (count_tw[ord(text[i])]) += 1

        # Remove the first character of previous window
        (count_tw[ord(text[i - m])]) -= 1

    # Check for the last window in text
    if compare(count_p, count_tw):
        print("Found at index ", n - m)

# Driver program to test above function
text = 'BACDGABCDA'
pattern = 'ABCD'
search(pattern, text)

