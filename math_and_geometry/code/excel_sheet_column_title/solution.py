"""
# 168. Excel Sheet Column Title

Given an integer `columnNumber`, return its corresponding column title as it appears in an Excel sheet.

```text
A -> 1
B -> 2
...
Z -> 26
AA -> 27
AB -> 28
...
```

## Examples

```text
Input: columnNumber = 1
Output: "A"

Input: columnNumber = 28
Output: "AB"

Input: columnNumber = 701
Output: "ZY"
```

## Constraints
- 1 <= columnNumber <= 2^31 - 1
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Base-26 conversion but 1-indexed (A=1, Z=26, AA=27)
        # Subtract 1 before modulo to handle the 1-indexed offset
        # O(log n) time, O(log n) space for result string
        result = []
        while columnNumber:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(reversed(result))


if __name__ == '__main__':
    s = Solution()
    assert s.convertToTitle(1) == "A"
    assert s.convertToTitle(26) == "Z"
    assert s.convertToTitle(28) == "AB"
    assert s.convertToTitle(701) == "ZY"
    print("All tests passed.")
