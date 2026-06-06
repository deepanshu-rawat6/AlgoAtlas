# LC 168 — Excel Sheet Column Title

Given a column number, return its Excel column title (A=1, B=2, ..., Z=26, AA=27, ...).

## Approaches

### 1. Base-26 with 1-Indexing Adjustment
- **Time:** O(log n) | **Space:** O(log n)
- Subtract 1 before taking modulo 26 to convert from 1-indexed to 0-indexed. `char = chr((columnNumber - 1) % 26 + ord('A'))`. Then `columnNumber = (columnNumber - 1) // 26`. Repeat until 0.

## Key Insight

Standard base-26 doesn't work directly because Excel uses 1-indexed letters (no "zero" digit — there's no column "0"). Subtracting 1 before each modulo operation shifts the range from `[1, 26]` to `[0, 25]`, making it compatible with standard modulo arithmetic. Without the `-1`, column 26 (Z) would incorrectly map to 0 instead of Z.

## Edge Cases

- `columnNumber = 1`: Return "A".
- `columnNumber = 26`: Return "Z" (not "Z0" — the `-1` trick handles this).
- `columnNumber = 27`: Return "AA".
- `columnNumber = 701`: Return "ZY".
- Large values (up to 2³¹ - 1): The loop terminates in O(log₂₆ n) ≈ O(log n) steps.
