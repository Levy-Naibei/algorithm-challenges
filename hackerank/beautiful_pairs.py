"""
You are given two arrays, A and B, both containing N integers.
A pair of indices (i,j) is beautiful if the ith element of array A is equal to the jth element of array B.
In other words, pair (i,j) is beautiful if and only if A[i]=B[j]. 
A set containing beautiful pairs is called a beautiful set.
A beautiful set is called pairwise disjoint if for every pair (l[i], r[j]) 
belonging to the set there is no repetition of either l[i] or r[i] values. 
For instance, if A=[10, 11, 12, 5, 14] and B=[8, 9, 11, 11, 5] the 
beautiful set [(1, 2), (1, 3), (3, 4)] is not pairwise disjoint as there is a repetition of 1, that is l[0][0] = l[1][0].
Your task is to change exactly 1 element in B so that the size of the pairwise disjoint beautiful set is maximum.
It should return an integer that represents the maximum number of pairwise disjoint beautiful pairs that can be formed.
"""

def beautiful_pairs(A, B):
    count_b = {}
    common_numbers = 0
    for num in B:
        count_b[num] = count_b.get(num, 0) + 1
    for num in A:
        if num in count_b and count_b[num] > 0:
            common_numbers += 1
            count_b[num] -= 1
    
    # If there is at least one common element, 
    # we can change one element in A to maximize the beautiful pairs
    if common_numbers < len(A):
        return common_numbers + 1
    # If all elements are common, we must change one element 
    # in A to keep the beautiful pairs pairwise disjoint 
    else:
        return common_numbers - 1

print(beautiful_pairs([1,2,3,4], [1,2,3,3]))
