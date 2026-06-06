"""
LC 139 — Word Break
====================

Given a string `s` and a dictionary of strings `wordDict`, return true if `s`
can be segmented into a space-separated sequence of one or more dictionary words.
The same word in the dictionary may be reused multiple times.

Examples
--------
```text
Input:  s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: "leetcode" can be segmented as "leet code".

Input:  s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: "applepenapple" can be segmented as "apple pen apple".

Input:  s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

Constraints
-----------
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters
- All strings in wordDict are unique
"""

from typing import List
from functools import lru_cache


class Solution:
    # Approach 1: Top-down memoization — O(n^2 * m) time, O(n) space
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp(i): can s[i:] be segmented? Try all words starting at i
        word_set = set(wordDict)

        @lru_cache(maxsize=None)
        def dp(i: int) -> bool:
            if i == len(s):
                return True
            return any(s[i:j] in word_set and dp(j) for j in range(i + 1, len(s) + 1))

        return dp(0)

    # Approach 2: Bottom-up DP — O(n^2 * m) time, O(n) space
    def wordBreak_dp(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = True if s[:i] can be segmented; check all j < i where dp[j] and s[j:i] in dict
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    assert sol.wordBreak("leetcode", ["leet", "code"]) is True
    assert sol.wordBreak("applepenapple", ["apple", "pen"]) is True
    assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    assert sol.wordBreak_dp("leetcode", ["leet", "code"]) is True
    assert sol.wordBreak_dp("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    print("All tests passed.")
