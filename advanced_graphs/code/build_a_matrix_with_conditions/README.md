# Build a Matrix With Conditions (LC 2392)

Given `k` and row/column ordering constraints, build a `k×k` matrix containing each
integer `1..k` exactly once such that row and column conditions are satisfied. Return
empty matrix if impossible.

## Approaches

### 1. Topological Sort (Kahn's BFS) for Rows and Columns
**Complexity:** O(k + conditions) time, O(k + conditions) space

Run Kahn's BFS topological sort independently on row conditions and column conditions.
If either has a cycle (order length < k), return `[]`. Otherwise, place each value at
`(row_pos[val], col_pos[val])` in the matrix.

**Why it works:** Row conditions define a partial order on which row each number occupies.
Column conditions define the same for columns. Topological sort gives a valid linear
ordering satisfying all constraints. A cycle means contradictory constraints — impossible.

## Key Insight

Row and column placements are **independent** topological sort problems. Solve them
separately, then combine: value `v` goes at `(row_order.index(v), col_order.index(v))`.
Cycle detection is built into Kahn's algorithm via the node count check.

## Edge Cases

- Cycle in row conditions — return `[]`.
- Cycle in column conditions — return `[]`.
- No conditions — any arrangement works; return identity-like placement.
- `k = 2` with conflicting conditions — return `[]`.
