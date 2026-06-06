# Longest Happy String (LC 1405)

Given counts `a`, `b`, `c` for letters 'a', 'b', 'c', construct the longest string that doesn't contain "aaa", "bbb", or "ccc" as a substring, using at most the given counts.

## Approaches

### Greedy Max-Heap
- **Time:** O(a + b + c)
- **Space:** O(1) — heap has at most 3 elements
- Use a max-heap of `(-count, char)`. Each step: pop the most frequent character. If the last two characters in the result are the same as the current character (would create a triple), pop the second most frequent instead, use it, then push the first back. Decrement the used character's count and push it back if still > 0.

## Key Insight

Greedily using the most frequent character maximizes length while the "last two same" check prevents triples. When the most frequent character is blocked, using the second most frequent "breaks" the run and allows the blocked character to be used again next step. This greedy is optimal because any deviation (using a less frequent character when the most frequent is available and safe) can only reduce the total length.

## Edge Cases

- One character has count 0 → it's never pushed to the heap.
- `a=7, b=1, c=0` → "aabaa" (5 chars); the single 'b' breaks the run once.
- `a=1, b=1, c=7` → 'c' dominates; result is "ccbccacc" (8 chars).
- If only one character remains and it would create a triple, the loop breaks early.
