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
