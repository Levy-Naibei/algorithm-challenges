"""
Given an array of strings, return another array containing 
all of its longest strings.
"""


def longest_strings(input_array):
    longest_strings = []
    max_len = 0

    for string in input_array:
        max_len = max(max_len, len(string))

    for string in input_array:
        if (len(string)) == max_len:
            longest_strings.append(string)
    
    return longest_strings

print(longest_strings(["aba", "aa", "ad", "vcd", "aba"]))