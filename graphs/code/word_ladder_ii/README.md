# LC 126 - Word Ladder II

Find **all** shortest transformation sequences from `beginWord` to `endWord`, changing one letter at a time, using only words from `wordList`.

## Approach: BFS (layer) + DFS backtrack — O(n×m×26)
1. **BFS layer-by-layer**: build a `parents` map (word → set of words that lead to it at shortest distance). Remove each layer from the word set to prevent revisiting.
2. **DFS backtrack**: from `endWord`, follow parent pointers back to `beginWord` to reconstruct all paths.

## Key Insight
Remove the entire current BFS layer from the word set **before** processing the next layer. This prevents words in the same layer from being each other's parents (which would create non-shortest paths), while still allowing multiple parents within a layer.

## Edge Cases
- `endWord` not in `wordList` → return `[]`
- No path exists → return `[]`
- `beginWord == endWord` → edge case, typically not in constraints

## Example
```
beginWord="hit", endWord="cog"
BFS: hit→hot→{dot,lot}→{dog,log}→cog
Parents: cog←{dog,log}, dog←dot, log←lot, dot←hot, lot←hot, hot←hit
DFS gives: [hit,hot,dot,dog,cog] and [hit,hot,lot,log,cog]
```
