"""
# 190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

## Examples

```text
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)

Input: n = 11111111111111111111111111111101
Output:    3221225471 (10111111111111111111111111111111)
```

## Constraints
- The input must be a binary string of length 32.
"""


class Solution:
    def reverseBits_bitbybit(self, n: int) -> int:
        # O(32) time — shift bits one at a time into result
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

    def reverseBits(self, n: int) -> int:
        # For each of 32 bits: shift result left, OR in the lowest bit of n, shift n right
        # O(1) time — divide and conquer: swap 16, 8, 4, 2, 1-bit groups
        n = (n >> 16) | (n << 16)
        n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
        n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
        n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
        return n & 0xFFFFFFFF


if __name__ == '__main__':
    s = Solution()
    for method in (s.reverseBits_bitbybit, s.reverseBits):
        assert method(43261596) == 964176192
        assert method(0) == 0
        assert method(0xFFFFFFFF) == 0xFFFFFFFF
    print("All tests passed.")
