# Word Search (LC 79)

Given a character grid and a word, return `true` if the word exists in the grid as a
sequence of adjacent (horizontally/vertically) cells, each used at most once.

## Approaches

### 1. DFS Backtracking with In-Place Marking
**Complexity:** O(m · n · 4^L) time, O(L) space (L = word length)

For each cell matching `word[0]`, DFS to match subsequent characters. Mark the current
cell as visited by replacing it with `'#'`; restore on backtrack.

**Why it works:** DFS explores all paths from a starting cell. In-place marking avoids
using a separate visited set. Restoring the cell on backtrack allows the same cell to
be used in different paths starting from different positions.

## Key Insight

In-place marking (`board[r][c] = '#'`) is the elegant trick — it temporarily "removes"
the cell from consideration during the current DFS path without extra memory. Restoring
it on backtrack is essential for correctness across different starting cells.

## Edge Cases

- Word longer than total cells — impossible, return `false`.
- Word with repeated characters — the in-place marking correctly prevents reuse within
  a single path.
- Single cell grid — return `true` if `word == board[0][0]`.
- Word not in grid — all DFS paths fail, return `false`.
