from typing import List
from collections import deque


class Solution:
    """
    ## 261. Graph Valid Tree

    You have `n` nodes labeled from `0` to `n - 1` and a list of undirected edges.
    Write a function to check whether these edges make up a valid tree.

    A valid tree must be connected and contain no cycles.

    ### Examples

    ```text
    Input:  n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: true

    Input:  n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    Output: false
    ```

    ### Constraints

    - `1 <= n <= 2000`
    - `0 <= edges.length <= 5000`
    - `edges[i].length == 2`
    - `0 <= ai, bi < n`
    - `ai != bi`
    - No self-loops or repeated edges.
    """

    def validTree_bfs(self, n: int, edges: List[List[int]]) -> bool:
        # O(V+E) time, O(V+E) space
        if len(edges) != n - 1:
            return False
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        queue = deque([0])
        visited.add(0)
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        return len(visited) == n

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree has exactly n-1 edges and is fully connected (no cycles)
        # Union-Find: if any edge connects already-connected nodes, it's a cycle
        # O(V+E) time, O(V) space — Union-Find
        if len(edges) != n - 1:
            return False
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> bool:
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        return all(union(a, b) for a, b in edges)


if __name__ == '__main__':
    s = Solution()
    assert s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True
    assert s.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False
    assert s.validTree(1, []) is True
    assert s.validTree(4, [[0, 1], [2, 3]]) is False

    assert s.validTree_bfs(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True
    assert s.validTree_bfs(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False
    print("All tests passed.")
