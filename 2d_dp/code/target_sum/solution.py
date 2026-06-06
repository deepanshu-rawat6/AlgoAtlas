"""
# 494. Target Sum

## Problem
You are given an integer array `nums` and an integer `target`. You want to build an
expression out of nums by adding one of the symbols '+' and '-' before each integer
in nums and then concatenate all the integers. Return the number of different
expressions that you can build which evaluates to `target`.

## Examples
```text
Input:  nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: -1+1+1+1+1 = 3, +1-1+1+1+1 = 3, +1+1-1+1+1 = 3,
             +1+1+1-1+1 = 3, +1+1+1+1-1 = 3

Input:  nums = [1], target = 1
Output: 1
```

## Constraints
- 1 <= nums.length <= 20
- 0 <= nums[i] <= 1000
- 0 <= sum(nums[i]) <= 1000
- -1000 <= target <= 1000
"""
from typing import List


class Solution:
    def findTargetSumWays_brute(self, nums: List[int], target: int) -> int:
        # Time: O(2^n), Space: O(n) recursion stack
        def dfs(i, curr):
            if i == len(nums):
                return 1 if curr == target else 0
            return dfs(i+1, curr + nums[i]) + dfs(i+1, curr - nums[i])
        return dfs(0, 0)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[i][sum] = ways to reach sum using first i numbers
        # Each number can be added (+) or subtracted (-)
        # Time: O(n*sum), Space: O(sum)
        from collections import defaultdict
        dp = defaultdict(int)
        dp[0] = 1
        for n in nums:
            next_dp = defaultdict(int)
            for s, cnt in dp.items():
                next_dp[s + n] += cnt
                next_dp[s - n] += cnt
            dp = next_dp
        return dp[target]


if __name__ == '__main__':
    s = Solution()
    assert s.findTargetSumWays([1,1,1,1,1], 3) == 5
    assert s.findTargetSumWays([1], 1) == 1
    assert s.findTargetSumWays([1], -1) == 1
    assert s.findTargetSumWays_brute([1,1,1,1,1], 3) == 5
    print("All tests passed.")
