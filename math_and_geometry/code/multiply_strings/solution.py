"""
# 43. Multiply Strings

Given two non-negative integers `num1` and `num2` represented as strings, return the product
of `num1` and `num2`, also represented as a string.

**Note:** You must not use any built-in BigInteger library or convert the inputs to integer directly.

## Examples

```text
Input: num1 = "2", num2 = "3"
Output: "6"

Input: num1 = "123", num2 = "456"
Output: "56088"
```

## Constraints
- 1 <= num1.length, num2.length <= 200
- num1 and num2 consist of digits only.
- Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Simulate grade-school multiplication digit by digit
        # Result digit at position i+j comes from nums1[i] * nums2[j]
        # Propagate carries after all multiplications
        # O(m*n) time — grade-school digit-by-digit multiplication with position tracking
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        pos = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                p1, p2 = i + j, i + j + 1
                total = mul + pos[p2]
                pos[p2] = total % 10
                pos[p1] += total // 10
        result = ''.join(str(d) for d in pos).lstrip('0')
        return result or "0"


if __name__ == '__main__':
    s = Solution()
    assert s.multiply("2", "3") == "6"
    assert s.multiply("123", "456") == "56088"
    assert s.multiply("0", "456") == "0"
    assert s.multiply("99", "99") == "9801"
    print("All tests passed.")
