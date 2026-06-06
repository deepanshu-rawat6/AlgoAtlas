"""
# 50. Pow(x, n)

Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., x^n).

## Examples

```text
Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/4 = 0.25
```

## Constraints
- -100.0 < x < 100.0
- -2^31 <= n <= 2^31 - 1
- n is an integer.
- Either x is not zero or n > 0.
- -10^4 <= x^n <= 10^4
"""


class Solution:
    def myPow_brute(self, x: float, n: int) -> float:
        # O(n) time — multiply x by itself n times (TLE for large n)
        if n < 0:
            x, n = 1 / x, -n
        result = 1.0
        for _ in range(n):
            result *= x
        return result

    def myPow(self, x: float, n: int) -> float:
        # Fast exponentiation: x^n = (x^(n//2))^2; halve n each step — O(log n)
        # Handle negative n by inverting x and using abs(n)
        # O(log n) time — fast exponentiation by squaring
        if n < 0:
            x, n = 1 / x, -n
        result = 1.0
        while n:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result


if __name__ == '__main__':
    s = Solution()
    for method in (s.myPow_brute, s.myPow):
        assert abs(method(2.0, 10) - 1024.0) < 1e-5
        assert abs(method(2.0, -2) - 0.25) < 1e-5
        assert abs(method(2.0, 0) - 1.0) < 1e-5
    print("All tests passed.")
