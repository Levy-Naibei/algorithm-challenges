"""
Define a word as a sequence of consecutive English letters.
Find the longest word from the given string.
"""

def longest_word(s):
    current_word = ""
    longest_word = ""
    
    for char in s:
        # checks if the current character char is an alphabetical letter. 
        if char.isalpha():
            current_word += char

        # if the current character char is not an alphabetical letter,
        # indicating that the current word has ended.
        else:
            # updates the longest_word to be the same as current_word
            # when we find a longer word.
            if len(current_word) > len(longest_word):
                longest_word = current_word
            # resets the current_word to an empty string,
            # as we have finished processing the current word.
            current_word = ""
    
    # Check one more time in case the longest word is at the end of s
    if len(current_word) > len(longest_word):
        longest_word = current_word
    
    return longest_word

print(longest_word("Ready, steady, go!"))
print(longest_word("To be or not to be"))
print(longest_word("You are the best!!!!!!!!!!!! CodeFighter ever!"))
print(longest_word("Ready[[[, steady, go!"))
