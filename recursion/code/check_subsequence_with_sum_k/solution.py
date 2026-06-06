"""
Check if Any Subsequence with Sum K Exists

Problem: Return True if any subsequence of nums sums to k, else False.

Examples:
    nums = [1, 2, 3, 4], k = 6 -> True  ([2,4] or [1,2,3])
    nums = [1, 2, 3],    k = 7 -> False

Constraints:
    1 <= nums.length <= 20
    0 <= nums[i] <= 100

Approach: Recursion with early termination O(2^n) worst case.
    Same include/exclude tree as count variant, but short-circuit on first hit.
"""

from typing import List


class Solution:
    def hasSubsequenceSum(self, nums: List[int], k: int) -> bool:
        def recurse(idx: int, remaining: int) -> bool:
            # Base case: found a valid subsequence
            if remaining == 0:
                return True
            # Base case: exhausted array without hitting sum
            if idx == len(nums):
                return False
            # Include current element (only if it doesn't overshoot)
            if nums[idx] <= remaining and recurse(idx + 1, remaining - nums[idx]):
                return True  # early termination
            # Exclude current element
            return recurse(idx + 1, remaining)

        return recurse(0, k)


if __name__ == '__main__':
    sol = Solution()
    assert sol.hasSubsequenceSum([1, 2, 3, 4], 6) is True
    assert sol.hasSubsequenceSum([1, 2, 3], 7) is False
    assert sol.hasSubsequenceSum([1, 2, 1], 2) is True
    assert sol.hasSubsequenceSum([5], 5) is True
    assert sol.hasSubsequenceSum([5], 3) is False
    print("All tests passed.")
