"""
# 150. Evaluate Reverse Polish Notation

## Problem
Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN).

Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or
another expression. Division truncates toward zero.

## Examples
```text
Input:  tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Input:  tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Input:  tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
```

## Constraints
- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator `+`, `-`, `*`, `/`, or an integer in the
  range `[-200, 200]`
- The given RPN expression is always valid
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Push numbers; on operator, pop two operands and push result
        # Use int(a/b) instead of a//b to truncate toward zero (not floor)
        # O(n) time, O(n) space — single stack evaluation
        stack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),  # truncate toward zero
        }
        for t in tokens:
            if t in ops:
                b, a = stack.pop(), stack.pop()
                stack.append(ops[t](a, b))
            else:
                stack.append(int(t))
        return stack[0]


if __name__ == "__main__":
    s = Solution()
    assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    assert s.evalRPN(["3", "-4", "/"]) == 0  # truncate toward zero: -0.75 -> 0
    print("All tests passed.")
