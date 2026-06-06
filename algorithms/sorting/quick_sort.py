"""
Quick Sort
==========
Strategy   : Pick a pivot, partition array so left < pivot <= right, recurse.
Stable     : No
In-place   : Yes (O(log n) stack space)
Time       : O(n log n) average, O(n²) worst (avoided with random pivot)
Space      : O(log n) average stack depth

Use when:
- General-purpose in-place sorting
- Cache performance matters (good locality)
- Average-case speed is priority over worst-case guarantee

Partition schemes:
- Lomuto  : simpler code, slightly more swaps
- Hoare   : fewer swaps, original scheme, trickier to implement correctly
"""

import random
from typing import List


# ─── Lomuto partition ────────────────────────────────────────────────────────

def _partition_lomuto(arr: List[int], low: int, high: int) -> int:
    """Partition using last element as pivot. Returns final pivot index."""
    pivot = arr[high]
    i = low - 1                     # i tracks boundary of elements <= pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_lomuto(arr: List[int], low: int = 0, high: int = None) -> None:
    if high is None:
        high = len(arr) - 1
    if low < high:
        # Randomize pivot to avoid O(n²) on sorted input
        rand = random.randint(low, high)
        arr[rand], arr[high] = arr[high], arr[rand]
        pi = _partition_lomuto(arr, low, high)
        quick_sort_lomuto(arr, low, pi - 1)
        quick_sort_lomuto(arr, pi + 1, high)


# ─── Hoare partition ─────────────────────────────────────────────────────────

def _partition_hoare(arr: List[int], low: int, high: int) -> int:
    """Hoare partition: pivot is first element, returns index where left/right meet.
    
    Note: pivot is NOT necessarily at the returned index after partitioning.
    Recurse on [low, pi] and [pi+1, high].
    """
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort_hoare(arr: List[int], low: int = 0, high: int = None) -> None:
    if high is None:
        high = len(arr) - 1
    if low < high:
        # Randomize pivot: swap random element to front before Hoare partition
        rand = random.randint(low, high)
        arr[rand], arr[low] = arr[low], arr[rand]
        pi = _partition_hoare(arr, low, high)
        quick_sort_hoare(arr, low, pi)
        quick_sort_hoare(arr, pi + 1, high)


# ─── Example ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    data = [3, 6, 8, 10, 1, 2, 1]
    print("Original:", data)

    a = data[:]
    quick_sort_lomuto(a)
    print("Lomuto  :", a)

    b = data[:]
    quick_sort_hoare(b)
    print("Hoare   :", b)

    # Worst case without randomization: already sorted array
    sorted_data = list(range(10))
    quick_sort_lomuto(sorted_data)   # safe because we randomize pivot
    print("Sorted  :", sorted_data)
