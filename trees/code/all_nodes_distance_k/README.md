# All Nodes Distance K in Binary Tree (LC 863)

Given a binary tree, a target node, and integer k, return all node values at distance k from the target (distance = number of edges).

## Approaches

### Build Parent Map + BFS
- **Time:** O(n), **Space:** O(n)
- First pass: DFS to build a `parent` map so each node knows its parent (enabling upward traversal).
- Second pass: BFS from the target node in all three directions (left child, right child, parent). Stop when distance reaches k; collect all nodes at that distance.

## Key Insight

A binary tree only has downward edges, but distance k can require going upward (through a parent) and then back down. The parent map converts the tree into an undirected graph, making BFS straightforward. The visited set prevents revisiting nodes (which would cause infinite loops via parent→child→parent cycles).

## Edge Cases

- k = 0 → return `[target.val]`.
- k larger than the tree's diameter → return `[]`.
- Target is the root → no upward traversal possible (parent is `None`).
- Target is a leaf → only upward + sibling paths are available.
