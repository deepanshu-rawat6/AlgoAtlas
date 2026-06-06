"""
LC 300 — Longest Increasing Subsequence
=========================================

Given an integer array `nums`, return the length of the longest strictly
increasing subsequence.

Examples
--------
```text
Input:  nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: [2, 3, 7, 101]

Input:  nums = [0, 1, 0, 3, 2, 3]
Output: 4

Input:  nums = [7, 7, 7, 7, 7, 7, 7]
Output: 1
```

Constraints
-----------
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4
"""

from typing import List
import bisect


class Solution:
    # Approach 1: DP — O(n^2) time, O(n) space
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = LIS ending at index i; for each j < i where nums[j] < nums[i], dp[i] = max(dp[i], dp[j]+1)
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # Approach 2: Binary search (patience sorting) — O(n log n) time, O(n) space
    def lengthOfLIS_bs(self, nums: List[int]) -> int:
        # Patience sorting: maintain 'tails' array; binary search for insertion position
        # tails[i] = smallest tail of all LIS of length i+1
        tails = []
        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)


if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert sol.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert sol.lengthOfLIS([7, 7, 7, 7]) == 1
    assert sol.lengthOfLIS_bs([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert sol.lengthOfLIS_bs([7, 7, 7, 7]) == 1
    print("All tests passed.")
