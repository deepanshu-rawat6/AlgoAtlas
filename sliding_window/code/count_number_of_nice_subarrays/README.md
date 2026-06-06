# Count Number of Nice Subarrays (LC 1248)

Given an array of integers `nums` and integer `k`, return the number of subarrays
containing exactly `k` odd numbers.

## Approaches

### 1. Prefix Sum — O(n) time, O(n) space
Map each number to 1 (odd) or 0 (even). Track running prefix sum of odd counts. For each position, count previous prefix sums equal to `prefix - k`.

**Why it works:** Reduces to "binary subarrays with sum k" — treating odd as 1 and even as 0 makes the problem identical.

### 2. atMost(k) - atMost(k-1) — O(n) time, O(1) space
`exactly(k) = atMost(k) - atMost(k-1)`. Each `atMost` uses a sliding window counting subarrays with at most `k` odd numbers.

**Why it works:** Same decomposition as Binary Subarrays With Sum. The sliding window shrinks when odd count exceeds the limit.

## Key Insight
Odd/even → 1/0 transformation reduces this to the exact same problem as LC 930. The `exactly = atMost(k) - atMost(k-1)` trick applies directly.

## Edge Cases
- `k == 0` → count subarrays with no odd numbers (all-even subarrays)
- All numbers are odd → only windows of exactly `k` consecutive elements
- No odd numbers in array and `k > 0` → 0
- `k > len(nums)` → 0
