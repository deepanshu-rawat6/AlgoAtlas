# Count Good Nodes in Binary Tree (LC 1448)

A node X is "good" if no node on the path from root to X has a value greater than X. Return the count of good nodes.

## Approaches

### DFS with Running Maximum
- **Time:** O(n), **Space:** O(h)
- DFS passing the maximum value seen so far on the current root-to-node path. A node is good if `node.val >= max_so_far`. Update `max_so_far = max(max_so_far, node.val)` before recursing into children.

## Key Insight

A node is good iff it's a "new maximum" on its root-to-node path (or ties the current max). By tracking the running max as we descend, we can check each node in O(1). The root is always good (no ancestors to be greater).

## Edge Cases

- Single node → always good (count = 1).
- All nodes have the same value → all are good (each equals the running max).
- Strictly decreasing path → only the root is good.
- Negative values → the running max starts at `root.val`, which may be negative; comparisons still work correctly.
