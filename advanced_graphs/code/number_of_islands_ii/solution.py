"""
# LC 305: Number of Islands II

Given an m x n grid, add land cells one at a time from `positions`. After each
addition, return the current number of islands (4-directionally connected).

## Examples
```text
Input: m=3, n=3, positions=[[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
# (0,1) merges with (0,0); the last two additions are isolated.
```

## Constraints
- Online Union-Find with lazy initialization — O(k * alpha(mn))
- Encode a cell (r,c) as r*n + c
- Duplicate positions leave the island count unchanged
"""
from typing import List

class Solution:
    # Union-Find with lazy initialization - add land cells one by one
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}
        count = 0

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal count
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            count -= 1  # merging two islands

        result = []
        for r, c in positions:
            cell = r * n + c
            if cell in parent:  # duplicate position
                result.append(count)
                continue

            parent[cell] = cell  # new island
            rank[cell] = 0
            count += 1

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                neighbor = nr * n + nc
                if 0 <= nr < m and 0 <= nc < n and neighbor in parent:
                    union(cell, neighbor)  # merge with adjacent land

            result.append(count)
        return result


if __name__ == "__main__":
    sol = Solution()

    # Example from README
    assert sol.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]) == [1, 1, 2, 3]

    # LC classic example
    assert sol.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]) == [1, 1, 2, 3]

    # Duplicate position leaves count unchanged
    assert sol.numIslands2(2, 2, [[0, 0], [0, 0], [1, 1]]) == [1, 1, 2]

    # Chain that eventually merges into one island
    assert sol.numIslands2(1, 3, [[0, 0], [0, 2], [0, 1]]) == [1, 2, 1]

    print("All tests passed.")
