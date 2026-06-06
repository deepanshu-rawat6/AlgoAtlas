"""
# 417. Pacific Atlantic Water Flow

## Problem
There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic
Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean
touches the island's right and bottom edges.

Water can flow to a neighboring cell (north, south, east, west) if the neighboring cell's
height is less than or equal to the current cell's height. Water can flow from any cell
adjacent to an ocean into that ocean.

Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.

## Examples
```text
Input:  heights = [[1,2,2,3,5],
                   [3,2,3,4,4],
                   [2,4,5,3,1],
                   [6,7,1,4,5],
                   [5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

```text
Input:  heights = [[1]]
Output: [[0,0]]
```

## Constraints
- `m == heights.length`
- `n == heights[i].length`
- `1 <= m, n <= 200`
- `0 <= heights[i][j] <= 10^5`
"""

from typing import List
from collections import deque


class Solution:
    def pacificAtlantic_brute(self, heights: List[List[int]]) -> List[List[int]]:
        # O((m*n)^2) time, O(m*n) space — check each cell independently
        rows, cols = len(heights), len(heights[0])

        def can_reach(r, c, ocean):
            visited = set()
            q = deque([(r, c)])
            visited.add((r, c))
            while q:
                cr, cc = q.popleft()
                if ocean == 'P' and (cr == 0 or cc == 0):
                    return True
                if ocean == 'A' and (cr == rows-1 or cc == cols-1):
                    return True
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = cr+dr, cc+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and heights[nr][nc] <= heights[cr][cc]:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return False

        return [[r, c] for r in range(rows) for c in range(cols)
                if can_reach(r, c, 'P') and can_reach(r, c, 'A')]

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # BFS/DFS from Pacific border cells and Atlantic border cells separately
        # Cells reachable from both oceans are the answer
        # Flow is reversed: water flows from ocean inward (uphill is ok)
        # O(m*n) time, O(m*n) space — reverse BFS from ocean borders inward
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            q = deque(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return visited

        pacific  = bfs([(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)])
        atlantic = bfs([(r, cols-1) for r in range(rows)] + [(rows-1, c) for c in range(cols)])
        return sorted([r, c] for r, c in pacific & atlantic)


if __name__ == '__main__':
    s = Solution()
    h = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    expected = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    assert s.pacificAtlantic(h) == expected
    assert s.pacificAtlantic([[1]]) == [[0,0]]
    print("All tests passed.")
