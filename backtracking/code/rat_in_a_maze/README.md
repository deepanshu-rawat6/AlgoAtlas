# Rat in a Maze (Classic Backtracking)

Given an `n×n` maze where `1` = open and `0` = blocked, find all paths from `(0,0)` to
`(n-1,n-1)`. The rat can move Down, Left, Right, Up. Return paths as direction strings
in lexicographical order.

## Approaches

### 1. Backtracking with Visited Matrix
**Complexity:** O(4ⁿ) time, O(n²) space

Try all 4 directions (D, L, R, U — in lexicographic order for sorted output). Mark the
current cell as visited before recursing; unmark on backtrack. Add the path string to
results when `(n-1, n-1)` is reached.

**Why it works:** Backtracking explores all possible paths. The visited matrix prevents
revisiting cells within the same path (avoiding cycles). Trying directions in
lexicographic order (D < L < R < U) ensures results are naturally sorted.

## Key Insight

The visited matrix is essential — without it, the rat could loop forever. Backtracking
(unmark on return) allows the same cell to be used in different paths. Trying directions
in alphabetical order (D, L, R, U) produces lexicographically sorted output without
post-processing.

## Edge Cases

- `maze[0][0] == 0` — no paths possible, return `[]`.
- `maze[n-1][n-1] == 0` — no paths possible, return `[]`.
- `n = 1` — already at destination, return `[""]`.
- Completely blocked maze — return `[]`.
