import heapq
from typing import List


class Solution:
    """
    ## 215. Kth Largest Element in an Array

    Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.

    Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

    You must solve it without sorting (for the optimal solution).

    ### Examples

    ```text
    Input: nums = [3, 2, 1, 5, 6, 4], k = 2
    Output: 5
    ```

    ```text
    Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
    Output: 4
    ```

    ### Constraints
    - `1 <= k <= nums.length <= 10^5`
    - `-10^4 <= nums[i] <= 10^4`
    """

    def findKthLargest_sort(self, nums: List[int], k: int) -> int:
        # O(n log n) — sort descending and index
        return sorted(nums, reverse=True)[k - 1]

    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        # O(n log k) — min-heap of size k
        heap: List[int] = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min-heap of size k: after processing all elements, top is k-th largest
        # O(n) average — quickselect; target index in sorted-asc = len-k
        target = len(nums) - k

        def partition(lo, hi):
            pivot, fill = nums[hi], lo
            for i in range(lo, hi):
                if nums[i] <= pivot:
                    nums[fill], nums[i] = nums[i], nums[fill]
                    fill += 1
            nums[fill], nums[hi] = nums[hi], nums[fill]
            return fill

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = partition(lo, hi)
            if mid == target:
                break
            elif mid < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return nums[target]


if __name__ == '__main__':
    s = Solution()
    assert s.findKthLargest_sort([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest_heap([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5

    assert s.findKthLargest_sort([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert s.findKthLargest_heap([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    print("All tests passed.")
