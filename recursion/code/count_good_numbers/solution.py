"""
LC 1922 - Count Good Numbers

Problem: A digit string is "good" if:
    - Even indices (0,2,4,...) contain even digits: {0,2,4,6,8} -> 5 choices
    - Odd  indices (1,3,5,...) contain prime digits: {2,3,5,7}  -> 4 choices
Count good strings of length n, return result mod 10^9+7.

Examples:
    n = 1  -> 5
    n = 4  -> 400
    n = 50 -> 564908303

Constraints:
    1 <= n <= 10^15
    Return answer mod 10^9 + 7
"""

import math

MOD = 10**9 + 7


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # even_count = ceil(n/2) positions with 5 choices each
        # odd_count  = floor(n/2) positions with 4 choices each
        # Use fast modular exponentiation (pow built-in) for O(log n)
        even_count = math.ceil(n / 2)
        odd_count = n // 2
        return (pow(5, even_count, MOD) * pow(4, odd_count, MOD)) % MOD


if __name__ == '__main__':
    sol = Solution()
    assert sol.countGoodNumbers(1) == 5
    assert sol.countGoodNumbers(4) == 400
    assert sol.countGoodNumbers(50) == 564908303
    print("All tests passed.")
