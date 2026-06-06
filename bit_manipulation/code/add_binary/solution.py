"""
# 67. Add Binary

Given two binary strings `a` and `b`, return their sum as a binary string.

## Examples

```text
Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"
```

## Constraints
- 1 <= a.length, b.length <= 10^4
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Simulate binary addition from right to left with carry
        # O(max(m,n)) time — iterate from end with carry, build result in reverse
        i, j, carry = len(a) - 1, len(b) - 1, 0
        result = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += ord(a[i]) - 48
                i -= 1
            if j >= 0:
                total += ord(b[j]) - 48
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return ''.join(reversed(result))


if __name__ == '__main__':
    s = Solution()
    assert s.addBinary("11", "1") == "100"
    assert s.addBinary("1010", "1011") == "10101"
    assert s.addBinary("0", "0") == "0"
    print("All tests passed.")
