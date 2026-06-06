class Solution:
    def strToInt(self, s: str) -> int:
        # Recursive approach: process one digit at a time from left to right.
        # strToInt(s[0:n]) = strToInt(s[0:n-1]) * 10 + digit_value(s[n-1])
        # Base case: single character -> return its digit value
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return ord(s[0]) - ord('0')  # convert char to digit without int()
        # Recurse on all but last char, then append last digit
        return self.strToInt(s[:-1]) * 10 + (ord(s[-1]) - ord('0'))


if __name__ == "__main__":
    sol = Solution()
    assert sol.strToInt("1234") == 1234
    assert sol.strToInt("0") == 0
    assert sol.strToInt("9") == 9
    assert sol.strToInt("100") == 100
    assert sol.strToInt("999") == 999
    print("All tests passed.")
