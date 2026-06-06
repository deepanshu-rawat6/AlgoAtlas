"""
LC 198 — House Robber
======================

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. Adjacent houses have
security systems connected — you cannot rob two adjacent houses.

Given an integer array `nums` representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Examples
--------
```text
Input:  nums = [1, 2, 3, 1]
Output: 4
Explanation: Rob house 1 (1) + house 3 (3) = 4

Input:  nums = [2, 7, 9, 3, 1]
Output: 12
Explanation: Rob house 1 (2) + house 3 (9) + house 5 (1) = 12
```

Constraints
-----------
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400
"""

from typing import List
from functools import lru_cache


class Solution:
    # Approach 1: Top-down memoization — O(n) time, O(n) space
    def rob(self, nums: List[int]) -> int:
        # dp(i) = max(rob house i + dp(i+2), skip house i = dp(i+1))
        n = len(nums)

        @lru_cache(maxsize=None)
        def dp(i: int) -> int:
            if i >= n:
                return 0
            return max(nums[i] + dp(i + 2), dp(i + 1))

        return dp(0)

    # Approach 2: Bottom-up DP — O(n) time, O(n) space
    def rob_dp(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i]): rob or skip current house
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

    # Approach 3: Space-optimized — O(n) time, O(1) space
    def rob_opt(self, nums: List[int]) -> int:
        # Rolling two variables: prev2=rob two ago, prev1=best so far
        prev2, prev1 = 0, 0
        for num in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + num)
        return prev1


if __name__ == "__main__":
    sol = Solution()
    assert sol.rob([1, 2, 3, 1]) == 4
    assert sol.rob([2, 7, 9, 3, 1]) == 12
    assert sol.rob([1]) == 1
    assert sol.rob_dp([1, 2, 3, 1]) == 4
    assert sol.rob_opt([1, 2, 3, 1]) == 4
    print("All tests passed.")
