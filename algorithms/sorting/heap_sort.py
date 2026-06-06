"""
Heap Sort
=========
Strategy   : Build a max-heap, then repeatedly extract the max to the end.
Stable     : No
In-place   : Yes (O(1) extra space)
Time       : O(n log n) — all cases
Space      : O(1)

Use when:
- O(1) extra space is required AND O(n log n) worst-case is needed
- Real-time systems where worst-case matters more than average-case
- Note: worse cache performance than quick sort in practice

Key operations:
- sift_down : restore heap property downward from index i
- build_heap : O(n) heapify from bottom up (not O(n log n) top-down)
"""

from typing import List


def sift_down(arr: List[int], i: int, heap_size: int) -> None:
    """Push arr[i] down to its correct position in the max-heap arr[0:heap_size]."""
    largest = i
    left  = 2 * i + 1
    right = 2 * i + 2

    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        sift_down(arr, largest, heap_size)


def build_heap(arr: List[int]) -> None:
    """Convert arr into a max-heap in O(n) time.
    
    Start from the last non-leaf node and sift down each node.
    Last non-leaf is at index n//2 - 1.
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)


def heap_sort(arr: List[int]) -> None:
    """Sort arr in-place in ascending order using heap sort."""
    build_heap(arr)                         # O(n): max element at arr[0]
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0] # move max to sorted region
        sift_down(arr, 0, end)              # restore heap on remaining elements


# ─── Example ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    data = [12, 11, 13, 5, 6, 7]
    print("Original  :", data)

    heap_sort(data)
    print("Heap sorted:", data)

    # Show intermediate heap state
    demo = [4, 10, 3, 5, 1]
    build_heap(demo)
    print("Max-heap  :", demo, "  (root is max:", demo[0], ")")
