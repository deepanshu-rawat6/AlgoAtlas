"""
LC 4 - Median of Two Sorted Arrays
=====================================

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log(m + n)).

Examples
--------
```text
Input:  nums1 = [1, 3], nums2 = [2]
Output: 2.0
Explanation: merged = [1, 2, 3], median = 2.0

Input:  nums1 = [1, 2], nums2 = [3, 4]
Output: 2.5
Explanation: merged = [1, 2, 3, 4], median = (2 + 3) / 2 = 2.5
```

Constraints
-----------
- nums1.length == m
- nums2.length == n
- 0 <= m, n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6
"""

from typing import List


class Solution:
    def method_merge(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge both arrays, sort, then find median by index — O(m+n)
        # O(m + n) time | O(m + n) space
        merged = sorted(nums1 + nums2)
        total = len(merged)
        mid = total // 2
        if total % 2 == 1:
            return float(merged[mid])
        return (merged[mid - 1] + merged[mid]) / 2.0

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary search on partition of smaller array; derive partition of larger
        # Valid partition: left1<=right2 and left2<=right1 (cross-check boundaries)
        # Odd total: median is min of right halves; even: average of inner boundary
        # O(log(min(m, n))) time | O(1) space
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half = (m + n) // 2

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2  # partition in nums1
            j = half - i        # partition in nums2

            left1  = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i]     if i < m else float('inf')
            left2  = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j]     if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return float(min(right1, right2))
                return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                hi = i - 1
            else:
                lo = i + 1
        return 0.0


if __name__ == "__main__":
    s = Solution()
    assert s.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert s.findMedianSortedArrays([], [1]) == 1.0
    assert s.method_merge([1, 3], [2]) == 2.0
    assert s.method_merge([1, 2], [3, 4]) == 2.5
    print("All tests passed.")
