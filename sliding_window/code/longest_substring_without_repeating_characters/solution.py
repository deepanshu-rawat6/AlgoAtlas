class Solution:
    """
    ## 3. Longest Substring Without Repeating Characters

    Given a string `s`, find the length of the longest substring without repeating
    characters.

    ### Examples

    ```text
    Input:  s = "abcabcbb"
    Output: 3
    Explanation: "abc" is the longest substring without repeating characters.

    Input:  s = "bbbbb"
    Output: 1
    Explanation: "b" is the longest substring.

    Input:  s = "pwwkew"
    Output: 3
    Explanation: "wke" is the longest substring.
    ```

    ### Constraints

    - `0 <= s.length <= 5 * 10^4`
    - `s` consists of English letters, digits, symbols, and spaces.
    """

    def lengthOfLongestSubstring_brute(self, s: str) -> int:
        # Try all substrings; check uniqueness via set — O(n^3)
        # O(n^3) time, O(min(n, m)) space where m is charset size
        best = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if len(set(s[i:j])) == j - i:
                    best = max(best, j - i)
        return best

    def lengthOfLongestSubstring(self, s: str) -> int:
        # Slide right pointer; if char already in window, jump left past its last occurrence
        # char_idx stores the most recent index of each character
        # O(n) time, O(min(n, m)) space
        char_idx: dict[str, int] = {}
        left = best = 0
        for right, ch in enumerate(s):
            if ch in char_idx and char_idx[ch] >= left:
                left = char_idx[ch] + 1
            char_idx[ch] = right
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("") == 0
    assert sol.lengthOfLongestSubstring_brute("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring_brute("bbbbb") == 1
    print("All tests passed.")
