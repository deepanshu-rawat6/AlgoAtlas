"""
# 13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

```text
Symbol  Value
I       1
V       5
X       10
L       50
C       100
D       500
M       1000
```

Roman numerals are usually written largest to smallest from left to right. However, when a smaller
value precedes a larger value, it is subtracted (e.g., IV = 4, IX = 9).

Given a roman numeral, convert it to an integer.

## Examples

```text
Input: s = "III"
Output: 3

Input: s = "LVIII"
Output: 58

Input: s = "MCMXCIV"
Output: 1994
```

## Constraints
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        # If current symbol < next symbol, subtract it (e.g. IV = 5-1)
        # Otherwise add it; process left to right
        # O(n) time — left-to-right scan, subtract when smaller value precedes larger
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and val[s[i]] < val[s[i+1]]:
                result -= val[s[i]]
            else:
                result += val[s[i]]
        return result


if __name__ == '__main__':
    s = Solution()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
    assert s.romanToInt("IV") == 4
    print("All tests passed.")
