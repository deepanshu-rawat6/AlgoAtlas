# Count and Say — LC 38

## Problem

The count-and-say sequence: each term describes the previous one by counting consecutive identical digits.

- `1` → "1"
- `2` → "11" (one 1)
- `3` → "21" (two 1s)
- `4` → "1211" (one 2, one 1)
- `5` → "111221"

Return the nth term.

## Approach: Iterative Simulation

**Why iterative?** Each term depends only on the previous one. Build term by term, n-1 times.

**Steps:**
1. Start with `result = "1"`
2. For each iteration: scan groups of consecutive identical chars
3. Each group contributes `str(count) + char` to the next term

**With `itertools.groupby`:** Pythonic one-liner per iteration.

**Complexity:** O(n × L) where L = average term length (grows roughly 30% per step)

## Key Insight

"Describe what you see": read the current string aloud as counts of consecutive digits. The description becomes the next term.

## Edge Cases

- n=1 → return "1" directly (no iteration)
- The sequence only contains digits 1, 2, 3 (provable by induction)
