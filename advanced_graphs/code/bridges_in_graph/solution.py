"""
# LC 1192: Critical Connections in a Network (Bridges)

Find all edges whose removal increases the number of connected components
(bridges) of an undirected graph.

## Examples
```text
Input: n=4, connections=[[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
# 0-1-2 form a cycle (no bridge among them); edge (1,3) is a bridge.
```

## Constraints
- Edge (u,v) is a bridge if low[v] > disc[u]
- Pass parent to avoid treating the tree edge back to parent as a back edge
- Graph may be disconnected; run DFS from every unvisited node
"""
from typing import List

class Solution:
    # Tarjan's bridge finding: edge (u,v) is bridge if low[v] > disc[u]
    # low[v] = min discovery time reachable from subtree of v (excluding parent edge)
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * n   # discovery time
        low = [0] * n     # lowest disc reachable
        timer = [0]
        bridges = []

        def dfs(node, parent):
            disc[node] = low[node] = timer[0]
            timer[0] += 1
            for neighbor in graph[node]:
                if disc[neighbor] == -1:  # unvisited
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > disc[node]:
                        bridges.append([node, neighbor])  # bridge found
                elif neighbor != parent:  # back edge (not to direct parent)
                    low[node] = min(low[node], disc[neighbor])

        for i in range(n):
            if disc[i] == -1:
                dfs(i, -1)

        return bridges


if __name__ == "__main__":
    sol = Solution()

    def norm(bridges):
        # normalize: sort each edge, then sort the list (order not deterministic)
        return sorted(sorted(edge) for edge in bridges)

    # Example from README: only edge (1,3) is a bridge
    assert norm(sol.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]])) == [[1, 3]]

    # A path 0-1-2-3: every edge is a bridge
    assert norm(sol.criticalConnections(4, [[0, 1], [1, 2], [2, 3]])) == [[0, 1], [1, 2], [2, 3]]

    # Triangle cycle: no bridges
    assert norm(sol.criticalConnections(3, [[0, 1], [1, 2], [2, 0]])) == []

    print("All tests passed.")
