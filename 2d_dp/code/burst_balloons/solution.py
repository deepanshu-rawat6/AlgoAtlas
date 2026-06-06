"""
# 312. Burst Balloons

## Problem
You are given `n` balloons, indexed from 0 to n-1. Each balloon is painted with a
number on it represented by an array `nums`. You are asked to burst all the balloons.
If you burst the i-th balloon, you will get `nums[i-1] * nums[i] * nums[i+1]` coins.
If i-1 or i+1 goes out of bounds, treat it as if there is a balloon with a 1 painted on it.
Return the maximum coins you can collect by bursting the balloons wisely.

## Examples
```text
Input:  nums = [3,1,5,8]
Output: 167
Explanation:
  Burst 1 -> 3*1*5 = 15, nums = [3,5,8]
  Burst 5 -> 3*5*8 = 120, nums = [3,8]
  Burst 3 -> 1*3*8 = 24, nums = [8]
  Burst 8 -> 1*8*1 = 8, nums = []
  Total = 15 + 120 + 24 + 8 = 167

Input:  nums = [1,5]
Output: 10
```

## Constraints
- 1 <= nums.length <= 300
- 0 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Interval DP: dp[l][r] = max coins from bursting all balloons in (l,r)
        # Try each balloon k as the LAST to burst in the interval
        # Coins from k = nums[l]*nums[k]*nums[r] + dp[l][k] + dp[k][r]
        # Time: O(n^3), Space: O(n^2)
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right]
                    )
        return dp[0][n-1]


if __name__ == '__main__':
    s = Solution()
    assert s.maxCoins([3,1,5,8]) == 167
    assert s.maxCoins([1,5]) == 10
    assert s.maxCoins([1]) == 1
    print("All tests passed.")
