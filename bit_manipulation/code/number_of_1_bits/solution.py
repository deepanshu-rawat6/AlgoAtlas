"""
# 191. Number of 1 Bits

Given a positive integer `n`, write a function that returns the number of set bits
in its binary representation (also known as the **Hamming weight**).

## Examples

```text
Input: n = 11
Output: 3
Explanation: 11 in binary is 1011, which has 3 set bits.

Input: n = 128
Output: 1
Explanation: 128 in binary is 10000000, which has 1 set bit.

Input: n = 2147483645
Output: 30
```

## Constraints
- 1 <= n <= 2^31 - 1
"""


class Solution:
    def hammingWeight_each_bit(self, n: int) -> int:
        # O(32) time — check each of the 32 bits with a mask
        count = 0
        for _ in range(32):
            count += n & 1
            n >>= 1
        return count

    def hammingWeight(self, n: int) -> int:
        # n & (n-1) clears the lowest set bit; count how many times until n=0
        # O(k) time where k = number of set bits — n & (n-1) clears lowest set bit
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    for method in (s.hammingWeight_each_bit, s.hammingWeight):
        assert method(11) == 3
        assert method(128) == 1
        assert method(1) == 1
    print("All tests passed.")
