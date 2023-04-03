from typing import List


def minimumPathSum(grid: List[List[int]])->int:
    m = len(grid)
    n = len(grid[0])

    for i in range(1,m):
        grid[i][0] += grid[i-1][0]

    for i in range(1,n):
        grid[0][i] += grid[0][i-1]


    for i in range(1,m):
        for j in range(1,n):
         grid[i][j] += min(grid[i][j-1], grid[i-1][j])

    return grid[m-1][n-1]


print(minimumPathSum([[1,3,1],[1,5,1],[4,2,1]]))