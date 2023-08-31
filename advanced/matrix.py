def solution(matrix):
    total_sum = 0
    rows = len(matrix)
    cols = len(matrix[0])
    
    for j in range(cols):
        is_suitable = True
        for i in range(rows):
            if matrix[i][j] == 0:
                # print("matrix[i][j] == ", matrix[i][j])
                is_suitable = False
            elif is_suitable:
                print("matrix[i][j] == ", matrix[i][j])
                total_sum += matrix[i][j]
    
    return total_sum

matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]

print(solution(matrix))
