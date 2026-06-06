"""
Count Subsequences with Sum K

Problem: Count all subsequences of an array whose elements sum to k.

Examples:
    nums = [1, 2, 1], k = 2 -> 2  (subsequences: [1,1] and [2])
    nums = [1, 1, 1], k = 2 -> 3

Constraints:
    1 <= nums.length <= 20
    0 <= nums[i] <= 100
    0 <= k <= 1000
"""

from typing import List


class Solution:
    # Approach 1: Recursion with memoization O(n * k)
    def countSubsequences(self, nums: List[int], k: int) -> int:
        from functools import lru_cache

        n = len(nums)

        @lru_cache(maxsize=None)
        def dp(idx: int, remaining: int) -> int:
            # Base case: processed all elements
            if idx == n:
                return 1 if remaining == 0 else 0
            # Exclude current element
            count = dp(idx + 1, remaining)
            # Include current element only if it doesn't exceed remaining sum
            if nums[idx] <= remaining:
                count += dp(idx + 1, remaining - nums[idx])
            return count

        return dp(0, k)

    # Approach 2: Backtracking O(2^n) — explicit include/exclude tree
    def countSubsequences_backtrack(self, nums: List[int], k: int) -> int:
        count = [0]

        def backtrack(idx: int, current_sum: int) -> None:
            # Base case: reached end, check if sum matches
            if idx == len(nums):
                if current_sum == k:
                    count[0] += 1
                return
            # Include nums[idx]
            backtrack(idx + 1, current_sum + nums[idx])
            # Exclude nums[idx]
            backtrack(idx + 1, current_sum)

        backtrack(0, 0)
        return count[0]


if __name__ == '__main__':
    sol = Solution()
    assert sol.countSubsequences([1, 2, 1], 2) == 2
    assert sol.countSubsequences([1, 1, 1], 2) == 3
    assert sol.countSubsequences_backtrack([1, 2, 1], 2) == 2
    assert sol.countSubsequences_backtrack([1, 1, 1], 2) == 3
    print("All tests passed.")
