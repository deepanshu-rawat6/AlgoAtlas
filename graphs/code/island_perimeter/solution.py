"""
# 463. Island Perimeter

## Problem
You are given `row x col` grid representing a map where `grid[i][j] = 1` represents land
and `grid[i][j] = 0` represents water. Grid cells are connected horizontally/vertically.
There is exactly one island (no lakes). Return the perimeter of the island.

## Examples
```text
Input:  grid = [[0,1,0,0],
                [1,1,1,0],
                [0,1,0,0],
                [1,1,0,0]]
Output: 16
```

```text
Input:  grid = [[1]]
Output: 4
```

```text
Input:  grid = [[1,0]]
Output: 4
```

## Constraints
- `row == grid.length`
- `col == grid[i].length`
- `1 <= row, col <= 100`
- `grid[i][j]` is `0` or `1`
- There is exactly one island in `grid`
"""

from typing import List
from collections import deque


class Solution:
    def islandPerimeter_counting(self, grid: List[List[int]]) -> int:
        # O(m*n) time, O(1) space
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
        return perimeter

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # For each land cell, add 4 sides; subtract 2 for each shared edge with neighbor
        # O(m*n) time, O(m*n) space — DFS
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 1
            if (r, c) in visited:
                return 0
            visited.add((r, c))
            return dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)
        return 0


if __name__ == '__main__':
    s = Solution()
    assert s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16
    assert s.islandPerimeter([[1]]) == 4
    assert s.islandPerimeter([[1,0]]) == 4
    assert s.islandPerimeter_counting([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16
    print("All tests passed.")
