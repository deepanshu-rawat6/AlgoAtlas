"""
# 139: Word Break (Recursive)

Given a string `s` and a list of words `wordDict`, return `True` if `s` can be
segmented into a space-separated sequence of one or more dictionary words.

## Examples
```text
Input:  s = "leetcode", wordDict = ["leet","code"]
Output: True

Input:  s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: False
```

## Constraints
- Dictionary words may be reused any number of times.
- Solved with recursion plus memoization on the start index.
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Recursive with memoization O(n^2).
        # Try every prefix of s; if prefix is in dict, recurse on the suffix.
        # Memoize results for each starting index to avoid recomputation.
        word_set = set(wordDict)
        memo = {}

        def dp(start):
            if start == len(s):  # consumed entire string — success
                return True
            if start in memo:
                return memo[start]
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set and dp(end):
                    memo[start] = True
                    return True
            memo[start] = False
            return False

        return dp(0)


if __name__ == "__main__":
    sol = Solution()
    assert sol.wordBreak("leetcode", ["leet", "code"]) is True
    assert sol.wordBreak("applepenapple", ["apple", "pen"]) is True
    assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    assert sol.wordBreak("a", ["a"]) is True
    print("All tests passed.")
