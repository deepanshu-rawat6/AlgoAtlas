"""
Trie (Prefix Tree)
==================
A tree where each path from root to a node represents a string prefix.
Each node stores children (one per character) and an end-of-word flag.

Use cases:
  - Autocomplete / prefix search
  - Spell checking
  - IP routing tables
  - Word games (Boggle, Scrabble)

Complexity (w = word length, p = prefix length):
  Insert:          O(w)
  Search:          O(w)
  StartsWith:      O(p)
  Delete:          O(w)
  Wildcard search: O(26^w) worst case
  Autocomplete:    O(p + total output length)
Space: O(ALPHABET_SIZE * total_characters)
"""

from typing import List, Optional


class TrieNode:
    __slots__ = ("children", "is_end", "count")

    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end: bool = False
        self.count: int = 0   # number of words passing through this node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # ── Insert ────────────────────────────────────────────────────────────────

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1
        node.is_end = True

    # ── Search ────────────────────────────────────────────────────────────────

    def search(self, word: str) -> bool:
        """Exact match."""
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Returns True if any inserted word starts with prefix."""
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    # ── Delete ────────────────────────────────────────────────────────────────

    def delete(self, word: str) -> bool:
        """
        Returns True if word was deleted.
        Uses backtracking: remove nodes that are no longer needed
        (not a prefix of another word and not end of another word).
        """
        def _delete(node: TrieNode, word: str, depth: int) -> bool:
            if depth == len(word):
                if not node.is_end:
                    return False   # word not in trie
                node.is_end = False
                return len(node.children) == 0  # safe to delete if leaf

            ch = word[depth]
            if ch not in node.children:
                return False
            child = node.children[ch]
            should_delete_child = _delete(child, word, depth + 1)
            if should_delete_child:
                del node.children[ch]
                child.count -= 1
                return not node.is_end and len(node.children) == 0
            child.count -= 1
            return False

        return _delete(self.root, word, 0)

    # ── Wildcard Search ───────────────────────────────────────────────────────

    def wildcard_search(self, pattern: str) -> bool:
        """
        '.' matches any single character.
        Uses DFS/backtracking over trie nodes.
        """
        def dfs(node: TrieNode, i: int) -> bool:
            if i == len(pattern):
                return node.is_end
            ch = pattern[i]
            if ch == '.':
                return any(dfs(child, i + 1) for child in node.children.values())
            if ch not in node.children:
                return False
            return dfs(node.children[ch], i + 1)

        return dfs(self.root, 0)

    # ── Autocomplete ──────────────────────────────────────────────────────────

    def autocomplete(self, prefix: str) -> List[str]:
        """Return all words that start with prefix."""
        node = self._find_node(prefix)
        if not node:
            return []
        results = []
        self._collect(node, prefix, results)
        return results

    def _collect(self, node: TrieNode, current: str, results: List[str]) -> None:
        if node.is_end:
            results.append(current)
        for ch, child in node.children.items():
            self._collect(child, current + ch, results)

    # ── Count words with prefix ───────────────────────────────────────────────

    def count_prefix(self, prefix: str) -> int:
        """Number of inserted words that start with prefix."""
        node = self._find_node(prefix)
        return node.count if node else 0


if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "app", "application", "apply", "apt", "bat", "ball"]
    for w in words:
        trie.insert(w)

    print("search 'app':", trie.search("app"))           # True
    print("search 'ap':", trie.search("ap"))             # False
    print("startsWith 'ap':", trie.starts_with("ap"))    # True
    print("startsWith 'xyz':", trie.starts_with("xyz"))  # False

    print("autocomplete 'app':", sorted(trie.autocomplete("app")))
    # ['app', 'apple', 'application', 'apply']

    print("wildcard 'a..le':", trie.wildcard_search("a..le"))  # True (apple)
    print("wildcard 'b.t':", trie.wildcard_search("b.t"))      # True (bat)
    print("wildcard 'b..t':", trie.wildcard_search("b..t"))    # False

    print("count prefix 'app':", trie.count_prefix("app"))  # 4

    trie.delete("app")
    print("After deleting 'app':")
    print("  search 'app':", trie.search("app"))          # False
    print("  search 'apple':", trie.search("apple"))      # True (still there)
    print("  autocomplete 'app':", sorted(trie.autocomplete("app")))
    # ['apple', 'application', 'apply']
