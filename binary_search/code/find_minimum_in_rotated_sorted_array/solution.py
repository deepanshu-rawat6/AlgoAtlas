"""
LC 153 - Find Minimum in Rotated Sorted Array
===============================================

Suppose an array of length `n` sorted in ascending order is rotated between 1
and n times. For example, the array nums = [0,1,2,4,5,6,7] might become
[4,5,6,7,0,1,2] if it was rotated 4 times.

Given the sorted rotated array `nums` of unique elements, return the minimum
element of this array.

You must write an algorithm that runs in O(log n) time.

Examples
--------
```text
Input:  nums = [3, 4, 5, 1, 2]
Output: 1

Input:  nums = [4, 5, 6, 7, 0, 1, 2]
Output: 0

Input:  nums = [11, 13, 15, 17]
Output: 11
```

Constraints
-----------
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique
- nums is sorted and rotated between 1 and n times
"""

from typing import List


class Solution:
    def method_linear(self, nums: List[int]) -> int:
        # O(n) time | O(1) space
        return min(nums)

    def findMin(self, nums: List[int]) -> int:
        # If mid > hi, the minimum is in the right half (rotation point is there)
        # Otherwise minimum is in the left half including mid
        # O(log n) time | O(1) space
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


if __name__ == "__main__":
    s = Solution()
    assert s.findMin([3, 4, 5, 1, 2]) == 1
    assert s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert s.findMin([11, 13, 15, 17]) == 11
    assert s.method_linear([3, 4, 5, 1, 2]) == 1
    print("All tests passed.")
