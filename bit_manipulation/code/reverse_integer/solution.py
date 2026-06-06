"""
# 7. Reverse Integer

Given a signed 32-bit integer `x`, return `x` with its digits reversed.
If reversing `x` causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1],
return 0.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

## Examples

```text
Input: x = 123
Output: 321

Input: x = -123
Output: -321

Input: x = 120
Output: 21
```

## Constraints
- -2^31 <= x <= 2^31 - 1
"""

INT_MIN, INT_MAX = -(2**31), 2**31 - 1


class Solution:
    def reverse_string(self, x: int) -> int:
        # O(log n) time — convert to string, reverse, check overflow
        sign = -1 if x < 0 else 1
        rev = int(str(abs(x))[::-1]) * sign
        return rev if INT_MIN <= rev <= INT_MAX else 0

    def reverse(self, x: int) -> int:
        # Extract digits via mod 10, build reversed number; check 32-bit overflow
        # O(log n) time — extract digits with modulo, check overflow before each step
        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0
        while x:
            x, digit = divmod(x, 10)
            result = result * 10 + digit
        result *= sign
        return result if INT_MIN <= result <= INT_MAX else 0


if __name__ == '__main__':
    s = Solution()
    for method in (s.reverse_string, s.reverse):
        assert method(123) == 321
        assert method(-123) == -321
        assert method(120) == 21
        assert method(1534236469) == 0  # overflow
    print("All tests passed.")
