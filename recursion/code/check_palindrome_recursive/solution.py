class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Base case: empty string or single char is always a palindrome
        if len(s) <= 1:
            return True
        # Recursive case: first and last chars must match, then check middle
        if s[0] != s[-1]:
            return False
        return self.isPalindrome(s[1:-1])


if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome("racecar") is True
    assert sol.isPalindrome("abba") is True
    assert sol.isPalindrome("a") is True
    assert sol.isPalindrome("") is True
    assert sol.isPalindrome("abc") is False
    assert sol.isPalindrome("abcba") is True
    print("All tests passed.")
