"""
# LC 827: Making A Large Island

Flip at most one `0` to `1` in an n x n binary grid. Return the size of the
largest island (4-directionally connected group of 1s) after the flip.

## Examples
```text
Input: grid=[[1,0],[0,1]]
Output: 3
# Flipping the 0 at (0,1) (or (1,0)) bridges the two size-1 islands → size 3.
```

## Constraints
- Label + lookup — O(n^2)
- Label each island with a unique id (starting at 2) and record its size
- For each 0 cell, sum sizes of distinct neighboring islands + 1
- If the grid is all 1s (no 0 to flip), the answer is n^2
"""
from typing import List
from collections import defaultdict

class Solution:
    # Label each island with unique id, store sizes. For each 0, sum unique neighbor island sizes + 1.
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2  # start from 2 (0 and 1 are used)
        island_size = defaultdict(int)

        def dfs(r, c, iid):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = iid  # label with island id
            return 1 + dfs(r+1,c,iid) + dfs(r-1,c,iid) + dfs(r,c+1,iid) + dfs(r,c-1,iid)

        # label all islands and record their sizes
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_size[island_id] = dfs(r, c, island_id)
                    island_id += 1

        # best without flipping (all 1s case)
        result = max(island_size.values(), default=0)

        # try flipping each 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    size = 1  # the flipped cell itself
                    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            iid = grid[nr][nc]
                            if iid not in seen:
                                size += island_size[iid]
                                seen.add(iid)
                    result = max(result, size)

        return result


if __name__ == "__main__":
    sol = Solution()

    # Example from README (solution mutates grid, so pass a fresh copy each time)
    assert sol.largestIsland([[1, 0], [0, 1]]) == 3

    # Flipping the single 0 joins two halves → size 4
    assert sol.largestIsland([[1, 1], [1, 0]]) == 4

    # All ones, no 0 to flip → answer is n^2
    assert sol.largestIsland([[1, 1], [1, 1]]) == 4

    # All zeros → flip any one cell → island of size 1
    assert sol.largestIsland([[0, 0], [0, 0]]) == 1

    print("All tests passed.")
