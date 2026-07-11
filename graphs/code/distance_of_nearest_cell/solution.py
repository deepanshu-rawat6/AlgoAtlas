"""
# LC 542: 01 Matrix (Distance of Nearest 0)

For each cell in a binary matrix, find the distance to the nearest `0`, where
distance is the number of 4-directional steps.

## Examples
```text
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
```

## Constraints
- A cell that is already `0` has distance 0.
- Use multi-source BFS from all `0` cells simultaneously.
- At least one `0` is present in the matrix.
"""
from typing import List
from collections import deque

class Solution:
    # Multi-source BFS: start from ALL 0s simultaneously, expand outward
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()

        # initialize BFS with all 0-cells at distance 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))

        # BFS expands layer by layer - first time we reach a 1-cell is shortest distance
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if dist[nr][nc] > dist[r][c] + 1:
                        dist[nr][nc] = dist[r][c] + 1
                        queue.append((nr, nc))

        return dist


if __name__ == "__main__":
    s = Solution()
    assert s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0,0,0],[0,1,0],[1,2,1]]
    assert s.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]) == [[0,0,0],[0,1,0],[0,0,0]]
    print("All tests passed.")
