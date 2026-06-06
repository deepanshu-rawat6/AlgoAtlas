"""
# LC 912: Sort an Array

Given an array of integers `nums`, sort the array in ascending order and return it.
You must solve the problem **without using any built-in functions** in O(n log n)
time complexity and with the smallest space complexity possible.

## Examples

```text
Input:  nums = [5,2,3,1]
Output: [1,2,3,5]

Input:  nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
```

## Constraints
- 1 <= nums.length <= 5 * 10^4
- -5 * 10^4 <= nums[i] <= 5 * 10^4
"""
from typing import List
import random


class Solution:
    # Approach 1: Merge Sort — O(n log n) time | O(n) space
    def sortArray_merge(self, nums: List[int]) -> List[int]:
        # Divide array in half recursively until single elements, then merge
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray_merge(nums[:mid])
        right = self.sortArray_merge(nums[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        # Merge two sorted halves by comparing front elements one at a time
        result, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i]); i += 1
            else:
                result.append(right[j]); j += 1
        return result + left[i:] + right[j:]

    # Approach 2: Quick Sort — O(n log n) avg | O(log n) space
    def sortArray_quick(self, nums: List[int]) -> List[int]:
        # Randomized pivot avoids worst-case O(n^2) on sorted input
        self._quick(nums, 0, len(nums) - 1)
        return nums

    def _quick(self, nums, lo, hi):
        # Partition around pivot, then recursively sort both halves
        if lo >= hi:
            return
        pivot_idx = self._partition(nums, lo, hi)
        self._quick(nums, lo, pivot_idx - 1)
        self._quick(nums, pivot_idx + 1, hi)

    def _partition(self, nums, lo, hi):
        # Randomly swap pivot to end, then move all <= pivot to the left
        rand = random.randint(lo, hi)
        nums[rand], nums[hi] = nums[hi], nums[rand]
        pivot, i = nums[hi], lo - 1
        for j in range(lo, hi):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[hi] = nums[hi], nums[i + 1]
        return i + 1

    # Approach 3: Heap Sort — O(n log n) time | O(1) space
    def sortArray(self, nums: List[int]) -> List[int]:
        # Heap sort: build max-heap, then repeatedly extract max to end
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(nums, n, i)
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self._heapify(nums, i, 0)
        return nums

    def _heapify(self, nums, n, i):
        # Sift down: swap with largest child to maintain heap property
        largest, l, r = i, 2 * i + 1, 2 * i + 2
        if l < n and nums[l] > nums[largest]:
            largest = l
        if r < n and nums[r] > nums[largest]:
            largest = r
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self._heapify(nums, n, largest)


if __name__ == "__main__":
    s = Solution()
    assert s.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
    assert s.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
    assert s.sortArray([-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]) == sorted([-4, 0, 7, 4, 9, -5, -1, 0, -7, -1])
    print("All tests passed.")
