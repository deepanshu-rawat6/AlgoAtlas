# Reverse String (LC 344)

Write a function that reverses a character array `s` in-place with O(1) extra memory.

## Approaches

### 1. Slice Reversal — O(n) time, O(n) space
`s[:] = s[::-1]` — creates a reversed copy and assigns back.

**Why it works:** Python slice assignment replaces the list contents in-place, but the slice itself is a new list — uses O(n) space.

### 2. Two Pointers — O(n) time, O(1) space
Left pointer at start, right at end. Swap `s[l]` and `s[r]`, move both inward. Stop when they meet.

**Why it works:** Swapping from both ends simultaneously reverses the array. Each element is touched exactly once; no extra space needed.

## Key Insight
Two-pointer swap from both ends: each swap places two elements in their final positions. The array is fully reversed after n/2 swaps.

## Edge Cases
- Single character → no swaps needed
- Even length → pointers meet between two middle elements
- Odd length → pointers meet at the middle element (no swap needed for it)
- All identical characters → swaps are no-ops but still correct
