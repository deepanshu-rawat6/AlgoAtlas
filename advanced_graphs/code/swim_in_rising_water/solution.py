from typing import List
from collections import deque
import heapq


class Solution:
    """
    ## 778. Swim in Rising Water

    You are given an `n x n` integer matrix `grid` where each value `grid[i][j]` represents the
    elevation at that point `(i, j)`.

    The rain starts to fall. At time `t`, the depth of the water everywhere is `t`. You can swim
    from a square to another 4-directionally adjacent square if and only if the elevation of both
    squares individually are at most `t`. You can swim infinite distances in zero time. Of course,
    you must stay within the boundaries of the grid during your swim.

    Return the least time until you can reach the bottom-right square `(n-1, n-1)` if you start
    at the top-left square `(0, 0)`.

    ---

    ### Examples

    ```text
    Input:  grid = [[0,2],[1,3]]
    Output: 3
    Explanation: At time 3, we can swim from (0,0) -> (0,1) -> (1,1).

    Input:  grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    Output: 16
    ```

    ---

    ### Constraints

    - `n == grid.length == grid[i].length`
    - `1 <= n <= 50`
    - `0 <= grid[i][j] < n^2`
    - Each value `grid[i][j]` is unique.
    """

    def swimInWater(self, grid: List[List[int]]) -> int:
        # Dijkstra variant: minimize the maximum elevation on the path to (n-1, n-1)
        # Priority queue stores (max_elevation_so_far, row, col)
        # O(n^2 log n) — binary search on time t, BFS to check reachability
        n = len(grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def can_reach(t: int) -> bool:
            if grid[0][0] > t:
                return False
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            q = deque([(0, 0)])
            while q:
                r, c = q.popleft()
                if r == n - 1 and c == n - 1:
                    return True
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] <= t:
                        visited[nr][nc] = True
                        q.append((nr, nc))
            return False

        lo, hi = grid[0][0], n * n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if can_reach(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def swimInWater_dijkstra(self, grid: List[List[int]]) -> int:
        # O(n^2 log n) — min-heap treating max elevation on path as cost
        n = len(grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]

        while heap:
            t, r, c = heapq.heappop(heap)
            if visited[r][c]:
                continue
            visited[r][c] = True
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
        return -1


if __name__ == '__main__':
    s = Solution()
    assert s.swimInWater([[0, 2], [1, 3]]) == 3
    assert s.swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5],
                          [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]) == 16

    assert s.swimInWater_dijkstra([[0, 2], [1, 3]]) == 3
    assert s.swimInWater_dijkstra([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5],
                                   [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]) == 16

    print("All tests passed.")
