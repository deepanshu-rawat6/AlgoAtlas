"""
# 64. Minimum Path Sum

## Problem
Given an `m x n` grid filled with non-negative numbers, find a path from the
top-left to the bottom-right which minimizes the sum of all numbers along its path.
You can only move either down or right at any point in time.

## Examples
```text
Input:  grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Path 1→3→1→1→1 = 7

Input:  grid = [[1,2,3],[4,5,6]]
Output: 12
```

## Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 200
"""
from typing import List


class Solution:
    def minPathSum_2d(self, grid: List[List[int]]) -> int:
        # Time: O(m*n), Space: O(m*n)
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp[i][j] = min path sum to reach (i,j) = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        # Time: O(m*n), Space: O(n)
        m, n = len(grid), len(grid[0])
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[n-1]


if __name__ == '__main__':
    s = Solution()
    assert s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7
    assert s.minPathSum([[1,2,3],[4,5,6]]) == 12
    assert s.minPathSum_2d([[1,3,1],[1,5,1],[4,2,1]]) == 7
    print("All tests passed.")
