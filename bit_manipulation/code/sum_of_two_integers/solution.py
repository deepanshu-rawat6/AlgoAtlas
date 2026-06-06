"""
# 371. Sum of Two Integers

Given two integers `a` and `b`, return the sum of the two integers without using
the operators `+` and `-`.

## Examples

```text
Input: a = 1, b = 2
Output: 3

Input: a = 2, b = 3
Output: 5
```

## Constraints
- -1000 <= a, b <= 1000
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # XOR gives sum without carry; AND<<1 gives the carry
        # Repeat until no carry remains; mask to 32 bits to handle negatives
        # O(32) time — XOR gives sum without carry; AND<<1 gives carry; repeat until no carry
        mask = 0xFFFFFFFF
        while b & mask:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        # handle negative numbers in Python's arbitrary precision integers
        return a if b == 0 else a & mask if (a & (mask + 1)) else a


if __name__ == '__main__':
    s = Solution()
    assert s.getSum(1, 2) == 3
    assert s.getSum(2, 3) == 5
    assert s.getSum(-1, 1) == 0
    assert s.getSum(-5, 3) == -2
    print("All tests passed.")
