# Tries

```mermaid
mindmap
  root((Tries))
    Basic Trie
      Implement Trie Prefix Tree LC208
    Wildcard Search
      Design Add And Search Words LC211
    Trie + DP
      Extra Characters in a String LC2707
    Trie + Backtracking
      Word Search II LC212
```

## Problem List

| # | Problem | LC | Difficulty |
|---|---------|-----|------------|
| 1 | Implement Trie Prefix Tree | [208](https://leetcode.com/problems/implement-trie-prefix-tree/) | 🟡 Medium |
| 2 | Design Add And Search Words | [211](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | 🟡 Medium |
| 3 | Extra Characters in a String | [2707](https://leetcode.com/problems/extra-characters-in-a-string/) | 🟡 Medium |
| 4 | Word Search II | [212](https://leetcode.com/problems/word-search-ii/) | 🔴 Hard |

---

## Approach Diagrams

### Trie Node Structure

```mermaid
flowchart TD
    A["TrieNode ───────────── children: dict[char → TrieNode] is_end: bool"] --> B["Example: insert 'cat'"]
    B --> C["root  children: c → ..."]
    C --> D["c-node  children: a → ..."]
    D --> E["a-node  children: t → ..."]
    E --> F["t-node  is_end = True"]
```

### Insert / Search / StartsWith Operations

```mermaid
flowchart TD
    A[Operation] --> B{"Type"}
    B -- insert word --> C[node = root]
    C --> D[For each char in word]
    D --> E{"char in node.children?"}
    E -- No --> F[Create new TrieNode]
    E -- Yes --> G[Move to child]
    F --> G
    G --> D
    D --> H[Mark last node is_end = True]
    B -- search word --> I[node = root]
    I --> J[For each char in word]
    J --> K{"char in node.children?"}
    K -- No --> L[Return False]
    K -- Yes --> M[Move to child]
    M --> J
    J --> N[Return node.is_end]
    B -- startsWith prefix --> O[Same as search but return True if all chars found]
```

### Wildcard Search with DFS — LC 211

```mermaid
flowchart TD
    A[search word with dots] --> B[DFS from root]
    B --> C[For each char in word]
    C --> D{"char == dot?"}
    D -- Yes --> E[Recurse into ALL children nodes]
    D -- No --> F{"char in node.children?"}
    F -- No --> G[Return False]
    F -- Yes --> H[Move to child]
    E --> I{"Any child returns True?"}
    I -- Yes --> J[Return True]
    I -- No --> G
    H --> C
    C --> K[Return node.is_end]
```

### Trie + Backtracking — Word Search II (LC 212)

```mermaid
flowchart TD
    A[Build Trie from word list] --> B[DFS on each board cell]
    B --> C{"char at cell in trie node children?"}
    C -- No --> D[Prune: return early]
    C -- Yes --> E[Move to trie child node]
    E --> F{"node.is_end?"}
    F -- Yes --> G[Add word to results mark node.is_end = False to avoid duplicates]
    F -- No --> H[Continue DFS]
    G --> H
    H --> I[Mark cell visited explore 4 neighbors]
    I --> J[Unmark cell backtrack]
    J --> K{"Trie node has no children left?"}
    K -- Yes --> L[Prune trie branch for efficiency]
    K -- No --> B
```

### When to Use Trie vs HashMap

```mermaid
flowchart TD
    A[String lookup problem] --> B{"Need prefix operations?"}
    B -- Yes --> C{"How many words?"}
    C -- Many, shared prefixes --> D[Trie space-efficient LC 208, 211, 212]
    C -- Few words --> E[HashSet is fine]
    B -- No --> F{"Exact match only?"}
    F -- Yes --> G[HashMap / HashSet simpler, O1 lookup]
    F -- No, need wildcard --> H[Trie + DFS LC 211]
    A --> I{"Need to find all words in a grid?"}
    I -- Yes --> J[Trie + Backtracking LC 212 better than running search per word]
    A --> K{"DP with word boundary checks?"}
    K -- Yes --> L[Trie speeds up boundary lookup LC 2707]
```

---

## Complexity Summary

| Problem | Time | Space | Notes |
|---------|------|-------|-------|
| Insert (208) | O(L) | O(L) | L = word length |
| Search (208) | O(L) | O(1) | |
| StartsWith (208) | O(L) | O(1) | |
| Add & Search (211) | O(L) insert, O(26^L) search worst | O(total chars) | Dot triggers full DFS |
| Extra Characters (2707) | O(n² · L) | O(total chars) | DP + trie lookup |
| Word Search II (212) | O(m·n · 4^L) | O(total chars) | Trie prunes repeated searches |

> L = average word length, m·n = board size

---

## Study Order

```mermaid
flowchart LR
    S1["Step 1 Implement Trie 208 Build the data structure"]
    S2["Step 2 Add & Search Words 211 Add wildcard DFS"]
    S3["Step 3 Extra Characters 2707 Trie + DP"]
    S4["Step 4 Word Search II 212 Trie + Backtracking"]
    S1 --> S2 --> S3 --> S4
```

**Key insight:** A Trie is just a tree where each edge is a character. Its power is shared prefixes — instead of storing "cat", "car", "card" three times, they share the "ca" path. Always implement LC 208 from scratch before attempting the others.
