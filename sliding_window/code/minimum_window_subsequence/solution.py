"""
LC 727 - Minimum Window Subsequence

Given strings s1 and s2, return the minimum window in s1 such that s2 is
a subsequence of that window. If no such window exists, return "".

Examples:
```text
Input: s1 = "abcdebdde", s2 = "bde"
Output: "bcde"

Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
Output: ""
```

Constraints:
- 1 <= s1.length <= 2 * 10^4
- 1 <= s2.length <= 100
- s1 and s2 consist of lowercase English letters
"""


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        # Approach 1: two-pointer forward + backward
        # Forward: find a window where s2 is a subsequence
        # Backward: shrink from right to minimize the window
        n, m = len(s1), len(s2)
        result = ""

        i = 0  # pointer into s1
        while i < n:
            # Forward pass: match s2 left-to-right starting from i
            j = 0
            while i < n and j < m:
                if s1[i] == s2[j]:
                    j += 1
                i += 1

            if j < m:
                break  # s2 not found, no more windows possible

            # i is now one past the end of the window; back up
            end = i - 1

            # Backward pass: shrink from end to find tightest window
            j = m - 1
            k = end
            while k >= 0 and j >= 0:
                if s1[k] == s2[j]:
                    j -= 1
                k -= 1

            start = k + 1  # tightest window start

            if not result or end - start + 1 < len(result):
                result = s1[start:end + 1]

            # Restart search from start + 1 to find next candidate
            i = start + 1

        return result

    def minWindow_dp(self, s1: str, s2: str) -> str:
        # Approach 2: DP
        # dp[i][j] = start index in s1 such that s1[dp[i][j]..i] contains s2[0..j-1]
        n, m = len(s1), len(s2)
        # dp[j] = earliest start in s1 to match s2[:j] ending at current s1 position
        dp = [-1] * (m + 1)
        dp[0] = 0  # empty s2 matched at any position
        result = ""

        for i in range(n):
            # Traverse s2 backwards to avoid using updated values
            for j in range(min(i + 1, m), 0, -1):
                if s1[i] == s2[j - 1] and dp[j - 1] != -1:
                    dp[j] = dp[j - 1]
            # Reset dp[0] for next character
            dp[0] = i + 1

            if dp[m] != -1:
                window = s1[dp[m]:i + 1]
                if not result or len(window) < len(result):
                    result = window

        return result


if __name__ == '__main__':
    s = Solution()
    assert s.minWindow("abcdebdde", "bde") == "bcde"
    assert s.minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "u") == ""
    assert s.minWindow("abcde", "ace") == "abcde"
    assert s.minWindow_dp("abcdebdde", "bde") == "bcde"
    assert s.minWindow_dp("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "u") == ""
    print("All tests passed.")
