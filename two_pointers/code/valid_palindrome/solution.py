"""
## LC 125: Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward
and backward.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Examples

```text
Input:  s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input:  s = "race a car"
Output: false

Input:  s = " "
Output: true
```

### Constraints

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.
"""


class Solution:
    def method_filter(self, s: str) -> bool:
        """O(n) time, O(n) space."""
        # Strip non-alphanumeric chars and lowercase, then compare to reverse
        filtered = [c.lower() for c in s if c.isalnum()]
        return filtered == filtered[::-1]

    def isPalindrome(self, s: str) -> bool:
        """O(n) time, O(1) space."""
        # Skip non-alphanumeric chars from both ends before comparing
        # Move both pointers inward; mismatch means not a palindrome
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    sol = Solution()

    assert sol.isPalindrome("A man, a plan, a canal: Panama") is True
    assert sol.isPalindrome("race a car") is False
    assert sol.isPalindrome(" ") is True
    assert sol.isPalindrome("0P") is False

    print("All tests passed.")
