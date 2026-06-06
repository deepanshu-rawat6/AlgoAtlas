"""
LC 377 — Combination Sum IV
=============================

Given an array of distinct integers `nums` and a target integer `target`,
return the number of possible combinations that add up to `target`.
The order of the combination matters (permutations count separately).

Examples
--------
```text
Input:  nums = [1, 2, 3], target = 4
Output: 7
Explanation:
  (1, 1, 1, 1)
  (1, 1, 2)
  (1, 2, 1)
  (1, 3)
  (2, 1, 1)
  (2, 2)
  (3, 1)

Input:  nums = [9], target = 3
Output: 0
```

Constraints
-----------
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 1000
- All elements of nums are unique
- 1 <= target <= 1000
"""

from typing import List
from functools import lru_cache


class Solution:
    # Approach 1: Top-down memoization — O(target * n) time, O(target) space
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp(rem) = sum of dp(rem-num) for each num <= rem; order matters (permutations)
        @lru_cache(maxsize=None)
        def dp(rem: int) -> int:
            if rem == 0:
                return 1
            return sum(dp(rem - num) for num in nums if num <= rem)

        return dp(target)

    # Approach 2: Bottom-up DP — O(target * n) time, O(target) space
    def combinationSum4_dp(self, nums: List[int], target: int) -> int:
        # dp[i] = number of ordered combinations summing to i
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        return dp[target]


if __name__ == "__main__":
    sol = Solution()
    assert sol.combinationSum4([1, 2, 3], 4) == 7
    assert sol.combinationSum4([9], 3) == 0
    assert sol.combinationSum4_dp([1, 2, 3], 4) == 7
    assert sol.combinationSum4_dp([9], 3) == 0
    print("All tests passed.")
