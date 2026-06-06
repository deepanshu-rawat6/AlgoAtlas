# Construct Quad Tree (LC 427)

Given an n×n binary grid (n is a power of 2), construct a Quad-Tree. Each node is a leaf if its region is uniform (all 0s or all 1s); otherwise split into four equal quadrants.

## Approaches

### Recursive Divide and Conquer
- **Time:** O(n² log n) — each level checks O(n²) cells total across all nodes
- **Space:** O(log n) recursion depth
- Check if all values in the current region are the same. If yes, create a leaf node. If no, split into four equal quadrants (top-left, top-right, bottom-left, bottom-right) and recurse on each.

## Key Insight

The divide-and-conquer mirrors the quad-tree structure directly. The uniformity check is the termination condition — once a region is uniform, no further splitting is needed. Since n is always a power of 2, halving is always exact.

## Edge Cases

- 1×1 grid → always a leaf node.
- All-uniform grid → single leaf node at the root.
- Checkerboard pattern → maximum depth (log n levels), all leaves at the bottom.
- The `val` of non-leaf nodes can be anything (the solution uses `True`); only leaf `val` is meaningful.
