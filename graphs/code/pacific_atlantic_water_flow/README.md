# Pacific Atlantic Water Flow (LC 417)

Given an `m x n` height matrix, water flows to neighbors with equal or lower height.
Pacific touches top/left borders; Atlantic touches bottom/right borders. Return all
cells from which water can flow to **both** oceans.

## Approaches

### 1. Brute Force BFS per Cell
**Complexity:** O((m·n)²) time, O(m·n) space

For each cell, run two separate BFS/DFS checks — one to see if it can reach the Pacific,
one for the Atlantic. Expensive due to redundant traversals.

### 2. Reverse BFS from Ocean Borders (optimal)
**Complexity:** O(m·n) time, O(m·n) space

Instead of flowing downhill from each cell, flow **uphill** from each ocean's border.
BFS from Pacific border cells (top row + left column) marks all cells that can drain to
Pacific. Same for Atlantic (bottom row + right column). The intersection is the answer.

**Why it works:** Reversing the flow direction (water flows uphill from ocean inward)
lets us do two BFS passes instead of one per cell. A cell reachable from both oceans
in the reverse direction can drain to both oceans in the forward direction.

## Key Insight

Reverse the problem: instead of asking "can this cell reach the ocean?", ask "which
cells can the ocean reach (going uphill)?". Two BFS passes replace O(m·n) individual
searches.

## Edge Cases

- Single cell grid — it borders both oceans, so return `[[0, 0]]`.
- Flat grid (all same height) — every cell can reach both oceans.
- Strictly increasing heights away from borders — only border cells qualify.
