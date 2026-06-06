# LC 1903 — Largest Odd Number in String

## Problem
Given a string `num` representing a large integer, return the largest-valued
odd integer that is a non-empty substring (contiguous) of `num`, or `""` if
no odd integer exists. The answer is always a prefix of `num`.

**Example:**
- `num = "52"` → `"5"`
- `num = "4206"` → `""`
- `num = "35427"` → `"35427"`

**Constraints:** `1 <= num.length <= 10^5`, `num` has no leading zeros (except `"0"`).

---

## Approach — Scan from Right  `O(n)` time · `O(1)` space

A number is odd if and only if its last digit is odd. To maximise the value,
we want the longest possible prefix. So scan from the rightmost character
leftward and return `num[:i+1]` at the first odd digit found.

**Why prefix?** Any prefix of a numeric string is a valid number, and a longer
prefix always represents a larger value (no leading zeros guaranteed). So the
largest odd substring is the longest prefix whose last digit is odd, which is
exactly the prefix ending at the rightmost odd digit.

---

## Key Insight
Largest odd number = longest prefix ending at the rightmost odd digit.
We never need to consider non-prefix substrings because a prefix is always
≥ any substring of the same or shorter length.

---

## Edge Cases
| Input | Output | Reason |
|-------|--------|--------|
| `"2"` | `""` | Only even digit |
| `"1"` | `"1"` | Single odd digit |
| `"4206"` | `""` | All even digits |
| `"35427"` | `"35427"` | Last digit already odd |
| `"10"` | `"1"` | Rightmost odd is index 0 |

---

## Complexity
- **Time:** O(n) — at most one full scan
- **Space:** O(1) — no extra storage (slice is O(k) output, not auxiliary)
