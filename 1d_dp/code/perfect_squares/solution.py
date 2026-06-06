"""
LC 279 — Perfect Squares
==========================

Given an integer `n`, return the least number of perfect square numbers that sum to `n`.
A perfect square is an integer that is the square of an integer (1, 4, 9, 16, ...).

Examples
--------
```text
Input:  n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4

Input:  n = 13
Output: 2
Explanation: 13 = 4 + 9
```

Constraints
-----------
- 1 <= n <= 10^4
"""

from collections import deque
import math


class Solution:
    # Approach 1: DP — O(n * sqrt(n)) time, O(n) space
    def numSquares(self, n: int) -> int:
        # dp[i] = min squares summing to i; try all perfect squares <= i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        squares = [i * i for i in range(1, int(math.isqrt(n)) + 1)]
        for i in range(1, n + 1):
            for sq in squares:
                if sq > i:
                    break
                dp[i] = min(dp[i], dp[i - sq] + 1)
        return dp[n]

    # Approach 2: BFS (level = number of squares used) — O(n * sqrt(n)) time, O(n) space
    def numSquares_bfs(self, n: int) -> int:
        # BFS levels = number of squares used; find shortest path from n to 0
        squares = [i * i for i in range(1, int(math.isqrt(n)) + 1)]
        visited = {n}
        queue = deque([n])
        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for sq in squares:
                    nxt = node - sq
                    if nxt == 0:
                        return steps
                    if nxt > 0 and nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
        return steps


if __name__ == "__main__":
    sol = Solution()
    assert sol.numSquares(12) == 3
    assert sol.numSquares(13) == 2
    assert sol.numSquares(1) == 1
    assert sol.numSquares_bfs(12) == 3
    assert sol.numSquares_bfs(13) == 2
    print("All tests passed.")
