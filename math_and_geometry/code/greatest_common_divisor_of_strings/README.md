# LC 1071 — Greatest Common Divisor of Strings

For two strings, "t divides s" means `s = t + t + ... + t`. Return the largest string `x` that divides both `str1` and `str2`.

## Approaches

### 1. Brute Force
- **Time:** O(n²) | **Space:** O(n)
- Try every prefix of the shorter string as a candidate divisor. Check if it divides both strings by verifying repetition.

### 2. GCD of Lengths
- **Time:** O(n) | **Space:** O(1)
- If `str1 + str2 == str2 + str1`, a common divisor exists. Its length is `gcd(len(str1), len(str2))`. Return `str1[:gcd_length]`.

## Key Insight

If a string `t` divides both `str1` and `str2`, then `str1 + str2 == str2 + str1` (both equal `t` repeated `(m+n)/len(t)` times). The concatenation check is a necessary and sufficient condition. The GCD of lengths gives the longest possible divisor length because any common divisor's length must divide both string lengths.

## Edge Cases

- `str1 + str2 != str2 + str1`: No common divisor, return `""`.
- One string is a multiple of the other: The shorter string (or its prefix) is the GCD.
- `str1 == str2`: Return `str1` (the whole string divides itself).
- `str1 = "LEET", str2 = "CODE"`: No common structure, return `""`.
