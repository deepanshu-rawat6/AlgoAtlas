"""
LC 1406 — Stone Game III
=========================

Alice and Bob take turns, with Alice going first. On each turn, a player can take
1, 2, or 3 stones from the front of the row. The player with the most stones wins.

Return "Alice" if Alice wins, "Bob" if Bob wins, or "Tie" if they end with the same score.
Both players play optimally.

Examples
--------
```text
Input:  stoneValue = [1, 2, 3, 7]
Output: "Bob"
Explanation: Alice takes 1, 2, or 3 stones; Bob always wins.

Input:  stoneValue = [1, 2, 3, -9]
Output: "Alice"

Input:  stoneValue = [1, 2, 3, 6]
Output: "Tie"
```

Constraints
-----------
- 1 <= stoneValue.length <= 5 * 10^4
- -1000 <= stoneValue[i] <= 1000
"""

from typing import List
from functools import lru_cache


class Solution:
    # Approach 1: Top-down memoization — O(n) time, O(n) space
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # dp(i) = max score advantage current player can get from index i
        # Try taking 1, 2, or 3 stones; subtract opponent's optimal play
        n = len(stoneValue)

        @lru_cache(maxsize=None)
        def dp(i: int) -> int:
            """Returns max score advantage current player can achieve from index i."""
            if i >= n:
                return 0
            best = float('-inf')
            total = 0
            for k in range(1, 4):
                if i + k - 1 < n:
                    total += stoneValue[i + k - 1]
                    best = max(best, total - dp(i + k))
            return best

        score = dp(0)
        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        return "Tie"

    # Approach 2: Bottom-up DP — O(n) time, O(n) space
    def stoneGameIII_dp(self, stoneValue: List[int]) -> str:
        # Bottom-up: dp[i] = max(sum of k stones - dp[i+k]) for k in 1..3
        n = len(stoneValue)
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            total = 0
            for k in range(1, 4):
                if i + k <= n:
                    total += stoneValue[i + k - 1]
                    dp[i] = max(dp[i], total - dp[i + k])
        score = dp[0]
        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        return "Tie"


if __name__ == "__main__":
    sol = Solution()
    assert sol.stoneGameIII([1, 2, 3, 7]) == "Bob"
    assert sol.stoneGameIII([1, 2, 3, -9]) == "Alice"
    assert sol.stoneGameIII([1, 2, 3, 6]) == "Tie"
    assert sol.stoneGameIII_dp([1, 2, 3, 7]) == "Bob"
    assert sol.stoneGameIII_dp([1, 2, 3, 6]) == "Tie"
    print("All tests passed.")
