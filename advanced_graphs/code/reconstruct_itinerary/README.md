# Reconstruct Itinerary (LC 332)

Given airline tickets as `[from, to]` pairs, reconstruct the itinerary starting from
`"JFK"` using all tickets exactly once. If multiple valid itineraries exist, return the
lexicographically smallest one.

## Approaches

### 1. DFS with Backtracking
**Complexity:** O(E²) time, O(E) space

Sort destinations for each airport. DFS greedily picks the smallest destination. If a
dead end is reached before all tickets are used, backtrack and try the next option.

**Why it works:** Sorting ensures lexicographic order. Backtracking handles cases where
a greedy choice leads to a dead end (not all tickets usable).

### 2. Hierholzer's Algorithm (Eulerian Path)
**Complexity:** O(E log E) time, O(E) space

Sort destinations in reverse order (so `pop()` gives the smallest). DFS: while the
current airport has outgoing edges, follow them. When stuck, append to result. Reverse
at the end.

**Why it works:** This is an **Eulerian path** problem — use every edge exactly once.
Hierholzer's algorithm finds Eulerian paths in O(E). Nodes are added to the result
on backtrack (post-order), so reversing gives the correct forward path.

## Key Insight

The itinerary is an **Eulerian path** starting at JFK. Hierholzer's algorithm finds it
efficiently. The trick: append airports to result on the way **back** (post-order DFS),
then reverse — this handles dead ends naturally without explicit backtracking.

## Edge Cases

- Linear itinerary (no branching) — single valid path.
- Airport with multiple outgoing flights — lexicographic sort determines order.
- Dead-end airport mid-path — Hierholzer handles by appending on backtrack.
