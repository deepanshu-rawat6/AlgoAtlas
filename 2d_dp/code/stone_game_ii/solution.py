"""
# 1140. Stone Game II

## Problem
Alice and Bob continue their games with piles of stones. There are a number of piles
arranged in a row, and each pile has a positive integer number of stones. Alice and
Bob take turns, with Alice going first. On each player's turn, that player can take
all the stones in the first X remaining piles, where 1 <= X <= 2M. Then M = max(M, X).
Initially M = 1. The goal is to maximize the number of stones Alice gets.

## Examples
```text
Input:  piles = [2,7,9,4,4]
Output: 10
Explanation: Alice takes 2 piles (2+7=9), M becomes 2.
             Bob takes 4 piles (9+4+4=17), M becomes 4.
             Alice has 9, Bob has 17... wait, Alice takes first 2 piles = 2+7=9,
             then Bob takes all remaining = 9+4+4=17? No:
             Alice takes 2 (X=2, M=2), Bob takes 4 (X=4, M=4), Alice gets 2+7=9,
             Bob gets 9+4+4=17. Actually optimal: Alice takes 1 pile (2), M=1,
             Bob takes 2 piles (7+9=16), M=2, Alice takes 4 piles (4+4=8)... 
             Optimal: Alice=10, Bob=16.

Input:  piles = [1,2,3,4,5,100]
Output: 104
```

## Constraints
- 1 <= piles.length <= 100
- 1 <= piles[i] <= 10^4
"""
from typing import List
from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # dp[i][m] = max stones current player can get from piles[i:] with M=m
        # Try taking x piles (1 <= x <= 2*m); update M = max(m, x)
        # Time: O(n^3), Space: O(n^2)
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i+1] + piles[i]

        @lru_cache(maxsize=None)
        def dp(i, M):
            if i + 2 * M >= n:
                return suffix[i]
            return suffix[i] - min(dp(i + x, max(M, x)) for x in range(1, 2 * M + 1))

        return dp(0, 1)


if __name__ == '__main__':
    s = Solution()
    assert s.stoneGameII([2,7,9,4,4]) == 10
    assert s.stoneGameII([1,2,3,4,5,100]) == 104
    print("All tests passed.")
