"""
# 22: Generate All Balanced Parentheses

Given `n` pairs of parentheses, generate all combinations of well-formed
(balanced) parentheses strings.

## Examples
```text
Input:  n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input:  n = 1
Output: ["()"]
```

## Constraints
- 1 <= n <= 8 (typical).
- The number of valid combinations equals the nth Catalan number.
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Recursion with open/close count tracking.
        # Place '(' if open < n (still have opening brackets to use).
        # Place ')' if close < open (can only close what's been opened).
        result = []

        def recurse(current, open_count, close_count):
            if len(current) == 2 * n:  # base case: used all n pairs
                result.append(current)
                return
            if open_count < n:
                recurse(current + "(", open_count + 1, close_count)
            if close_count < open_count:
                recurse(current + ")", open_count, close_count + 1)

        recurse("", 0, 0)
        return result


if __name__ == "__main__":
    sol = Solution()
    r = sol.generateParenthesis(3)
    assert len(r) == 5
    assert "(((())))" not in r  # invalid
    assert "((()))" in r
    assert "(()())" in r
    assert len(sol.generateParenthesis(1)) == 1
    assert sol.generateParenthesis(1) == ["()"]
    print("All tests passed.")
