# Generate Parentheses (LC 22)

Given `n` pairs of parentheses, generate all combinations of well-formed parentheses.

## Approaches

### 1. Backtracking with Open/Close Counts
**Complexity:** O(4ⁿ / √n) time (Catalan number), O(n) space

Track `open_count` and `close_count`. Add `(` if `open_count < n`; add `)` if
`close_count < open_count`. Add to result when string length reaches `2n`.

**Why it works:** The two rules enforce validity: we can only open if we haven't used
all `n` opens, and we can only close if there's an unmatched open. These constraints
prune all invalid sequences, generating only valid ones.

## Key Insight

The constraints `open < n` and `close < open` are necessary and sufficient for
well-formed parentheses. They encode the invariant that at any prefix, the number of
`(` ≥ number of `)`, and the total of each equals `n` at the end.

## Edge Cases

- `n = 1` — only `"()"`.
- `n = 0` — return `[""]` or `[]` depending on interpretation (problem guarantees n ≥ 1).
- Large `n` — output grows as the Catalan number C(n), which is exponential.
