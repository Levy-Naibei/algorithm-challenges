"""
Staircase detail
This is a staircase of size :
   #
  ##
 ###
####
Its base and height are both equal to . It is drawn using # symbols and spaces. 
The last line is not preceded by any spaces.
Write a program that prints a staircase of size n.
"""

def stair_case(num_stairs):
    for stairs in range(1, num_stairs + 1):
        print(" " * (num_stairs - stairs) + "#" * stairs)

print(stair_case(5))
