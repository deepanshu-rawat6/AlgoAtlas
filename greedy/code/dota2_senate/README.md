# LC 649 — Dota2 Senate

Senators from Radiant (R) and Dire (D) take turns banning opponents. Each senator bans the next available opponent. Return which party wins when both sides play optimally.

## Approaches

### 1. Queue Simulation
- **Time:** O(n) | **Space:** O(n)
- Maintain two queues of senator indices. Each round, the senator with the smaller index acts first and bans the front of the opposing queue. The winner re-enqueues with index `+= n` to maintain relative order in future rounds. Continue until one queue is empty.

## Key Insight

The optimal strategy is always to ban the **next** senator from the opposing party (the one who would act soonest). Using indices to determine who acts first within a round, and re-enqueueing winners with `index + n` to simulate future rounds, correctly models the circular voting process without actually simulating each round explicitly.

## Edge Cases

- Single senator: That party wins immediately.
- All same party: That party wins (no opponents to ban).
- `"RD"`: R acts first (index 0 < 1), bans D. Radiant wins.
- `"RDD"`: R bans first D; second D bans R; Dire wins.
