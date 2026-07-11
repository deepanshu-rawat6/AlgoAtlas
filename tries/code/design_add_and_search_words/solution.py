"""
# 211: Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding whether a
string matches any previously added string, where the search word may contain
`'.'` wildcards that each match any single letter.

## Examples
```text
Input:  addWord("bad"); addWord("dad"); addWord("mad")
        search("pad"); search("bad"); search(".ad"); search("b..")
Output: False; True; True; True
```

## Constraints
- 1 <= word.length <= 25
- Words in addWord consist of lowercase English letters.
- Words in search consist of '.' or lowercase English letters.
- At most 10^4 calls to addWord and search.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    """
    **LC 211: Design Add and Search Words Data Structure**

    Design a data structure that supports adding new words and finding if a
    string matches any previously added string. The search word can contain
    dots `'.'` where each dot can match any letter.

    * `WordDictionary()` — Initializes the object.
    * `addWord(word)` — Adds `word` to the data structure.
    * `search(word)` — Returns `true` if any string matches `word`.
      A `'.'` matches any single character.

    Example 1:
    ```text
    Input:  ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
            [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    Output: [null,null,null,null,false,true,true,true]
    ```

    **Constraints:**
    * `1 <= word.length <= 25`
    * `word` in `addWord` consists of lowercase English letters
    * `word` in `search` consists of `'.'` or lowercase English letters
    * At most `10^4` calls to `addWord` and `search`
    """

    def __init__(self):
        # O(1)
        pass

    def addWord(self, word: str) -> None:
        # Standard trie insert: create nodes as needed, mark end_of_word
        # O(m) where m = len(word)
        pass

    def search(self, word: str) -> bool:
        # DFS through trie; '.' matches any child node (try all branches)
        # Regular char must match exactly; return True if end_of_word reached
        # O(m * 26^d) where d = number of dots, worst case O(m * 26^m)
        pass


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print(wd.search("pad"))   # Expected: False
    print(wd.search("bad"))   # Expected: True
    print(wd.search(".ad"))   # Expected: True
    print(wd.search("b.."))   # Expected: True
