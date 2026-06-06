# Valid Parentheses (LC 20)

Given a string of `()[]{}` characters, determine if it is valid — every opening bracket is closed by the same type in the correct order.

## Approaches

### 1. Stack with Mapping
- **Time:** O(n) | **Space:** O(n)
- Use a dict mapping each closing bracket to its expected opening bracket.
- Push opening brackets onto the stack. On a closing bracket, check if the stack top matches; if not (or stack is empty), return False.
- Return `True` only if the stack is empty at the end (all brackets matched).

## Key Insight

A stack naturally models nesting: the most recently opened bracket must be closed first (LIFO). The closing bracket map lets us check the match in O(1) without a chain of if-else conditions. An empty stack at the end guarantees every opener was paired.

## Edge Cases

- Empty string → valid (vacuously true).
- Only opening brackets (e.g., `"((("`) → stack non-empty at end → False.
- Only closing brackets (e.g., `")))"`) → stack empty on first check → False.
- Interleaved mismatches like `"([)]"` → stack top mismatch → False.
- Single character → always False (can't be a matched pair).
