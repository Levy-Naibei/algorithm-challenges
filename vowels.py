def vowels_count(v):
    vowels = 0
    for char in set(v):
        if char.lower() in ["a", "e", "i", "o", "u"]:
            vowels += 1
    return vowels
print(vowels_count("welcome"))
