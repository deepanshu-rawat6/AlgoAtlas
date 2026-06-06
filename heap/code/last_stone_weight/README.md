# Last Stone Weight (LC 1046)

Given stone weights, repeatedly smash the two heaviest: if equal both are destroyed; if unequal the difference survives. Return the weight of the last remaining stone (or 0 if none).

## Approaches

### Sort on Every Iteration
- **Time:** O(n² log n) — sort after each smash
- **Space:** O(n)
- Keep a sorted list; pop the two largest, compute difference, re-insert with `bisect.insort`. Correct but slow.

### Max-Heap (optimal)
- **Time:** O(n log n)
- **Space:** O(n)
- Python only has a min-heap, so negate all values to simulate a max-heap. Each iteration: pop two largest (most negative), compute `y - x`, push `-(y-x)` if non-zero. Repeat until one or zero stones remain.

## Key Insight

The problem always needs the two largest elements — exactly what a max-heap provides in O(log n). Negating values is the standard Python trick to turn `heapq` (min-heap) into a max-heap without any extra data structure.

## Edge Cases

- Single stone → return it directly (loop never executes).
- Two equal stones → both destroyed, return 0.
- All stones equal → all cancel out, return 0.
- After smashing, the remainder may be smaller than other stones already in the heap — the heap re-orders correctly.
