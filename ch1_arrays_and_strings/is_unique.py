"""
    Implement an algorithm to determine if a string has all unique characters. 
    What if you cannot use additional data structures? 
"""

"""
    Determines if a string has all unique characters. Uses a dictionary to keep count of character 
    frequency.

    @param string_input: string that needs to be checked
    @return true or false if the string has all unique characters
"""
def is_unique(string_input):
    char_count = dict()
    
    if string_input == "": # Consider basic case
        return True
    
    for s in string_input:
        if s not in char_count:
            char_count[s] = 1
        else:
            char_count[s] = char_count[s] + 1
            return False
    return True

# Driver code
unique_string = 'shilpa'
not_unique_string = 'array'

result_1 = is_unique(unique_string)
print(result_1) # True
result_2 = is_unique(not_unique_string)
print(result_2) # False