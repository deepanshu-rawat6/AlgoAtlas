# Amount of Time for Binary Tree to Be Infected (LC 2385)

A fire starts at node `start` and spreads to all adjacent nodes each second. Return the minimum time for the entire tree to burn.

## Approaches

### Build Parent Map + BFS (Multi-source spread)
- **Time:** O(n), **Space:** O(n)
- First pass: DFS to build a `parent` map and locate the `start` node.
- Second pass: BFS from `start`, spreading to left child, right child, and parent each second. Count BFS levels (each level = 1 second). Stop when no more nodes can be reached.

## Key Insight

This is identical to "All Nodes Distance K" but instead of finding nodes at exactly distance k, we want the maximum distance from `start` to any node — that's the time for the last node to burn. BFS naturally gives this: the number of levels processed equals the answer. The parent map is essential for fire to spread upward through the tree.

## Edge Cases

- Single node → returns 0 (already burning at t=0).
- `start` is a leaf → fire must travel up to the root and then down the other subtree.
- `start` is the root → fire spreads purely downward; answer is the tree height.
- The time counter starts at -1 and increments before processing each level, so a single-node tree correctly returns 0.
