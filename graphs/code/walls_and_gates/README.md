# Walls and Gates (LC 286)

Given an `m x n` grid with `-1` (wall), `0` (gate), and `INF` (empty room), fill each
empty room with the distance to its nearest gate. Modify in-place.

## Approaches

### 1. BFS from Each Empty Room (brute force)
**Complexity:** O((m·n)²) time, O(m·n) space

For each `INF` cell, run BFS until a gate is found. Expensive because each cell
independently explores the grid.

**Why it works:** BFS guarantees shortest path, so the first gate reached gives the
minimum distance. But repeating this for every cell is wasteful.

### 2. Multi-Source BFS from All Gates (optimal)
**Complexity:** O(m·n) time, O(m·n) space

Seed the BFS queue with all gate cells simultaneously. Expand outward level by level —
each level increments the distance. An `INF` cell is updated only once (first time
reached = shortest distance).

**Why it works:** Starting from all gates at once means each empty room is reached by
the nearest gate first. No room is processed twice, giving linear time.

## Key Insight

Multi-source BFS is the key optimization. Instead of asking "how far is the nearest gate
from this room?", ask "how far can each gate reach?" — the answers are the same but
computed in a single O(m·n) pass.

## Edge Cases

- No gates in the grid — all `INF` cells remain `INF`.
- No empty rooms — nothing to update.
- Room completely surrounded by walls — remains `INF`.
- Gate adjacent to another gate — distance stays 0.
