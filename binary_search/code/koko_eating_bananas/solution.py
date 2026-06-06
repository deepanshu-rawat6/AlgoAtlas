"""
LC 875 - Koko Eating Bananas
=============================

Koko loves to eat bananas. There are `n` piles of bananas, the i-th pile has
`piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she
chooses some pile of bananas and eats `k` bananas from that pile. If the pile
has less than `k` bananas, she eats all of them instead and will not eat any
more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas
before the guards return. Return the minimum integer `k` such that she can eat
all the bananas within `h` hours.

Examples
--------
```text
Input:  piles = [3, 6, 7, 11], h = 8
Output: 4

Input:  piles = [30, 11, 23, 4, 20], h = 5
Output: 30

Input:  piles = [30, 11, 23, 4, 20], h = 6
Output: 23
```

Constraints
-----------
- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9
"""

import math
from typing import List


class Solution:
    def _hours_needed(self, piles: List[int], k: int) -> int:
        # Compute total hours needed at speed k: ceil(pile/k) per pile
        return sum(math.ceil(p / k) for p in piles)

    def method_linear(self, piles: List[int], h: int) -> int:
        # Try every speed from 1 upward — O(max(piles)*n)
        # O(max(piles) * n) time | O(1) space
        k = 1
        while self._hours_needed(piles, k) > h:
            k += 1
        return k

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search on speed: lo=1, hi=max(piles)
        # If hours_needed(mid) <= h, mid might be the answer — search left half
        # O(n * log(max(piles))) time | O(1) space
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if self._hours_needed(piles, mid) <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    s = Solution()
    assert s.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert s.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert s.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    assert s.method_linear([3, 6, 7, 11], 8) == 4
    print("All tests passed.")
