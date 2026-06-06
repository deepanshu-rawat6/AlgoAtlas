# Merge Two Sorted Lists (LC 21)

Merge two sorted linked lists into one sorted list by splicing their nodes together.

## Approaches

### 1. Iterative with Dummy Head
- **Time:** O(n + m) | **Space:** O(1)
- Use a dummy node to simplify head selection. At each step, attach the smaller of the two current nodes to the result list and advance that pointer.
- After one list is exhausted, attach the remainder of the other.

### 2. Recursive
- **Time:** O(n + m) | **Space:** O(n + m) call stack
- Base case: if either list is None, return the other.
- Attach the smaller head and recurse on the rest.

## Key Insight

The dummy head eliminates the special case of choosing the initial head — we always append to `dummy.next` and return `dummy.next` at the end. The iterative approach is preferred in practice (O(1) space vs O(n+m) for recursion).

Both lists are already sorted, so we only ever need to compare the current front of each list — no lookahead needed.

## Edge Cases

- Both lists empty → return None.
- One list empty → return the other list as-is.
- Lists of different lengths → the remainder of the longer list is attached directly (no extra traversal).
- Duplicate values across lists → both are included; `<=` ensures stability.
