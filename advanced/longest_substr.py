def longest_substr(s):
    """
    sliding window technique to find length of
    longest substr without repeating chars
    """
    
    n = len(s)
    """initializes an empty dictionary to store characters 
    and their indices as we traverse the string."""
    char_map = {}
    max_length = 0
    start = 0

    """loop iterates over the indices of the string s from 0 to n-1."""
    for end in range(n):
        """
        If the character is repeating, we update the start pointer to move
        past the last occurrence of s[end] (plus one).
        This ensures that the new window only contains unique characters.
        """
        if s[end] in char_map:
            start = max(start, char_map[s[end]] + 1)

        """
        store the index, end, of each character encountered in the 
        string s during the iteration.
        By storing the index of each character in the dictionary, 
        we can efficiently update the start pointer to the appropriate position
        to exclude the repeated character from the new window. 
        This ensures that the window only contains unique characters.
        """
        char_map[s[end]] = end
        """
        calculate the length of the current non-repeating substring 
        as end - start + 1 and update the max_length variable if necessary.
        """
        max_length = max(max_length, end - start + 1)

    return max_length


print(longest_substr("abcabcbb"))
