"""
LC 647 — Palindromic Substrings
=================================

Given a string `s`, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Examples
--------
```text
Input:  s = "abc"
Output: 3
Explanation: "a", "b", "c"

Input:  s = "aaa"
Output: 6
Explanation: "a", "a", "a", "aa", "aa", "aaa"
```

Constraints
-----------
- 1 <= s.length <= 1000
- s consists of lowercase English letters
"""


class Solution:
    # Approach 1: Expand around center — O(n^2) time, O(1) space
    def countSubstrings(self, s: str) -> int:
        # Expand around each center; count every valid palindrome found
        count = 0

        def expand(l: int, r: int) -> None:
            nonlocal count
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        return count

    # Approach 2: DP table — O(n^2) time, O(n^2) space
    def countSubstrings_dp(self, s: str) -> int:
        # dp[i][j] = True if s[i..j] is palindrome; count all True entries
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    assert sol.countSubstrings("abc") == 3
    assert sol.countSubstrings("aaa") == 6
    assert sol.countSubstrings_dp("abc") == 3
    assert sol.countSubstrings_dp("aaa") == 6
    print("All tests passed.")
