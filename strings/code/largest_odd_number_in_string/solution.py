"""
# LC 1903: Largest Odd Number in String

Given a string `num` representing a large integer, return the largest-valued odd
integer (as a string) that is a non-empty substring of `num`, or `""` if no odd
integer exists. A substring is a contiguous sequence of characters.

## Examples

```text
Input:  num = "52"
Output: "5"

Input:  num = "4206"
Output: ""

Input:  num = "35427"
Output: "35427"
```

## Constraints
- 1 <= num.length <= 10^5
- num only consists of digits and does not contain any leading zeros
"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Scan from right; first odd digit found → return prefix up to that index
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""


# Tests
if __name__ == '__main__':
    sol = Solution()
    assert sol.largestOddNumber("52") == "5"
    assert sol.largestOddNumber("4206") == ""
    assert sol.largestOddNumber("35427") == "35427"
    assert sol.largestOddNumber("2") == ""
    assert sol.largestOddNumber("1") == "1"
    print("All tests passed.")
