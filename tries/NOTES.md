# Tries (Prefix Trees)

## Core Intuition

A trie stores strings character by character in a tree. Each node represents a prefix.
Use when you need fast prefix lookups, autocomplete, or searching a dictionary of words.

- **TrieNode**: children map (dict or array[26]) + `is_end` flag
- **Insert**: Walk/create nodes for each character — O(m) where m = word length
- **Search**: Walk nodes; check `is_end` at last char — O(m)
- **StartsWith**: Same as search but do not require `is_end` — O(m)
- **Wildcard**: DFS with branching on `.` nodes — O(26^m) worst case (all dots)
- **Trie + Backtracking**: Build trie from word list, then DFS grid — prune when current trie node is None

**When Trie beats HashMap:**
- Prefix queries: HashMap cannot enumerate all strings with a given prefix without scanning all keys
- Wildcard matching: `.` expansion fans out over trie children naturally; set lookup cannot do this
- Shared prefix storage: "apple" and "application" share 5 nodes — saves space and allows early termination

**Three core operations — all O(m) in word length m:**
- `insert(word)`: walk and create nodes; set `is_end = True` on last node
- `search(word)`: walk nodes; return `node.is_end` at end, False if any node missing
- `startsWith(prefix)`: walk nodes; return True if all nodes exist, end flag irrelevant

**Trie + Backtracking (word_search_ii):**
- Build trie from word list once; then DFS the board tracking the current trie node
- If `node.children[ch]` is None, prune the entire DFS branch immediately
- After finding a word, set `node.word = None` to mark used — avoids duplicate results
- Optionally remove childless nodes bottom-up to shrink the trie during search

**Trie + DP (extra_characters_in_a_string):**
- `dp[i]` = minimum extra characters in `s[0..i-1]`
- At each position `i`, start a trie walk from position `j` to `i`; if trie marks a word end, update `dp[i] = min(dp[i], dp[j])`
- Trie walk from `j` allows early exit when no dictionary word starts with the current prefix — O(n * m) vs O(n^2) set scan in theory

**Suffix Trie vs Prefix Trie:**
- All four problems here use a prefix trie (insert left-to-right)
- Suffix tries/suffix arrays handle substring queries (does s contain t anywhere?) — different beast

---

## Java Idioms

### TrieNode Structure

Define as an inner class or package-private class. Use a fixed 26-element array for lowercase-only problems — faster than HashMap (no hashing, no boxing, cache-friendly):

```java
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd;
}
```

For problems with arbitrary characters or Unicode, swap `TrieNode[26]` for `HashMap<Character, TrieNode>`.

### Indexing

```java
int idx = c - 'a';  // 'a' -> 0, 'z' -> 25
```

### Insert Loop (common mistake vs correct form)

Wrong — does not store the new node back into the parent:
```java
// BUG: node.children[idx] is still null after this
if (node.children[idx] == null) new TrieNode();  // node lost
node = node.children[idx];                        // NullPointerException
```

Correct:
```java
for (char c : word.toCharArray()) {
    int idx = c - 'a';
    if (node.children[idx] == null) {
        node.children[idx] = new TrieNode();  // assign back into parent
    }
    node = node.children[idx];
}
node.isEnd = true;
```

### Wildcard Search (design_add_and_search_words)

Iterative search cannot branch on `.` cleanly. Use a recursive DFS helper:

```java
private boolean dfs(TrieNode node, String word, int i) {
    if (i == word.length()) return node.isEnd;
    char c = word.charAt(i);
    if (c == '.') {
        for (TrieNode child : node.children) {
            if (child != null && dfs(child, word, i + 1)) return true;
        }
        return false;
    }
    TrieNode next = node.children[c - 'a'];
    return next != null && dfs(next, word, i + 1);
}
```

### Word Search II (board DFS)

Build trie from word list, then DFS from each cell. Mark visited cells in-place:

```java
board[r][c] = '#';   // mark visited
// ... recurse into 4 neighbors, passing current trie node's child ...
board[r][c] = tmp;   // restore
```

Check `node.word != null` (or `node.isEnd`) to add to result; set `node.word = null` after adding to prevent duplicates.

### Extra Characters — Trie + DP

```java
// dp[i] = min extra chars in s[0..i-1]; dp[0] = 0
int[] dp = new int[n + 1];
Arrays.fill(dp, Integer.MAX_VALUE);
dp[0] = 0;
for (int i = 1; i <= n; i++) {
    dp[i] = dp[i - 1] + 1;  // default: s[i-1] is an extra char
    TrieNode node = root;
    for (int j = i - 1; j >= 0; j--) {
        int idx = s.charAt(j) - 'a';
        if (node.children[idx] == null) break;  // no word starts here, prune
        node = node.children[idx];
        if (node.isEnd && dp[j] != Integer.MAX_VALUE) {
            dp[i] = Math.min(dp[i], dp[j]);
        }
    }
}
return dp[n];
```

---

## Problems

| Problem | Key Insight | Tricky Part | Common Mistakes | Time | Space |
|---|---|---|---|---|---|
| **Implement Trie** (LC 208, Medium) | TrieNode with children dict/array and `is_end` flag; three operations walk the same path | `search` vs `startsWith`: both walk identically but only `search` checks `is_end` | Using a flat dict of full strings — defeats prefix sharing; not marking `is_end` on insert | O(m) per operation | O(n * m) total nodes |
| **Add and Search Words** (LC 211, Medium) | Standard trie insert; `search` uses recursive DFS — on `.`, branch into all non-null children | `.` forces recursion; iterative approach with a queue works but is messier; must handle `.` at end of pattern | Trying iterative search and getting stuck on branching; forgetting that `.` can match zero chars does not apply — it matches exactly one | O(m) insert, O(26^m) worst-case search | O(n * m) nodes |
| **Extra Characters in a String** (LC 2707, Medium) | `dp[i]` = min extra chars in `s[0..i-1]`; for each i walk trie backwards from i to find words ending at i | Walk trie from `j` going left-to-right through `s[j..i-1]` — direction matters; inner loop iterates `j` from `i-1` down to 0 | Not initializing `dp[0] = 0`; scanning with set instead of trie (both work, trie prunes earlier); off-by-one on dp indices | O(n^2) with trie walk | O(n + d * m) where d = dict size, m = avg word length |
| **Word Search II** (LC 212, Hard) | Build trie from all words once; DFS board tracking current trie node; prune when node has no child for current char | In-place board marking (`board[r][c] = '#'`) for visited; restore after DFS; after finding word set `node.word = None` to skip duplicates | Running separate Word Search I per word — O(words * m * n * 4^L); forgetting to restore board cell; adding duplicate words when word appears multiple times in grid | O(m * n * 4 * 3^(L-1)) DFS | O(total chars in words) for trie |

---

## Edge Cases

1. **Empty string insert/search**: An empty word terminates immediately; `is_end` must be set on the root node itself. Check that insert and search both handle `len(word) == 0` — root's `is_end` is set after the (empty) loop.

2. **Prefix searched as full word** (`search` vs `startsWith`): Inserting "apple" then searching "app" must return False. The trie path exists but `is_end` is not set at the "p" node. A common bug is returning True whenever the path exists.

3. **Wildcard `.` at end of pattern**: Pattern "ab." must match any three-letter word starting with "ab". The `.` still consumes exactly one character — it does not match zero. The DFS base case `i == word.length()` handles this correctly only if the last `.` has already advanced `i`.

4. **Duplicate words in word list (word_search_ii)**: The problem states all words are unique, but a defensive implementation sets `node.word = None` after collecting a word. Without this, the same word could be added to the result multiple times if multiple DFS paths reach the same trie node.

5. **Very long words**: Trie depth equals the maximum word length. A trie holding one 2000-character word has 2000 nodes in a single chain. This is correct but means the DFS in word_search_ii recurses to depth L, not depth of the board.

6. **`startsWith` vs `search` confusion**: `startsWith("app")` must return True even if "app" was never inserted — only "apple" was. The difference is solely the `is_end` check at the end. Mixing up the return value of the two methods is the single most common bug in LC 208.

7. **Word is a prefix of another word in dictionary**: Inserting "app" then "apple" — the node for "app" must have `is_end = True` and also have a child "l". Both can be true simultaneously. A node's `is_end` flag is independent of whether it has children.

8. **No dictionary match (extra_characters)**: If no word in the dictionary matches any substring of `s`, then `dp[i] = i` for all i — every character is extra. The transition `dp[i] = dp[i-1] + 1` (default skip) handles this automatically as long as `dp[0] = 0`.

---

## General Notes

- For lowercase-only problems (all four here), prefer `children = [None] * 26` / `TrieNode[26]` over a dict — O(1) indexed access, better cache behavior, no hash overhead.
- The DFS in word_search_ii prunes on `node = node.children.get(ch)` returning None — this is where the trie pays off vs brute force.
- Trie + DP (extra_characters) is a template for any "segment string using a dictionary" DP problem.
- When inserting into a trie in Java, always assign the new node back to `parent.children[idx]` before advancing `node` — forgetting the assignment is the #1 Java trie bug.
