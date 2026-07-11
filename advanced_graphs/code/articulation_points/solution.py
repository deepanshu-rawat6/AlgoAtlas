"""
# Articulation Points (Tarjan's Algorithm)

Find all vertices whose removal increases the number of connected components
of an undirected graph.

## Examples
```text
Input: n=5, edges=[[0,1],[1,2],[2,0],[1,3],[3,4]]
Output: [1,3]
# Removing node 1 disconnects {0,2} from {3,4}; removing node 3 disconnects {4}.
```

## Constraints
- Non-root node u is an articulation point if some child v has low[v] >= disc[u]
- Root node is an articulation point if it has 2+ children in the DFS tree
- Graph may be disconnected; run DFS from every unvisited node
"""
from typing import List

class Solution:
    # Tarjan's articulation points:
    # node u is AP if: (1) root with 2+ children, OR (2) non-root with low[v] >= disc[u]
    def articulationPoints(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * n
        low = [0] * n
        timer = [0]
        is_ap = [False] * n

        def dfs(node, parent):
            disc[node] = low[node] = timer[0]
            timer[0] += 1
            children = 0
            for neighbor in graph[node]:
                if disc[neighbor] == -1:
                    children += 1
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    # non-root AP condition
                    if parent != -1 and low[neighbor] >= disc[node]:
                        is_ap[node] = True
                    # root AP condition: root is AP if it has 2+ children in DFS tree
                    if parent == -1 and children > 1:
                        is_ap[node] = True
                elif neighbor != parent:
                    low[node] = min(low[node], disc[neighbor])

        for i in range(n):
            if disc[i] == -1:
                dfs(i, -1)

        return [i for i in range(n) if is_ap[i]]


if __name__ == "__main__":
    sol = Solution()

    # Example from README: node 1 and node 3 are articulation points
    assert sol.articulationPoints(5, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]) == [1, 3]

    # Simple bridge: 0-1-2 in a line, both endpoints' middle is AP
    assert sol.articulationPoints(3, [[0, 1], [1, 2]]) == [1]

    # Triangle (cycle) → no articulation points
    assert sol.articulationPoints(3, [[0, 1], [1, 2], [2, 0]]) == []

    # Single node, no edges → no articulation points
    assert sol.articulationPoints(1, []) == []

    print("All tests passed.")
