"""
# 695. Max Area of Island

## Problem
You are given an `m x n` binary matrix `grid`. An island is a group of `1`s (representing
land) connected 4-directionally (horizontal or vertical). The area of an island is the
number of cells with value `1` in the island. Return the maximum area of an island in
`grid`. If there is no island, return `0`.

## Examples
```text
Input:  grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
```

```text
Input:  grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j]` is `0` or `1`
"""

from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland_dfs(self, grid: List[List[int]]) -> int:
        # O(m*n) time, O(m*n) space — DFS flood fill tracking area
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        return max(dfs(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 1) or 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS flood fill: return size of each island; track global maximum
        # O(m*n) time, O(m*n) space — BFS flood fill tracking area
        rows, cols = len(grid), len(grid[0])
        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    area, q = 1, deque([(r, c)])
                    while q:
                        cr, cc = q.popleft()
                        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nr, nc = cr+dr, cc+dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                area += 1
                                q.append((nr, nc))
                    best = max(best, area)
        return best


if __name__ == '__main__':
    import copy
    s = Solution()
    g = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    assert s.maxAreaOfIsland_dfs(copy.deepcopy(g)) == 6
    assert s.maxAreaOfIsland(copy.deepcopy(g)) == 6
    assert s.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]) == 0
    print("All tests passed.")
