# LC 135 — Candy

There are `n` children in a line, each with a rating. Give each child at least 1 candy. Children with a higher rating than their neighbor must get more candies. Return the minimum total candies.

## Approaches

### 1. Two-Pass Greedy
- **Time:** O(n) | **Space:** O(n)
- Left pass: if `ratings[i] > ratings[i-1]`, give `candies[i] = candies[i-1] + 1`.
- Right pass: if `ratings[i] > ratings[i+1]`, give `candies[i] = max(candies[i], candies[i+1] + 1)`.
- Sum the result.

## Key Insight

Each pass enforces one direction of the constraint independently. The left pass ensures every child beats their left neighbor when needed; the right pass ensures they beat their right neighbor. Taking the `max` at each position satisfies both constraints simultaneously with the minimum candy count. A single pass can't handle both directions at once.

## Edge Cases

- Single child: Return 1.
- All equal ratings: Every child gets 1 candy.
- Strictly increasing ratings: Candies are `[1, 2, 3, ..., n]`.
- Strictly decreasing ratings: Candies are `[n, ..., 2, 1]` — the right pass handles this.
- Valley shape (e.g., `[3, 1, 3]`): Middle child gets 1, both ends get 2.
