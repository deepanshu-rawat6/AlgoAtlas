# Find Critical and Pseudo-Critical Edges in MST (LC 1489)

Given a weighted undirected graph, find all **critical edges** (removal increases MST
weight) and **pseudo-critical edges** (can appear in some but not all MSTs).

## Approaches

### 1. Kruskal's with Per-Edge Inclusion/Exclusion
**Complexity:** O(E² · α(V)) time, O(V) space

1. Compute base MST weight using Kruskal's.
2. For each edge `i`:
   - **Critical**: skip edge `i` in Kruskal's. If MST weight increases (or graph disconnects), it's critical.
   - **Pseudo-critical**: force edge `i` into the MST first, then run Kruskal's. If total weight equals base MST weight, it's pseudo-critical.

**Why it works:**
- Critical edges are those whose removal makes the MST heavier — they're the only bridge
  between two components at their weight level.
- Pseudo-critical edges can be included without increasing MST weight but aren't required
  (another edge of equal weight can substitute).

## Key Insight

Test each edge by **exclusion** (critical check) and **forced inclusion** (pseudo-critical
check). The base MST weight is the reference. This brute-force approach is feasible
because E ≤ 200.

## Edge Cases

- All edges have the same weight — all are pseudo-critical, none are critical (unless
  the graph has a bridge).
- A bridge edge — always critical (removing it disconnects the graph).
- Parallel edges (same endpoints, same weight) — neither is critical; both are pseudo-critical.
