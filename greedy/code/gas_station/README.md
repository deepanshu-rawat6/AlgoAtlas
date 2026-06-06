# LC 134 — Gas Station

There are `n` gas stations in a circle. `gas[i]` is the fuel available and `cost[i]` is the fuel to travel to the next station. Return the starting station index to complete the circuit, or -1 if impossible.

## Approaches

### 1. Brute Force
- **Time:** O(n²) | **Space:** O(1)
- Try each station as a starting point and simulate the full circuit.

### 2. Greedy Single Pass
- **Time:** O(n) | **Space:** O(1)
- Track `total` (overall fuel balance) and `tank` (current running balance). When `tank < 0`, the current start is invalid — reset `start = i + 1` and `tank = 0`. If `total >= 0` at the end, `start` is the answer.

## Key Insight

If the total gas ≥ total cost, a solution is guaranteed to exist and is unique. The greedy insight: if you run out of fuel at station `i`, no station between `start` and `i` can be the starting point (they all had positive running balances, so starting later would only make things worse). The next candidate must be `i + 1`.

## Edge Cases

- `total < 0`: No solution exists, return -1.
- Single station: Only works if `gas[0] >= cost[0]`.
- All stations have `gas[i] == cost[i]`: Any station works; return 0.
- Solution is guaranteed unique when it exists.
