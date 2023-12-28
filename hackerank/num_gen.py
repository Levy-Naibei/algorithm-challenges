"""
A Decent Number has the following properties:
Its digits can only be 3's and/or 5's.
The number of 3's it contains is divisible by 5.
The number of 5's it contains is divisible by 3.
It is the largest such number for its length.

For example, the numbers 55533333 and 555555 are both decent numbers because 
there are three 5's and five 3's in the first, and  six 5's in the second. 
They are the largest values for those length numbers that have proper divisibility of digit occurrences.
Print the decent number for the given length, or -1 if a decent number of that length cannot be formed. 
No return value is expected. decent_number function has the following parameter(s):

int n: the length of the decent number to create
"""
def decent_number(n):
    
    # Find the largest number of 5's divisible by 3
    # the loop keeps subtracting 5 from num_fives until we find the largest number of 5's 
    # that is divisible by 3. Once num_fives becomes divisible by 3, the loop stops, 
    # and we have the largest number of 5's for a decent number.
    num_fives = n
    while num_fives % 3 != 0:
        num_fives -= 5
    
    # If num_fives becomes negative, no decent number is possible
    if num_fives < 0:
        print("-1")
        return
    
    print('5' * num_fives + '3' * (n - num_fives))
 
decent_number(13)