"""
LC 81 - Search in Rotated Sorted Array II
==========================================

There is an integer array `nums` sorted in non-decreasing order (not
necessarily with distinct values). Before being passed to your function, `nums`
is rotated at an unknown pivot index k.

Given the array `nums` after the possible rotation and an integer `target`,
return true if `target` is in `nums`, or false if it is not in `nums`.

You must decrease the overall operation steps as much as possible.

Examples
--------
```text
Input:  nums = [2, 5, 6, 0, 0, 1, 2], target = 0
Output: true

Input:  nums = [2, 5, 6, 0, 0, 1, 2], target = 3
Output: false
```

Constraints
-----------
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- nums is sorted and rotated at some pivot
- -10^4 <= target <= 10^4
"""

from typing import List


class Solution:
    def method_linear(self, nums: List[int], target: int) -> bool:
        # O(n) time | O(1) space
        return target in nums

    def search(self, nums: List[int], target: int) -> bool:
        # Same as rotated search but duplicates can obscure which half is sorted
        # When nums[lo]==nums[mid]==nums[hi], shrink both ends by 1 to break tie
        # O(log n) average, O(n) worst time | O(1) space
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            # can't determine sorted half — shrink bounds
            if nums[lo] == nums[mid] == nums[hi]:
                lo += 1
                hi -= 1
            elif nums[lo] <= nums[mid]:  # left half sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:  # right half sorted
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.search([2, 5, 6, 0, 0, 1, 2], 0) is True
    assert s.search([2, 5, 6, 0, 0, 1, 2], 3) is False
    assert s.search([1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 13) is True
    assert s.method_linear([2, 5, 6, 0, 0, 1, 2], 0) is True
    print("All tests passed.")
