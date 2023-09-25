"""
Ticket numbers usually consist of an even number of digits.
A ticket number is considered lucky if the sum of the 
first half of the digits is equal to the sum of the second half.
Given a ticket number n, determine if it's lucky or not.
"""


def is_lucky(n):
    ticket_str = str(n)
    mid_point = len(ticket_str) // 2
    first_half = ticket_str[:mid_point]
    second_half = ticket_str[mid_point:]

    sum_first_half = sum(int(digit) for digit in first_half)
    sum_second_half = sum(int(digit) for digit in second_half)

    return sum_first_half == sum_second_half


print(is_lucky(239017))
