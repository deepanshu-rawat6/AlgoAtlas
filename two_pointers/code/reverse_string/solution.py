from typing import List


class Solution:
    """
    ## LC 344: Reverse String

    Write a function that reverses a string. The input string is given as an array
    of characters `s`. You must do this by modifying the input array in-place with
    O(1) extra memory.

    ### Examples

    ```text
    Input:  s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

    Input:  s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
    ```

    ### Constraints

    - `1 <= s.length <= 10^5`
    - `s[i]` is a printable ASCII character.
    """

    def method_pythonic(self, s: List[str]) -> None:
        """O(n) time, O(n) space (slice creates a copy)."""
        # Slice reversal creates a copy and assigns back — O(n) space
        s[:] = s[::-1]

    def reverseString(self, s: List[str]) -> None:
        """O(n) time, O(1) space."""
        # Swap characters from both ends moving inward — O(1) space
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


if __name__ == "__main__":
    sol = Solution()

    s = ["h", "e", "l", "l", "o"]
    sol.reverseString(s)
    assert s == ["o", "l", "l", "e", "h"], f"Failed: {s}"

    s = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(s)
    assert s == ["h", "a", "n", "n", "a", "H"], f"Failed: {s}"

    s = ["a"]
    sol.reverseString(s)
    assert s == ["a"], f"Failed: {s}"

    print("All tests passed.")
