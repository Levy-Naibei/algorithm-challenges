"""
the bike's timer is that n minutes have passed since 00:00.
Using the bike's timer, calculate the current time. 
Return an answer as the sum of digits
that the digital timer in the format hh:mm would show.
"""

def late_ride(n):
    # Calculate hours and minutes
    hours = n // 60
    minutes = n % 60
    
    # Convert hours and minutes to string and concatenate
    time_str = str(hours) + str(minutes)
    print(time_str)
    
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in time_str)
    
    return digit_sum

print(late_ride(143))
