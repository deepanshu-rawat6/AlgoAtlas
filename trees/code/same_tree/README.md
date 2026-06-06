# Same Tree (LC 100)

Given roots of two binary trees, return `true` if they are structurally identical with the same node values.

## Approaches

### Recursive DFS
- **Time:** O(n), **Space:** O(h)
- Both None → `True`. One None → `False`. Values differ → `False`. Otherwise recurse on both left and right pairs.

### Iterative BFS
- **Time:** O(n), **Space:** O(n)
- Use a queue of node pairs. For each pair: both None → skip; one None or values differ → `False`; otherwise enqueue their children pairs.

## Key Insight

Two trees are the same iff every corresponding node pair has the same value and the same structure. The recursion checks this pair by pair. The base cases handle structural differences (one subtree has a node where the other has None).

## Edge Cases

- Both empty → `True`.
- One empty, one not → `False`.
- Same structure but different values → `False` (caught by value comparison).
- Same values but different structure → `False` (caught by None checks).
