# Maximum Width of Binary Tree (LC 662)

Return the maximum width of a binary tree. Width of a level = distance between the leftmost and rightmost non-null nodes (including null nodes in between).

## Approaches

### BFS with Position Indexing
- **Time:** O(n), **Space:** O(n)
- Assign each node a position index: root = 0, left child = `2*i`, right child = `2*i+1` (like a heap array). BFS level by level. Width of each level = `last_index - first_index + 1`. Normalize indices at each level (subtract the first index) to prevent integer overflow for deep trees.

## Key Insight

The heap-style indexing encodes the position of each node in a complete binary tree, including the "virtual" null nodes between real nodes. The width is simply the span of indices at each level. Normalization (subtracting the level's first index) is critical — without it, indices grow exponentially and overflow for trees with depth > 60.

## Edge Cases

- Single node → width is 1.
- Left-skewed tree → width is always 1 (only one node per level).
- A tree where the widest level is not the deepest level — BFS checks every level and takes the max.
- Overflow prevention: normalization ensures indices stay small regardless of tree depth.
