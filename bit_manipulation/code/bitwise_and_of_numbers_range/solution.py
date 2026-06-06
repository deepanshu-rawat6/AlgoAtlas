"""
# 201. Bitwise AND of Numbers Range

Given two integers `left` and `right` that represent the range `[left, right]`,
return the bitwise AND of all numbers in this range, inclusive.

## Examples

```text
Input: left = 5, right = 7
Output: 4

Input: left = 0, right = 0
Output: 0

Input: left = 1, right = 2147483647
Output: 0
```

## Constraints
- 0 <= left <= right <= 2^31 - 1
"""


class Solution:
    def rangeBitwiseAnd_shift(self, left: int, right: int) -> int:
        # O(32) time — right-shift both until equal to find common prefix
        shift = 0
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Right-shift both until equal: common prefix of all numbers in range
        # Bits that differ across the range will be 0 in the AND result
        # O(32) time — Brian Kernighan: strip lowest set bit of right until right <= left
        while right > left:
            right &= right - 1
        return right


if __name__ == '__main__':
    s = Solution()
    for method in (s.rangeBitwiseAnd_shift, s.rangeBitwiseAnd):
        assert method(5, 7) == 4
        assert method(0, 0) == 0
        assert method(1, 2147483647) == 0
    print("All tests passed.")
