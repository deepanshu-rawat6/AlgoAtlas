from typing import List


class Solution:
    """
    ## 684. Redundant Connection

    In this problem, a tree is an undirected graph that is connected and has no cycles.

    You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`,
    with one additional edge added. The added edge has two different vertices chosen from
    `1` to `n`, and was not an edge that already existed.

    Return an edge that can be removed so that the resulting graph is a tree. If there are
    multiple answers, return the answer that occurs last in the input.

    ### Examples

    ```text
    Input:  edges = [[1,2],[1,3],[2,3]]
    Output: [2,3]

    Input:  edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    Output: [1,4]
    ```

    ### Constraints

    - `n == edges.length`
    - `3 <= n <= 1000`
    - `edges[i].length == 2`
    - `1 <= ai, bi <= n`
    - `ai != bi`
    - No repeated edges.
    - The given graph is connected.
    """

    def findRedundantConnection_dfs(self, edges: List[List[int]]) -> List[int]:
        # O(V*E) time, O(V+E) space
        n = len(edges)
        graph = [[] for _ in range(n + 1)]

        def has_path(src: int, dst: int, visited: set) -> bool:
            if src == dst:
                return True
            visited.add(src)
            for nei in graph[src]:
                if nei not in visited and has_path(nei, dst, visited):
                    return True
            return False

        for a, b in edges:
            if has_path(a, b, set()):
                return [a, b]
            graph[a].append(b)
            graph[b].append(a)
        return []

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union-Find: process edges in order; the first edge that connects already-connected nodes is redundant
        # O(V*alpha(V)) ≈ O(V) time, O(V) space — Union-Find
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

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

        for a, b in edges:
            if not union(a, b):
                return [a, b]
        return []


if __name__ == '__main__':
    s = Solution()
    assert s.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert s.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]

    assert s.findRedundantConnection_dfs([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert s.findRedundantConnection_dfs([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
    print("All tests passed.")
