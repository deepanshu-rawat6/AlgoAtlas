"""
LC 1095 - Find in Mountain Array
==================================

You may recall that an array `arr` is a mountain array if and only if:
  - arr.length >= 3
  - There exists some index i (0-indexed) with 0 < i < arr.length - 1 such
    that arr[0] < arr[1] < ... < arr[i] > arr[i+1] > ... > arr[arr.length-1]

Given a mountain array `mountainArr`, return the minimum index such that
mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array
using a MountainArray interface:
  - MountainArray.get(k) returns the element of the array at index k (0-indexed)
  - MountainArray.length() returns the length of the array

Submissions making more than 100 calls to MountainArray.get will be judged
Wrong Answer.

Examples
--------
```text
Input:  array = [1, 2, 3, 4, 5, 3, 1], target = 3
Output: 2

Input:  array = [0, 1, 2, 4, 2, 1], target = 3
Output: -1
```

Constraints
-----------
- 3 <= mountain_arr.length() <= 10^4
- 0 <= target <= 10^9
- 0 <= mountain_arr.get(index) <= 10^9
"""


class MountainArray:
    """Mock interface for testing."""

    def __init__(self, arr: list):
        self._arr = arr
        self._calls = 0

    def get(self, index: int) -> int:
        self._calls += 1
        assert self._calls <= 100, "Exceeded 100 API calls"
        return self._arr[index]

    def length(self) -> int:
        return len(self._arr)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Step 1: find peak — binary search where arr[mid] < arr[mid+1] means peak is right
        # Step 2: binary search ascending left half [0..peak]
        # Step 3: binary search descending right half [peak+1..n-1] (reversed comparisons)
        # O(log n) time | O(1) space
        n = mountain_arr.length()

        # 1. Find peak index
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                lo = mid + 1
            else:
                hi = mid
        peak = lo

        # 2. Binary search ascending left half
        lo, hi = 0, peak
        while lo <= hi:
            mid = (lo + hi) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1

        # 3. Binary search descending right half
        lo, hi = peak + 1, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val > target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.findInMountainArray(3, MountainArray([1, 2, 3, 4, 5, 3, 1])) == 2
    assert s.findInMountainArray(3, MountainArray([0, 1, 2, 4, 2, 1])) == -1
    assert s.findInMountainArray(1, MountainArray([1, 2, 3, 4, 5, 3, 1])) == 0
    assert s.findInMountainArray(5, MountainArray([1, 2, 3, 4, 5, 3, 1])) == 4
    print("All tests passed.")
