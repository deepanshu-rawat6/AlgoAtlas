"""
# LC 140: Word Break II

Given a string `s` and a dictionary of strings `wordDict`, add spaces in `s` to
construct a sentence where each word is a valid dictionary word. Return all such
possible sentences in any order. The same dictionary word may be reused.

## Examples
```text
Input:  s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Input:  s = "pineapplepenapple",
        wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
```

## Constraints
- 1 <= s.length <= 20
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 10
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        ## 140. Word Break II

        Given a string s and a dictionary of strings wordDict, add spaces in s to
        construct a sentence where each word is a valid dictionary word. Return all
        such possible sentences in any order.

        Note that the same word in the dictionary may be reused multiple times in
        the segmentation.

        ### Examples

        ```text
        Input:  s = "catsanddog",
                wordDict = ["cat","cats","and","sand","dog"]
        Output: ["cats and dog","cat sand dog"]

        Input:  s = "pineapplepenapple",
                wordDict = ["apple","pen","applepen","pine","pineapple"]
        Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]

        Input:  s = "catsandog",
                wordDict = ["cats","dog","sand","and","cat"]
        Output: []
        ```

        ### Constraints
        - `1 <= s.length <= 20`
        - `1 <= wordDict.length <= 1000`
        - `1 <= wordDict[i].length <= 10`
        - s and wordDict[i] consist of only lowercase English letters.
        - All strings in wordDict are unique.
        """
        # DFS with memoization: at each position try all words that match
        # Cache results per start index to avoid recomputation
        # O(2^n) time worst case, O(n) memoization reduces repeated work; O(n) stack space
        word_set = set(wordDict)
        memo = {}

        def bt(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return ['']
            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    for rest in bt(end):
                        sentences.append(word + (' ' + rest if rest else ''))
            memo[start] = sentences
            return sentences

        return bt(0)


if __name__ == '__main__':
    s = Solution()
    assert sorted(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])) == sorted(["cats and dog", "cat sand dog"])
    assert sorted(s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])) == sorted(["pine apple pen apple", "pineapple pen apple", "pine applepen apple"])
    assert s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == []
    print("All tests passed.")
