"""
# LC 8: String to Integer (atoi)

Implement `myAtoi(string s)` which converts a string to a 32-bit signed integer.
The algorithm: (1) skip leading whitespace, (2) read optional `+`/`-` sign,
(3) read digits until a non-digit character, (4) clamp result to `[-2^31, 2^31-1]`.

## Examples

```text
Input:  s = "42"
Output: 42

Input:  s = "   -42"
Output: -42

Input:  s = "4193 with words"
Output: 4193

Input:  s = "-91283472332"
Output: -2147483648
```

## Constraints
- 0 <= s.length <= 200
- s consists of English letters, digits, `' '`, `'+'`, `'-'`, and `'.'`
"""


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
