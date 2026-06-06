from typing import List


class Solution:
    """
    ## 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

    Given a weighted undirected connected graph with `n` vertices numbered from `0` to `n - 1`,
    and an array `edges` where `edges[i] = [ai, bi, weighti]` represents a bidirectional and
    weighted edge between nodes `ai` and `bi`.

    A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices
    without cycles and with the minimum possible total edge weight.

    Find all the **critical** and **pseudo-critical** edges in the given graph's MST.

    - An MST edge whose deletion from the graph would cause the MST weight to increase is called
      a **critical edge**.
    - A **pseudo-critical edge** is one that can appear in some MSTs but not all.

    Return a list of two lists: the first list contains the indices of all critical edges, and
    the second list contains the indices of all pseudo-critical edges.

    ---

    ### Examples

    ```text
    Input:  n=5, edges=[[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
    Output: [[0,1],[2,3,4,5]]

    Input:  n=4, edges=[[0,1,1],[1,2,1],[0,2,1],[2,3,1]]
    Output: [[3],[0,1,2]]
    ```

    ---

    ### Constraints

    - `2 <= n <= 100`
    - `1 <= edges.length <= min(200, n * (n - 1) / 2)`
    - `edges[i].length == 3`
    - `0 <= ai < bi < n`
    - `1 <= weighti <= 1000`
    - All pairs `(ai, bi)` are distinct.
    """

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Critical edge: removing it increases MST weight
        # Pseudo-critical: forcing it in doesn't increase MST weight
        # Use Kruskal's MST as baseline; test each edge by exclusion/inclusion
        # O(E^2 * alpha(n)) — Kruskal's with per-edge inclusion/exclusion to find base MST weight
        indexed = [(w, u, v, i) for i, (u, v, w) in enumerate(edges)]
        indexed.sort()

        def make_uf():
            parent = list(range(n))
            rank = [0] * n
            return parent, rank

        def find(parent, x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(parent, rank, x, y):
            px, py = find(parent, x), find(parent, y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        def kruskal(skip_idx=-1, force_idx=-1):
            parent, rank = make_uf()
            weight = 0
            cnt = 0
            if force_idx != -1:
                w, u, v, _ = indexed[force_idx]
                union(parent, rank, u, v)
                weight += w
                cnt += 1
            for i, (w, u, v, orig) in enumerate(indexed):
                if i == skip_idx:
                    continue
                if union(parent, rank, u, v):
                    weight += w
                    cnt += 1
            return weight if cnt == n - 1 else float('inf')

        base = kruskal()
        critical, pseudo = [], []

        for i in range(len(indexed)):
            # Critical: removing raises MST weight
            if kruskal(skip_idx=i) > base:
                critical.append(indexed[i][3])
            # Pseudo-critical: forcing inclusion keeps same MST weight
            elif kruskal(force_idx=i) == base:
                pseudo.append(indexed[i][3])

        return [sorted(critical), sorted(pseudo)]


if __name__ == '__main__':
    s = Solution()
    res = s.findCriticalAndPseudoCriticalEdges(
        5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
    )
    assert res == [[0, 1], [2, 3, 4, 5]], res

    res2 = s.findCriticalAndPseudoCriticalEdges(4, [[0,1,1],[1,2,1],[0,2,1],[2,3,1]])
    assert res2 == [[3], [0, 1, 2]], res2

    print("All tests passed.")
