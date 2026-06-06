"""
Bucket Sort
===========
Strategy   : Distribute elements into buckets, sort each bucket, concatenate.
Stable     : Yes (if inner sort is stable)
In-place   : No  (O(n + k) extra space for buckets)
Time       : O(n + k) average for uniform distribution, O(n²) worst case
Space      : O(n + k)

Use when:
- Input is uniformly distributed over a known range (e.g., floats in [0, 1))
- n is large and data is roughly uniform
- Can be adapted for integers by choosing bucket width

Do NOT use when:
- Data is heavily skewed (all elements fall into one bucket → O(n²))
- Range is unknown or unbounded
"""

from typing import List


def bucket_sort_floats(arr: List[float]) -> List[float]:
    """Sort floats in [0.0, 1.0) using bucket sort.
    
    Each bucket covers a range of 1/n. Uses insertion sort within buckets
    (efficient for small bucket sizes under uniform distribution).
    """
    n = len(arr)
    if n <= 1:
        return arr[:]

    buckets: List[List[float]] = [[] for _ in range(n)]

    # Distribute into buckets
    for x in arr:
        idx = int(x * n)            # maps [0,1) → [0, n-1]
        idx = min(idx, n - 1)       # guard for x == 1.0
        buckets[idx].append(x)

    # Sort each bucket with insertion sort (stable, fast for small lists)
    def insertion_sort(lst: List[float]) -> None:
        for i in range(1, len(lst)):
            key = lst[i]
            j = i - 1
            while j >= 0 and lst[j] > key:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = key

    result = []
    for bucket in buckets:
        insertion_sort(bucket)
        result.extend(bucket)
    return result


def bucket_sort_integers(arr: List[int], bucket_size: int = 5) -> List[int]:
    """Sort integers using bucket sort with configurable bucket width."""
    if not arr:
        return []
    min_val, max_val = min(arr), max(arr)
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets: List[List[int]] = [[] for _ in range(bucket_count)]

    for x in arr:
        buckets[(x - min_val) // bucket_size].append(x)

    result = []
    for bucket in buckets:
        bucket.sort()               # use Python's Timsort for each bucket
        result.extend(bucket)
    return result


# ─── Example ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    import random

    # Float example
    floats = [random.random() for _ in range(10)]
    print("Floats original:", [round(x, 3) for x in floats])
    print("Floats sorted  :", [round(x, 3) for x in bucket_sort_floats(floats)])

    # Integer example
    ints = [random.randint(0, 50) for _ in range(12)]
    print("Ints original  :", ints)
    print("Ints sorted    :", bucket_sort_integers(ints))
