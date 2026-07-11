"""
# Kosaraju's Algorithm — Strongly Connected Components

Find all Strongly Connected Components (SCCs) in a directed graph. An SCC is a
maximal set of nodes where every node is reachable from every other node.

## Examples
```text
Input: n=5, edges=[[0,1],[1,2],[2,0],[1,3],[3,4]]
Output: [[0,1,2],[3],[4]]
# 0->1->2->0 form a cycle (one SCC); 3 and 4 are singletons.
```

## Constraints
- Two-pass DFS — O(V+E)
- Pass 1 records finish order on the original graph
- Pass 2 runs DFS on the transposed graph in reverse finish order
"""
from typing import List
from collections import defaultdict

class Solution:
    # Kosaraju's: 1) DFS on original, push to stack in finish order
    #             2) Transpose graph  3) DFS in reverse finish order on transposed
    def findSCCs(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        rev_graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            rev_graph[v].append(u)

        visited = [False] * n
        stack = []

        def dfs1(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs1(neighbor)
            stack.append(node)  # push after all descendants processed

        def dfs2(node, component):
            visited[node] = True
            component.append(node)
            for neighbor in rev_graph[node]:
                if not visited[neighbor]:
                    dfs2(neighbor, component)

        # Pass 1: fill stack with finish order
        for i in range(n):
            if not visited[i]:
                dfs1(i)

        # Pass 2: process in reverse finish order on transposed graph
        visited = [False] * n
        sccs = []
        while stack:
            node = stack.pop()
            if not visited[node]:
                component = []
                dfs2(node, component)
                sccs.append(sorted(component))

        return sccs


if __name__ == "__main__":
    sol = Solution()

    # SCC order in the outer list is not deterministic → compare sorted list of components
    assert sorted(sol.findSCCs(5, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]])) == [[0, 1, 2], [3], [4]]

    # Single cycle over all nodes → one SCC
    assert sorted(sol.findSCCs(3, [[0, 1], [1, 2], [2, 0]])) == [[0, 1, 2]]

    # DAG → every node is its own SCC
    assert sorted(sol.findSCCs(3, [[0, 1], [1, 2]])) == [[0], [1], [2]]

    print("All tests passed.")
