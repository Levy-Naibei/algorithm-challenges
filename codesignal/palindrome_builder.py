"""
Given a string, find the shortest possible string which can be achieved
by adding characters to the end of initial string to make it a palindrome.
"""

def build_palindrome(string):
    for i in range(len(string)):
        # check whether the suffix is a palindrome
        if string[i:] == string[i:][::-1]:
            # combine the original string and reversed prefix
            # to create shortest palindrome
            return string + string[:i][::-1]
    # if the entire string is not a palindrome, add a reversed substring
    return string + string[:-1][::-1]

print(build_palindrome("abcdc"))
