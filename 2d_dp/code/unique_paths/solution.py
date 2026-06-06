"""
# 62. Unique Paths

## Problem
A robot is located at the top-left corner of an `m x n` grid. The robot can only
move either down or right at any point in time. The robot is trying to reach the
bottom-right corner of the grid. How many possible unique paths are there?

## Examples
```text
Input:  m = 3, n = 7
Output: 28

Input:  m = 3, n = 2
Output: 3
Explanation: From top-left, 3 paths:
  1. Right -> Down -> Down
  2. Down -> Down -> Right
  3. Down -> Right -> Down
```

## Constraints
- 1 <= m, n <= 100
"""
from math import comb


class Solution:
    def uniquePaths_2d(self, m: int, n: int) -> int:
        # Time: O(m*n), Space: O(m*n)
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

    def uniquePaths_1d(self, m: int, n: int) -> int:
        # Time: O(m*n), Space: O(n)
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[n-1]

    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] = paths to reach (i,j) = dp[i-1][j] + dp[i][j-1]
        # Time: O(m+n), Space: O(1)
        return comb(m + n - 2, n - 1)


if __name__ == '__main__':
    s = Solution()
    assert s.uniquePaths(3, 7) == 28
    assert s.uniquePaths(3, 2) == 3
    assert s.uniquePaths(1, 1) == 1
    assert s.uniquePaths_2d(3, 7) == 28
    assert s.uniquePaths_1d(3, 7) == 28
    print("All tests passed.")
