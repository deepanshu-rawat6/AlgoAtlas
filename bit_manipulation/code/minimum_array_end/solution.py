"""
# 3133. Minimum Array End

You are given two integers `n` and `x`. You have to construct an array of **positive** integers
`nums` of size `n` where for every `0 <= i < n - 1`, `nums[i + 1]` is greater than `nums[i]`,
and the result of the bitwise AND of all elements of `nums` is `x`.

Return the **minimum** possible value of `nums[n - 1]`.

## Examples

```text
Input: n = 3, x = 4
Output: 6
Explanation: nums = [4, 5, 6], AND = 4 & 5 & 6 = 4.

Input: n = 2, x = 7
Output: 15
Explanation: nums = [7, 15], AND = 7 & 15 = 7.
```

## Constraints
- 1 <= n, x <= 10^8
"""


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # Fill the 0-bits of x with bits of (n-1) in order
        # This gives the smallest number >= x that ANDs with x to give x
        # O(64) time — embed (n-1) into the zero-bits of x to get minimum last element
        result = x
        remaining = n - 1
        bit = 1
        while remaining:
            if not (result & bit):          # bit position is free (0 in x)
                if remaining & 1:
                    result |= bit
                remaining >>= 1
            bit <<= 1
        return result


if __name__ == '__main__':
    s = Solution()
    assert s.minEnd(3, 4) == 6
    assert s.minEnd(2, 7) == 15
    assert s.minEnd(1, 1) == 1
    print("All tests passed.")
