
"""
Given a string. determine if it can be rearranged into a palindrome. Return the string YES or
NO.
Example
s = 'aabbccdd'
One way this can be arranged into a palindrome is abcddcba. Return YES.
Function Description
Complete the gameOfThrones function below.
gameOfThrones has the following parameter(s):
• string s: a string to analyze
Returns
• string: either YES or NO
Input Format
A single line which contains s.
Constraints
•1<lsl < 10
• s contains only lowercase letters in the range ascii a ... z

Sample Input 0
aaabbbb
Sample Output 0
YES
Explanation 0
A palindromic permutation of the given string is bbaaabb.
Sample Input 1
cdefghmnopqrstuvw
Sample Output 1
NO
Explanation 1
Palindromes longer than 1 character are made up of pairs of characters. 

Sample Input 2
cdcdcdcdeeeef
Sample Output 2
YES
Explanation 2
An example palindrome from the string: ddcceefeeccdd
"""

def gameOfThrones(s):
    # count the freq of each char in the str
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
 
    # a string  can be rearranged into a palindrome if atmost 1 char has an odd count
    # and the rest have even counts
    # check for number of chars with odd counts.
    odd_count = sum(1 for char, count in char_count.items() if count % 2 != 0)
    if odd_count > 1:
        return 'NO'
    else:
        return 'YES'

print(gameOfThrones("cdefghmnopqrstuvw"))
    