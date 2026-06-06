from typing import List
from collections import deque


class Solution:
    """
    ## 310. Minimum Height Trees

    A tree is an undirected graph in which any two vertices are connected by exactly
    one path. Given a tree of `n` nodes labeled from `0` to `n - 1`, and an array of
    `n - 1` edges, find all the nodes that can be the root of a Minimum Height Tree (MHT).

    Return a list of all MHT root labels. You may return the answer in any order.

    ### Examples

    ```text
    Input:  n = 4, edges = [[1,0],[1,2],[1,3]]
    Output: [1]

    Input:  n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    Output: [3,4]

    Input:  n = 1, edges = []
    Output: [0]
    ```

    ### Constraints

    - `1 <= n <= 2 * 10^4`
    - `edges.length == n - 1`
    - `0 <= ai, bi < n`
    - `ai != bi`
    - All pairs `(ai, bi)` are distinct.
    - The given input is guaranteed to be a tree.
    """

    def findMinHeightTrees_brute(self, n: int, edges: List[List[int]]) -> List[int]:
        # O(V^2) time, O(V+E) space — BFS from each node
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def bfs_height(root: int) -> int:
            visited = {root}
            queue = deque([root])
            height = 0
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
                height += 1
            return height

        min_h = float('inf')
        heights = []
        for i in range(n):
            h = bfs_height(i)
            heights.append(h)
            min_h = min(min_h, h)
        return [i for i, h in enumerate(heights) if h == min_h]

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Iteratively remove leaf nodes (degree 1) layer by layer
        # The remaining 1 or 2 nodes are the roots of minimum height trees
        # O(V+E) time, O(V+E) space — iterative leaf removal
        if n == 1:
            return [0]
        graph = [set() for _ in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leaves = deque(i for i in range(n) if len(graph[i]) == 1)
        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = deque()
            for leaf in leaves:
                nei = next(iter(graph[leaf]))
                graph[nei].remove(leaf)
                if len(graph[nei]) == 1:
                    new_leaves.append(nei)
            leaves = new_leaves
        return list(leaves)


if __name__ == '__main__':
    s = Solution()
    assert s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]) == [1]
    assert sorted(s.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])) == [3, 4]
    assert s.findMinHeightTrees(1, []) == [0]

    assert s.findMinHeightTrees_brute(4, [[1, 0], [1, 2], [1, 3]]) == [1]
    assert sorted(s.findMinHeightTrees_brute(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])) == [3, 4]
    print("All tests passed.")
