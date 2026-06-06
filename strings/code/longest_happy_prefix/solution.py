class Solution:
    def longestPrefix(self, s: str) -> str:
        """
        Approach 1: KMP LPS array O(n)
        LPS[n-1] = length of longest proper prefix of s that is also a suffix.
        That's exactly the happy prefix.
        """
        n = len(s)
        lps = [0] * n
        length, i = 0, 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length != 0:
                length = lps[length - 1]
            else:
                i += 1
        return s[:lps[-1]]

    def longestPrefix_hash(self, s: str) -> str:
        """
        Approach 2: Rolling hash O(n)
        Simultaneously build prefix hash (left→right) and suffix hash (right→left).
        Largest k where prefix_hash[k] == suffix_hash[k] is the answer.
        """
        BASE, MOD = 131, 10**9 + 7
        n = len(s)
        prefix = suffix = 0
        power = 1
        best = 0
        for i in range(n - 1):  # exclude full string (proper prefix/suffix)
            prefix = (prefix * BASE + ord(s[i])) % MOD
            suffix = (ord(s[n - 1 - i]) * power + suffix) % MOD
            power = power * BASE % MOD
            if prefix == suffix:
                best = i + 1
        return s[:best]


# Tests
if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPrefix("level") == "l"
    assert sol.longestPrefix("ababab") == "abab"
    assert sol.longestPrefix("leetcodeleet") == "leet"
    assert sol.longestPrefix("a") == ""
    assert sol.longestPrefix_hash("level") == "l"
    assert sol.longestPrefix_hash("ababab") == "abab"
    print("All tests passed")
