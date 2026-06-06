"""
LC 1011 - Capacity To Ship Packages Within D Days
===================================================

A conveyor belt has packages that must be shipped from one port to another
within `days` days. The i-th package on the conveyor belt has a weight of
`weights[i]`. Each day, we load the ship with packages in the order given by
`weights`. We may not load more weight than the maximum weight capacity of the
ship.

Return the least weight capacity of the ship that will result in all the
packages on the conveyor belt being shipped within `days` days.

Examples
--------
```text
Input:  weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15

Input:  weights = [3,2,2,4,1,4], days = 3
Output: 6

Input:  weights = [1,2,3,1,1], days = 4
Output: 3
```

Constraints
-----------
- 1 <= days <= weights.length <= 5 * 10^4
- 1 <= weights[i] <= 500
"""

from typing import List


class Solution:
    def _days_needed(self, weights: List[int], cap: int) -> int:
        # Simulate loading: start new day when adding next package exceeds capacity
        days, load = 1, 0
        for w in weights:
            if load + w > cap:
                days += 1
                load = 0
            load += w
        return days

    def method_linear(self, weights: List[int], days: int) -> int:
        # Try every capacity from max(weights) upward — O(sum*n)
        # O(sum(weights) * n) time | O(1) space
        cap = max(weights)
        while self._days_needed(weights, cap) > days:
            cap += 1
        return cap

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Binary search on capacity: lo=max(weights) (must fit heaviest), hi=sum(weights)
        # If days_needed(mid) <= days, mid is feasible — try smaller capacity
        # O(n * log(sum(weights))) time | O(1) space
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if self._days_needed(weights, mid) <= days:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    s = Solution()
    assert s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
    assert s.shipWithinDays([3, 2, 2, 4, 1, 4], 3) == 6
    assert s.shipWithinDays([1, 2, 3, 1, 1], 4) == 3
    assert s.method_linear([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
    print("All tests passed.")
