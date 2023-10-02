"""
A string is said to be beautiful if each letter in the string appears
at most as many times as the previous letter in the alphabet within the
string; ie: b occurs no more times than a; c occurs no more times than b; etc.
Note that letter a has no previous letter. Given a string, check whether it is beautiful.
"""
import string
def is_beautiful(input_str):
    last_char = 30
    for i in string.ascii_lowercase:
        char_count = input_str.count(i)
        if char_count > last_char:
            return False
        last_char = char_count
    return True

print(is_beautiful("bbbaacdafe"))
