# Guess Number Higher or Lower (LC 374)

A number is picked from 1 to n. Use the `guess(num)` API (returns -1/0/1) to find it.

## Approaches

### 1. Linear Scan
- **Time:** O(n) | **Space:** O(1)
- Try every number from 1 to n until `guess(i) == 0`.

### 2. Binary Search
- **Time:** O(log n) | **Space:** O(1)
- Binary search in `[1, n]`. Call `guess(mid)`:
  - `0` → found, return `mid`.
  - `1` → pick is higher, search right (`lo = mid + 1`).
  - `-1` → pick is lower, search left (`hi = mid - 1`).

## Key Insight

The `guess` API provides a three-way comparison, which is exactly what binary search needs. The search space halves with each call. This is the same as standard binary search, just with the comparison externalized to an API instead of a direct array lookup.

## Edge Cases

- `n = 1`, `pick = 1` → single iteration, `guess(1) == 0`.
- `pick = n` (maximum) → `lo` converges to `n`.
- `pick = 1` (minimum) → `hi` converges to 1.
- Large `n` (up to 2³¹ - 1): use `(lo + hi) // 2` to avoid overflow (Python handles this natively).
