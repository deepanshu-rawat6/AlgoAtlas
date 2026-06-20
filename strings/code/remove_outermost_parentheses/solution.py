"""
# LC 1021: Remove Outermost Parentheses

A valid parentheses string (VPS) can be decomposed into primitive parts — VPS
substrings that cannot be split further. Remove the outermost parentheses of every
primitive string in the primitive decomposition of `s`.

## Examples

```text
Input:  s = "(()())(())"
Output: "()()()"

Input:  s = "(()())(())(()(()))"
Output: "()()()()(())"

Input:  s = "()()"
Output: ""
```

## Constraints
- 1 <= s.length <= 10^5
- s is a valid parentheses string
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # Track depth; skip char when transitioning 0->1 (open) or 1->0 (close)
        result = []
        depth = 0
        for ch in s:
            if ch == '(':
                if depth > 0:          # not the outermost open
                    result.append(ch)
                depth += 1
            else:
                depth -= 1
                if depth > 0:          # not the outermost close
                    result.append(ch)
        return ''.join(result)


# Tests
if __name__ == '__main__':
    sol = Solution()
    assert sol.removeOuterParentheses("(()())(())") == "()()()"
    assert sol.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"
    assert sol.removeOuterParentheses("()()") == ""
    assert sol.removeOuterParentheses("((()))") == "(())"
    print("All tests passed.")
