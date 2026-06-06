# Binary Tree Level Order Traversal (LC 102)

Return the level-order traversal of a binary tree as a list of lists (one list per level, left to right).

## Approaches

### BFS with Queue
- **Time:** O(n), **Space:** O(n)
- Use a deque. Each iteration, process all nodes currently in the queue (that's one level), collect their values, and enqueue their children. The queue size at the start of each iteration equals the level width.

### DFS with Depth Index
- **Time:** O(n), **Space:** O(n)
- DFS with a `depth` parameter. When `depth == len(result)`, append a new list. Append the current node's value to `result[depth]`.

## Key Insight

BFS naturally processes nodes level by level. The key is snapshotting `len(queue)` at the start of each level iteration — this tells you exactly how many nodes belong to the current level before any children are enqueued. The DFS approach works because DFS visits nodes in a predictable depth order, and the depth index maps directly to the result list index.

## Edge Cases

- Empty tree → return `[]`.
- Single node → return `[[node.val]]`.
- Unbalanced tree → levels have varying widths; BFS handles this naturally.
