"""
# LC 802: Find Eventual Safe States

Return, in ascending order, all nodes of a directed graph from which every
path eventually leads to a terminal node (no cycle is reachable).

## Examples
```text
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
```

## Constraints
- A node with no outgoing edges is always safe (terminal).
- If all nodes form one cycle, return `[]`.
- Handle disconnected components.
"""
from typing import List
from collections import deque

class Solution:
    # Approach 1: DFS with 3-color marking (0=unvisited, 1=in-stack, 2=safe)
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n  # 0=unvisited, 1=visiting(in cycle path), 2=safe

        def dfs(node) -> bool:
            if state[node] == 1: return False  # back edge = cycle
            if state[node] == 2: return True   # already confirmed safe
            state[node] = 1  # mark as being visited
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False  # neighbor leads to cycle
            state[node] = 2  # all neighbors safe, mark safe
            return True

        return [i for i in range(n) if dfs(i)]

    # Approach 2: Reverse graph + topological sort (Kahn's)
    def eventualSafeNodes_topo(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        rev = [[] for _ in range(n)]
        out_degree = [0] * n

        for u in range(n):
            for v in graph[u]:
                rev[v].append(u)  # reverse edge
            out_degree[u] = len(graph[u])

        # nodes with out_degree 0 are terminal (safe)
        queue = deque(i for i in range(n) if out_degree[i] == 0)
        safe = set()

        while queue:
            node = queue.popleft()
            safe.add(node)
            for parent in rev[node]:
                out_degree[parent] -= 1
                if out_degree[parent] == 0:
                    queue.append(parent)

        return sorted(safe)


if __name__ == "__main__":
    s = Solution()
    assert s.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]) == [2,4,5,6]
    assert s.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]) == [4]
    assert s.eventualSafeNodes_topo([[1,2],[2,3],[5],[0],[5],[],[]]) == [2,4,5,6]
    assert s.eventualSafeNodes_topo([[1,2,3,4],[1,2],[3,4],[0,4],[]]) == [4]
    print("All tests passed.")
