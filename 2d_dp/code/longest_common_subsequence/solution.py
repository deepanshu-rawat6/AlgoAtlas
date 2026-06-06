"""
# 1143. Longest Common Subsequence

## Problem
Given two strings `text1` and `text2`, return the length of their longest common
subsequence. A subsequence is a sequence derived from a string by deleting some
(or no) characters without changing the relative order of the remaining characters.

## Examples
```text
Input:  text1 = "abcde", text2 = "ace"
Output: 3
Explanation: LCS is "ace"

Input:  text1 = "abc", text2 = "abc"
Output: 3

Input:  text1 = "abc", text2 = "def"
Output: 0
```

## Constraints
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters
"""


class Solution:
    def longestCommonSubsequence_2d(self, text1: str, text2: str) -> int:
        # Time: O(m*n), Space: O(m*n)
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] = LCS of text1[:i] and text2[:j]
        # If chars match: dp[i][j] = dp[i-1][j-1] + 1; else max of skip either
        # Time: O(m*n), Space: O(min(m,n))
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        n = len(text2)
        dp = [0] * (n + 1)
        for c1 in text1:
            prev = 0
            for j, c2 in enumerate(text2):
                temp = dp[j+1]
                dp[j+1] = prev + 1 if c1 == c2 else max(dp[j+1], dp[j])
                prev = temp
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    assert s.longestCommonSubsequence("abcde", "ace") == 3
    assert s.longestCommonSubsequence("abc", "abc") == 3
    assert s.longestCommonSubsequence("abc", "def") == 0
    assert s.longestCommonSubsequence_2d("abcde", "ace") == 3
    print("All tests passed.")
