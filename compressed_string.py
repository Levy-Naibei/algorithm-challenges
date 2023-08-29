def compress_str(s):
    if not s:
        return ""

    compressed = []
    count = 1
    for i in range(1, len(s)):
        """If the current character s[i] is the same
        as the previous character s[i-1],
        it means the count needs to be incremented."""
        if s[i] == s[i - 1]:
            count += 1
        else:
            """
            If the current character s[i] is different from
            the previous character s[i-1], it means a new character is encountered.
            The previous character and its count are added to the compressed list.
            """
            compressed.append(s[i - 1] + str(count))
            count = 1

    # Add the last character and its count
    compressed.append(s[-1] + str(count))

    compressed_string = "".join(compressed)
    """ 
    If the compressed string is not shorter, 
    the original string s is returned as it would not result in any compression.
    """
    if len(compressed_string) >= len(s):
        return s
    else:
        """
        If the compressed string is shorter, it means compression is possible,
        so the compressed string is returned."""
        return compressed_string


print(compress_str("aabcccccaaa"))
