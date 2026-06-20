"""
## LC 88: Merge Sorted Array

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing
order, and two integers `m` and `n`, representing the number of elements in
`nums1` and `nums2` respectively.

Merge `nums2` into `nums1` as one sorted array in-place. `nums1` has a length
of `m + n`, where the last `n` elements are set to `0` and should be ignored.

### Examples

```text
Input:  nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Input:  nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Input:  nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
```

### Constraints

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`
"""
from typing import List


class Solution:
    def method_merge_sort(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """O((m+n) log(m+n)) time, O(n) space."""
        # Copy nums2 into the spare space of nums1, then sort — O((m+n) log(m+n))
        nums1[m:] = nums2[:n]
        nums1.sort()

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """O(m+n) time, O(1) space — fill from the end."""
        # Fill from the END to avoid overwriting unprocessed elements in nums1
        # Compare largest remaining from each array, place the bigger one at k
        # Remaining nums2 elements (if any) are copied directly — nums1 elements already in place
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    sol.merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6], f"Failed: {nums1}"

    nums1 = [1]
    sol.merge(nums1, 1, [], 0)
    assert nums1 == [1], f"Failed: {nums1}"

    nums1 = [0]
    sol.merge(nums1, 0, [1], 1)
    assert nums1 == [1], f"Failed: {nums1}"

    print("All tests passed.")
