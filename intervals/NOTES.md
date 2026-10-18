# Intervals

## Core Intuition

Interval problems reduce to: sort by start (or end), then decide how to merge, count, or schedule. After sorting, you only ever need to compare the current interval with the last processed one (or the top of a heap).

- **Sort-then-scan**: The foundational pattern. Sort by start; walk left to right; if `current.start <= last.end` they overlap — extend `last.end = max(last.end, current.end)`. Used in merge_intervals and insert_interval.
- **Greedy by end time**: For non_overlapping_intervals — sort by end, keep the interval finishing earliest, skip (count as removed) anything that conflicts. Minimises removals because an early-ending interval blocks the fewest future ones.
- **Sweep line**: Count how many intervals are "active" at any point. Split each interval into a `+1` event at start and a `-1` event at end; walk events in order; running sum is the concurrent count. Two-pointer variant: sort starts and ends separately, advance the end pointer whenever a meeting has finished.
- **Heap-based (active set)**: Sort by start; maintain a min-heap of end times for in-progress intervals. If the earliest-ending interval finishes before the next one starts, reuse its slot. Heap size = answer. Used in meeting_rooms_ii and meeting_rooms_iii.
- **Offline query approach**: For minimum_interval — sort intervals by start, sort queries by value (keeping original indices), sweep queries left to right pushing newly-eligible intervals onto a min-heap (by size), evicting expired ones from the top.

## Java Idioms

```java
// Sort by start time (standard for merge, insert, meeting rooms)
Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

// Sort by end time (non_overlapping_intervals greedy)
Arrays.sort(intervals, (a, b) -> a[1] - b[1]);

// Output size unknown: build list, convert at the end
List<int[]> res = new ArrayList<>();
// ... populate ...
return res.toArray(new int[0][]);

// Sweep line: encode start/end events in one array
int[][] events = new int[2 * n][2];
for (int i = 0; i < n; i++) {
    events[2 * i]     = new int[]{intervals[i][0],  1};  // start
    events[2 * i + 1] = new int[]{intervals[i][1], -1};  // end
}
Arrays.sort(events, (a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);

// Meeting Rooms II: min-heap of end times
PriorityQueue<Integer> endTimes = new PriorityQueue<>();

// Meeting Rooms III / minimum_interval: heap sorted by interval size
PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
// store [size, end] so smallest interval surfaces first

// Merging end times: always take max (containment case)
int newEnd = Math.max(last[1], current[1]);
```

## Problems

| Problem | Key Insight | Tricky Part | Common Mistakes | Time | Space |
|---|---|---|---|---|---|
| **insert_interval** (LC 57) | Three phases: copy intervals ending before new one, merge all overlapping, copy remainder | Overlap condition: `existing.end >= new.start && existing.start <= new.end` | Off-by-one on overlap check; forgetting the case where new interval fits between two existing ones without overlapping either | O(n) | O(n) |
| **merge_intervals** (LC 56) | Sort by start; extend `last.end = max(last.end, curr.end)` when `curr.start <= last.end` | Must use `max` not just assign — one interval may be fully contained inside another | Skipping `max` so a contained interval shrinks the merged end; not sorting first | O(n log n) | O(n) |
| **non_overlapping_intervals** (LC 435) | Sort by end; greedily keep interval with earliest end; increment removal counter on conflict | Count intervals *removed*, not kept; sort by *end* not start | Sorting by start instead of end; returning count of kept intervals instead of removed | O(n log n) | O(1) |
| **meeting_rooms** (LC 252) | Sort by start; any `intervals[i].start < intervals[i-1].end` means conflict | Sort is mandatory before the linear scan | Comparing without sorting first; using `<=` instead of `<` (adjacent meetings are fine) | O(n log n) | O(1) |
| **meeting_rooms_ii** (LC 253) | Min-heap of end times; if `heap[0] <= curr.start`, pop and push new end (reuse room); else push (new room) | Sweep-line alternative: sort starts and ends separately, two pointers — advance end pointer only when a meeting *fully* ends before next starts (`start >= end`, strict) | Using `<=` in sweep line (makes adjacent meetings share a room when they shouldn't); forgetting `heapreplace` for the reuse case | O(n log n) | O(n) |
| **meeting_rooms_iii** (LC 2402) | Two heaps: `available` (room numbers, min-heap), `occupied` ([end_time, room], min-heap); when none free, pull earliest-ending room | Must track *which room* is used per meeting to count per-room assignments; ties broken by lowest room number (heap handles this if room number is second key) | Using only one heap; not counting per-room usage; not initialising `available` with all room numbers 0..n-1 | O((n+m) log n) | O(n) |
| **minimum_interval_to_include_each_query** (LC 1851) | Sort intervals by start; sort queries offline with original indices; sweep pushing `[size, end]` onto min-heap, evicting expired intervals | Must remove from heap all intervals whose `end < query` *before* reading the top; use `end - start + 1` for size | Sorting intervals by size upfront (wrong — breaks the sweep); not saving original query index; integer overflow on size if using 32-bit arithmetic with large bounds | O((n+q) log n) | O(n+q) |

## Pattern Recognition Guide

Use this to pick the right approach when a new problem appears:

1. **Combine overlapping intervals into fewer intervals** → sort by start, merge (merge_intervals pattern).
2. **Insert one interval into a sorted list** → three-phase linear pass, no re-sort needed (insert_interval pattern).
3. **Remove minimum intervals to make list non-overlapping** → sort by end, greedy keep (non_overlapping_intervals pattern).
4. **Can a single person/entity attend all events?** → sort by start, check pairwise overlap (meeting_rooms pattern).
5. **How many parallel resources needed at peak?** → min-heap of end times, heap size = answer (meeting_rooms_ii pattern). Use two heaps if you also need to track *which* resource (meeting_rooms_iii pattern).
6. **For each point/query, find the containing interval with some property (e.g. smallest)?** → offline sort both, sweep with min-heap keyed on that property (minimum_interval pattern).

Key disambiguation: "remove minimum" sounds like counting — it's actually a greedy scheduling problem. "How many rooms" sounds like counting — it's actually a heap/sweep problem.

## Algorithm Skeletons

**Insert Interval**
```python
result = []
i, n = 0, len(intervals)
# Phase 1: intervals ending before new interval starts
while i < n and intervals[i][1] < new_interval[0]:
    result.append(intervals[i]); i += 1
# Phase 2: merge overlapping
while i < n and intervals[i][0] <= new_interval[1]:
    new_interval[0] = min(new_interval[0], intervals[i][0])
    new_interval[1] = max(new_interval[1], intervals[i][1])
    i += 1
result.append(new_interval)
# Phase 3: remainder
result.extend(intervals[i:])
```

**Non-Overlapping Intervals (greedy)**
```python
intervals.sort(key=lambda x: x[1])  # sort by END
end, removed = intervals[0][1], 0
for start, e in intervals[1:]:
    if start < end:       # conflict: remove current (keep earlier-ending one)
        removed += 1
    else:
        end = e           # advance the boundary
return removed
```

**Merge Intervals**
```python
intervals.sort(key=lambda x: x[0])
result = [intervals[0]]
for start, end in intervals[1:]:
    if start <= result[-1][1]:
        result[-1][1] = max(result[-1][1], end)
    else:
        result.append([start, end])
```

**Meeting Rooms II (heap)**
```python
intervals.sort()
heap = []  # end times
for start, end in intervals:
    if heap and heap[0] <= start:
        heapq.heapreplace(heap, end)
    else:
        heapq.heappush(heap, end)
return len(heap)
```

**Minimum Interval per Query**
```python
intervals.sort()
sorted_q = sorted(enumerate(queries), key=lambda x: x[1])
result = [-1] * len(queries)
heap, i = [], 0
for idx, q in sorted_q:
    while i < len(intervals) and intervals[i][0] <= q:
        s, e = intervals[i]
        heapq.heappush(heap, (e - s + 1, e))
        i += 1
    while heap and heap[0][1] < q:
        heapq.heappop(heap)
    if heap:
        result[idx] = heap[0][0]
```

## General Edge Cases

- **Single interval**: every problem degenerates trivially — nothing to merge, compare, or schedule. Test it anyway; index-out-of-bounds bugs live here.
- **No overlap, adjacent intervals**: `[1,2]` and `[2,3]` *touch* but don't overlap. Merge Intervals: merge them (`start <= last.end` uses `<=`, so `2 <= 2` → merge). Meeting Rooms: they don't conflict (`start < last.end` uses strict `<`, so `2 < 2` is false → same room). Know which comparison each problem uses.
- **Complete containment**: `[1,10]` fully contains `[2,5]`. The inner interval must not shrink the merged result — always `max(last.end, curr.end)`, never just `curr.end`.
- **Insert before all existing**: new interval ends before the first existing start — the three-phase insert just copies everything after the new interval; nothing gets merged.
- **Insert after all existing**: new interval starts after the last existing end — same logic, nothing gets merged, new interval appended.
- **All intervals identical**: meeting rooms → answer is n; merge → answer is 1 interval; non-overlapping → remove n-1.
- **Query falls outside all intervals** (minimum_interval): heap is empty after eviction → result stays `-1`. Must not read `heap[0]` without checking `if heap`.
- **Integer overflow on interval size**: `end - start + 1` with large bounds (up to 10^7) fits in 32-bit int, but if you compute size as part of a sort key involving multiplication, overflow is possible. In Java, use `(a, b) -> Integer.compare(a[0], b[0])` rather than subtraction when values approach `Integer.MAX_VALUE`.
