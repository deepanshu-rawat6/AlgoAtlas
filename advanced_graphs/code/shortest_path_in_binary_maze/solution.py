"""
# LC 1091: Shortest Path in Binary Matrix

Find the length of the shortest clear path (cells with value `0`) from `(0,0)`
to `(n-1,n-1)` moving in 8 directions. Return -1 if no such path exists.

## Examples
```text
Input: grid=[[0,1],[1,0]]
Output: 2
# Move diagonally (0,0) -> (1,1); both cells are clear.
```

## Constraints
- BFS on an unweighted grid — O(n^2)
- 8-directional movement (includes diagonals)
- Return -1 if start or end cell is blocked (value 1)
"""
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

        while queue:
            r, c, dist = queue.popleft()
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


if __name__ == "__main__":
    sol = Solution()

    # Example from README (solution mutates grid, so pass a fresh copy each time)
    assert sol.shortestPathBinaryMatrix([[0, 1], [1, 0]]) == 2

    # Single clear cell → path length 1
    assert sol.shortestPathBinaryMatrix([[0]]) == 1

    # LC classic example: 3x3 shortest clear path
    assert sol.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4

    # Blocked start → no path
    assert sol.shortestPathBinaryMatrix([[1, 0], [0, 0]]) == -1

    print("All tests passed.")
