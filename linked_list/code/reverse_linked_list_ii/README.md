# Reverse Linked List II (LC 92)

Reverse the nodes of a linked list from position `left` to `right` in one pass.

## Approaches

### 1. Single Pass In-Place Reversal
- **Time:** O(n) | **Space:** O(1)
- Advance `pre` to the node just before position `left`.
- Repeatedly move `curr.next` to the front of the sublist (insert after `pre`):
  - Save `nxt = curr.next`
  - `curr.next = nxt.next`
  - `nxt.next = pre.next`
  - `pre.next = nxt`
- Repeat `right - left` times.

## Key Insight

The "insert at front" technique reverses the sublist without needing a separate reverse pass. Each iteration takes the node immediately after `curr` and inserts it right after `pre` (the anchor before the sublist). After `right - left` iterations, the sublist is fully reversed. `curr` stays fixed as the tail of the reversed segment.

The dummy head handles the case where `left = 1` (reversing from the very beginning).

## Edge Cases

- `left == right`: no reversal needed (loop runs 0 times).
- `left = 1`: dummy head ensures `pre` is the dummy, and the result's head is correctly updated.
- Reverse entire list (`left = 1`, `right = n`): works correctly.
- Two-node list with `left = 1`, `right = 2`: single swap.
