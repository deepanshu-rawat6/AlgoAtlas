"""
LC 152 — Maximum Product Subarray
===================================

Given an integer array `nums`, find a contiguous subarray that has the largest product,
and return the product.

Examples
--------
```text
Input:  nums = [2, 3, -2, 4]
Output: 6
Explanation: [2, 3] has the largest product 6.

Input:  nums = [-2, 0, -1]
Output: 0
Explanation: The result cannot be 2 because [-2, -1] is not a subarray.
```

Constraints
-----------
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List


class Solution:
    # Approach 1: Brute force — O(n^2) time, O(1) space
    def maxProduct_brute(self, nums: List[int]) -> int:
        # Try all subarrays; track running product — O(n^2)
        best = nums[0]
        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                best = max(best, prod)
        return best

    # Approach 2: Track running min and max — O(n) time, O(1) space
    def maxProduct(self, nums: List[int]) -> int:
        # Track both max and min products (negatives can flip sign)
        # At each step, new max/min comes from: num alone, num*prev_max, num*prev_min
        cur_max = cur_min = best = nums[0]
        for num in nums[1:]:
            candidates = (num, cur_max * num, cur_min * num)
            cur_max, cur_min = max(candidates), min(candidates)
            best = max(best, cur_max)
        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProduct([2, 3, -2, 4]) == 6
    assert sol.maxProduct([-2, 0, -1]) == 0
    assert sol.maxProduct([-2]) == -2
    assert sol.maxProduct([0, 2]) == 2
    assert sol.maxProduct_brute([2, 3, -2, 4]) == 6
    print("All tests passed.")
