"""
# LC 785: Is Graph Bipartite?

A graph is bipartite if its nodes can be split into two groups such that
every edge connects nodes from different groups (i.e., it is 2-colorable and
contains no odd-length cycles). Return whether the given adjacency-list graph
is bipartite.

## Examples
```text
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: True

Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: False
```

## Constraints
- Disconnected components must each be checked independently.
- A self-loop makes a graph non-bipartite.
- An empty graph or a single node is bipartite.
"""
from typing import List
from collections import deque

class Solution:
    # Approach 1: BFS coloring - try to 2-color the graph
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1 = unvisited, 0 and 1 are the two colors

        for start in range(n):  # handle disconnected components
            if color[start] != -1:
                continue
            queue = deque([start])
            color[start] = 0
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]  # assign opposite color
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False  # same color on both ends = odd cycle
        return True

    # Approach 2: DFS coloring
    def isBipartite_dfs(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(node, c):
            color[node] = c
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - c):
                        return False
                elif color[neighbor] == c:
                    return False  # conflict
            return True

        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isBipartite([[1,3],[0,2],[1,3],[0,2]]) is True
    assert s.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]) is False
    assert s.isBipartite_dfs([[1,3],[0,2],[1,3],[0,2]]) is True
    assert s.isBipartite_dfs([[1,2,3],[0,2],[0,1,3],[0,2]]) is False
    print("All tests passed.")
