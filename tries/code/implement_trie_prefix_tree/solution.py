"""
# 208: Implement Trie (Prefix Tree)

Implement a trie (prefix tree) supporting insertion, exact-match search, and
prefix search: `insert(word)`, `search(word)`, and `startsWith(prefix)`.

## Examples
```text
Input:  insert("apple"); search("apple"); search("app")
        startsWith("app"); insert("app"); search("app")
Output: True; False; True; True
```

## Constraints
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    """
    **LC 208: Implement Trie (Prefix Tree)**

    A trie (prefix tree) is a tree data structure used to efficiently store
    and retrieve keys in a dataset of strings. Implement the `Trie` class:

    * `Trie()` — Initializes the trie object.
    * `insert(word)` — Inserts the string `word` into the trie.
    * `search(word)` — Returns `true` if `word` is in the trie (exact match).
    * `startsWith(prefix)` — Returns `true` if any previously inserted string
      has the prefix `prefix`.

    Example 1:
    ```text
    Input:  ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    Output: [null, null, true, false, true, null, true]
    ```

    **Constraints:**
    * `1 <= word.length, prefix.length <= 2000`
    * `word` and `prefix` consist only of lowercase English letters
    * At most `3 * 10^4` calls in total
    """

    def __init__(self):
        # O(1)
        pass

    def insert(self, word: str) -> None:
        # Walk character by character; create new TrieNode if path doesn't exist
        # Mark end_of_word on the final node
        # O(m) where m = len(word)
        pass

    def search(self, word: str) -> bool:
        # Walk the trie; return True only if path exists AND end_of_word is set
        # O(m)
        pass

    def startsWith(self, prefix: str) -> bool:
        # Walk the trie; return True if the prefix path exists (end_of_word irrelevant)
        # O(m)
        pass


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))       # Expected: True
    print(trie.search("app"))         # Expected: False
    print(trie.startsWith("app"))     # Expected: True
    trie.insert("app")
    print(trie.search("app"))         # Expected: True
