# Car Fleet (LC 853)

`n` cars drive toward a `target`. A car can't pass the one ahead — if it catches up, they form a fleet. Return the number of fleets that arrive.

## Approaches

### 1. Sort + Monotonic Stack of Arrival Times
- **Time:** O(n log n) | **Space:** O(n)
- Sort cars by position descending (closest to target first).
- Compute each car's arrival time: `(target - pos) / speed`.
- Maintain a stack of arrival times. A car forms a new fleet only if its arrival time is **strictly greater** than the car ahead (stack top) — meaning it can't catch up.
- If a car arrives ≤ the car ahead, it catches up and joins that fleet (don't push).

## Key Insight

Processing from closest to target outward means each car only needs to compare with the fleet immediately ahead of it. A car with a **longer** arrival time than the car ahead will never catch it — it becomes a new fleet. A car with a **shorter or equal** arrival time will catch up before or at the target — it merges into the fleet ahead. The stack length at the end equals the number of distinct fleets.

## Edge Cases

- Single car → always 1 fleet.
- All cars same speed → each is its own fleet (arrival times are all different since positions differ).
- Car behind arrives faster than car ahead → they merge; the merged fleet travels at the slower car's speed (arrival time of the ahead car).
- `[0, 2, 4]` with speeds `[4, 2, 1]` → all merge into 1 fleet (each catches the one ahead).
