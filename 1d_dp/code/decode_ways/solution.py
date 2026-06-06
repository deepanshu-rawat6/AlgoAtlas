"""
LC 91 — Decode Ways
====================

A message containing letters A-Z can be encoded into numbers using:
  'A' -> "1", 'B' -> "2", ..., 'Z' -> "26"

Given a string `s` containing only digits, return the number of ways to decode it.

Examples
--------
```text
Input:  s = "12"
Output: 2
Explanation: "AB" (1 2) or "L" (12)

Input:  s = "226"
Output: 3
Explanation: "BZ" (2 26), "VF" (22 6), "BBF" (2 2 6)

Input:  s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero.
```

Constraints
-----------
- 1 <= s.length <= 100
- s contains only digits
- s may contain leading zeros
"""

from functools import lru_cache


class Solution:
    # Approach 1: Top-down memoization — O(n) time, O(n) space
    def numDecodings(self, s: str) -> int:
        # dp(i): ways to decode s[i:]; '0' has 0 ways; two-digit check for 10-26
        @lru_cache(maxsize=None)
        def dp(i: int) -> int:
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            result = dp(i + 1)
            if i + 1 < len(s) and int(s[i:i + 2]) <= 26:
                result += dp(i + 2)
            return result

        return dp(0)

    # Approach 2: Bottom-up DP — O(n) time, O(n) space
    def numDecodings_dp(self, s: str) -> int:
        # Bottom-up from end; dp[i] = dp[i+1] + dp[i+2] if two-digit valid
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] != '0':
                dp[i] = dp[i + 1]
                if i + 1 < n and int(s[i:i + 2]) <= 26:
                    dp[i] += dp[i + 2]
        return dp[0]

    # Approach 3: Space-optimized — O(n) time, O(1) space
    def numDecodings_opt(self, s: str) -> int:
        # Space-optimized: next1=dp[i+1], next2=dp[i+2]; roll forward
        n = len(s)
        next2, next1 = 1, 1  # dp[n+1]=1 (sentinel), dp[n]=1 (base case)
        for i in range(n - 1, -1, -1):
            curr = 0
            if s[i] != '0':
                curr = next1
                if i + 1 < n and int(s[i:i + 2]) <= 26:
                    curr += next2
            next2, next1 = next1, curr
        return next1


if __name__ == "__main__":
    sol = Solution()
    assert sol.numDecodings("12") == 2
    assert sol.numDecodings("226") == 3
    assert sol.numDecodings("06") == 0
    assert sol.numDecodings("0") == 0
    assert sol.numDecodings_dp("226") == 3
    assert sol.numDecodings_opt("226") == 3
    print("All tests passed.")
