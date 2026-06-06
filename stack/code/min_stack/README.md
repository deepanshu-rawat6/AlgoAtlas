# Min Stack (LC 155)

Design a stack supporting `push`, `pop`, `top`, and `getMin` — all in O(1) time.

## Approaches

### 1. Two Stacks (Parallel Min Tracking)
- **Time:** O(1) all ops | **Space:** O(n)
- Maintain a `min_stack` in parallel with the main stack.
- On `push(val)`: push `min(val, min_stack[-1])` to `min_stack` (or `val` if empty).
- On `pop`: pop from both stacks simultaneously.
- `getMin()` returns `min_stack[-1]` — always the current minimum.

### 2. Single Stack of Tuples
- **Time:** O(1) all ops | **Space:** O(n)
- Each entry is `(value, current_min_at_this_point)`.
- Avoids a second stack object; same logic, slightly more compact.

## Key Insight

The challenge is that `pop` can change the minimum, so we can't just store one global min. By tracking the minimum **at each stack level**, we always know what the minimum becomes after a pop — it's the min stored in the new top. Each push records a snapshot of the minimum at that moment.

## Edge Cases

- Popping the current minimum: the new minimum is correctly restored from the previous stack entry.
- Duplicate minimums: both entries record the same min value, so popping one still leaves the correct min.
- All same values: `min_stack` holds the same value at every level.
- All calls to `pop`, `top`, `getMin` are guaranteed on non-empty stacks.
