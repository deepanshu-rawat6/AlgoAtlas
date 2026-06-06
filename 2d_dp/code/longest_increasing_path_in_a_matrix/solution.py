"""
# 329. Longest Increasing Path in a Matrix

## Problem
Given an `m x n` integers matrix, return the length of the longest increasing path.
From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary.

## Examples
```text
Input:  matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: Longest path is [1, 2, 6, 9]

Input:  matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: Longest path is [3, 4, 5, 6]

Input:  matrix = [[1]]
Output: 1
```

## Constraints
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 200
- 0 <= matrix[i][j] <= 2^31 - 1
"""
from typing import List
from collections import deque


class Solution:
    def longestIncreasingPath_dfs(self, matrix: List[List[int]]) -> int:
        # Time: O(m*n), Space: O(m*n)
        m, n = len(matrix), len(matrix[0])
        memo = {}

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            best = 1
            for dr, dc in ((0,1),(0,-1),(1,0),(-1,0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            memo[(r, c)] = best
            return best

        return max(dfs(r, c) for r in range(m) for c in range(n))

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # DFS with memoization from each cell; only move to strictly larger neighbors
        # dp[r][c] = longest path starting at (r,c)
        # Time: O(m*n), Space: O(m*n)
        m, n = len(matrix), len(matrix[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        indegree = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                        indegree[nr][nc] += 1
        queue = deque((r, c) for r in range(m) for c in range(n) if indegree[r][c] == 0)
        length = 0
        while queue:
            length += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            queue.append((nr, nc))
        return length


if __name__ == '__main__':
    s = Solution()
    assert s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]) == 4
    assert s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]) == 4
    assert s.longestIncreasingPath([[1]]) == 1
    assert s.longestIncreasingPath_dfs([[9,9,4],[6,6,8],[2,1,1]]) == 4
    print("All tests passed.")
