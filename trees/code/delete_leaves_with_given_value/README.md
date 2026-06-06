# Delete Leaves With a Given Value (LC 1325)

Delete all leaf nodes with value equal to `target`. Repeat until no such leaves remain (a node that becomes a leaf after deletion should also be deleted if its value equals `target`).

## Approaches

### Post-Order DFS
- **Time:** O(n), **Space:** O(h)
- Process children before the current node (post-order). After recursing, check if the current node has become a leaf with value `target` — if so, return `None` (delete it). Otherwise return the node.

## Key Insight

Post-order is essential here: we must process children first so that when we check the current node, its children have already been cleaned up. A node that was not a leaf originally may become one after its children are deleted — post-order handles this cascading deletion naturally in a single pass.

## Edge Cases

- Root is a leaf with value `target` → return `None` (entire tree deleted).
- Chain of nodes all with value `target` → all deleted bottom-up in one pass.
- A node with value `target` but non-target children → not deleted (it's not a leaf).
- Target value not present → tree unchanged.
