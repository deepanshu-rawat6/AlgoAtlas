class Solution:
    """
    ## 567. Permutation in String

    Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of
    `s1`, or `false` otherwise.

    In other words, return `true` if one of `s1`'s permutations is a substring of `s2`.

    ### Examples

    ```text
    Input:  s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains "ba", a permutation of s1.

    Input:  s1 = "ab", s2 = "eidboaoo"
    Output: false
    ```

    ### Constraints

    - `1 <= s1.length, s2.length <= 10^4`
    - `s1` and `s2` consist of lowercase English letters.
    """

    def checkInclusion_brute(self, s1: str, s2: str) -> bool:
        # Sort each window of length len(s1) and compare to sorted s1 — O(n*m log m)
        # O(n * m log m) time, O(m) space
        target = sorted(s1)
        m = len(s1)
        for i in range(len(s2) - m + 1):
            if sorted(s2[i:i + m]) == target:
                return True
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Fixed-size window of length len(s1); use 26-element frequency arrays
        # Slide window right: add new char, remove char that fell out of window
        # If frequency arrays match, current window is a permutation of s1
        # O(n) time, O(1) space (fixed 26-char alphabet)
        if len(s1) > len(s2):
            return False
        need = [0] * 26
        have = [0] * 26
        for ch in s1:
            need[ord(ch) - ord('a')] += 1
        m = len(s1)
        for i, ch in enumerate(s2):
            have[ord(ch) - ord('a')] += 1
            if i >= m:
                have[ord(s2[i - m]) - ord('a')] -= 1
            if have == need:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    assert sol.checkInclusion("ab", "eidbaooo") == True
    assert sol.checkInclusion("ab", "eidboaoo") == False
    assert sol.checkInclusion("a", "a") == True
    assert sol.checkInclusion_brute("ab", "eidbaooo") == True
    assert sol.checkInclusion_brute("ab", "eidboaoo") == False
    print("All tests passed.")
