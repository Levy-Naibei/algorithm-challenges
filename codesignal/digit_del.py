"""
Given some integer, find the maximal number you can obtain
by deleting exactly one digit of the given number.
"""

def del_digit(n):
    max_num = 0
    num_str = str(n)

    for i in range(len(num_str)):
        num_without_digit = int(num_str[:i] + num_str[i+1:])
        max_num = max(max_num, num_without_digit)
    
    return max_num

print(del_digit(54))
