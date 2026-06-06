# IPO (LC 502)

Given k project slots, initial capital `w`, and projects with `(capital[i], profits[i])`, greedily pick at most k projects to maximize final capital. A project can only be started if current capital ≥ its required capital.

## Approaches

### Two Heaps (Greedy)
- **Time:** O(n log n) — sort + heap operations
- **Space:** O(n)
- Sort projects by required capital. Use a max-heap of profits for "available" projects.
- Each round: unlock all projects whose required capital ≤ current `w` (push their profits to the max-heap). Pick the most profitable available project (pop from max-heap), add its profit to `w`. Repeat up to k times.

## Key Insight

Greedy works here because profits are additive and non-negative — taking the most profitable available project never prevents a better future choice (more capital only unlocks more projects). The two-structure approach (sorted array for unlocking, max-heap for selection) efficiently separates the two concerns: "what can I afford?" and "what's the best I can afford?".

## Edge Cases

- Can't afford any project initially → return `w` unchanged.
- k > number of projects → do as many as possible, stop when heap is empty.
- All projects have capital = 0 → all are immediately available; pick top-k by profit.
- Projects with profit = 0 → never worth picking (but won't hurt if picked; the heap just won't push them since profit 0 is valid).
