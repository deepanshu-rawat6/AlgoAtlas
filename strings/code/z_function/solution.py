from typing import List


class Solution:
    def zFunction(self, s: str) -> List[int]:
        """
        Approach 1: Z-array O(n) time and space
        Z[i] = length of longest substring starting at i matching prefix of s.
        Maintain [l, r] = rightmost Z-box seen so far.
        """
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i < r:
                # reuse: Z[i] >= min(Z[i-l], r-i), then try to extend
                z[i] = min(z[i - l], r - i)
            # extend as far as possible
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            # update rightmost Z-box
            if i + z[i] > r:
                l, r = i, i + z[i]
        return z

    def patternSearch(self, text: str, pattern: str) -> List[int]:
        """
        Use Z-function for pattern matching: build pattern + '#' + text
        Positions where Z[i] == len(pattern) are match starts.
        """
        m = len(pattern)
        combined = pattern + '#' + text
        z = self.zFunction(combined)
        return [i - m - 1 for i in range(m + 1, len(combined)) if z[i] == m]


# Tests
if __name__ == "__main__":
    sol = Solution()
    # z[0] is conventionally 0 (or n, but we use 0)
    assert sol.zFunction("aabxaa") == [0, 1, 0, 0, 2, 1]
    assert sol.zFunction("aaaa") == [0, 3, 2, 1]
    assert sol.zFunction("abcabc") == [0, 0, 0, 3, 0, 0]

    assert sol.patternSearch("aabxaa", "aa") == [0, 4]
    assert sol.patternSearch("AABAACAADAABAABA", "AABA") == [0, 9, 12]
    print("All tests passed")
