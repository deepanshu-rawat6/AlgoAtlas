"""
LC 69 - Sqrt(x)
================

Given a non-negative integer `x`, return the square root of `x` rounded down
to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator (e.g., pow(x, 0.5)
or x ** 0.5).

Examples
--------
```text
Input:  x = 4
Output: 2

Input:  x = 8
Output: 2
Explanation: The square root of 8 is 2.828..., rounded down to 2.
```

Constraints
-----------
- 0 <= x <= 2^31 - 1
"""


class Solution:
    def method_linear(self, x: int) -> int:
        # O(sqrt(x)) time | O(1) space
        i = 0
        while (i + 1) * (i + 1) <= x:
            i += 1
        return i

    def mySqrt(self, x: int) -> int:
        # Binary search: find largest integer whose square <= x
        # When mid*mid <= x, record mid as candidate and search right for larger
        # O(log x) time | O(1) space
        if x < 2:
            return x
        lo, hi = 1, x // 2
        while lo <= hi:
            mid = (lo + hi) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi


if __name__ == "__main__":
    s = Solution()
    for x, expected in [(0, 0), (1, 1), (4, 2), (8, 2), (9, 3), (2147395600, 46340)]:
        assert s.mySqrt(x) == expected, f"mySqrt({x}) = {s.mySqrt(x)}, expected {expected}"
        assert s.method_linear(x) == expected, f"method_linear({x}) failed"
    print("All tests passed.")
