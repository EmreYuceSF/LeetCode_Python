import numpy as np

def minFallingPathSum(matrix: list[list[int]]) -> int:
    n = len(matrix)
    if n ==1:
        return matrix[0][0]
    matrix = matrix + [[0]*n]
    print(matrix)
    #matrix  = np.array(matrix, dtype="int16")
    
    def climbUp(matrix, length):
        if length ==0:
            return min(matrix[0])
        
        for i in range(n:=len(matrix[0])):
            if i == 0:
                matrix[length-1][0] += min(matrix[length][0], matrix[length][1])
            elif i == n-1:
                matrix[length-1][i] += min(matrix[length][-1], matrix[length][-2])
            else:
                matrix[length-1][i] += min(matrix[length][i-1], matrix[length][i], matrix[length][i+1])
        matrix.pop()
        return climbUp(matrix, length-1)
           
    return climbUp(matrix, n)
print(minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
    
    