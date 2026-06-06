"""
# 20. Valid Parentheses

## Problem
Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`,
`'['`, and `']'`, determine if the input string is valid.

A string is valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples
```text
Input:  s = "()"
Output: true

Input:  s = "()[]{}"
Output: true

Input:  s = "(]"
Output: false

Input:  s = "([)]"
Output: false

Input:  s = "{[]}"
Output: true
```

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only: `'()[]{}'`
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # Push opening brackets; on closing bracket, check top matches
        # Stack empty at end means all brackets were properly closed
        # O(n) time, O(n) space — stack-based bracket matching
        stack = []
        match = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch in match:
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack


if __name__ == "__main__":
    s = Solution()
    assert s.isValid("()") is True
    assert s.isValid("()[]{}") is True
    assert s.isValid("(]") is False
    assert s.isValid("([)]") is False
    assert s.isValid("{[]}") is True
    assert s.isValid("") is True
    print("All tests passed.")
