# Maximum Frequency Stack (LC 895)

Design a stack that pops the most frequently pushed element. On ties, pop the most recently pushed among the most frequent.

## Approaches

### 1. Frequency Map + Group Map
- **Time:** O(1) push and pop | **Space:** O(n)
- `freq[val]`: tracks how many times each value has been pushed.
- `group[f]`: a list of values that currently have frequency `f` (in push order).
- `max_freq`: the current maximum frequency.
- **Push**: increment `freq[val]`, append to `group[freq[val]]`, update `max_freq`.
- **Pop**: pop from `group[max_freq]` (most recent among most frequent), decrement `freq[val]`, decrease `max_freq` if that group is now empty.

## Key Insight

The key observation is that a value pushed for the k-th time belongs to **all** frequency groups 1 through k simultaneously. By storing it in `group[k]`, we can always find the most recent element at the highest frequency in O(1). When `max_freq` drops (its group empties), it can only drop by 1 — because you can't skip a frequency level.

## Edge Cases

- Same value pushed multiple times: it appears in multiple frequency groups; popping it decrements its frequency and removes it from the current group.
- All same values: `max_freq` grows with each push; each pop decrements it by 1.
- Tie-breaking: `group[f]` is a list in push order, so `pop()` (from the end) gives the most recently pushed.
- At least one element is guaranteed before any `pop` call.
