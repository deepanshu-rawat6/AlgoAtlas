# Binary Tree Zigzag Level Order Traversal (LC 103)

Return the zigzag level order traversal: odd levels left-to-right, even levels right-to-left (alternating).

## Approaches

### BFS with Direction Flag
- **Time:** O(n), **Space:** O(n)
- Standard BFS level-order traversal. After collecting each level's values, reverse the list if the current direction is right-to-left. Toggle the direction flag after each level.

## Key Insight

The zigzag pattern is just level-order traversal with alternating reversal. Collecting the level normally and reversing is simpler and equally efficient compared to using a deque with direction-based insertion. The direction flag toggles after every level.

## Edge Cases

- Empty tree → return `[]`.
- Single node → `[[root.val]]` (level 0, left-to-right, no reversal needed).
- Two levels → first level is `[root.val]`, second level is reversed children.
- The reversal is applied to the collected list, not to the BFS queue — children are always enqueued left-to-right regardless of direction.
