# Implement Trie (Prefix Tree) (LC 208)

Design a trie that supports inserting words, exact-match search, and prefix search.
- `insert(word)` — add word to the trie.
- `search(word)` — return `True` only if the exact word exists.
- `startsWith(prefix)` — return `True` if any inserted word starts with the prefix.

## Approaches

### Trie with HashMap children
- **Time:** O(m) per operation, where m = word/prefix length
- **Space:** O(n * m) total for all inserted words
- Each `TrieNode` holds a `children: dict` mapping characters to child nodes, plus an `is_end` flag.
- `insert`: walk character by character, creating nodes as needed; mark `is_end = True` on the last node.
- `search`: walk the path; return `True` only if path exists **and** `is_end` is set.
- `startsWith`: same walk, but ignore `is_end` — any complete path is a valid prefix.

## Key Insight

The trie encodes shared prefixes structurally. "apple" and "app" share the path `a→p→p`; the difference is that "app" sets `is_end` at depth 3 while "apple" continues to depth 5. `search` needs `is_end`; `startsWith` only needs the path to exist.

## Edge Cases

- Searching a word that is a prefix of an inserted word (e.g., search "app" after inserting "apple") → `False` because `is_end` is not set at "app".
- Inserting the same word twice is idempotent — `is_end` is just set again.
- Empty string: `startsWith("")` should return `True` (root always exists).
