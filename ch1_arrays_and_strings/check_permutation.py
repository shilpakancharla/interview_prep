"""
    Given two strings, write a method to decide if one is a permutation of the other.
"""

"""
    Determines if two strings are permutations of each other.

    @param string_input_1: string that needs to be checked
    @param string_input_2: string that needs to be checked
    @return true or false if the two strings are permutations
"""
def check_permutation(string_input_1, string_input_2):
    char_frequency_1 = dict()
    char_frequency_2 = dict()

    if len(string_input_1) != len(string_input_2):
        return False

    for s1, s2 in zip(string_input_1, string_input_2):
        if s1 not in char_frequency_1:
            char_frequency_1[s1] = 1
        else:
            char_frequency_1[s1] = char_frequency_1[s1] + 1

        if s2 not in char_frequency_2:
            char_frequency_2[s2] = 1
        else:
            char_frequency_2[s2] = char_frequency_2[s2] + 1

    for key1, key2 in zip(sorted(char_frequency_1), sorted(char_frequency_2)):
        if char_frequency_1[key1] != char_frequency_2[key2]:
            return False

    return True

# Driver code
string_1 = "wazup bro"
string_2 = " orbpuwaz"
string_3 = "hiiiya"
string_4 = "hiya"

result_1 = check_permutation(string_1, string_2)
print(result_1)
result_2 = check_permutation(string_3, string_4)
print(result_2)