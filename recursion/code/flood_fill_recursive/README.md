# Flood Fill (LC 733) — Recursive

## Problem Statement
Given a 2D image grid, a starting cell `(sr, sc)`, and a new `color`, perform
a flood fill: change the color of the starting cell and all 4-directionally
connected cells of the same original color to `color`.

**Example:**
- image=[[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2
- → [[2,2,2],[2,2,0],[2,0,1]]

---

## Approach: DFS Recursion — O(m·n) time, O(m·n) space

1. Record `original = image[sr][sc]` before any changes.
2. If `original == color`, return immediately (already filled — avoids infinite loop).
3. DFS: fill current cell, then recurse on all 4 neighbors.
4. Base cases: out of bounds, or cell color ≠ original color.

**Why record original color first:** Once we start filling, cells change to
`color`. Without recording the original, we can't distinguish "already visited"
from "different region."

**Why the `original == color` early exit:** If the starting cell already has
the target color, every neighbor check would pass (same color), causing
infinite recursion.

---

## Key Insight
Flood fill is DFS on an implicit graph where nodes are cells and edges connect
4-directional neighbors of the same original color. The recursion terminates
because each cell is filled (changed) exactly once — it can never pass the
`image[r][c] != original` check again after being visited.

---

## Edge Cases
- Starting cell already has target color → return image unchanged.
- Single cell grid → fill that one cell.
- Disconnected regions of same color → only the connected component is filled.
- Color 0 → works normally; the `original == color` guard handles it.

---

## Complexity Summary
| Metric | Value    |
|--------|----------|
| Time   | O(m·n)   |
| Space  | O(m·n) stack (worst case all cells connected) |
