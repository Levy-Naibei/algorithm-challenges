"""
Some phone usage rate may be described as follows:
first minute of a call costs min1 cents,
each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
each minute after 10th costs min11 cents.
You have s cents on your account before the call. 
What is the duration of the longest call (in minutes rounded down to the nearest integer) you can have?
"""

def phone_call(min1, min2_10, min11, s):
    # If the balance is less than the cost of the first minute
    # call duration is 0
    if s < min1:
        return 0
    elif s < min1 + 9 * min2_10:
        # If the balance allows for the first 10 minutes
        # call duration is 1 plus the integer division of the remaining balance by min2_10
        return 1 + (s - min1) // min2_10
    else:
        # If the balance allows for more than 10 minutes
        # the call duration is 10 plus the integer division 
        # of the remaining balance after the first 10 minutes by min11.
        return 10 + (s - min1 - 9 * min2_10) // min11

print(phone_call(3, 1, 2, 20))
