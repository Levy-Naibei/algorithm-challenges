"""
Several people are standing in a row and need to be divided into two teams.
The first person goes into team 1, the second goes into team 2, 
the third goes into team 1 again, the fourth into team 2, and so on.
You are given an array of positive integers - the weights of the people. 
Return an array of two integers, where the first element is the 
total weight of team 1, and the second element is the total weight 
of team 2 after the division is complete.
"""

def solution(input_array):
    team_one = 0
    team_two = 0
    for i in range(len(input_array)):
        if i == 0 or i % 2 == 0:
            team_one += input_array[i]
        else:
            team_two += input_array[i]
    
    return [team_one, team_two]

print(solution([50, 60, 60, 45, 70]))
