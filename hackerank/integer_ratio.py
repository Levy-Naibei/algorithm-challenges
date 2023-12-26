"""
Given an array of integers, calculate the ratios of its elements that are 
positive, negative, and zero. Print the decimal value of each fraction
on a new line with  places after the decimal. Note: This challenge introduces precision problems. 
The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
"""

def plus_minus(arr):
    pos = neg = zero = 0
    n = len(arr)
    for i in arr:
        if i == 0:
            zero += 1
        elif i < 0:
            neg += 1
        else:
            pos += 1
    
    ratios = print(f"{round(pos/n, 6)}\n {round(neg/n, 6)}\n {round(zero/n, 6)}")
        
    return ratios

print(plus_minus([-2,3,0,-3,3,-4]))
