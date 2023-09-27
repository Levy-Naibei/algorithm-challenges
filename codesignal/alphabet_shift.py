"""
Given a string, your task is to replace each of its characters
by the next one in the English alphabet; i.e. replace a with b,
replace b with c, etc (z would be replaced by a).
"""

def alphabetic_shift(input_string):
    new_string = ""
    for char in input_string:
        # convert char to ascii code equivalent using ord
        # increment the ascii_code by 1 and wrap around 'a' if it is 'z'
        # The % 26 is used to ensure that the shift remains within 
        # the 26 letters of the lowercase alphabet. ord('a') is added 
        # back to the result to obtain the new ASCII code of the shifted letter.
        new_ascii_code = (ord(char) - ord('a') + 1) % 26 + ord('a')
        # convert back to char and append to new_string
        new_string += chr(new_ascii_code)

    return new_string

print(alphabetic_shift("crazy"))
