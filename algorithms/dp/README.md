# Dynamic Programming Patterns

## Files

| File | Contents |
|------|----------|
| [`knapsack.py`](knapsack.py) | 0/1 Knapsack, Unbounded Knapsack, Subset Sum, Coin Change, Partition |
| [`lcs_edit_distance.py`](lcs_edit_distance.py) | LCS, Edit Distance (Levenshtein), Shortest Common Supersequence |
| [`lis.py`](lis.py) | LIS O(n²) and O(n log n), path reconstruction, count LIS, non-decreasing variant |
| [`interval_dp.py`](interval_dp.py) | Matrix Chain, Burst Balloons, Palindrome Partitioning, Merge Stones |

---

## DP Pattern Classification

### 1. Linear DP — state depends on previous elements
- LIS, Kadane's (max subarray), Jump Game
- State: `dp[i]` = answer for prefix/suffix ending/starting at `i`

### 2. Knapsack DP — pick/skip items with a capacity constraint
- 0/1 Knapsack, Subset Sum, Coin Change, Partition Equal Subset
- State: `dp[i][w]` = answer using first `i` items with capacity `w`
- Key: **reverse** capacity loop for 0/1, **forward** for unbounded

### 3. String DP — two sequences, align characters
- LCS, Edit Distance, Longest Common Substring
- State: `dp[i][j]` = answer for `s1[:i]` and `s2[:j]`
- Recurrence branches on `s1[i-1] == s2[j-1]`

### 4. Interval DP — answer for [i,j] from sub-intervals
- Matrix Chain, Burst Balloons, Palindrome Partitioning
- **Always iterate by increasing interval length**
- State: `dp[i][j]` = answer for subarray/substring `[i..j]`

### 5. Tree DP — state propagated up/down a tree
- House Robber III, Binary Tree Cameras
- State: `dp[node]` = answer for subtree rooted at `node`

### 6. Bitmask DP — subset enumeration
- TSP, Assignment Problem, Hamiltonian Path
- State: `dp[mask][i]` = answer visiting nodes in `mask`, ending at `i`

---

## Complexity Summary

| Problem | Time | Space (optimized) |
|---------|------|-------------------|
| 0/1 Knapsack | O(n·W) | O(W) |
| Unbounded Knapsack | O(n·W) | O(W) |
| Coin Change | O(n·amount) | O(amount) |
| LCS | O(mn) | O(min(m,n)) |
| Edit Distance | O(mn) | O(min(m,n)) |
| LIS O(n²) | O(n²) | O(n) |
| LIS O(n log n) | O(n log n) | O(n) |
| Interval DP | O(n³) | O(n²) |

---

## Decision Guide

```
Is the problem asking for optimal value over a sequence?
├── Items with weight/value + capacity → Knapsack
├── Two sequences to align → LCS / Edit Distance
├── Increasing subsequence → LIS
└── Subarray/substring interval → Interval DP

Can items be reused?
├── Yes → Unbounded Knapsack (forward loop)
└── No  → 0/1 Knapsack (reverse loop)

Need path reconstruction?
└── Store parent/split pointers alongside dp table
```

---

## Space Optimization Cheat Sheet

**1D rolling array** (knapsack, coin change):
```python
dp = [0] * (capacity + 1)
for item in items:
    for w in range(capacity, item.weight - 1, -1):  # reverse for 0/1
        dp[w] = max(dp[w], dp[w - item.weight] + item.value)
```

**Two-row rolling** (LCS, edit distance):
```python
prev = [base_case] * (n + 1)
for i in range(1, m + 1):
    curr = [base_case] * (n + 1)
    for j in range(1, n + 1):
        curr[j] = recurrence(prev, curr, i, j)
    prev = curr
```
