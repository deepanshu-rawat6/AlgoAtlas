from typing import List
import heapq


class Solution:
    """
    ## 1584. Min Cost to Connect All Points

    You are given an array `points` representing integer coordinates of some points on a 2D plane,
    where `points[i] = [xi, yi]`.

    The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the **Manhattan distance**
    between them: `|xi - xj| + |yi - yj|`.

    Return the minimum cost to make all points connected. All points are connected if there is
    exactly one simple path between any two points.

    ---

    ### Examples

    ```text
    Input:  points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    Output: 20

    Input:  points = [[3,12],[-2,5],[-4,1]]
    Output: 18
    ```

    ---

    ### Constraints

    - `1 <= points.length <= 1000`
    - `-10^6 <= xi, yi <= 10^6`
    - All pairs `(xi, yi)` are distinct.
    """

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's MST: start from any node, greedily add cheapest edge to unvisited node
        # Manhattan distance is the edge weight between two points
        # O(n^2) — Prim's algorithm with visited set
        n = len(points)
        visited = set()
        heap = [(0, 0)]  # (cost, index)
        total = 0

        while len(visited) < n:
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue
            visited.add(i)
            total += cost
            for j in range(n):
                if j not in visited:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(heap, (dist, j))

        return total

    def minCostConnectPoints_kruskal(self, points: List[List[int]]) -> int:
        # O(n^2 log n) — Kruskal's with Union-Find on all edges
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        edges.sort()

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

        total, edges_used = 0, 0
        for dist, i, j in edges:
            if union(i, j):
                total += dist
                edges_used += 1
                if edges_used == n - 1:
                    break
        return total


if __name__ == '__main__':
    s = Solution()
    assert s.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    assert s.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18
    assert s.minCostConnectPoints([[0, 0]]) == 0

    assert s.minCostConnectPoints_kruskal([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    assert s.minCostConnectPoints_kruskal([[3, 12], [-2, 5], [-4, 1]]) == 18

    print("All tests passed.")
