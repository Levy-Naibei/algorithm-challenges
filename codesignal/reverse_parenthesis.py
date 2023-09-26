"""
Write a function that reverses characters in (possibly nested) 
parentheses in the input string.
Input strings will always be well-formed with matching ()s.
"""

def reverse_in_parenthesis(input_string):
    result = ""
    stack = []

    for char in input_string:
        if char == "(":
            stack.append(result)
            # reset to an empty string to start collecting characters
            # inside the new set of parentheses.
            result = ""
        elif char == ")":
            reversed_chars = result[::-1]
            # pops the previous result from the stack, 
            # appends the reversed characters, and stores 
            # the new result in the result variable.
            result = stack.pop() + reversed_chars
        else:
            result += char

    return result

print(reverse_in_parenthesis("foo(bar(baz))blim"))
