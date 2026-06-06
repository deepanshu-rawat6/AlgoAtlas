# LC 978 — Longest Turbulent Subarray

A subarray is turbulent if the comparison sign strictly alternates between adjacent pairs (e.g., `> < > <` or `< > < >`). Return the length of the longest turbulent subarray.

## Approaches

### 1. DP with inc/dec Arrays
- **Time:** O(n) | **Space:** O(n)
- `inc[i]` = length of turbulent subarray ending at `i` where `arr[i-1] < arr[i]`.
- `dec[i]` = length ending at `i` where `arr[i-1] > arr[i]`.
- If `arr[i] > arr[i-1]`: `inc[i] = dec[i-1] + 1`. If less: `dec[i] = inc[i-1] + 1`. Equal: both stay 1.

### 2. Sliding Window
- **Time:** O(n) | **Space:** O(1)
- Track current turbulent length. Reset to 2 when the alternation breaks (but adjacent elements differ), or to 1 when elements are equal.

## Key Insight

The turbulent property requires the comparison sign to **flip** at each step. The DP captures this by tracking two separate lengths: one for subarrays ending with an upswing (`inc`) and one ending with a downswing (`dec`). An upswing can only extend a previous downswing and vice versa. Equal adjacent elements break turbulence entirely.

## Edge Cases

- Single element: Return 1.
- All equal elements: Return 1 (no turbulence possible).
- Two equal adjacent elements in the middle: Resets the current turbulent length.
- Strictly alternating array: The entire array is turbulent.
