# Power Set (Recursive)

## Problem Statement
Given an array `nums`, return all possible subsets (the power set).
The solution set must not contain duplicate subsets.

**Example:** nums=[1,2,3] → [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

---

## Approach: Include / Exclude — O(2^n) time, O(2^n) space

At each index, make a binary choice:
- **Exclude** `nums[idx]`: recurse without adding it.
- **Include** `nums[idx]`: add it, recurse, then backtrack (pop).

**Why this works:** Every element is independently either in or out of a subset.
The binary branching at each of n positions generates exactly 2^n leaves, each
representing one unique subset.

**Why recursion is clean here:** The decision tree structure maps directly to
the call stack — each level handles one element's include/exclude decision.

---

## Key Insight
The include/exclude pattern is the foundation of most subset/combination
problems. Backtracking (pop after include) ensures the `current` list is
correctly restored before the exclude branch runs.

---

## Edge Cases
- Empty input `[]`: returns `[[]]` (only the empty subset).
- Single element `[x]`: returns `[[], [x]]`.
- Duplicates in input: this approach does not deduplicate; sort + skip needed for that variant.

---

## Complexity Summary
| Metric  | Value   |
|---------|---------|
| Time    | O(2^n)  |
| Space   | O(2^n)  |
| Subsets | 2^n     |
