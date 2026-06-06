"""
LC 8 Variant - String to Integer (atoi) - Recursive Implementation

Problem: Implement atoi which converts a string to a 32-bit signed integer recursively.
Steps: strip leading whitespace, read optional sign, read digits until non-digit.

Examples:
    s = "   -42"       -> -42
    s = "4193 with words" -> 4193
    s = "words and 987"  -> 0

Constraints:
    0 <= s.length <= 200
    Clamp result to [-2^31, 2^31 - 1]
"""

INT_MIN, INT_MAX = -(2**31), 2**31 - 1


class Solution:
    def myAtoi(self, s: str) -> int:
        # Strip leading whitespace upfront, then delegate to recursive helper
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        start = 0
        if s[0] in ('+', '-'):
            sign = -1 if s[0] == '-' else 1
            start = 1

        def recurse(idx: int, current: int) -> int:
            # Base case: end of string or non-digit character
            if idx == len(s) or not s[idx].isdigit():
                return current
            # Recursive case: shift current left and add new digit
            return recurse(idx + 1, current * 10 + int(s[idx]))

        result = sign * recurse(start, 0)
        return max(INT_MIN, min(INT_MAX, result))  # clamp to 32-bit range


if __name__ == '__main__':
    sol = Solution()
    assert sol.myAtoi("   -42") == -42
    assert sol.myAtoi("4193 with words") == 4193
    assert sol.myAtoi("words and 987") == 0
    assert sol.myAtoi("") == 0
    assert sol.myAtoi("-91283472332") == INT_MIN
    assert sol.myAtoi("91283472332") == INT_MAX
    print("All tests passed.")
