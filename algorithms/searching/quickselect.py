"""
Quick Select
============
Strategy   : Partition like quick sort, but only recurse into the side containing k.
Time       : O(n) average, O(n²) worst (avoided with random pivot)
Space      : O(1) iterative, O(log n) recursive stack

Use when:
- Need kth smallest/largest without sorting the full array
- O(n) average is acceptable (vs O(n log n) for sort, O(n log k) for heap)

Comparison:
┌──────────────┬──────────────┬────────┬──────────────────────────────┐
│ Approach     │ Time         │ Space  │ Notes                        │
├──────────────┼──────────────┼────────┼──────────────────────────────┤
│ Sort         │ O(n log n)   │ O(n)   │ Simple, modifies array       │
│ Min-heap     │ O(n log k)   │ O(k)   │ Good for streaming/online    │
│ Quick Select │ O(n) avg     │ O(1)   │ Fastest average, modifies arr│
└──────────────┴──────────────┴────────┴──────────────────────────────┘
"""

import random
from typing import List
import heapq


# ─── Lomuto partition (returns pivot's final index) ──────────────────────────

def _partition(arr: List[int], lo: int, hi: int) -> int:
    """Randomized Lomuto partition. Returns final index of pivot."""
    rand = random.randint(lo, hi)
    arr[rand], arr[hi] = arr[hi], arr[rand]     # random pivot → arr[hi]
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1


# ─── Quick Select ────────────────────────────────────────────────────────────

def quickselect(arr: List[int], k: int) -> int:
    """Return the kth smallest element (1-indexed) in arr.
    
    Modifies arr in-place. O(n) average time.
    """
    arr = arr[:]                    # work on a copy to avoid mutating input
    lo, hi = 0, len(arr) - 1
    target = k - 1                  # convert to 0-indexed

    while lo <= hi:
        pi = _partition(arr, lo, hi)
        if pi == target:
            return arr[pi]
        elif pi < target:
            lo = pi + 1
        else:
            hi = pi - 1

    raise ValueError(f"k={k} out of range for array of length {len(arr)}")


# ─── Heap approach (for comparison) ─────────────────────────────────────────

def kth_smallest_heap(arr: List[int], k: int) -> int:
    """Return kth smallest using a max-heap of size k. O(n log k) time, O(k) space.
    
    Preferred when: streaming data, k << n, or you need top-k elements.
    """
    max_heap = []
    for x in arr:
        heapq.heappush(max_heap, -x)        # negate for max-heap
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return -max_heap[0]


# ─── Example ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    data = [7, 10, 4, 3, 20, 15]
    print("Array:", data)

    for k in [1, 2, 3, 4]:
        qs = quickselect(data, k)
        hp = kth_smallest_heap(data, k)
        print(f"  k={k}: quickselect={qs}, heap={hp}")

    # LeetCode 215: Kth Largest Element in an Array
    def kth_largest(nums: List[int], k: int) -> int:
        return quickselect(nums, len(nums) - k + 1)

    nums = [3, 2, 1, 5, 6, 4]
    print(f"\nKth largest (k=2) in {nums}: {kth_largest(nums, 2)}")  # 5
