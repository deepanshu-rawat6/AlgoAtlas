from typing import List
# from collections import deque

class Solution:
    """
    **LC 994: Rotting Oranges**

    Given an `m x n` grid where each cell has one of three values:
    * `0` — empty cell
    * `1` — fresh orange
    * `2` — rotten orange

    Every minute, any fresh orange that is **4-directionally adjacent** to a rotten
    orange becomes rotten.

    Return the minimum number of minutes until no cell has a fresh orange.
    Return `-1` if it is impossible.

    Example 1:
    ```text
    Input:  grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4
    ```

    Example 2:
    ```text
    Input:  grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange at (2,0) is never reachable — rotting only happens 4-directionally.
    ```

    Example 3:
    ```text
    Input:  grid = [[0,2]]
    Output: 0
    Explanation: No fresh oranges exist at minute 0.
    ```

    **Constraints:**
    * `m == grid.length`
    * `n == grid[i].length`
    * `1 <= m, n <= 10`
    * `grid[i][j]` is `0`, `1`, or `2`
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Multi-source BFS from all initially rotten oranges simultaneously
        # Each BFS level = 1 minute; count fresh oranges; return -1 if any remain
        # your code here
        pass


if __name__ == "__main__":
    sol = Solution()

    # Example 1: expected 4
    print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))

    # Example 2: expected -1
    print(sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))

    # Example 3: expected 0
    print(sol.orangesRotting([[0, 2]]))
