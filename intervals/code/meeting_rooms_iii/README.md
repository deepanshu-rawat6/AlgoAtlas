# LC 2402 — Meeting Rooms III

You have `n` rooms (0 to n-1). Assign each meeting to the lowest-numbered available room. If no room is free, delay the meeting until the earliest room finishes (preserving duration). Return the room that held the most meetings.

## Approaches

### 1. Two Min-Heaps
- **Time:** O(m log n) | **Space:** O(n)
- `available`: min-heap of free room indices.
- `ongoing`: min-heap of `(end_time, room_index)`.
- For each meeting (sorted by start): free rooms whose end ≤ start. If a room is available, assign the lowest-indexed one. If not, take the earliest-finishing room and delay the meeting (preserving duration). Track usage count per room.

## Key Insight

Two heaps handle the two competing priorities: lowest room index (for available rooms) and earliest end time (for busy rooms). Sorting meetings by start time ensures we process them in order. When delaying, the new end time is `finish + (end - start)` — the duration is preserved, not the original end time.

## Edge Cases

- Single room: All meetings go to room 0.
- All meetings non-overlapping: Each goes to room 0 (always available).
- All meetings at the same time: Assigned to rooms 0, 1, 2, ... in order.
- Tie in meeting count: Return the lowest-indexed room.
