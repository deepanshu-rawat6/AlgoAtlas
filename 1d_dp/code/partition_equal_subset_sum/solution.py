"""
LC 416 — Partition Equal Subset Sum
=====================================

Given an integer array `nums`, return true if you can partition the array into
two subsets such that the sum of the elements in both subsets is equal.

Examples
--------
```text
Input:  nums = [1, 5, 11, 5]
Output: true
Explanation: [1, 5, 5] and [11]

Input:  nums = [1, 2, 3, 5]
Output: false
```

Constraints
-----------
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100
"""

from typing import List
from functools import lru_cache


class Solution:
    # Approach 1: Top-down memoization — O(n * sum) time, O(n * sum) space
    def canPartition(self, nums: List[int]) -> bool:
        # Reduce to subset sum: can we find a subset summing to total/2?
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        @lru_cache(maxsize=None)
        def dp(i: int, rem: int) -> bool:
            if rem == 0:
                return True
            if i == len(nums) or rem < 0:
                return False
            return dp(i + 1, rem - nums[i]) or dp(i + 1, rem)

        return dp(0, target)

    # Approach 2: Bottom-up DP (boolean set) — O(n * sum) time, O(sum) space
    def canPartition_dp(self, nums: List[int]) -> bool:
        # dp = set of reachable sums; for each num, add num to all existing sums
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = {0}
        for num in nums:
            dp |= {s + num for s in dp if s + num <= target}
        return target in dp

    # Approach 3: Bitset optimization — O(n * sum / 64) time, O(sum / 64) space
    def canPartition_bitset(self, nums: List[int]) -> bool:
        # Bitset trick: bit i set means sum i is reachable; shift and OR for each num
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        bits = 1
        for num in nums:
            bits |= bits << num
        return bool((bits >> target) & 1)


if __name__ == "__main__":
    sol = Solution()
    assert sol.canPartition([1, 5, 11, 5]) is True
    assert sol.canPartition([1, 2, 3, 5]) is False
    assert sol.canPartition_dp([1, 5, 11, 5]) is True
    assert sol.canPartition_dp([1, 2, 3, 5]) is False
    assert sol.canPartition_bitset([1, 5, 11, 5]) is True
    assert sol.canPartition_bitset([1, 2, 3, 5]) is False
    print("All tests passed.")
