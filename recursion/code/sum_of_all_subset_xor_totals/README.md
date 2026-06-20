# LC 1863 — Sum of All Subset XOR Totals

The XOR total of an array is the XOR of all its elements (0 if empty). Return the sum of XOR totals for every subset of `nums`.

## Approaches

### 1. Backtracking over All Subsets
- **Time:** O(2ⁿ) | **Space:** O(n) call stack
- At each index, branch: include `nums[i]` in the current XOR or skip it. At each leaf (all elements processed), add the current XOR value to the total sum.

### 2. Math Shortcut
- **Time:** O(n) | **Space:** O(1)
- Answer = `(OR of all nums) << (n - 1)`. Each bit that appears in any element contributes to exactly `2^(n-1)` subsets.

## Key Insight

For any bit position, if that bit appears in at least one element, it contributes to exactly `2^(n-1)` subset XOR totals (half of all subsets). The OR of all elements tells us which bits appear at least once. Multiplying by `2^(n-1)` gives the total contribution of all bits. The backtracking approach is more general but the math shortcut is elegant and O(n).

Note: The solution stub in `solution.py` has `pass` — both approaches are described above.

## Edge Cases

- Single element `[x]`: Two subsets — `[]` (XOR=0) and `[x]` (XOR=x). Sum = x.
- All zeros: All XOR totals are 0, sum = 0.
- `nums = [1, 3]`: Subsets XOR totals: 0, 1, 3, 2. Sum = 6.
