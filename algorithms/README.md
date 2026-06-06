# Algorithms Reference

Documented implementations of core DSA algorithms for LeetCode and interviews.

## Structure

```
algorithms/
├── trees/
│   ├── traversals.py       — Inorder/Preorder/Postorder, BFS, Morris O(1)
│   ├── bst_operations.py   — Search/Insert/Delete, Min/Max, Successor, Validate
│   ├── segment_tree.py     — Range queries, lazy propagation
│   └── trie.py             — Prefix tree, wildcard, autocomplete
├── strings/
│   ├── kmp.py              — Pattern matching O(n+m)
│   ├── rabin_karp.py       — Rolling hash, multi-pattern search
│   └── manacher.py         — Longest palindrome O(n)
└── dp/
    ├── knapsack.py         — 0/1, unbounded, subset sum, coin change
    ├── lcs_edit_distance.py — LCS, Levenshtein distance
    ├── lis.py              — O(n²) and O(n log n) LIS
    └── interval_dp.py      — Matrix chain, burst balloons, palindrome cuts
```

---

## Master Complexity Table

| Algorithm | Time | Space | When to Use |
|-----------|------|-------|-------------|
| **Tree Traversals** | | | |
| Recursive DFS | O(n) | O(h) | General tree problems |
| Iterative DFS | O(n) | O(h) | Avoid stack overflow on deep trees |
| Morris Traversal | O(n) | O(1) | Space-constrained inorder/preorder |
| Level-order BFS | O(n) | O(w) | Level processing, shortest path |
| **BST** | | | |
| Search/Insert/Delete | O(h) | O(h) | Ordered dynamic set |
| Validate BST | O(n) | O(h) | Verify BST property |
| **Segment Tree** | | | |
| Build | O(n) | O(4n) | One-time setup |
| Point update + range query | O(log n) | O(4n) | Static structure, point updates |
| Range update + range query | O(log n) | O(4n) | Lazy propagation needed |
| **Trie** | | | |
| Insert/Search/Delete | O(w) | O(n·Σ) | Prefix queries, autocomplete |
| Wildcard search | O(26^w) worst | — | Dictionary matching with `.` |
| **String Matching** | | | |
| KMP | O(n+m) | O(m) | Single pattern, guaranteed linear |
| Rabin-Karp | O(n+m) avg | O(1) | Multiple patterns, 2D matching |
| Manacher | O(n) | O(n) | All palindrome problems |
| **Dynamic Programming** | | | |
| 0/1 Knapsack | O(n·W) | O(W) | Pick/skip items, capacity limit |
| Unbounded Knapsack | O(n·W) | O(W) | Reusable items (coin change) |
| LCS | O(mn) | O(min(m,n)) | Common subsequence of two strings |
| Edit Distance | O(mn) | O(min(m,n)) | String transformation cost |
| LIS O(n²) | O(n²) | O(n) | Small n, need path reconstruction |
| LIS O(n log n) | O(n log n) | O(n) | Large n, length only |
| Interval DP | O(n³) | O(n²) | Optimal split of contiguous range |

`h` = tree height, `w` = word length, `Σ` = alphabet size, `W` = capacity, `n/m` = input sizes

---

## Quick Decision Guide

```
Pattern matching in text?
├── Single pattern, must be O(n+m) → KMP
├── Multiple patterns → Rabin-Karp
└── Palindrome substring → Manacher

Tree problem?
├── Need sorted order / BST property → BST operations
├── Range queries on array → Segment Tree
├── Prefix/word lookup → Trie
└── Just traverse → traversals.py

DP problem?
├── Items + capacity → Knapsack
│   ├── Each item once → 0/1 (reverse loop)
│   └── Reuse allowed → Unbounded (forward loop)
├── Two strings → LCS or Edit Distance
├── Increasing subsequence → LIS
│   ├── n ≤ 1000 → O(n²) with path
│   └── n > 1000 → O(n log n)
└── Optimal split of interval → Interval DP
    ├── Minimize cost → Matrix Chain template
    └── Maximize value → Burst Balloons template
```

---

## Running Any File

All files are self-contained with `if __name__ == '__main__'` examples:

```bash
python trees/traversals.py
python trees/bst_operations.py
python trees/segment_tree.py
python trees/trie.py

python strings/kmp.py
python strings/rabin_karp.py
python strings/manacher.py

python dp/knapsack.py
python dp/lcs_edit_distance.py
python dp/lis.py
python dp/interval_dp.py
```

No external dependencies — standard library only.
