"""
LC 704 - Binary Search
======================

Given an array of integers `nums` which is sorted in ascending order, and an
integer `target`, write a function to search `target` in `nums`. If `target`
exists, return its index. Otherwise, return -1.

Examples
--------
```text
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4

Input:  nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
```

Constraints
-----------
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All integers in nums are unique
- nums is sorted in ascending order
"""

from typing import List


class Solution:
    def method_brute_force(self, nums: List[int], target: int) -> int:
        # O(n) time | O(1) space
        for i, v in enumerate(nums):
            if v == target:
                return i
        return -1

    def search(self, nums: List[int], target: int) -> int:
        # Standard binary search: compare mid to target, halve search space
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
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert s.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert s.method_brute_force([-1, 0, 3, 5, 9, 12], 9) == 4
    assert s.method_brute_force([-1, 0, 3, 5, 9, 12], 2) == -1
    print("All tests passed.")
