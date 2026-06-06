# Evaluate Reverse Polish Notation (LC 150)

Evaluate an arithmetic expression in Reverse Polish Notation (postfix). Operators are `+`, `-`, `*`, `/`; division truncates toward zero.

## Approaches

### 1. Stack Evaluation
- **Time:** O(n) | **Space:** O(n)
- Push numbers onto the stack. When an operator is encountered, pop two operands, apply the operator, and push the result.
- Use `int(a / b)` (not `a // b`) for division to truncate toward zero rather than floor.
- The final answer is the single remaining element on the stack.

## Key Insight

RPN eliminates the need for parentheses and operator precedence rules — operands always appear before their operator. A stack is the natural fit: operands accumulate until an operator "consumes" the top two. The expression is guaranteed valid, so the stack always has ≥ 2 elements when an operator appears.

The division subtlety: Python's `//` floors toward negative infinity (`-7 // 2 = -4`), but the problem requires truncation toward zero (`-7 / 2 = -3`). Using `int(a / b)` handles this correctly.

## Edge Cases

- Single number token → return it directly (stack has one element).
- Negative numbers in tokens (e.g., `"-11"`) → parsed correctly by `int()`.
- Division truncation: `3 / -4 = 0` (not -1), `-3 / 4 = 0` (not -1).
- The input is always a valid RPN expression — no need to handle malformed input.
