"""
You are given an array of integers representing coordinates of obstacles 
situated on a straight line. Assume that you are jumping from the point 
with coordinate 0 to the right. You are allowed only to make jumps of 
the same length represented by some integer. Find the minimal length of 
the jump enough to avoid all the obstacles.
"""


def jump_obstacles(input_array):
    max_jump_length = max(input_array) + 1

    for jump_length in range(1, max_jump_length):
        avoid_obstacle = True
        for coord in input_array:
            if coord % jump_length == 0:
                avoid_obstacle = False
                break
        if avoid_obstacle:
            return jump_length
    
    return max_jump_length


print(jump_obstacles([19, 32, 11, 23]))
