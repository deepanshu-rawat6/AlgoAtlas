# Find the Town Judge (LC 997)

In a town of `n` people, the town judge (if they exist) trusts nobody and is trusted by
everyone else. Given a `trust` array where `trust[i] = [a, b]` means person `a` trusts
person `b`, return the judge's label or `-1` if no judge exists.

## Approaches

### 1. Net Trust Score
**Complexity:** O(n + e) time, O(n) space

Maintain a score array: `+1` for each incoming trust, `-1` for each outgoing trust.
The judge has score exactly `n - 1` (trusted by all `n-1` others, trusts nobody).

**Why it works:** The judge's two properties map directly to in-degree = n-1 and
out-degree = 0. Combining them into a single net score simplifies the check to one pass.

## Key Insight

Model the problem as a directed graph. The judge is the unique node with
**in-degree = n-1** and **out-degree = 0**. A single net-score array captures both
constraints simultaneously.

## Edge Cases

- `n = 1`, `trust = []` — person 1 is trivially the judge (no one else to trust them,
  and they trust nobody).
- Multiple people with high in-degree but one of them also trusts someone — not the judge.
- Nobody has in-degree `n-1` — return `-1`.
