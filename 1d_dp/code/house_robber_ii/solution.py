"""
LC 213 — House Robber II
=========================

All houses are arranged in a circle. The first and last houses are adjacent.
You cannot rob two adjacent houses. Return the maximum amount you can rob.

Examples
--------
```text
Input:  nums = [2, 3, 2]
Output: 3
Explanation: Cannot rob house 1 (2) and house 3 (2) since they are adjacent.

Input:  nums = [1, 2, 3]
Output: 3

Input:  nums = [1, 2, 3, 1]
Output: 4
```

Constraints
-----------
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000
"""

from typing import List


class Solution:
    # Approach 1: Two linear passes (exclude first or exclude last) — O(n) time, O(1) space
    def rob(self, nums: List[int]) -> int:
        # Circular constraint: can't rob both first and last house
        # Run linear rob on [0..n-2] and [1..n-1]; take the max
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses: List[int]) -> int:
            prev2, prev1 = 0, 0
            for num in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + num)
            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


if __name__ == "__main__":
    sol = Solution()
    assert sol.rob([2, 3, 2]) == 3
    assert sol.rob([1, 2, 3]) == 3
    assert sol.rob([1, 2, 3, 1]) == 4
    assert sol.rob([1]) == 1
    print("All tests passed.")
