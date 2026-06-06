"""
# 10. Regular Expression Matching

## Problem
Given an input string `s` and a pattern `p`, implement regular expression matching
with support for '.' and '*' where:
- '.' matches any single character.
- '*' matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

## Examples
```text
Input:  s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element 'a'. "aa" matches.

Input:  s = "ab", p = ".*"
Output: true
Explanation: ".*" matches any string.

Input:  s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

## Constraints
- 1 <= s.length <= 20
- 1 <= p.length <= 20
- s contains only lowercase English letters
- p contains only lowercase English letters, '.', and '*'
- It is guaranteed for each occurrence of '*', there will be a previous valid character to match
"""
from functools import lru_cache


class Solution:
    def isMatch_memo(self, s: str, p: str) -> bool:
        # Time: O(m*n), Space: O(m*n)
        @lru_cache(maxsize=None)
        def dp(i, j):
            if j == len(p):
                return i == len(s)
            first = i < len(s) and p[j] in (s[i], '.')
            if j + 1 < len(p) and p[j+1] == '*':
                return dp(i, j+2) or (first and dp(i+1, j))
            return first and dp(i+1, j+1)
        return dp(0, 0)

    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] = does s[:i] match p[:j]
        # '*' can match zero (dp[i][j-2]) or more (dp[i-1][j] if chars match)
        # Time: O(m*n), Space: O(m*n)
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j-1] == '*' and j >= 2:
                dp[0][j] = dp[0][j-2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]  # zero occurrences
                    if p[j-2] in (s[i-1], '.'):
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                elif p[j-1] in (s[i-1], '.'):
                    dp[i][j] = dp[i-1][j-1]
        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    assert s.isMatch("aa", "a*") == True
    assert s.isMatch("ab", ".*") == True
    assert s.isMatch("aa", "a") == False
    assert s.isMatch("aab", "c*a*b") == True
    assert s.isMatch("mississippi", "mis*is*p*.") == False
    assert s.isMatch_memo("aa", "a*") == True
    assert s.isMatch_memo("ab", ".*") == True
    print("All tests passed.")
