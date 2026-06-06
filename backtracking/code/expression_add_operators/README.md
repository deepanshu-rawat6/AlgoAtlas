# Expression Add Operators (LC 282)

Given a string of digits and a target, insert `+`, `-`, or `*` between digits to make
the expression evaluate to the target. Return all valid expressions.

## Approaches

### 1. Backtracking with Multiplication Tracking
**Complexity:** O(4ⁿ) time, O(n) space

At each position, choose how many digits to take as the next operand (handles multi-digit
numbers). Track the running total and the **previous operand** for multiplication handling.

For `*`: undo the previous addition/subtraction, then apply multiplication:
`new_total = total - prev + prev * curr`

**Why it works:** Standard left-to-right evaluation doesn't handle `*` precedence.
Tracking `prev` (the last operand added/subtracted) lets us "undo" it and apply
multiplication correctly. This simulates operator precedence without a full parser.

## Key Insight

The multiplication trick: when we see `*`, we need to undo the previous operation and
re-apply with multiplication. If the expression so far is `2+3` (total=5, prev=3) and
we multiply by 4: `5 - 3 + 3*4 = 14`. Tracking `prev` makes this O(1) per step.

## Edge Cases

- Leading zeros: `"05"` is invalid as a multi-digit number — break if `num[idx] == '0'`
  and `i > idx`.
- Single digit string — only the digit itself, no operators needed.
- Target is negative — subtraction can produce negative intermediates.
- Very large numbers — intermediate values can overflow (use Python's arbitrary precision).
