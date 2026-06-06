"""
LC 5 — Longest Palindromic Substring
======================================

Given a string `s`, return the longest palindromic substring in `s`.

Examples
--------
```text
Input:  s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input:  s = "cbbd"
Output: "bb"
```

Constraints
-----------
- 1 <= s.length <= 1000
- s consists of only digits and English letters
"""


class Solution:
    # Approach 1: Brute force — O(n^3) time, O(1) space
    def longestPalindrome_brute(self, s: str) -> str:
        # Try all substrings; check each for palindrome property — O(n^3)
        def is_palindrome(t: str) -> bool:
            return t == t[::-1]

        best = s[0]
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if j - i > len(best) and is_palindrome(s[i:j]):
                    best = s[i:j]
        return best

    # Approach 2: Expand around center — O(n^2) time, O(1) space
    def longestPalindrome(self, s: str) -> str:
        # Expand around each center (odd and even length) to find longest palindrome
        start, end = 0, 0

        def expand(l: int, r: int) -> tuple:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        for i in range(len(s)):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i + 1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start:end + 1]

    # Approach 3: DP table — O(n^2) time, O(n^2) space
    def longestPalindrome_dp(self, s: str) -> str:
        # dp[i][j] = True if s[i..j] is palindrome; build from shorter to longer
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1
        for i in range(n):
            dp[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = length == 2 or dp[i + 1][j - 1]
                    if dp[i][j] and length > max_len:
                        start, max_len = i, length
        return s[start:start + max_len]


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPalindrome("babad") in ("bab", "aba")
    assert sol.longestPalindrome("cbbd") == "bb"
    assert sol.longestPalindrome("a") == "a"
    assert sol.longestPalindrome_brute("babad") in ("bab", "aba")
    assert sol.longestPalindrome_dp("babad") in ("bab", "aba")
    print("All tests passed.")
