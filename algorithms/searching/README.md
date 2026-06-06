# Searching Algorithms

## Overview

| Algorithm       | Time         | Space  | Requirement              |
|-----------------|--------------|--------|--------------------------|
| Linear Search   | O(n)         | O(1)   | None                     |
| Binary Search   | O(log n)     | O(1)   | Sorted array             |
| Quick Select    | O(n) avg     | O(1)   | None (modifies array)    |

## Binary Search Variants

| Variant        | Returns                                      | Use case                          |
|----------------|----------------------------------------------|-----------------------------------|
| `exact`        | index of target, or -1                       | Does value exist?                 |
| `lower_bound`  | first index where arr[i] >= target           | Insert position (left)            |
| `upper_bound`  | first index where arr[i] > target            | Insert position (right)           |
| `first_true`   | first index where predicate is True          | Binary search on answer           |

## When to Use

- **Binary Search** — sorted array, O(log n) lookup, finding boundaries
- **Binary Search on Answer** — optimization problems where you can check feasibility
  (e.g., "minimum capacity to ship in D days", "koko eating bananas")
- **Quick Select** — find kth smallest/largest without full sort, O(n) average

## Files

- `binary_search.py` — all variants + rotated array + search on answer template
- `quickselect.py` — kth smallest, randomized partition
