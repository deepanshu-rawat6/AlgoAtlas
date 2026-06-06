"""
# 286. Walls and Gates

## Problem
You are given an `m x n` grid `rooms` initialized with these three possible values:
- `-1` — A wall or an obstacle.
- `0` — A gate.
- `INF` — Infinity means an empty room. We use `2147483647` to represent `INF`.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach
a gate, leave it as `INF`. Modify `rooms` in-place.

## Examples
```text
Input:
  INF  -1   0  INF
  INF INF INF  -1
  INF  -1 INF  -1
    0  -1 INF INF

Output:
    3  -1   0   1
    2   2   1  -1
    1  -1   2  -1
    0  -1   3   4
```

```text
Input:  rooms = [[-1]]
Output: [[-1]]
```

## Constraints
- `m == rooms.length`
- `n == rooms[i].length`
- `1 <= m, n <= 250`
- `rooms[i][j]` is `-1`, `0`, or `2^31 - 1`
"""

from typing import List
from collections import deque

INF = 2147483647


class Solution:
    def wallsAndGates_brute(self, rooms: List[List[int]]) -> None:
        # O((m*n)^2) time, O(m*n) space — BFS from each empty room
        rows, cols = len(rooms), len(rooms[0])

        def bfs(sr, sc):
            q = deque([(sr, sc, 0)])
            visited = {(sr, sc)}
            while q:
                r, c, dist = q.popleft()
                if rooms[r][c] == 0:
                    return dist
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and rooms[nr][nc] != -1:
                        visited.add((nr, nc))
                        q.append((nr, nc, dist+1))
            return INF

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == INF:
                    rooms[r][c] = bfs(r, c)

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        # Multi-source BFS from all gates (0 cells) simultaneously
        # Each BFS level increments distance; INF cells get updated with shortest distance
        # O(m*n) time, O(m*n) space — multi-source BFS from all gates simultaneously
        rows, cols = len(rooms), len(rooms[0])
        q = deque((r, c) for r in range(rows) for c in range(cols) if rooms[r][c] == 0)
        while q:
            r, c = q.popleft()
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))


if __name__ == '__main__':
    import copy
    s = Solution()
    rooms = [[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]
    expected = [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

    r1 = copy.deepcopy(rooms)
    s.wallsAndGates(r1)
    assert r1 == expected

    r2 = copy.deepcopy(rooms)
    s.wallsAndGates_brute(r2)
    assert r2 == expected

    print("All tests passed.")
