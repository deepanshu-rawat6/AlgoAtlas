"""
# 338. Counting Bits

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i`
(0 <= i <= n), `ans[i]` is the number of 1's in the binary representation of `i`.

## Examples

```text
Input: n = 2
Output: [0,1,1]

Input: n = 5
Output: [0,1,1,2,1,2]
```

## Constraints
- 0 <= n <= 10^5
"""

from typing import List


class Solution:
    def countBits_naive(self, n: int) -> List[int]:
        # O(n * 32) time — count bits for each number independently
        def count(x: int) -> int:
            c = 0
            while x:
                x &= x - 1
                c += 1
            return c
        return [count(i) for i in range(n + 1)]

    def countBits(self, n: int) -> List[int]:
        # dp[i] = dp[i >> 1] + (i & 1): right shift removes last bit, add it back
        # O(n) time — dp: bits[i] = bits[i >> 1] + (i & 1)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


if __name__ == '__main__':
    s = Solution()
    for method in (s.countBits_naive, s.countBits):
        assert method(2) == [0, 1, 1]
        assert method(5) == [0, 1, 1, 2, 1, 2]
    print("All tests passed.")
