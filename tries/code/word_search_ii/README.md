# Word Search II (LC 212)

Given an m×n board of characters and a list of words, return all words that can be formed by sequentially adjacent (horizontal/vertical) cells, using each cell at most once per word.

## Approaches

### Brute Force — DFS per word
- **Time:** O(w * m * n * 4^L) where w = words, L = max word length
- **Space:** O(L) recursion stack
- For each word, run an independent DFS from every cell. Extremely slow when the word list is large.

### Trie + Backtracking DFS (optimal)
- **Time:** O(m * n * 4^L) — single DFS pass covers all words simultaneously
- **Space:** O(total characters in all words) for the trie
- Build a trie from all words. DFS from every cell; at each step check if the current path is a trie prefix — if not, prune immediately. When a trie node has `word` set, record the word and **remove it from the trie** to avoid duplicates.

## Key Insight

The trie turns the word list into a shared prefix structure. Instead of re-running DFS for each word, one DFS traversal checks all words simultaneously. Pruning happens the moment the current board path diverges from every trie prefix — this is far more efficient than per-word DFS. Removing found words from the trie prevents duplicates and further prunes the search.

## Edge Cases

- Same word appearing multiple times in the word list — trie deduplicates naturally.
- A word that is a prefix of another word — both can be found independently via `is_end` markers.
- Single-cell board with a single-character word.
- Words longer than the board can accommodate → never found (DFS exhausts cells).
