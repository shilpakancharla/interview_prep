"""
    Print all permutations with respect to cases.
"""

# Function to generate permutations
def permute(inp):
    n = len(inp)
    
    # Number of permutations is 2^n
    mx = 1 << n

    # Converting string to lower case
    inp = inp.lower()

    # Using all subsequences and permuting them
    for i in range(max):
        # If jth bit is set, we convert it to upper case
        combination = [k for k in inp]
        for j in range(n):
            if (((i >> j) & 1) == 1):
                combination[j] = inp[j].upper()

        temp = ""
        # Printing current combination
        for i in combination:
            temp += i
        print(temp)