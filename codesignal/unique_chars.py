"""
Given a string, find the number of different characters in it.
"""

def unique_chars(string):
    return len(set(string))

print(unique_chars("cabca"))
