# Design Add and Search Words Data Structure (LC 211)

Extend a trie to support wildcard search where `'.'` matches any single character.
- `addWord(word)` — standard trie insert.
- `search(word)` — return `True` if any stored word matches; `'.'` matches any letter.

## Approaches

### Trie + DFS for wildcards
- **Time:** O(m) for `addWord`; O(m * 26^d) for `search` where d = number of dots
- **Space:** O(n * m) for stored words
- `addWord`: standard trie insert — walk characters, create nodes, mark `is_end`.
- `search`: DFS through the trie. For a regular character, follow the exact child. For `'.'`, recursively try **all** children. Return `True` if any branch reaches `is_end` at the end of the word.

## Key Insight

A dot forces branching — you must explore every possible child at that position. DFS naturally handles this: if any branch succeeds, return `True` immediately. The worst case is a word of all dots against a trie full of 3-letter words, but in practice the trie prunes most branches early.

## Edge Cases

- `search(".")` on an empty trie → `False`.
- `search(".ad")` — the dot at position 0 tries all 26 possible first characters.
- A word with multiple dots compounds the branching: `search("b..")` tries all combinations for positions 1 and 2.
- Searching a word longer than any stored word → `False` (path runs out before `is_end`).
