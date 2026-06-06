"""
# 1071. Greatest Common Divisor of Strings

For two strings `s` and `t`, we say "t divides s" if and only if `s = t + t + ... + t`
(i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.

## Examples

```text
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Input: str1 = "LEET", str2 = "CODE"
Output: ""
```

## Constraints
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of English uppercase letters.
"""

from math import gcd


class Solution:
    def gcdOfStrings_brute(self, str1: str, str2: str) -> str:
        # O(n^2) time — check every prefix of the shorter string
        shorter, longer = (str1, str2) if len(str1) <= len(str2) else (str2, str1)
        for length in range(len(shorter), 0, -1):
            t = shorter[:length]
            if len(str1) % length == 0 and len(str2) % length == 0:
                if t * (len(str1) // length) == str1 and t * (len(str2) // length) == str2:
                    return t
        return ""

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If str1+str2 == str2+str1, a GCD string exists
        # Its length is gcd(len(str1), len(str2))
        # O(n) time — GCD of lengths gives candidate; verify with concatenation check
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]


if __name__ == '__main__':
    s = Solution()
    for method in (s.gcdOfStrings_brute, s.gcdOfStrings):
        assert method("ABCABC", "ABC") == "ABC"
        assert method("ABABAB", "ABAB") == "AB"
        assert method("LEET", "CODE") == ""
    print("All tests passed.")
