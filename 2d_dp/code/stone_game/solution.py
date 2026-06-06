"""
# 877. Stone Game

## Problem
Alice and Bob play a game with piles of stones. There are an even number of piles
arranged in a row, and each pile has a positive integer number of stones. The total
number of stones is odd. Alice and Bob take turns, with Alice going first. Each turn,
a player takes the entire pile of stones from either the beginning or the end of the
row. The player with the most stones at the end wins. Assuming Alice and Bob play
optimally, return true if Alice wins the game, or false if Bob wins.

## Examples
```text
Input:  piles = [5,3,4,5]
Output: true
Explanation: Alice starts first. Alice takes 5 (right). Bob takes 5 (left).
             Alice takes 4. Bob takes 3. Alice has 9, Bob has 8. Alice wins.

Input:  piles = [3,7,2,3]
Output: true
```

## Constraints
- 2 <= piles.length <= 500
- piles.length is even
- 1 <= piles[i] <= 500
- sum(piles[i]) is odd
"""
from typing import List


class Solution:
    def stoneGame_dp(self, piles: List[int]) -> bool:
        # Time: O(n^2), Space: O(n^2)
        n = len(piles)
        # dp[i][j] = max score difference (current player - other) for piles[i..j]
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        return dp[0][n-1] > 0

    def stoneGame(self, piles: List[int]) -> bool:
        # Alice always wins with optimal play (mathematical proof)
        # Or dp[i][j] = max score difference for current player on piles[i..j]
        # Time: O(1), Space: O(1)
        return True  # Alice always wins with even piles and odd total


if __name__ == '__main__':
    s = Solution()
    assert s.stoneGame([5,3,4,5]) == True
    assert s.stoneGame([3,7,2,3]) == True
    assert s.stoneGame_dp([5,3,4,5]) == True
    assert s.stoneGame_dp([3,7,2,3]) == True
    print("All tests passed.")
