from collections import Counter

def check_anagram(str1, str2):
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False

    # Create character frequency counters for both strings
    counter1 = Counter(str1)
    counter2 = Counter(str2)

    # Compare the counters to check if they are equal
    return counter1 == counter2

    # char_count = [0] * 26  # Initialize a list of 26 zeros to represent character counts

    # for char in str1:
    #     char_count[ord(char) - ord('a')] += 1

    # for char in str2:
    #     char_count[ord(char) - ord('a')] -= 1
    #     if char_count[ord(char) - ord('a')] < 0:
    #         return False

    # return True

print(check_anagram("silent", "listen"))
