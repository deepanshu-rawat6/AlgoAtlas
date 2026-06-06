"""
# M Coloring Problem

Given an undirected graph and m colors, determine if the graph can be colored
with at most m colors such that no two adjacent vertices share the same color.

## Examples

```text
Input:  n=4, edges=[[0,1],[1,2],[2,3],[3,0],[0,2]], m=3
Output: True

Input:  n=3, edges=[[0,1],[1,2],[0,2]], m=2
Output: False (triangle needs 3 colors)
```

## Constraints
- 1 <= n <= 20
- 1 <= m <= n
"""
from typing import List


class Solution:
    def graphColoring(self, n: int, edges: List[List[int]], m: int) -> bool:
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # color[i] = color assigned to node i (0 = uncolored)
        color = [0] * n

        def is_safe(node, c):
            # Check if assigning color c to node is valid
            # No adjacent node should have the same color
            for neighbor in graph[node]:
                if color[neighbor] == c:
                    return False
            return True

        def backtrack(node):
            # All nodes colored successfully
            if node == n:
                return True

            # Try each color 1..m for current node
            for c in range(1, m + 1):
                if is_safe(node, c):
                    color[node] = c
                    if backtrack(node + 1):
                        return True
                    color[node] = 0  # Backtrack
            return False

        return backtrack(0)


if __name__ == "__main__":
    sol = Solution()
    print(sol.graphColoring(4, [[0,1],[1,2],[2,3],[3,0],[0,2]], 3))  # True
    print(sol.graphColoring(3, [[0,1],[1,2],[0,2]], 2))              # False
