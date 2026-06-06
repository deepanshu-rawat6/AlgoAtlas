# Tree Algorithms

## Files

| File | Contents |
|------|----------|
| [`traversals.py`](traversals.py) | Inorder/Preorder/Postorder (recursive + iterative), Level-order BFS, Morris O(1) space |
| [`bst_operations.py`](bst_operations.py) | Search, Insert, Delete, Min/Max, Successor/Predecessor, Validate BST |
| [`segment_tree.py`](segment_tree.py) | Build/Update/Query (sum, min, max), Lazy propagation for range updates |
| [`trie.py`](trie.py) | Insert, Search, StartsWith, Delete, Wildcard search, Autocomplete |

---

## Complexity Summary

| Operation | Traversals | BST | Segment Tree | Trie |
|-----------|-----------|-----|--------------|------|
| Build | O(n) | O(n log n) | O(n) | O(n·w) |
| Search/Query | O(n) | O(h) | O(log n) | O(w) |
| Insert/Update | — | O(h) | O(log n) | O(w) |
| Delete | — | O(h) | — | O(w) |
| Space | O(h) / O(1) Morris | O(n) | O(4n) | O(n·Σ) |

`h` = tree height (O(log n) balanced, O(n) skewed), `w` = word length, `Σ` = alphabet size

---

## When to Use What

**Traversals**
- Inorder → sorted output from BST; expression evaluation
- Preorder → serialize/copy a tree; directory listing
- Postorder → delete tree; evaluate postfix expressions
- Level-order → shortest path in unweighted tree; level-by-level processing
- Morris → when O(1) extra space is required (embedded systems, streaming)

**BST**
- Ordered dynamic set with O(log n) operations (use balanced BST like AVL/Red-Black in practice)
- Range queries, floor/ceiling, rank/select operations
- Validate that a tree satisfies BST property

**Segment Tree**
- Range aggregate queries (sum/min/max) with point updates → plain segment tree
- Range updates + range queries → lazy propagation segment tree
- Typical problems: range sum, range minimum query (RMQ), count inversions

**Trie**
- Prefix-based lookups: autocomplete, spell check, IP routing
- When you need to search many strings sharing common prefixes
- Wildcard/regex matching over a dictionary
- Faster than hash map when prefix queries are needed

---

## Key Patterns

```
# Generic tree DFS template
def dfs(node):
    if not node:
        return base_case
    left  = dfs(node.left)
    right = dfs(node.right)
    return combine(node.val, left, right)

# Generic BFS template
from collections import deque
def bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        process(node)
        for child in [node.left, node.right]:
            if child:
                queue.append(child)
```
