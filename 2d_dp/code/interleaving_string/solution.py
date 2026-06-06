"""
# 97. Interleaving String

## Problem
Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an interleaving
of `s1` and `s2`. An interleaving of two strings s and t is a configuration where
s and t are divided into n and m substrings respectively, and the strings are
interleaved (maintaining relative order of characters from each string).

## Examples
```text
Input:  s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Input:  s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Input:  s1 = "", s2 = "", s3 = ""
Output: true
```

## Constraints
- 0 <= s1.length, s2.length <= 100
- 0 <= s3.length <= 200
- s1, s2, and s3 consist of lowercase English letters
"""


class Solution:
    def isInterleave_2d(self, s1: str, s2: str, s3: str) -> bool:
        # Time: O(m*n), Space: O(m*n)
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                            (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[m][n]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp[i][j] = can s1[:i] and s2[:j] interleave to form s3[:i+j]
        # True if (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        # Time: O(m*n), Space: O(n)
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(1, n + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n + 1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or \
                         (dp[j-1] and s2[j-1] == s3[i+j-1])
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    assert s.isInterleave("aabcc", "dbbca", "aadbbcbcac") == True
    assert s.isInterleave("aabcc", "dbbca", "aadbbbaccc") == False
    assert s.isInterleave("", "", "") == True
    assert s.isInterleave_2d("aabcc", "dbbca", "aadbbcbcac") == True
    print("All tests passed.")
