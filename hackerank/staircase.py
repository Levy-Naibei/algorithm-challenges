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
    for i in range(1, num_stairs + 1):
        spaces = " " * (num_stairs - i)
        stairs = "#" * i
        print(spaces + stairs)
stair_case(5)
