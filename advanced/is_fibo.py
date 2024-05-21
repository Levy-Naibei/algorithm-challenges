"""
You are given an integer,N. Write a program to determine if N is an element of the Fibonacci sequence.
A Fibonacci sequence is one where every element is a sum of the previous two elements in the sequence. 
The first two elements are  and 0, 1
"""
def isFibo(n):
    a, b = 0, 1
    
    # Edge case: if n is one of the first two Fibonacci numbers
    if n == a or n == b:
        return "IsFibo"
    
    # Generate Fibonacci numbers iteratively
    while b <= n:
        # Next Fibonacci number
        a, b = b, a + b
        if b == n:
            return "IsFibo"
    
    return "IsNotFibo"

print(isFibo(5))
