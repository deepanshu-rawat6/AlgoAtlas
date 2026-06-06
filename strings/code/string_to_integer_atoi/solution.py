class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1
        i, n = 0, len(s)

        # Step 1: skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: read optional sign
        sign = 1
        if i < n and s[i] in '+-':
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3: read digits, stop at first non-digit
        result = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        # Step 4: apply sign and clamp to 32-bit signed integer range
        result *= sign
        return max(INT_MIN, min(INT_MAX, result))


# Tests
if __name__ == '__main__':
    sol = Solution()
    assert sol.myAtoi("42") == 42
    assert sol.myAtoi("   -42") == -42
    assert sol.myAtoi("4193 with words") == 4193
    assert sol.myAtoi("words and 987") == 0
    assert sol.myAtoi("-91283472332") == -(2**31)
    assert sol.myAtoi("91283472332") == 2**31 - 1
    assert sol.myAtoi("  +0 123") == 0
    print("All tests passed.")
