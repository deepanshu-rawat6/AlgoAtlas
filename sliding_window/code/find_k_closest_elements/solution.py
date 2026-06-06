from typing import List
import bisect


class Solution:
    """
    ## 658. Find K Closest Elements

    Given a sorted integer array `arr`, two integers `k` and `x`, return the `k`
    closest integers to `x` in the array. The result should also be sorted in ascending
    order.

    An integer `a` is closer to `x` than an integer `b` if:
    - `|a - x| < |b - x|`, or
    - `|a - x| == |b - x|` and `a < b`

    ### Examples

    ```text
    Input:  arr = [1, 2, 3, 4, 5], k = 4, x = 3
    Output: [1, 2, 3, 4]

    Input:  arr = [1, 2, 3, 4, 5], k = 4, x = -1
    Output: [1, 2, 3, 4]
    ```

    ### Constraints

    - `1 <= k <= arr.length <= 10^4`
    - `arr` is sorted in ascending order.
    - `-10^4 <= arr[i], x <= 10^4`
    """

    def findClosestElements_sort(self, arr: List[int], k: int, x: int) -> List[int]:
        # Sort by distance to x, take first k, then re-sort for ascending order
        # O(n log n) time, O(n) space
        return sorted(sorted(arr, key=lambda a: (abs(a - x), a))[:k])

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Binary search for the left boundary of the k-element window
        # Compare distance of left edge vs right edge: x-arr[mid] vs arr[mid+k]-x
        # Move window right if left edge is farther from x than right edge
        # O(log n + k) time, O(1) space
        lo, hi = 0, len(arr) - k
        while lo < hi:
            mid = (lo + hi) // 2
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo + k]


if __name__ == "__main__":
    sol = Solution()
    assert sol.findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
    assert sol.findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
    assert sol.findClosestElements([1, 2, 3, 4, 5], 4, 10) == [2, 3, 4, 5]
    assert sol.findClosestElements_sort([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
    assert sol.findClosestElements_sort([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
    print("All tests passed.")
