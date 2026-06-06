from typing import List
from collections import deque
import heapq


class Solution:
    """
    ## 1631. Path With Minimum Effort

    You are a hiker preparing for an upcoming hike. You are given `heights`, a 2D array of size
    `rows x columns`, where `heights[row][col]` represents the height of cell `(row, col)`.
    You are situated in the top-left cell, `(0, 0)`, and you hope to travel to the bottom-right
    cell, `(rows-1, columns-1)`. You can move **up**, **down**, **left**, or **right**, and you
    wish to find the route that requires the minimum **effort**.

    The **effort** of a route is the maximum absolute difference in heights between two consecutive
    cells of the route.

    Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

    ---

    ### Examples

    ```text
    Input:  heights = [[1,2,2],[3,8,2],[5,3,5]]
    Output: 2
    Explanation: The route [1,3,5,3,5] has a maximum absolute difference of 2.

    Input:  heights = [[1,2,3],[3,8,4],[5,3,5]]
    Output: 1
    Explanation: The route [1,2,3,4,5] has a maximum absolute difference of 1.

    Input:  heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    Output: 0
    ```

    ---

    ### Constraints

    - `rows == heights.length`
    - `cols == heights[i].length`
    - `1 <= rows, cols <= 100`
    - `1 <= heights[i][j] <= 10^6`
    """

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Dijkstra: minimize the maximum absolute difference along the path
        # Priority queue stores (max_effort_so_far, row, col)
        # O(m*n*log(10^6)) — binary search on effort, BFS to validate
        rows, cols = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def can_reach(effort: int) -> bool:
            visited = [[False] * cols for _ in range(rows)]
            q = deque([(0, 0)])
            visited[0][0] = True
            while q:
                r, c = q.popleft()
                if r == rows - 1 and c == cols - 1:
                    return True
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                        if abs(heights[nr][nc] - heights[r][c]) <= effort:
                            visited[nr][nc] = True
                            q.append((nr, nc))
            return False

        lo, hi = 0, 10**6 - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if can_reach(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def minimumEffortPath_dijkstra(self, heights: List[List[int]]) -> int:
        # O(m*n*log(m*n)) — Dijkstra treating effort as edge weight
        rows, cols = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0
        heap = [(0, 0, 0)]  # (effort, row, col)

        while heap:
            e, r, c = heapq.heappop(heap)
            if r == rows - 1 and c == cols - 1:
                return e
            if e > effort[r][c]:
                continue
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_e = max(e, abs(heights[nr][nc] - heights[r][c]))
                    if new_e < effort[nr][nc]:
                        effort[nr][nc] = new_e
                        heapq.heappush(heap, (new_e, nr, nc))
        return effort[rows - 1][cols - 1]


if __name__ == '__main__':
    s = Solution()
    assert s.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
    assert s.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1
    assert s.minimumEffortPath([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]) == 0

    assert s.minimumEffortPath_dijkstra([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
    assert s.minimumEffortPath_dijkstra([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1

    print("All tests passed.")
