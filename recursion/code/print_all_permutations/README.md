# Print All Permutations

## Problem Statement
Given an array of distinct integers `nums`, return all possible permutations.

**Example:** nums=[1,2,3] → [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

---

## Approach 1: Swap-Based — O(n!) time, O(n) extra space

Fix one element at position `start` by swapping it with each element from
`start` to end. Recurse on `start+1`. Backtrack by swapping back.

**Why:** Operates in-place on the original array — no extra list of "remaining"
elements needed. The swap fixes a choice at the current position; backtracking
undoes it so the next choice can be tried.

**Why O(n!):** n choices at level 0, n-1 at level 1, … → n! leaves.

---

## Approach 2: Pick from Remaining — O(n!) time, O(n²) space

At each step, pick any element from `remaining` for the current position.
Pass a new `remaining` list (without the picked element) to the next call.

**Why:** More intuitive — directly models "choose one from what's left."
Slightly higher space cost due to list slicing at each level.

---

## Key Insight
Both approaches explore the same decision tree. Swap-based is preferred when
working in-place; pick-from-remaining is cleaner conceptually but allocates
more memory.

---

## Edge Cases
- Single element `[x]`: returns `[[x]]`.
- Two elements `[a,b]`: returns `[[a,b],[b,a]]`.
- Empty array: returns `[[]]` (one empty permutation).

---

## Complexity Summary
| Approach          | Time  | Space  |
|-------------------|-------|--------|
| Swap-based        | O(n!) | O(n)   |
| Pick from remaining | O(n!) | O(n²) |
