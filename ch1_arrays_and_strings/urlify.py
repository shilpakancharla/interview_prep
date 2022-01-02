"""
    Write a metho to replace all sapces in a string with '%20'. You may assume that the string has sufficient space at the end
    to hold the additional characters, and that you are given the "true" length of the string.
"""

"""
    Inserts '%20' where there is a blank space in the string.

    @param string: string to URLify
    @param length: true length of string
    @return string that has been URLified
"""
def urlify(string, length):
    if string == "":
        return string
    
    # Remove leading and trailing whitespace
    string = string.strip()
    space_count = string.count(' ')
    new_length = length + space_count * 2
    string_list = list(string)
    
    # Start filling character from end
    index = new_length - 1
    
    # Fill the string array
    for f in range(length - 2, new_length - 2):
        string_list.append('0')
    
    # Fill rest of the string from end
    for j in range(length - 1, 0, -1):
        # Inserts %20 in place of space
        if string_list[j] == ' ':
            string_list[index] = '0'
            string_list[index - 1] = '2'
            string_list[index - 2] = '%'
            index = index - 3
        else:
            string_list[index] = string_list[j]
            index -= 1
    
    return ''.join(string_list)

# Driver code
input_string = 'Mr John Smith   '
length = 13
result = urlify(input_string, length)
print(result)