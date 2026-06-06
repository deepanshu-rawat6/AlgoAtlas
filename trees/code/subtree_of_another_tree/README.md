# Subtree of Another Tree (LC 572)

Return `true` if `subRoot` is a subtree of `root` — i.e., there exists a node in `root` whose subtree is identical to `subRoot`.

## Approaches

### Recursive DFS + isSameTree
- **Time:** O(m * n) where m = nodes in root, n = nodes in subRoot
- **Space:** O(m) recursion stack
- For each node in `root`, check if the subtree rooted there is identical to `subRoot` using a `isSameTree` helper. If not, recurse on left and right children.

## Key Insight

A subtree match requires exact structural and value equality from that node downward — the same check as "same tree." By reusing `isSameTree` at every node in `root`, we cover all possible subtree roots. The recursion terminates early when a match is found.

## Edge Cases

- `subRoot` is the entire `root` → valid (a tree is a subtree of itself).
- `subRoot` is a single node → check if any node in `root` has that value and no children.
- A node in `root` has the same value as `subRoot`'s root but different structure → `isSameTree` returns `False`, recursion continues.
- `root` is `None` → `False` (can't contain any subtree).
