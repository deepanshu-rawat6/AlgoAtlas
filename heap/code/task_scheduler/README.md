# Task Scheduler (LC 621)

Given tasks (each a letter) and a cooldown `n`, find the minimum CPU time to finish all tasks. The same task must have at least `n` units between executions; the CPU can idle.

## Approaches

### Heap + Cooldown Queue (simulation)
- **Time:** O(t * n) where t = number of tasks
- **Space:** O(1) — at most 26 distinct tasks
- Use a max-heap of task counts. Each time unit: pop the most frequent task, decrement its count, and put it in a cooldown queue with its re-availability time. When a task's cooldown expires, push it back to the heap. If the heap is empty but cooldown queue isn't, the CPU idles.

### Math Formula (optimal)
- **Time:** O(t)
- **Space:** O(1)
- The most frequent task determines the minimum frame structure. With `max_freq` occurrences, we need `(max_freq - 1)` full frames of size `(n + 1)`, plus a final partial frame containing all tasks tied for `max_freq`. Formula: `max((max_freq - 1) * (n + 1) + count_of_max_freq, len(tasks))`. The `len(tasks)` floor handles the case where tasks are dense enough to fill all slots without idling.

## Key Insight

The bottleneck is always the most frequent task. It forces a minimum schedule length because it must appear `max_freq` times with at least `n` gaps between each occurrence. If other tasks fill those gaps completely, no idling is needed and the answer is just `len(tasks)`.

## Edge Cases

- n = 0 → no cooldown, answer is `len(tasks)`.
- All tasks are the same letter → maximum idling required.
- Multiple tasks tied for max frequency → they all fit in the final partial frame, increasing the answer by their count.
- Tasks are diverse enough to fill every slot → formula returns `len(tasks)`.
