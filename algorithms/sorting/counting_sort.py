"""
Counting Sort
=============
Strategy   : Count occurrences of each value, compute prefix sums to place elements.
Stable     : Yes (iterate output array right-to-left)
In-place   : No  (O(k) count array + O(n) output array)
Time       : O(n + k)  where k = range of input values
Space      : O(n + k)

Use when:
- Input is integers (or can be mapped to integers)
- Range k is small relative to n  (e.g., ages, exam scores, characters)
- Stability is needed (e.g., as a subroutine in radix sort)

Do NOT use when:
- k >> n  (e.g., sorting 10 numbers in range 0–10^9)
- Input is floating point or strings with large alphabet
"""

from typing import List


def counting_sort(arr: List[int]) -> List[int]:
    """Return a new sorted list. Input must be non-negative integers.
    
    Stable: equal elements appear in original relative order.
    """
    if not arr:
        return []

    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Step 1: count occurrences
    for x in arr:
        count[x] += 1

    # Step 2: prefix sums — count[i] now = number of elements <= i
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 3: place elements in output (right-to-left for stability)
    output = [0] * len(arr)
    for x in reversed(arr):
        count[x] -= 1
        output[count[x]] = x

    return output


def counting_sort_with_offset(arr: List[int]) -> List[int]:
    """Handle negative integers by shifting by min value."""
    if not arr:
        return []
    min_val = min(arr)
    shifted = [x - min_val for x in arr]
    sorted_shifted = counting_sort(shifted)
    return [x + min_val for x in sorted_shifted]


# ─── Example ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    scores = [4, 2, 2, 8, 3, 3, 1]
    print("Original:", scores)
    print("Sorted  :", counting_sort(scores))

    # With negatives
    temps = [-3, 1, -1, 0, 2, -2]
    print("Temps   :", temps)
    print("Sorted  :", counting_sort_with_offset(temps))

    # Character sorting (map chars to ints)
    chars = ['d', 'a', 'c', 'b', 'a']
    as_ints = [ord(c) - ord('a') for c in chars]
    sorted_ints = counting_sort(as_ints)
    print("Chars   :", ''.join(chr(x + ord('a')) for x in sorted_ints))
