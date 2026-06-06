# Fruit Into Baskets (LC 904)

You have two baskets, each holding one type of fruit. Given `fruits[i]` (fruit type at tree `i`),
return the maximum number of fruits you can pick from a contiguous subarray.
Equivalent to: longest subarray with at most 2 distinct values.

## Approaches

### 1. Sliding Window — O(n) time, O(1) space
Maintain a frequency map of fruit types in the current window. Expand right always. When more than 2 distinct types appear, shrink from the left until only 2 remain.

**Why it works:** The window always contains at most 2 fruit types. Shrinking removes the leftmost fruit and deletes its type from the map when its count hits zero.

## Key Insight
"At most 2 distinct values" = standard variable-size sliding window with a frequency map. Shrink when the constraint is violated.

## Edge Cases
- Single fruit type → entire array
- All distinct fruit types → window of size 2 (or 1 if only one element)
- Two fruit types alternating → entire array
- Array of length 1 → 1
