class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        Approach 1: KMP on s + '#' + reverse(s) O(n) time and space
        The LPS value at the last position = length of longest palindromic prefix.
        Prepend reverse of the remaining suffix to make the whole string a palindrome.
        '#' separator prevents LPS from crossing the boundary.
        """
        if not s:
            return s
        rev = s[::-1]
        t = s + '#' + rev
        # compute LPS for t
        lps = [0] * len(t)
        length, i = 0, 1
        while i < len(t):
            if t[i] == t[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length != 0:
                length = lps[length - 1]
            else:
                i += 1
        # lps[-1] = length of longest palindromic prefix of s
        pal_prefix_len = lps[-1]
        return rev[:len(s) - pal_prefix_len] + s

    def shortestPalindrome_hash(self, s: str) -> str:
        """
        Approach 2: Rolling hash O(n) — find largest k where s[:k] is palindrome.
        Forward hash == backward hash means s[:k] is a palindrome.
        """
        BASE, MOD = 131, 10**9 + 7
        fwd = bwd = 0
        power = 1
        best = 0
        for i, c in enumerate(s):
            v = ord(c)
            fwd = (fwd * BASE + v) % MOD
            bwd = (bwd + v * power) % MOD
            power = power * BASE % MOD
            if fwd == bwd:
                best = i + 1  # s[:best] is a palindrome (probabilistic)
        return s[best:][::-1] + s


# Tests
if __name__ == "__main__":
    sol = Solution()
    assert sol.shortestPalindrome("aacecaaa") == "aaacecaaa"
    assert sol.shortestPalindrome("abcd") == "dcbabcd"
    assert sol.shortestPalindrome("") == ""
    assert sol.shortestPalindrome("a") == "a"
    assert sol.shortestPalindrome_hash("aacecaaa") == "aaacecaaa"
    assert sol.shortestPalindrome_hash("abcd") == "dcbabcd"
    print("All tests passed")
