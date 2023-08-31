def valid_palindrome(s):
    # check whether string is palindrome or not
    def is_palindrome(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try removing either the character at the left or right index
            return is_palindrome(s, left + 1, right) or is_palindrome(
                s, left, right - 1
            )
        left += 1
        right -= 1
    
    return True

print(valid_palindrome("eyes"))
