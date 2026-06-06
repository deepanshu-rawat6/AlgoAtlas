# String to Integer (Recursive)

## Problem Statement
Convert a string of digit characters to its integer value without using
`int()`, `atoi`, or any built-in conversion. Use pure recursion.

**Example:** "1234" → 1234

---

## Approach: Left-to-Right Digit Accumulation — O(n) time, O(n) stack space

Recurrence:
```
strToInt("") = 0
strToInt(s) = strToInt(s[:-1]) * 10 + digit_value(s[-1])
```

Process all but the last character first (recursive call), then append the
last digit by multiplying the accumulated result by 10 and adding the new digit.

`digit_value(c) = ord(c) - ord('0')` converts a char to its numeric value
without calling `int()`.

**Why this works:** Each recursive call handles a shorter prefix. When we
return, we "shift" the accumulated value left by one decimal place (×10) and
add the next digit — exactly how positional notation works.

---

## Key Insight
`strToInt(s[0:n]) = strToInt(s[0:n-1]) * 10 + digit_value(s[n-1])`

This mirrors how we read numbers: left digits are more significant, so each
new digit from the right extends the number by one decimal place.

---

## Edge Cases
- Single digit `"0"` → 0.
- Leading zeros `"007"` → 7 (naturally handled).
- Empty string `""` → 0 (base case).
- Does not handle negative numbers or non-digit characters.

---

## Complexity Summary
| Metric | Value  |
|--------|--------|
| Time   | O(n)   |
| Space  | O(n) stack |
