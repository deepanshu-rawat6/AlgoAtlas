"""
Binary Search
=============
Strategy   : Repeatedly halve the search space on a sorted (or monotonic) domain.
Time       : O(log n)
Space      : O(1)

Variants:
1. exact        — find index of target value
2. lower_bound  — first index where arr[i] >= target  (leftmost insertion point)
3. upper_bound  — first index where arr[i] > target   (rightmost insertion point)
4. first_true   — first index where predicate(i) is True (generalized template)
5. search_rotated — binary search on a rotated sorted array
6. search_on_answer — template for "minimize/maximize X such that feasible(X)"

Key insight: always think in terms of "which half can I eliminate?"
"""

from typing import List, Callable, Optional


# ─── 1. Exact match ──────────────────────────────────────────────────────────

def binary_search(arr: List[int], target: int) -> int:
    """Return index of target in sorted arr, or -1 if not found."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2      # avoids overflow (matters in other langs)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# ─── 2. Lower bound ──────────────────────────────────────────────────────────

def lower_bound(arr: List[int], target: int) -> int:
    """Return first index i where arr[i] >= target.
    
    Returns len(arr) if all elements < target.
    Equivalent to bisect_left.
    """
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


# ─── 3. Upper bound ──────────────────────────────────────────────────────────

def upper_bound(arr: List[int], target: int) -> int:
    """Return first index i where arr[i] > target.
    
    Returns len(arr) if all elements <= target.
    Equivalent to bisect_right.
    """
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


# ─── 4. First true (generalized template) ────────────────────────────────────

def first_true(lo: int, hi: int, predicate: Callable[[int], bool]) -> Optional[int]:
    """Return the smallest integer in [lo, hi] where predicate is True.
    
    Assumes predicate is monotonic: False...False True...True.
    Returns None if predicate is False for all values.
    
    Template for "binary search on answer" problems.
    """
    result = None
    while lo <= hi:
        mid = (lo + hi) // 2
        if predicate(mid):
            result = mid
            hi = mid - 1    # try to find an earlier True
        else:
            lo = mid + 1
    return result


# ─── 5. Rotated sorted array ─────────────────────────────────────────────────

def search_rotated(arr: List[int], target: int) -> int:
    """Search target in a rotated sorted array with no duplicates.
    
    Example: [4, 5, 6, 7, 0, 1, 2] rotated from [0,1,2,4,5,6,7]
    Key: one half is always sorted — use that to decide which half to search.
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        # Left half is sorted
        if arr[lo] <= arr[mid]:
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


# ─── 6. Binary search on answer (template) ───────────────────────────────────

def min_capacity_to_ship(weights: List[int], days: int) -> int:
    """LeetCode 1011: Capacity To Ship Packages Within D Days.
    
    Binary search on answer: find minimum capacity such that we can ship
    all packages within `days` days.
    
    feasible(cap): can we ship everything with this capacity in <= days?
    """
    def feasible(capacity: int) -> bool:
        current_load, day_count = 0, 1
        for w in weights:
            if current_load + w > capacity:
                day_count += 1
                current_load = 0
            current_load += w
        return day_count <= days

    lo = max(weights)           # minimum possible: must fit heaviest package
    hi = sum(weights)           # maximum possible: ship everything in one day
    return first_true(lo, hi, feasible)


# ─── Example ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 11, 13]
    print("Array:", arr)
    print("binary_search(7)    :", binary_search(arr, 7))       # 3
    print("binary_search(6)    :", binary_search(arr, 6))       # -1
    print("lower_bound(6)      :", lower_bound(arr, 6))         # 3 (first >= 6)
    print("upper_bound(7)      :", upper_bound(arr, 7))         # 4 (first > 7)

    rotated = [4, 5, 6, 7, 0, 1, 2]
    print("\nRotated:", rotated)
    print("search_rotated(0)   :", search_rotated(rotated, 0))  # 4
    print("search_rotated(3)   :", search_rotated(rotated, 3))  # -1

    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("\nMin capacity (10 days):", min_capacity_to_ship(weights, 5))  # 15
