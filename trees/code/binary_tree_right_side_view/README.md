# Binary Tree Right Side View (LC 199)

Return the values of nodes visible when looking at the tree from the right side, ordered top to bottom.

## Approaches

### BFS (Level Order)
- **Time:** O(n), **Space:** O(n)
- Process the tree level by level. The last node in each level is visible from the right. Record `queue[-1].val` (or the last node processed in each level iteration).

### DFS (Right-First)
- **Time:** O(n), **Space:** O(h)
- DFS visiting the right child before the left. The first node visited at each depth is the rightmost node at that level. When `depth == len(result)`, append the current node's value.

## Key Insight

The right side view is simply the last node at each level. BFS makes this explicit. The DFS approach works because visiting right before left means the first time we reach a new depth, we're at the rightmost node of that level.

## Edge Cases

- Empty tree → return `[]`.
- Tree with only left children → the leftmost nodes are visible (they're the only nodes at each level).
- Perfectly balanced tree → right child is always visible.
