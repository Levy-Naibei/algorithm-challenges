def longest_common_prefix(strs):
    if not strs:
        return ""

    # This ensures we have the string with the
    # fewest characters to iterate over
    shortest_str = min(strs, key=len)
    for i, char in enumerate(shortest_str):
        """
        For each character at index i, we use a generator expression
        with any to check if any other string in strs does not match
        the character at the same index. If a mismatch is found,
        we return the longest common prefix found so far,
        which is shortest_str[:i].
        """
        if any(string[i] != char for string in strs):
            return shortest_str[:i]

    """
    If no mismatches are found, we return the entire shortest_str 
    as the longest common prefix.
    """
    return shortest_str


print(longest_common_prefix(["flower", "flow", "flight"]))
