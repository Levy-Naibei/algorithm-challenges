def find_duplicate_chars(s):
    char_count = {}
    duplicates = []

    if not s:
        return []

    for char in s:
        """if the character char is already present in the char_count dictionary
        increment its count by 1 using char_count[char] += 1."""
        if char in char_count:
            # print(char_count[char])
            char_count[char] += 1
            """If the count of the character char becomes 2 after incrementing,
        it means the character is a duplicate."""
            if char_count[char] == 2:
                duplicates.append(char)
        else:
            """
            If the character char is not already present
            in the char_count dictionary, add it with a count of 1.
            """
            char_count[char] = 1
    return duplicates


print(find_duplicate_chars("hellooworldh"))
