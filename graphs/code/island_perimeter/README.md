# Island Perimeter (LC 463)

Given a grid where `1` = land and `0` = water, return the perimeter of the single island.
There are no lakes (water inside the island).

## Approaches

### 1. Counting with Shared Edges
**Complexity:** O(m·n) time, O(1) space

For each land cell, start with 4 sides. Subtract 2 for each shared edge with an adjacent
land cell (checking only up and left to avoid double-counting).

**Why it works:** Each land cell contributes 4 to the perimeter. Each shared edge between
two land cells removes 2 (one from each cell's contribution). Checking only two directions
avoids counting each shared edge twice.

### 2. DFS Flood Fill
**Complexity:** O(m·n) time, O(m·n) space (visited set + recursion)

DFS from the first land cell. For each direction, add 1 to perimeter if the neighbor is
out-of-bounds or water; add 0 if already visited.

**Why it works:** Each boundary between land and non-land (water or edge) contributes
exactly 1 to the perimeter. DFS counts these boundaries naturally.

## Key Insight

Perimeter = (number of land cells × 4) − (2 × number of shared land-land edges).
The counting approach computes this directly in O(1) space without any traversal overhead.

## Edge Cases

- Single land cell — perimeter is 4.
- Straight line of cells — perimeter = 2 × (length + 1).
- No land cells — return 0 (problem guarantees exactly one island, so this won't occur).
