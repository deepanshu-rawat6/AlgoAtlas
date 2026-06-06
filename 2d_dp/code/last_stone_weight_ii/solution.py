"""
# 1049. Last Stone Weight II

## Problem
You are given an array of integers `stones` where `stones[i]` is the weight of the
i-th stone. We are playing a game with the stones. On each turn, we choose any two
stones and smash them together. If x == y, both stones are destroyed. If x != y,
the stone of weight x is destroyed and the stone of weight y has new weight y - x.
Return the smallest possible weight of the left stone (0 if all destroyed).

## Examples
```text
Input:  stones = [2,7,4,1,8,1]
Output: 1
Explanation: Combine 2 and 4 -> 2, combine 7 and 8 -> 1, combine 2 and 1 -> 1,
             combine 1 and 1 -> 0, left with 1.

Input:  stones = [31,26,33,21,40]
Output: 5
```

## Constraints
- 1 <= stones.length <= 30
- 1 <= stones[i] <= 100
"""
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Minimize |S1 - S2| where S1+S2=total; equivalent to partition equal subset sum
        # Find largest subset sum <= total//2; answer = total - 2*that_sum
        # Time: O(n*sum), Space: O(sum)
        total = sum(stones)
        target = total // 2
        dp = {0}
        for s in stones:
            dp = {x + s for x in dp} | dp
        best = max(x for x in dp if x <= target)
        return total - 2 * best


if __name__ == '__main__':
    s = Solution()
    assert s.lastStoneWeightII([2,7,4,1,8,1]) == 1
    assert s.lastStoneWeightII([31,26,33,21,40]) == 5
    assert s.lastStoneWeightII([1]) == 1
    print("All tests passed.")
