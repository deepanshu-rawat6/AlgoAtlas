"""
LC 35 - Search Insert Position
================================

Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be inserted in
order.

You must write an algorithm with O(log n) runtime complexity.

Examples
--------
```text
Input:  nums = [1, 3, 5, 6], target = 5
Output: 2

Input:  nums = [1, 3, 5, 6], target = 2
Output: 1

Input:  nums = [1, 3, 5, 6], target = 7
Output: 4
```

Constraints
-----------
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums contains distinct values sorted in ascending order
- -10^4 <= target <= 10^4
"""

from typing import List


class Solution:
    def method_linear(self, nums: List[int], target: int) -> int:
        # O(n) time | O(1) space
        for i, v in enumerate(nums):
            if v >= target:
                return i
        return len(nums)

    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search; lo converges to the insertion point when target not found
        # O(log n) time | O(1) space
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


if __name__ == "__main__":
    s = Solution()
    assert s.searchInsert([1, 3, 5, 6], 5) == 2
    assert s.searchInsert([1, 3, 5, 6], 2) == 1
    assert s.searchInsert([1, 3, 5, 6], 7) == 4
    assert s.method_linear([1, 3, 5, 6], 5) == 2
    assert s.method_linear([1, 3, 5, 6], 2) == 1
    assert s.method_linear([1, 3, 5, 6], 7) == 4
    print("All tests passed.")
