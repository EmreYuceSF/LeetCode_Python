def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    n=len(obstacleGrid[0])
    m=len(obstacleGrid)
    row = [1]*n
    matrix = [row]
    newRow = [1]*n
    for j in range(m-1):
        for i in range(n-2,-1,-1):
            newRow[i] = newRow[i]+newRow[i+1]
        a = newRow.copy()
        matrix.insert(0,a)
    total = matrix[0][0]
    
    for j in range(m):
        for i in range(n):
            if obstacleGrid[j][i] == 1:
                total -= (matrix[j][i])
    return total
        
        
print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))