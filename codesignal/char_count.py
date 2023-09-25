"""
Given two strings, find the number of common characters between them.
"""

def common_char_count(str_one, str_two):
    chars = 0
    # char_count = {}
    
    for char in str_one:
        # char_count[char] = char_count.get(char, 0) + 1
        if char in str_two:
            char += 1
        # else:
        #     char = 0
    
    return chars

print(common_char_count("aabcc", "adcaa"))
