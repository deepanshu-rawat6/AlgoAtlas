# LC 7 — Reverse Integer

Given a signed 32-bit integer `x`, return `x` with its digits reversed. Return 0 if the reversed value overflows the 32-bit signed integer range.

## Approaches

### 1. String Reversal
- **Time:** O(log n) | **Space:** O(log n)
- Convert to string, reverse, convert back. Handle sign separately. Check overflow.

### 2. Digit Extraction with Modulo
- **Time:** O(log n) | **Space:** O(1)
- Extract digits one by one using `divmod(x, 10)`. Build the reversed number by `result = result * 10 + digit`. Check overflow at the end.

## Key Insight

The modulo approach avoids string conversion and works digit by digit. The overflow check is applied after building the full reversed number. In Python, integers have arbitrary precision so overflow doesn't happen during computation — we just check the final result against `[-2³¹, 2³¹ - 1]`. In other languages, overflow must be checked before each multiplication.

## Edge Cases

- Negative numbers: Handle sign separately, reverse the absolute value.
- Trailing zeros become leading zeros after reversal (e.g., `120` → `21`).
- Overflow: `1534236469` reversed is `9646324351` which exceeds INT_MAX, return 0.
- `x = 0`: Return 0.
