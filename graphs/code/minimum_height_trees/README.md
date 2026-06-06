# Minimum Height Trees (LC 310)

Given a tree of `n` nodes, find all nodes that minimize the tree height when chosen as
root. There are at most 2 such nodes.

## Approaches

### 1. BFS from Each Node (brute force)
**Complexity:** O(V²) time, O(V + E) space

For each node, BFS to compute the tree height. Return nodes with minimum height.

**Why it works:** Correct but slow — recomputes the entire tree height for each candidate root.

### 2. Iterative Leaf Removal (optimal)
**Complexity:** O(V + E) time, O(V + E) space

Repeatedly remove leaf nodes (degree 1) layer by layer until 1 or 2 nodes remain.
These are the MHT roots.

**Why it works:** The center of a tree (the node(s) minimizing max distance to any leaf)
is found by peeling leaves inward. This is analogous to finding the tree's centroid.
A tree always has 1 or 2 centers.

## Key Insight

The MHT root(s) are the **center(s)** of the tree — the node(s) that minimize the
maximum distance to any leaf. Leaf removal converges to the center in O(V) time,
similar to topological sort from the outside in.

## Edge Cases

- `n = 1` — return `[0]` (single node is its own root).
- `n = 2` — both nodes are valid roots, return both.
- Star graph (one center, all others leaves) — return the center node.
- Path graph — return the middle 1 or 2 nodes.
