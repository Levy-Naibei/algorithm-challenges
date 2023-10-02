"""
Given a string, output its longest prefix which contains only digits.
"""

def longest_digit_pref(string):
    longest_pref = ""
    
    for i in string:
        if i.isdigit():
            longest_pref += i
        else:
            break

    return longest_pref

print(longest_digit_pref("123aa1"))
