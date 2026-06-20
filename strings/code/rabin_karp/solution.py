"""
# Rabin-Karp Rolling Hash (LC 28 variant)

Implement the Rabin-Karp algorithm for substring search using a rolling hash.
Given strings `haystack` and `needle`, return the index of the first occurrence of
`needle` in `haystack`, or `-1` if not found.

## Examples

```text
Input:  haystack = "hello", needle = "ll"
Output: 2

Input:  haystack = "aaaaa", needle = "bba"
Output: -1

Input:  haystack = "mississippi", needle = "issip"
Output: 4
```

## Constraints
- 0 <= haystack.length, needle.length <= 5 * 10^4
- haystack and needle consist of only lowercase English letters
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Approach 1: Rabin-Karp rolling hash O(n+m) average, O(nm) worst case
        Hash needle; slide window over haystack updating hash in O(1).
        Verify on hash match to handle collisions.
        """
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        if m > n:
            return -1

        BASE, MOD = 31, 10**9 + 7
        # precompute BASE^(m-1) mod MOD
        power = pow(BASE, m - 1, MOD)

        def char_val(c: str) -> int:
            return ord(c) - ord('a') + 1

        # compute hash of needle and first window
        needle_hash = 0
        window_hash = 0
        for i in range(m):
            needle_hash = (needle_hash * BASE + char_val(needle[i])) % MOD
            window_hash = (window_hash * BASE + char_val(haystack[i])) % MOD

        if window_hash == needle_hash and haystack[:m] == needle:
            return 0

        for i in range(1, n - m + 1):
            # roll: remove leftmost char, add new rightmost char
            window_hash = (window_hash - char_val(haystack[i - 1]) * power) % MOD
            window_hash = (window_hash * BASE + char_val(haystack[i + m - 1])) % MOD
            if window_hash == needle_hash and haystack[i:i + m] == needle:
                return i

        return -1

    def strStr_naive(self, haystack: str, needle: str) -> int:
        """Approach 2: Brute force O(nm) — baseline for comparison"""
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1


# Tests
if __name__ == "__main__":
    sol = Solution()
    assert sol.strStr("hello", "ll") == 2
    assert sol.strStr("aaaaa", "bba") == -1
    assert sol.strStr("", "") == 0
    assert sol.strStr("mississippi", "issip") == 4
    assert sol.strStr_naive("hello", "ll") == 2
    print("All tests passed")
