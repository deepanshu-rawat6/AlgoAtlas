# Evaluate Division (LC 399)

Given equations like `a/b = k`, answer queries of the form `c/d = ?`. Return `-1.0` if
the answer doesn't exist (unknown variable or disconnected components).

## Approaches

### 1. BFS on Weighted Graph
**Complexity:** O(Q · (V + E)) time, O(V + E) space

Build a weighted directed graph: edge `a → b` with weight `k`, edge `b → a` with weight
`1/k`. For each query `(c, d)`, BFS from `c` multiplying edge weights along the path.

**Why it works:** Division chains multiply: `a/b · b/c = a/c`. BFS finds a path from
`c` to `d` and the product of weights along the path gives the answer.

### 2. Union-Find with Weights (optimal)
**Complexity:** O(E · α(V) + Q) time, O(V) space

Union-Find where each node tracks its ratio relative to its root. `find(x)` returns
`(root, x/root)`. For query `(c, d)`: if same root, answer is `(c/root) / (d/root)`.

**Why it works:** Ratios are transitive. Storing each node's ratio to its component root
allows O(α) query answering after O(E) setup.

## Key Insight

Division is a **multiplicative path problem** on a weighted graph. The ratio `a/b` is
the product of edge weights on any path from `a` to `b`. BFS finds the path; the
product gives the answer.

## Edge Cases

- Query variable not in any equation — return `-1.0`.
- `c == d` and `c` is a known variable — return `1.0`.
- `c == d` but `c` is unknown — return `-1.0`.
- Disconnected components — variables in different components return `-1.0`.
