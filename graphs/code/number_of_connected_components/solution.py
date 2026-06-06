from typing import List


class Solution:
    """
    ## 323. Number of Connected Components in an Undirected Graph

    You have `n` nodes labeled from `0` to `n - 1` and a list of undirected edges.
    Write a function to find the number of connected components in the graph.

    ### Examples

    ```text
    Input:  n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2

    Input:  n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
    Output: 1
    ```

    ### Constraints

    - `1 <= n <= 2000`
    - `1 <= edges.length <= 5000`
    - `edges[i].length == 2`
    - `0 <= ai, bi < n`
    - `ai != bi`
    - No repeated edges.
    """

    def countComponents_dfs(self, n: int, edges: List[List[int]]) -> int:
        # O(V+E) time, O(V+E) space
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n

        def dfs(node: int) -> None:
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union-Find or DFS: count distinct connected components
        # O(V+E) time, O(V) space — Union-Find
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

        components = n
        for a, b in edges:
            if union(a, b):
                components -= 1
        return components


if __name__ == '__main__':
    s = Solution()
    assert s.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert s.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
    assert s.countComponents(3, []) == 3

    assert s.countComponents_dfs(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert s.countComponents_dfs(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
    print("All tests passed.")
