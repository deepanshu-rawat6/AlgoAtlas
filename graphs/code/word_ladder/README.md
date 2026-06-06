# Word Ladder (LC 127)

Find the length of the shortest transformation sequence from `beginWord` to `endWord`,
where each step changes exactly one letter and every intermediate word must be in
`wordList`. Return 0 if no sequence exists.

## Approaches

### 1. Standard BFS
**Complexity:** O(m² · n) time, O(m² · n) space (m = word length, n = wordList size)

BFS from `beginWord`. For each word, try replacing each character with a-z. If the
result is in `wordSet` and unvisited, enqueue it. Return level count when `endWord` found.

**Why it works:** BFS explores words by transformation distance. The first time `endWord`
is reached, it's via the shortest path.

### 2. Bidirectional BFS (optimal)
**Complexity:** O(m² · n) time, O(m² · n) space (but ~2× faster in practice)

Expand from both `beginWord` and `endWord` simultaneously. Always expand the smaller
frontier. When a word from one frontier appears in the other, the path is complete.

**Why it works:** Bidirectional BFS halves the effective search depth, dramatically
reducing the number of nodes explored in practice.

## Key Insight

Word transformation is an unweighted graph problem. Each word is a node; edges connect
words differing by one letter. BFS finds the shortest path. The trick is efficient
neighbor generation: try all 26 letters at each position rather than comparing all pairs.

## Edge Cases

- `endWord` not in `wordList` — return 0 immediately.
- `beginWord` == `endWord` — problem states they differ, but handle gracefully.
- No valid transformation path — return 0.
- Single-character words — each word connects to up to 25 others.
