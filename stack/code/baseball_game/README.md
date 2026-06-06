# Baseball Game (LC 682)

Simulate a baseball game with special scoring rules: integers record scores, `"C"` removes the last score, `"D"` doubles the last, `"+"` sums the last two. Return the total.

## Approaches

### 1. Stack Simulation
- **Time:** O(n) | **Space:** O(n)
- Use a list as a mutable record (stack). Process each operation:
  - Integer: append the value.
  - `"C"`: pop the last score.
  - `"D"`: append `record[-1] * 2`.
  - `"+"`: append `record[-1] + record[-2]`.
- Return `sum(record)`.

## Key Insight

The operations only ever reference or modify the **most recent** scores, which is exactly what a stack provides in O(1). There's no need for random access — each operation looks at the top 1 or 2 elements. The stack naturally maintains the history needed for `"D"` and `"+"`.

## Edge Cases

- `"C"` after `"D"` or `"+"` removes the computed score, not the original inputs.
- Negative scores are valid (e.g., `"-2"` is a valid integer token).
- The problem guarantees `"+"` always has ≥ 2 previous scores and `"C"`/`"D"` always have ≥ 1.
- Single operation `["1"]` → returns 1.
