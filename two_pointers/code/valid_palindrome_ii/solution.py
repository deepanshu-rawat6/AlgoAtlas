class Solution:
    """
    ## LC 680: Valid Palindrome II

    Given a string `s`, return `true` if the `s` can be palindrome after deleting
    at most one character from it.

    ### Examples

    ```text
    Input:  s = "aba"
    Output: true

    Input:  s = "abca"
    Output: true
    Explanation: Delete 'c' to get "aba".

    Input:  s = "abc"
    Output: false
    ```

    ### Constraints

    - `1 <= s.length <= 10^5`
    - `s` consists of lowercase English letters.
    """

    def method_brute_force(self, s: str) -> bool:
        """O(n^2) time — try removing each character."""
        # Try removing each character and check if result is palindrome
        def is_palindrome(t: str) -> bool:
            return t == t[::-1]

        if is_palindrome(s):
            return True
        for i in range(len(s)):
            if is_palindrome(s[:i] + s[i + 1:]):
                return True
        return False

    def validPalindrome(self, s: str) -> bool:
        """O(n) time, O(1) space."""
        # Walk inward until a mismatch; then try skipping left or right char
        # If either skip produces a palindrome, one deletion suffices
        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    sol = Solution()

    assert sol.validPalindrome("aba") is True
    assert sol.validPalindrome("abca") is True
    assert sol.validPalindrome("abc") is False
    assert sol.validPalindrome("a") is True
    assert sol.validPalindrome("deeee") is True

    print("All tests passed.")
