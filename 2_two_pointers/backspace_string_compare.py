"""
    Given two strings 's' and 't', return 'True' if they are equal when both
    are typed into empty text editors. '#' means a backspace character.
"""

# Use stack to do the operation on both and then compare
def backspace_compare(s, t):
    s = []
    for item in s:
        if item == '#':
            if s:
                s.pop()
        else:
            s.append(item)
    t = []
    for item in t:
        if item == '#':
            if t:
                t.pop()
        else:
            t.append(item)

    return s == t

# Driver code
s = 'ab#c'
t = 'ad#c'
print(backspace_compare(s, t))