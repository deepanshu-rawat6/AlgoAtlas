"""
Merge Sort
==========
Strategy   : Divide and conquer — split array in half, sort each half, merge.
Stable     : Yes (equal elements keep original order)
In-place   : No  (requires O(n) auxiliary space)
Time       : O(n log n) — all cases
Space      : O(n) auxiliary

Use when:
- Stability is required
- Sorting linked lists (no random access needed)
- External sorting (data doesn't fit in memory)
- Guaranteed worst-case O(n log n) is needed
"""

from typing import List


# ─── Core merge ──────────────────────────────────────────────────────────────

def merge(arr: List[int], left: int, mid: int, right: int) -> None:
    """Merge two sorted subarrays arr[left:mid+1] and arr[mid+1:right+1] in-place."""
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:   # <= keeps sort stable
            arr[k] = L[i]; i += 1
        else:
            arr[k] = R[j]; j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]; i += 1; k += 1
    while j < len(R):
        arr[k] = R[j]; j += 1; k += 1


# ─── Top-down (recursive) ────────────────────────────────────────────────────

def merge_sort_top_down(arr: List[int], left: int = 0, right: int = None) -> None:
    """Sort arr[left:right+1] in-place using recursive top-down merge sort."""
    if right is None:
        right = len(arr) - 1
    if left >= right:
        return
    mid = (left + right) // 2
    merge_sort_top_down(arr, left, mid)
    merge_sort_top_down(arr, mid + 1, right)
    merge(arr, left, mid, right)


# ─── Bottom-up (iterative) ───────────────────────────────────────────────────

def merge_sort_bottom_up(arr: List[int]) -> None:
    """Sort arr in-place using iterative bottom-up merge sort.
    
    Avoids recursion overhead; same O(n log n) time, O(n) space.
    Starts with width=1 (single elements are sorted), doubles each pass.
    """
    n = len(arr)
    width = 1
    while width < n:
        for left in range(0, n, 2 * width):
            mid = min(left + width - 1, n - 1)
            right = min(left + 2 * width - 1, n - 1)
            if mid < right:
                merge(arr, left, mid, right)
        width *= 2


# ─── Example ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    import random

    data = random.sample(range(100), 10)
    print("Original :", data)

    a = data[:]
    merge_sort_top_down(a)
    print("Top-down :", a)

    b = data[:]
    merge_sort_bottom_up(b)
    print("Bottom-up:", b)

    # Stability demo — sort (value, index) pairs by value
    pairs = [(3, 'a'), (1, 'b'), (3, 'c'), (2, 'd')]
    merge_sort_top_down(pairs)   # won't work directly; shown conceptually
    # Real stability: equal keys preserve original order
    words = ["banana", "apple", "cherry", "apricot"]
    merge_sort_top_down(words)
    print("Strings  :", words)
