# Car Pooling (LC 1094)

Given trips `[numPassengers, from, to]` and a car `capacity`, return `true` if all passengers can be picked up and dropped off without exceeding capacity at any point.

## Approaches

### Event Sorting
- **Time:** O(n log n)
- **Space:** O(n)
- Create pickup events `(from, +num)` and dropoff events `(to, -num)`. Sort by location. Simulate: accumulate passenger delta at each stop; if current count exceeds capacity, return `False`.

### Difference Array (optimal)
- **Time:** O(n + max_stop) — O(n) for filling, O(1001) for scanning
- **Space:** O(1001)
- Since stop positions are bounded by 1000, use a difference array of size 1001. For each trip: `diff[from] += num`, `diff[to] -= num`. Scan the prefix sum; if it ever exceeds capacity, return `False`.

## Key Insight

The difference array exploits the bounded stop range. Instead of sorting events, we directly mark the start and end of each trip's passenger load. The prefix sum at each stop gives the exact passenger count at that location. This is O(n) with a very small constant.

## Edge Cases

- Passengers drop off at `to` before the next pickup at the same stop — the dropoff event at `to` decrements before any pickup at `to` is counted (difference array handles this correctly since `diff[to] -= num` means passengers are gone at stop `to`).
- Multiple trips starting or ending at the same stop — all deltas accumulate correctly.
- Capacity exactly met (not exceeded) → valid.
