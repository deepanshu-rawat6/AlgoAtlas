class Solution:
    """
    ## 424. Longest Repeating Character Replacement

    You are given a string `s` and an integer `k`. You can choose any character of the
    string and change it to any other uppercase English character. You can perform this
    operation at most `k` times.

    Return the length of the longest substring containing the same letter you can get
    after performing the above operations.

    ### Examples

    ```text
    Input:  s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with 'B's or vice versa.

    Input:  s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' -> "AABBBBA" (length 4).
    ```

    ### Constraints

    - `1 <= s.length <= 10^5`
    - `s` consists of only uppercase English letters.
    - `0 <= k <= s.length`
    """

    def characterReplacement_brute(self, s: str, k: int) -> int:
        # Try all windows; window is valid if (size - max_freq) <= k — O(n^2)
        # O(n^2) time, O(1) space
        best = 0
        for i in range(len(s)):
            freq: dict[str, int] = {}
            for j in range(i, len(s)):
                freq[s[j]] = freq.get(s[j], 0) + 1
                window = j - i + 1
                if window - max(freq.values()) <= k:
                    best = max(best, window)
        return best

    def characterReplacement(self, s: str, k: int) -> int:
        # Expand right; window is valid if (size - max_freq) <= k replacements
        # When invalid, slide left by 1 (shrink window, don't reset max_freq)
        # max_freq only increases — we only care about windows larger than current best
        # O(n) time, O(1) space
        freq: dict[str, int] = {}
        left = max_freq = best = 0
        for right, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            max_freq = max(max_freq, freq[ch])
            window = right - left + 1
            if window - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.characterReplacement("ABAB", 2) == 4
    assert sol.characterReplacement("AABABBA", 1) == 4
    assert sol.characterReplacement("A", 0) == 1
    assert sol.characterReplacement_brute("ABAB", 2) == 4
    assert sol.characterReplacement_brute("AABABBA", 1) == 4
    print("All tests passed.")
