"""
LC 410 - Split Array Largest Sum
==================================

Given an integer array `nums` and an integer `k`, split `nums` into `k`
non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

Examples
--------
```text
Input:  nums = [7, 2, 5, 10, 8], k = 2
Output: 18
Explanation: Split into [7,2,5] and [10,8]. Largest sum = max(14,18) = 18.

Input:  nums = [1, 2, 3, 4, 5], k = 2
Output: 9
```

Constraints
-----------
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 10^6
- 1 <= k <= min(50, nums.length)
"""

from typing import List


class Solution:
    def method_dp(self, nums: List[int], k: int) -> int:
        # O(n^2 * k) time | O(n * k) space
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, v in enumerate(nums):
            prefix[i + 1] = prefix[i] + v

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for m in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[m][j - 1], prefix[i] - prefix[m]))
        return dp[n][k]

    def splitArray(self, nums: List[int], k: int) -> int:
        # Binary search on the answer (max subarray sum): lo=max(nums), hi=sum(nums)
        # Check if we can split into <= m subarrays with max sum <= mid
        # O(n * log(sum(nums))) time | O(1) space
        def can_split(cap: int) -> bool:
            parts, curr = 1, 0
            for v in nums:
                if curr + v > cap:
                    parts += 1
                    curr = 0
                curr += v
            return parts <= k

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_split(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    s = Solution()
    assert s.splitArray([7, 2, 5, 10, 8], 2) == 18
    assert s.splitArray([1, 2, 3, 4, 5], 2) == 9
    assert s.method_dp([7, 2, 5, 10, 8], 2) == 18
    assert s.method_dp([1, 2, 3, 4, 5], 2) == 9
    print("All tests passed.")
