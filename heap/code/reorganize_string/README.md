# Reorganize String (LC 767)

Rearrange characters of `s` so no two adjacent characters are the same. Return any valid arrangement, or `""` if impossible.

## Approaches

### Greedy Max-Heap
- **Time:** O(n log k) where k ≤ 26
- **Space:** O(k)
- Use a max-heap of `(count, char)` pairs. Each step: pop the most frequent character and append it. Hold the previous character in a "cooldown" slot — it can't be placed again until the next step. After placing the current character, push the previous one back if its count is still > 0. If the heap is empty before the string is complete, return `""`.

## Key Insight

Always placing the most frequent remaining character minimizes the chance of getting stuck with a character that can't be placed (because it was just used). The one-step cooldown is sufficient because we only need to avoid immediate repetition. If the most frequent character has count > `ceil(n/2)`, it's impossible — it would inevitably appear adjacent to itself.

## Edge Cases

- Single character → valid (no adjacency possible).
- `"aaab"` → impossible; `'a'` count (3) > `ceil(4/2)` = 2.
- All characters the same → impossible unless length is 1.
- Two characters with equal counts → they alternate perfectly.
- The result length check (`len(result) == len(s)`) catches the impossible case without explicit pre-checking.
