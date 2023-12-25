"""
program that compare 3 array values and returns an ouput array with score/points
after comparing 2 arrays a and b
"""
def compare_triplets(a, b):
    alice_points=0
    bob_points=0
    
    for i in range(len(a)):
        if a[i] > b[i]:
            alice_points += 1
        elif a[i] < b[i]:
            bob_points += 1
        
    return [alice_points, bob_points]

print(compare_triplets([2,3,4], [4,5,2]))
