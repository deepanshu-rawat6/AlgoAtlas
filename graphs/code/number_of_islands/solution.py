"""
# 200. Number of Islands

## Problem
Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and
`'0'`s (water), return the number of islands. An island is surrounded by water and is
formed by connecting adjacent lands horizontally or vertically.

## Examples
```text
Input:  grid = [["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]]
Output: 1
```

```text
Input:  grid = [["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]]
Output: 3
```

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`
"""

from typing import List
from collections import deque


class Solution:
    def numIslands_dfs(self, grid: List[List[str]]) -> int:
        # DFS flood fill: mark visited cells as '0' to avoid revisiting
        # Each DFS call from an unvisited '1' cell counts as one island
        # O(m*n) time, O(m*n) space — DFS flood fill
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        return count

    def numIslands_bfs(self, grid: List[List[str]]) -> int:
        # BFS flood fill: same idea but uses a queue instead of recursion
        # O(m*n) time, O(min(m,n)) space — BFS flood fill
        rows, cols = len(grid), len(grid[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    grid[r][c] = '0'
                    q = deque([(r, c)])
                    while q:
                        cr, cc = q.popleft()
                        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nr, nc = cr+dr, cc+dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                q.append((nr, nc))
        return count

    def numIslands(self, grid: List[List[str]]) -> int:
        # Union-Find: union adjacent land cells; count distinct components
        # O(m*n) time, O(m*n) space — Union-Find
        rows, cols = len(grid), len(grid[0])
        parent = list(range(rows * cols))
        rank = [0] * (rows * cols)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        count = sum(grid[r][c] == '1' for r in range(rows) for c in range(cols))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    for dr, dc in [(1,0),(0,1)]:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            if union(r*cols+c, nr*cols+nc):
                                count -= 1
        return count


if __name__ == '__main__':
    import copy
    s = Solution()
    g1 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    g2 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    assert s.numIslands(copy.deepcopy(g1)) == 3
    assert s.numIslands(copy.deepcopy(g2)) == 1
    assert s.numIslands_dfs(copy.deepcopy(g1)) == 3
    assert s.numIslands_bfs(copy.deepcopy(g1)) == 3
    print("All tests passed.")
