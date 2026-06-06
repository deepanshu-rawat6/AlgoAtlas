"""
LC 33 - Search in Rotated Sorted Array
========================================

There is an integer array `nums` sorted in ascending order (with distinct
values). Prior to being passed to your function, `nums` is possibly rotated at
an unknown pivot index k such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]].

Given the array `nums` after the possible rotation and an integer `target`,
return the index of `target` if it is in `nums`, or -1 if it is not in `nums`.

You must write an algorithm with O(log n) runtime complexity.

Examples
--------
```text
Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4

Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1

Input:  nums = [1], target = 0
Output: -1
```

Constraints
-----------
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique
- nums is an ascending array that is possibly rotated
- -10^4 <= target <= 10^4
"""

from typing import List


class Solution:
    def method_linear(self, nums: List[int], target: int) -> int:
        # O(n) time | O(1) space
        for i, v in enumerate(nums):
            if v == target:
                return i
        return -1

    def search(self, nums: List[int], target: int) -> int:
        # Determine which half is sorted by comparing nums[lo] to nums[mid]
        # Check if target falls in the sorted half; if yes search there, else other half
        # O(log n) time | O(1) space
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:  # left half sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:  # right half sorted
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert s.search([1], 0) == -1
    assert s.method_linear([4, 5, 6, 7, 0, 1, 2], 0) == 4
    print("All tests passed.")
