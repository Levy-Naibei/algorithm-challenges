def reverse_words(string):
    words = string.split()
    return ' '.join(words[::-1])

print(reverse_words("hello world"))
