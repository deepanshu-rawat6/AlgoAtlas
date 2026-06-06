"""
# 63. Unique Paths II

## Problem
You are given an `m x n` integer array `obstacleGrid`. A robot is initially located
at the top-left corner. The robot tries to reach the bottom-right corner. An obstacle
is marked with `1` and free space with `0`. Return the number of unique paths.

## Examples
```text
Input:  obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid.
  Two ways to reach bottom-right:
  1. Right -> Right -> Down -> Down
  2. Down -> Down -> Right -> Right

Input:  obstacleGrid = [[0,1],[0,0]]
Output: 1
```

## Constraints
- m == obstacleGrid.length
- n == obstacleGrid[i].length
- 1 <= m, n <= 100
- obstacleGrid[i][j] is 0 or 1
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles_2d(self, obstacleGrid: List[List[int]]) -> int:
        # Time: O(m*n), Space: O(m*n)
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Same as unique paths but set dp[i][j]=0 if obstacle at (i,j)
        # Time: O(m*n), Space: O(n)
        n = len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1
        for row in obstacleGrid:
            for j in range(n):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        return dp[n-1]


if __name__ == '__main__':
    s = Solution()
    assert s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2
    assert s.uniquePathsWithObstacles([[0,1],[0,0]]) == 1
    assert s.uniquePathsWithObstacles([[1]]) == 0
    assert s.uniquePathsWithObstacles_2d([[0,0,0],[0,1,0],[0,0,0]]) == 2
    print("All tests passed.")
