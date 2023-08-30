def is_valid_parentheses(s):
  stack = None
  opening_brackets = {"(", "[", "{"}
  bracket_map = {")": "(", "]": "[", "}": "{"}

  for char in s:
    if stack is None:
        stack = [char]
    elif char in opening_brackets:
        stack.append(char)
    elif char in bracket_map:
        """If char is a closing bracket, the stack is checked to ensure
        it is not None (stack is None) and that the top of the stack
        matches the corresponding opening bracket character (stack[-1] != bracket_map[char]).
        If either condition is true, it means the parentheses are not balanced or properly nested,
        and the function returns the current state of the stack along with the string "Invalid".
        """
        if stack is None or stack[-1] != bracket_map[char]:
            return stack, "Invalid"
        stack.pop()

    """After processing all the characters, the function checks 
    the final state of the stack. If it is None, it means all opening 
    brackets have been closed, and the function returns the stack along with the 
    string "Valid". Otherwise, if there are remaining opening brackets in the stack, 
    it means the parentheses are invalid, and the function 
    returns the stack along with the string "Invalid"."""

  return stack, "Valid" if stack is None else "Invalid"


print(is_valid_parentheses("{[()]}"))
