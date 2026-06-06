from typing import List


class Solution:
    def computeLPS(self, pattern: str) -> List[int]:
        """
        Build LPS (Longest Proper Prefix which is also Suffix) array O(m).
        LPS[i] = length of longest proper prefix of pattern[0..i] = suffix.
        """
        m = len(pattern)
        lps = [0] * m
        length = 0  # length of previous longest prefix-suffix
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length != 0:
                # don't increment i; try shorter prefix
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        return lps

    def kmpSearch(self, text: str, pattern: str) -> int:
        """
        Approach 1: KMP O(n+m) — return index of first occurrence, -1 if not found.
        On mismatch at pattern[j], jump to lps[j-1] instead of restarting.
        """
        n, m = len(text), len(pattern)
        if m == 0:
            return 0
        lps = self.computeLPS(pattern)
        i = j = 0  # i = text index, j = pattern index
        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1
            if j == m:
                return i - j  # found at index i-j
            elif i < n and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]  # key: reuse prefix info
                else:
                    i += 1
        return -1

    def kmpSearchAll(self, text: str, pattern: str) -> List[int]:
        """Return all occurrence indices."""
        n, m = len(text), len(pattern)
        if m == 0:
            return []
        lps = self.computeLPS(pattern)
        results = []
        i = j = 0
        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1
            if j == m:
                results.append(i - j)
                j = lps[j - 1]  # continue searching
            elif i < n and text[i] != pattern[j]:
                j = lps[j - 1] if j != 0 else 0
                if j == 0:
                    i += 1
        return results


# Tests
if __name__ == "__main__":
    sol = Solution()
    assert sol.computeLPS("AABAACAABAA") == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
    assert sol.kmpSearch("AABAACAADAABAABA", "AABA") == 0
    assert sol.kmpSearch("hello", "ll") == 2
    assert sol.kmpSearch("aaaaa", "bba") == -1
    assert sol.kmpSearchAll("AABAACAADAABAABA", "AABA") == [0, 9, 12]
    print("All tests passed")
