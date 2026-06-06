"""
# 72. Edit Distance

## Problem
Given two strings `word1` and `word2`, return the minimum number of operations
required to convert `word1` to `word2`. You have the following three operations:
- Insert a character
- Delete a character
- Replace a character

## Examples
```text
Input:  word1 = "horse", word2 = "ros"
Output: 3
Explanation:
  horse -> rorse (replace 'h' with 'r')
  rorse -> rose  (delete 'r')
  rose  -> ros   (delete 'e')

Input:  word1 = "intention", word2 = "execution"
Output: 5
```

## Constraints
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters
"""


class Solution:
    def minDistance_2d(self, word1: str, word2: str) -> int:
        # Time: O(m*n), Space: O(m*n)
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[m][n]

    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] = min edits to convert word1[:i] to word2[:j]
        # Match: dp[i-1][j-1]; else 1 + min(insert, delete, replace)
        # Time: O(m*n), Space: O(min(m,n))
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        n = len(word2)
        dp = list(range(n + 1))
        for c1 in word1:
            prev = dp[0]
            dp[0] += 1
            for j, c2 in enumerate(word2):
                temp = dp[j+1]
                dp[j+1] = prev if c1 == c2 else 1 + min(prev, dp[j+1], dp[j])
                prev = temp
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    assert s.minDistance("horse", "ros") == 3
    assert s.minDistance("intention", "execution") == 5
    assert s.minDistance("", "") == 0
    assert s.minDistance("a", "") == 1
    assert s.minDistance_2d("horse", "ros") == 3
    print("All tests passed.")
