# House Robber III (LC 337)

Rob houses arranged in a binary tree. Adjacent (directly linked) houses can't both be robbed. Return the maximum amount that can be robbed.

## Approaches

### DFS with Memoization
- **Time:** O(n), **Space:** O(n)
- For each node, compute `rob_this` (rob current node + skip children, take grandchildren) and `skip_this` (skip current, take best of each child). Cache results by node reference.

### DFS Returning Pair (optimal)
- **Time:** O(n), **Space:** O(h)
- Each DFS call returns `(rob_this, skip_this)` for the subtree. `rob_this = node.val + left_skip + right_skip`. `skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)`. No memoization needed — each node is visited once.

## Key Insight

This is the tree version of House Robber I. The key is that skipping a node doesn't force you to rob its children — you take the best of rob/skip for each child independently. The pair-return approach avoids memoization by computing both options simultaneously in a single bottom-up pass.

## Edge Cases

- Single node → rob it (return its value).
- All nodes have value 0 → return 0.
- A path graph (linear tree) → reduces to the classic 1D House Robber problem.
- Robbing a node means skipping both its children, but grandchildren are free to be robbed.
