class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        """
        Approach 1: Interval DP O(n^2) time and space
        dp[i][j] = number of distinct palindromic subsequences in s[i..j].

        For each of 4 chars c in {a,b,c,d}:
          lo = first occurrence of c in [i,j]
          hi = last occurrence of c in [i,j]
          - no c in range:       add 0
          - lo == hi (one c):    add 1  ("c")
          - lo+1 == hi (two adj):add 2  ("c", "cc")
          - else:                add dp[lo+1][hi-1] + 2
            (each inner palindrome wrapped by c, plus "c" and "cc")
        """
        MOD = 10**9 + 7
        n = len(s)

        # precompute next[i][c] and prev[i][c] for O(1) lo/hi lookup
        # next_occ[i][c] = next occurrence of char c at or after index i
        # prev_occ[i][c] = prev occurrence of char c at or before index i
        chars = 'abcd'
        next_occ = [[n] * 4 for _ in range(n + 1)]
        prev_occ = [[-1] * 4 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for ci, c in enumerate(chars):
                next_occ[i][ci] = i if s[i] == c else next_occ[i + 1][ci]

        for i in range(n):
            for ci, c in enumerate(chars):
                prev_occ[i][ci] = i if s[i] == c else prev_occ[i - 1][ci]

        dp = [[0] * n for _ in range(n)]

        # fill by increasing interval length
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for ci, c in enumerate(chars):
                    lo = next_occ[i][ci]
                    hi = prev_occ[j][ci]
                    if lo > j:          # c not in [i,j]
                        continue
                    elif lo == hi:      # exactly one c
                        dp[i][j] = (dp[i][j] + 1) % MOD
                    elif lo + 1 == hi:  # two adjacent c's
                        dp[i][j] = (dp[i][j] + 2) % MOD
                    else:               # two c's with stuff in between
                        dp[i][j] = (dp[i][j] + dp[lo + 1][hi - 1] + 2) % MOD

        return dp[0][n - 1]


# Tests
if __name__ == "__main__":
    sol = Solution()
    assert sol.countPalindromicSubsequences("bccb") == 6
    # "b","c","c","b","bc","cb","bcb","bccb","cc" — wait, distinct: b,c,bb,cc,bcb,bccb = 6
    assert sol.countPalindromicSubsequences("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba") == 104860361
    print("All tests passed")
