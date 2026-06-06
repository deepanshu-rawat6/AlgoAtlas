"""
# 115. Distinct Subsequences

## Problem
Given two strings `s` and `t`, return the number of distinct subsequences of `s`
which equals `t`. A subsequence of a string is a new string formed from the original
string by deleting some (can be none) of the characters without disturbing the
relative positions of the remaining characters.

## Examples
```text
Input:  s = "rabbbit", t = "rabbit"
Output: 3
Explanation: Three ways to generate "rabbit" from "rabbbit":
  rabb[b]it -> rabbit (delete 3rd b)
  rab[b]bit -> rabbit (delete 2nd b)
  ra[b]bbit -> rabbit (delete 1st b)

Input:  s = "babgbag", t = "bag"
Output: 5
```

## Constraints
- 1 <= s.length, t.length <= 1000
- s and t consist of English letters
"""


class Solution:
    def numDistinct_2d(self, s: str, t: str) -> int:
        # Time: O(m*n), Space: O(m*n)
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[m][n]

    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] = ways to form t[:j] from s[:i]
        # If s[i-1]==t[j-1]: dp[i-1][j-1] + dp[i-1][j]; else dp[i-1][j]
        # Time: O(m*n), Space: O(n)
        n = len(t)
        dp = [0] * (n + 1)
        dp[0] = 1
        for c in s:
            for j in range(n, 0, -1):
                if c == t[j-1]:
                    dp[j] += dp[j-1]
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    assert s.numDistinct("rabbbit", "rabbit") == 3
    assert s.numDistinct("babgbag", "bag") == 5
    assert s.numDistinct("a", "b") == 0
    assert s.numDistinct_2d("rabbbit", "rabbit") == 3
    print("All tests passed.")
