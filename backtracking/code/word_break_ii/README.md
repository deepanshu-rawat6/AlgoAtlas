# Word Break II (LC 140)

Given a string `s` and a word dictionary, return all ways to segment `s` into a
space-separated sequence of dictionary words.

## Approaches

### 1. DFS with Memoization
**Complexity:** O(2ⁿ) worst case, O(n) memoization reduces repeated work; O(n) space

DFS from each position: try all prefixes that are valid dictionary words, recurse on
the remainder. Cache results per start index to avoid recomputing the same suffix.

**Why it works:** Without memoization, the same suffix is explored multiple times from
different paths. Caching `memo[start]` = list of sentences from position `start` ensures
each suffix is computed at most once.

## Key Insight

Memoization is the key optimization. The function `bt(start)` returns all valid
sentences for `s[start:]`. Since there are only `n` possible start positions, the
total work is bounded by `n × (number of words × word length)` rather than exponential.

## Edge Cases

- No valid segmentation — return `[]`.
- Single word equals `s` — return `[s]`.
- Word can be reused multiple times — the recursion naturally handles this.
- Overlapping words (e.g., `"cats"` and `"cat"`) — both paths are explored.
