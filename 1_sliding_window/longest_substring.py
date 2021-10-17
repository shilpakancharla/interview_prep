"""
    Given a string, you need to print the longest possible substring that has
    exactly 'k' unique characters. If there are more than one substrings of longest
    possible length, then print any one of them.
"""

CHAR_RANGE = 128

def k_unique(s, k):
    # Store the longest substring boundaries (beginning and ending of substring)
    end = begin = 0

    # Instantiate set to store distinct characters in a window
    window = set()

    # Frequency array to store frequency of characters present in the current window
    freq = [0] * CHAR_RANGE

    # Sliding window boundaries (low is lower end of boundary, high is higher end of boundary)
    low = high = 0

    while high < len(s):
        window.add(s[high]) # Add a character to the set
        # Increment the frequency of that character
        freq[ord(s[high])] = freq[ord(s[high])] + 1

        # If the window size is more than 'k', remove characters from the left
        while len(window) > k:
            # If the leftmost character's frequency becomes 0 after removing it in the
            # window, remove it from the set as well
            freq[ord(s[low])] = freq[ord(s[low])] - 1
            if freq[ord(s[low])] == 0:
                window.remove(s[low])
            low = low + 1 # Reduce window size
        
        # Update the maximum window size if necessary
        if end - begin < high - low:
            end = high
            begin = low

        high = high + 1 # Increase the window size

    # Return the longest substring found at 's[begin...end]'
    return s[begin:end + 1]

if __name__ == '__main__':
    s = 'abcbdbdbbdcdabd'
    k = 2
    print(k_unique(s, k))