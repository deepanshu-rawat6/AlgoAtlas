# Strings — Learning Notes

## Decision Diagram: Which Algorithm to Use?

```mermaid
flowchart TD
    A[String Problem] --> B{"What are you doing?"}
    B --> C[Pattern Matching]
    B --> D[Palindrome]
    B --> E[Bracket Balancing]
    B --> F[Sequence Generation]

    C --> G{"Need exact match?"}
    G -->|Yes, single pattern| H{"Priority?"}
    G -->|Yes, multiple patterns| I[Aho-Corasick]
    H -->|Worst-case guarantee| J[KMP O(n+m)]
    H -->|Simple implementation| K[Rabin-Karp O(n+m) avg]
    H -->|Also need prefix info| L[Z-Function O(n)]

    D --> M{"What kind?"}
    M -->|Longest palindromic prefix| N[KMP on s+'#'+rev(s)]
    M -->|Count palindromic subsequences| O[Interval DP O(n²)]
    M -->|Longest palindromic substring| P[Manacher / Expand Center]

    E --> Q[Stack: remove matched pairs\nthen ceil(open/2)+ceil(close/2)]
    F --> R[Simulate iteratively\ngroup consecutive chars]
```

---

## Per-Problem Notes

### 1. Minimum Bracket Reversals

**Core idea**: After removing all matched `{}` pairs with a stack, the remaining string is always of the form `}}}...{{{` (all closes before all opens). Each `}}` pair needs 1 reversal, each `{{` pair needs 1 reversal.

**Formula**: `ceil(close/2) + ceil(open/2)` where close = remaining `}`, open = remaining `{`.

**Gotcha**: If original length is odd → impossible → return -1.

**Why stack?** Stack naturally cancels `{` when followed by `}`, leaving only the unmatched portion.

---

### 2. Count and Say

**Core idea**: Read the previous term aloud — count consecutive identical digits and write `count + digit`.

**Simulation**: Start with `"1"`, iterate n-1 times. Each iteration: scan groups of same chars.

**Gotcha**: n=1 returns `"1"` directly (no iteration needed).

**Pattern**: `itertools.groupby` makes grouping trivial in Python.

---

### 3. Rabin-Karp

**Core idea**: Hash the needle, then slide a window of same length over haystack, updating hash in O(1).

**Rolling hash formula**:
```
hash_new = (hash_old - ord(s[i]) * base^(m-1)) * base + ord(s[i+m])
```

**Gotcha**: Hash collision → verify with actual string comparison. Use large prime modulus to reduce collisions.

**Why rolling hash?** Avoids O(m) recomputation per window; total O(n) hash updates.

---

### 4. Z-Function

**Core idea**: Z[i] = length of longest substring starting at i that matches a prefix of s.

**Z-box [l, r]**: The rightmost interval where s[l..r] = s[0..r-l]. For new i:
- If i ≤ r: Z[i] ≥ min(Z[i-l], r-i+1), then extend
- If i > r: compute from scratch, update [l, r]

**Use case**: Pattern matching — concatenate `pattern + '#' + text`, find positions where Z[i] = len(pattern).

**vs KMP**: Z-function is often easier to implement; KMP's LPS is more memory-efficient for streaming.

---

### 5. KMP Algorithm

**Core idea**: LPS[i] = length of longest proper prefix of `pattern[0..i]` that is also a suffix.

**LPS build**: Two pointers `len` (length of previous longest prefix-suffix) and `i`. On mismatch, `len = LPS[len-1]` (don't reset to 0!).

**Search**: On mismatch at pattern[j], jump to `j = LPS[j-1]` instead of restarting from 0.

**Gotcha**: When j == 0 and mismatch, just advance i (can't go further back).

**Why LPS?** Encodes "how much of the pattern can we reuse" — avoids redundant comparisons.

---

### 6. Shortest Palindrome

**Core idea**: Find the longest palindromic prefix of s. The answer is `reverse(s[len:]) + s`.

**KMP trick**: Build string `t = s + '#' + reverse(s)`. The LPS value at the last position of t gives the length of the longest palindromic prefix of s.

**Why '#' separator?** Prevents the LPS from spanning across the boundary between s and reverse(s).

**Rolling hash alternative**: Compute forward and backward hashes simultaneously; find largest prefix where both match.

---

### 7. Longest Happy Prefix

**Direct KMP application**: The answer is `s[:LPS[n-1]]` where LPS is computed on s itself.

**LPS[n-1]** = length of longest proper prefix of s that is also a suffix = the happy prefix length.

**Rolling hash alternative**: Maintain prefix hash from left and suffix hash from right; find largest k where they match.

**Gotcha**: "Proper" means not equal to s itself — LPS handles this by definition.

---

### 8. Count Palindromic Subsequences

**Core idea**: Interval DP. `dp[i][j]` = number of distinct palindromic subsequences in `s[i..j]`.

**Recurrence** (for each of 4 chars `c`):
- Find `lo` = first occurrence of c in [i,j], `hi` = last occurrence
- If no c: add 0
- If lo == hi (one c): add 1
- If lo+1 == hi (two adjacent c): add 2
- Else: add `dp[lo+1][hi-1] + 2`

**Why +2?** The two c's wrap around all inner palindromes (each inner palindrome becomes a new one), plus "c" and "cc" themselves.

**Modulo**: Answer mod 10^9 + 7.

**Gotcha**: Precompute `next[i][c]` and `prev[i][c]` arrays for O(1) lo/hi lookup, otherwise O(n) per cell → O(n³) total.
