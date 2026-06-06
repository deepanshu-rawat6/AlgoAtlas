# Sort Stack Using Recursion

Sort a stack in ascending order (smallest on top) using only recursion — no auxiliary data structures allowed.

## Approaches

### 1. Pop + Sort + Insert in Sorted Position
- **Time:** O(n²) | **Space:** O(n) call stack
- `sortStack`: pop the top, recursively sort the remaining stack, then insert the popped element into its correct sorted position using `_insertSorted`.
- `_insertSorted`: if stack is empty or top ≤ value, push. Otherwise, pop the top, recurse to find the right position, then restore the top.

## Key Insight

This is recursive insertion sort on a stack. `sortStack` reduces the problem by one element (pop top, sort rest), then `_insertSorted` places the element in the correct position by temporarily removing larger elements, inserting, and restoring them. The call stack serves as the only auxiliary storage. The pattern mirrors `reverseStack` but with a sorted insertion instead of bottom insertion.

## Edge Cases

- Empty stack: Return as-is.
- Single element: Already sorted.
- Already sorted: `_insertSorted` finds the correct position immediately (no extra work).
- Reverse sorted: Maximum recursion depth for `_insertSorted` at each step.
