from typing import List
from collections import deque

class Solution:
    # BFS in 8 directions - first time we reach (n-1,n-1) is shortest path
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1  # start or end is blocked

        if n == 1:
            return 1  # single cell grid

        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        grid[0][0] = 1  # mark visited by setting to 1

        for r, c, dist in queue:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        if nr == n - 1 and nc == n - 1:
                            return dist + 1  # reached destination
                        grid[nr][nc] = 1  # mark visited
                        queue.append((nr, nc, dist + 1))

        return -1  # no path found
