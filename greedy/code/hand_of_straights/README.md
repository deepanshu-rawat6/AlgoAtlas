# LC 846 — Hand of Straights

Given a hand of cards and a `groupSize`, return `true` if the cards can be rearranged into groups of `groupSize` consecutive cards.

## Approaches

### 1. Sort + Greedy with Counter
- **Time:** O(n log n) | **Space:** O(n)
- Count card frequencies. Iterate sorted unique cards. For each card with remaining count > 0, greedily form groups starting from that card: consume `count` groups of `groupSize` consecutive cards. If any required card is missing, return `False`.

## Key Insight

Always start a new group from the **smallest** available card. If the smallest card can't start a group (not enough consecutive cards), no valid arrangement exists — there's no other way to use that card. Sorting ensures we always process the smallest card first, making the greedy choice correct.

## Edge Cases

- `len(hand) % groupSize != 0`: Impossible, return `False` immediately.
- `groupSize = 1`: Always true (every card forms its own group).
- Cards with large gaps (e.g., `[1, 10]` with `groupSize = 2`): Return `False`.
- Duplicate cards: The counter handles multiple groups starting at the same value.
