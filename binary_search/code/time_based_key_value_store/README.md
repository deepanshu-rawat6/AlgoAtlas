# Time Based Key-Value Store (LC 981)

Design a key-value store that stores multiple values per key at different timestamps. `get(key, timestamp)` returns the value with the largest `timestamp_prev <= timestamp`.

## Approaches

### 1. Linear Scan
- **Time:** O(n) per get | **Space:** O(n)
- Store `(timestamp, value)` pairs per key. On `get`, scan all pairs and return the last one with `ts <= timestamp`.

### 2. Binary Search
- **Time:** O(log n) per get, O(1) per set | **Space:** O(n)
- Since `set` calls have strictly increasing timestamps, the list per key is always sorted.
- On `get`, use `bisect_right` to find the insertion point for `(timestamp, chr(127))` (a sentinel that sorts after any value at the same timestamp), then step back one to get the floor entry.

## Key Insight

Strictly increasing timestamps on `set` means each key's list is naturally sorted — no sorting needed. `bisect_right` with a high sentinel value finds the first entry strictly greater than the target timestamp; subtracting 1 gives the largest timestamp ≤ target. If the result index is -1, no valid entry exists.

## Edge Cases

- `get` with timestamp smaller than all stored timestamps → `bisect_right` returns 0, index becomes -1 → return `""`.
- `get` for a key that was never set → empty list → `bisect_right` returns 0 → return `""`.
- Exact timestamp match → `bisect_right` places after it, step back gives the exact entry.
- Multiple values at different timestamps for the same key → binary search finds the floor correctly.
