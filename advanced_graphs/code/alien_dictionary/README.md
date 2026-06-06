# Alien Dictionary (LC 269)

Given a sorted list of words in an alien language, deduce the character ordering of the
alien alphabet. Return any valid ordering, or `""` if contradictory (cycle exists).

## Approaches

### 1. Kahn's BFS Topological Sort
**Complexity:** O(C) time, O(C) space (C = total characters across all words)

Compare adjacent word pairs to extract ordering constraints (edges). Build a directed
graph of character dependencies. Kahn's BFS topological sort gives the alien alphabet
order. Return `""` if a cycle is detected (processed chars < total unique chars).

**Why it works:** Each adjacent word pair reveals at most one ordering constraint
(the first differing character). Topological sort on these constraints gives a valid
alphabet order. A cycle means contradictory constraints.

### 2. DFS Topological Sort
**Complexity:** O(C) time, O(C) space

Same graph construction. DFS with 3-state coloring detects cycles. Post-order DFS
gives reverse topological order; reverse at the end.

**Why it works:** Same as Course Schedule — DFS post-order naturally produces reverse
topological order. A back edge (in-progress node revisited) signals a cycle.

## Key Insight

Extract ordering constraints by comparing adjacent words — only the **first differing
character** in each pair gives information. Then topological sort on the constraint
graph gives the alphabet. Early exit: if `word[i]` is a prefix of `word[i-1]` but
shorter, the input is invalid.

## Edge Cases

- Adjacent words where first is a prefix of second but longer — return `""`.
- Cycle in character ordering — return `""`.
- Single word — return its unique characters in any order.
- Characters appearing in only one word with no constraints — include them in any position.
