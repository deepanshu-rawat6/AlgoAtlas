# Maximum Points You Can Obtain from Cards (LC 1423)

There are cards in a row. Each step you take one card from the beginning or end.
Take exactly `k` cards. Return the maximum score.

## Approaches

### 1. Minimize Middle Window — O(n) time, O(1) space
Taking `k` cards from the edges = leaving `n-k` cards in the middle. Find the minimum sum subarray of size `n-k`. Answer = `total_sum - min_middle`.

**Why it works:** The cards you don't take form a contiguous window of size `n-k`. Minimizing that window maximizes the cards you take.

### 2. Prefix Sum from Both Ends — O(k) time, O(k) space
Try all splits: take `i` cards from the front and `k-i` from the back, for `i` in `[0, k]`. Use prefix sums for O(1) per split.

**Why it works:** Enumerates all valid ways to split `k` picks between front and back. Prefix sums make each split O(1).

## Key Insight
Invert the problem: instead of maximizing the edges, minimize the middle window of size `n-k`. One sliding window pass suffices.

## Edge Cases
- `k == len(cardPoints)` → take all cards, return total sum
- `k == 1` → max of first and last card
- All cards have equal value → any selection gives the same score
