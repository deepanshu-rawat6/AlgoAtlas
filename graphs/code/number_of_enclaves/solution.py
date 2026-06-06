from typing import List
from collections import deque

class Solution:
    # BFS from all boundary land cells, mark reachable land, count unmarked land
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        # seed BFS with all boundary land cells
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 1:
                    queue.append((r, c))
                    grid[r][c] = 0  # mark visited by sinking to 0

        # flood-fill from boundary - sink all connected land
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    queue.append((nr, nc))

        # remaining 1s are enclaves (not reachable from boundary)
        return sum(grid[r][c] for r in range(rows) for c in range(cols))
