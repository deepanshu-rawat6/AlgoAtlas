from collections import Counter


class Solution:
    """
    ## 76. Minimum Window Substring

    Given two strings `s` and `t` of lengths `m` and `n` respectively, return the
    minimum window substring of `s` such that every character in `t` (including
    duplicates) is included in the window. If there is no such substring, return the
    empty string `""`.

    ### Examples

    ```text
    Input:  s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"

    Input:  s = "a", t = "a"
    Output: "a"

    Input:  s = "a", t = "aa"
    Output: ""
    ```

    ### Constraints

    - `1 <= m, n <= 10^5`
    - `s` and `t` consist of uppercase and lowercase English letters.
    """

    def minWindow_brute(self, s: str, t: str) -> str:
        # Try all substrings starting at i; stop as soon as t is covered — O(n^2*m)
        # O(n^2 * m) time, O(m) space
        need = Counter(t)
        best = ""
        for i in range(len(s)):
            have: dict[str, int] = {}
            for j in range(i, len(s)):
                have[s[j]] = have.get(s[j], 0) + 1
                if all(have.get(c, 0) >= need[c] for c in need):
                    if not best or j - i + 1 < len(best):
                        best = s[i:j + 1]
                    break
        return best

    def minWindow(self, s: str, t: str) -> str:
        # 'formed' counts how many unique chars in t are satisfied in current window
        # Expand right until all chars satisfied; then shrink left to minimize window
        # Track best window length and start index throughout
        # O(n + m) time, O(m) space
        if not t:
            return ""
        need = Counter(t)
        have: dict[str, int] = {}
        formed = 0
        required = len(need)
        left = 0
        best_len, best_l = float("inf"), 0
        for right, ch in enumerate(s):
            have[ch] = have.get(ch, 0) + 1
            if ch in need and have[ch] == need[ch]:
                formed += 1
            while formed == required:
                if right - left + 1 < best_len:
                    best_len, best_l = right - left + 1, left
                lch = s[left]
                have[lch] -= 1
                if lch in need and have[lch] < need[lch]:
                    formed -= 1
                left += 1
        return "" if best_len == float("inf") else s[best_l:best_l + best_len]


if __name__ == "__main__":
    sol = Solution()
    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert sol.minWindow("a", "a") == "a"
    assert sol.minWindow("a", "aa") == ""
    assert sol.minWindow_brute("ADOBECODEBANC", "ABC") == "BANC"
    assert sol.minWindow_brute("a", "a") == "a"
    assert sol.minWindow_brute("a", "aa") == ""
    print("All tests passed.")
