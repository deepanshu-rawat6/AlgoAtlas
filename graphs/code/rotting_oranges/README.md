# Rotting Oranges (LC 994)

Given an `m x n` grid with `0` (empty), `1` (fresh orange), `2` (rotten orange): each
minute, fresh oranges adjacent to rotten ones become rotten. Return the minimum minutes
until no fresh oranges remain, or `-1` if impossible.

## Approaches

### 1. Multi-Source BFS from All Rotten Oranges
**Complexity:** O(m·n) time, O(m·n) space

Seed the BFS queue with all initially rotten oranges. Count fresh oranges. Each BFS
level represents one minute — rot adjacent fresh oranges and decrement the fresh count.
Return the level count when fresh count reaches 0, or `-1` if fresh oranges remain.

**Why it works:** All rotten oranges spread simultaneously, so starting BFS from all of
them at once correctly models parallel spreading. BFS levels naturally correspond to
minutes elapsed.

## Key Insight

This is a **multi-source BFS** problem — identical in structure to Walls and Gates.
The key insight is that all rotten oranges act as simultaneous sources. Starting BFS
from all of them at once gives the correct minimum time for each fresh orange to rot.

## Edge Cases

- No fresh oranges initially — return 0.
- Fresh orange isolated by empty cells and walls — return `-1`.
- All oranges already rotten — return 0.
- Grid with only empty cells — return 0.
