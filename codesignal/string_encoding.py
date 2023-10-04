"""
Given a string, return its encoding defined as follows:
"""

def string_encoding(string):
    encoded_chars = []

    i = 0 # to keep track of current index in the input string
    # iterate through the input string until i reaches the end of the string.
    while i < len(string):
        # cant be initialized with 0;
        # char count should be always 1 or more
        count = 1

        # checks if we haven't reached the end of the string (i + 1 < len(s))
        # and if the next character (s[i + 1]) is the same as the current
        # character (string[i]).
        while i + 1 < len(string) and string[i + 1] == string[i]:
            # increment the char and move to the next char in the string
            count += 1
            i += 1

        if count > 1:
            encoded_chars.append(str(count) + string[i])
        else:
            encoded_chars.append(string[i])
        
        i += 1

    return ''.join(encoded_chars)

print(string_encoding("abbcabb"))
print(string_encoding("wwwwwwwawwwwwww"))
print(string_encoding("ssiiggkooo"))
