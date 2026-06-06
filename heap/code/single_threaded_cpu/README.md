# Single-Threaded CPU (LC 1834)

Given tasks `[enqueueTime, processingTime]`, simulate a CPU that always picks the shortest available task (ties broken by index). Return the order tasks are processed.

## Approaches

### Sort + Min-Heap Simulation
- **Time:** O(n log n) — sort + heap operations
- **Space:** O(n)
- Sort tasks by enqueue time (keeping original indices). Use a min-heap of `(processingTime, originalIndex)` for available tasks.
- Simulate: advance a `time` counter. At each step, push all tasks with `enqueueTime <= time` into the heap. Pop the shortest task, record it, advance `time` by its processing time. If the heap is empty, jump `time` to the next task's enqueue time (CPU idle).

## Key Insight

The CPU idle jump is critical: when no task is available, time must leap to the next enqueue time rather than incrementing by 1 (which would be O(max_time) and too slow). The min-heap on `(processingTime, index)` naturally breaks ties by index since tuples compare lexicographically.

## Edge Cases

- All tasks enqueue at the same time → pure shortest-job-first ordering.
- CPU idle gap: if the current time is before the next task's enqueue time, jump directly to avoid O(max_time) simulation.
- Two tasks with identical processing times → smaller original index wins (heap tuple comparison handles this).
- Single task → trivially returns `[0]`.
