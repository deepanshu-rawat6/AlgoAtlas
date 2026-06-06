# LC 57 — Insert Interval

Given a sorted list of non-overlapping intervals, insert a new interval and merge if necessary. Return the resulting non-overlapping intervals.

## Approaches

### 1. Linear Scan and Merge
- **Time:** O(n) | **Space:** O(n)
- Three phases:
  1. Add all intervals that end before the new interval starts (`intervals[i][1] < newInterval[0]`).
  2. Merge all overlapping intervals into the new interval (`intervals[i][0] <= newInterval[1]`).
  3. Append the merged interval and all remaining intervals.

## Key Insight

The sorted order allows a single linear pass. An interval overlaps with `newInterval` iff its start ≤ `newInterval[1]` AND its end ≥ `newInterval[0]`. During the merge phase, expand `newInterval` by taking the min of starts and max of ends. The three-phase structure cleanly separates before, overlap, and after regions.

## Edge Cases

- Empty intervals list: Return `[newInterval]`.
- New interval doesn't overlap anything: Insert it in the correct sorted position.
- New interval overlaps all existing intervals: Merge into one.
- New interval is contained within an existing interval: The existing interval absorbs it.
- `[[1,5]]` with `newInterval = [2,3]`: Result is `[[1,5]]` (contained).
