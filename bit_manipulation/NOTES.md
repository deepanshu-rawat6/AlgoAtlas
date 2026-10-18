# Bit Manipulation

## Core Intuition
Operate directly on binary representations. Key tricks:

- **XOR**: `a ^ a = 0`, `a ^ 0 = a`
  - Cancels duplicates: XOR all elements in a list where every value appears twice → single survivor remains
  - Find missing number: XOR indices 0..n with array values; missing number survives
  - Swap without temp: `a ^= b; b ^= a; a ^= b;` (fails when a and b are the same variable)
  - Compare bits: XOR of two numbers shows which bit positions differ

- **AND / OR masking**:
  - Isolate bit i: `(n >> i) & 1`
  - Set bit i: `n | (1 << i)`
  - Clear bit i: `n & ~(1 << i)`
  - Toggle bit i: `n ^ (1 << i)`
  - Isolate lowest set bit (LSB): `n & (-n)` or `n & ~(n - 1)`
  - Clear lowest set bit: `n & (n - 1)` — the Brian Kernighan trick

- **Shift operations**:
  - Left shift: `n << k` is multiply by 2^k (watch for overflow)
  - Right shift: signed `>>` fills with sign bit; unsigned `>>>` fills with 0
  - Always use `>>>` when treating an int as unsigned (e.g., Hamming weight, reverse bits)

- **Brian Kernighan trick**: `n &= n - 1` strips the lowest set bit each iteration.
  Counting set bits costs O(k) where k = number of set bits, not O(32).

- **When to use bit DP**: subsets of small n (n ≤ 20). Bitmask DP enumerates all 2^n subsets
  and is the standard approach for traveling-salesman variants and minimum-cost subset cover.

- **Complement / Two's complement**: `-n = ~n + 1`; `Integer.MIN_VALUE` is its own negation
  (negating overflows back to itself).

---

## Java Idioms

Java `int` is always 32-bit signed. There is no unsigned int — use `long` for 64-bit unsigned,
or use `>>>` carefully to avoid sign-extension.

### Standard library methods

```java
Integer.bitCount(n)              // count set bits (Hamming weight)
Integer.highestOneBit(n)         // value of the highest set bit (e.g. 8 for n=12)
Integer.lowestOneBit(n)          // value of the lowest set bit (same as n & -n)
Integer.numberOfLeadingZeros(n)  // leading zeros in 32-bit representation
Integer.numberOfTrailingZeros(n) // trailing zeros (position of LSB)
Integer.toBinaryString(n)        // unsigned binary string (no "0b" prefix)
Integer.reverse(n)               // reverse all 32 bits
Integer.reverseBytes(n)          // reverse the four bytes (byte-swap)
```

### Signed vs unsigned right shift — critical distinction

```java
int x = -1;           // all 32 bits set: 0xFFFFFFFF
x >> 1   == -1        // arithmetic shift: fills with sign bit (1)
x >>> 1  == Integer.MAX_VALUE  // logical shift: fills with 0
```

Use `>>>` whenever you treat the int as a raw bit pattern (reverse bits, Hamming weight on
negative inputs, etc.).

### Bit masking patterns

```java
// Set bit i:    n | (1 << i)
// Clear bit i:  n & ~(1 << i)
// Toggle bit i: n ^ (1 << i)
// Check bit i:  (n >> i) & 1
// Isolate LSB:  n & (-n)   or   n & ~(n - 1)
// Clear LSB:    n & (n - 1)
// Power of 2:   n > 0 && (n & (n - 1)) == 0
```

### XOR swap — and its failure case

```java
a ^= b;
b ^= a;
a ^= b;
// Works for distinct variables. Fails when a and b alias the same location:
// arr[i] ^= arr[i] → zeroes it out before the second step.
```

### Fast exponentiation via bits

```java
long result = 1, base = x;
while (exp > 0) {
    if ((exp & 1) != 0) result *= base;
    base *= base;
    exp >>>= 1;
}
```

### Gray code

```java
int gray = i ^ (i >> 1);  // converts index i to its Gray code
```

### Count set bits — Brian Kernighan

```java
int count = 0;
while (n != 0) { n &= n - 1; count++; }
return count;
```

### Parity (even/odd number of set bits)

```java
n ^= n >> 16;
n ^= n >> 8;
n ^= n >> 4;
n ^= n >> 2;
n ^= n >> 1;
return n & 1;  // 0 = even parity, 1 = odd parity
```

---

## Algorithm Skeletons

### Enumerate all subsets via bitmask (Python)

```python
n = len(arr)
for mask in range(1 << n):
    subset = [arr[i] for i in range(n) if (mask >> i) & 1]
    # process subset
```

### Count set bits — Brian Kernighan (Python)

```python
def count_bits(n: int) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
```

### XOR find single number (Python)

```python
def single_number(nums: list[int]) -> int:
    result = 0
    for x in nums:
        result ^= x
    return result  # all pairs cancel; unique element survives
```

---

## Decision Guide

```
Bit Manipulation Problem
|
+-- Find unique element?        → XOR all elements (duplicates cancel)
+-- Count set bits (one number)?→ Brian Kernighan: n &= n-1 loop
+-- Count set bits (0..n array)?→ DP: bits[i] = bits[i>>1] + (i & 1)
+-- Find missing number?        → XOR indices 0..n with array values
+-- Arithmetic without operators→ XOR for sum bits, AND+shift for carry
+-- Reverse bits?               → Extract LSB, shift into result, 32 iters; use >>>
+-- String binary addition?     → Simulate from right with carry
+-- Range AND?                  → Right-shift a and b until equal, shift back
+-- Construct minimum number?   → Spread bits of (n-1) into zero-positions of x
+-- Enumerate subsets?          → Bitmask 0..(1<<n)-1
```

---

## Per-Problem Reference

| Problem | Key Insight | Tricky Part | Common Mistakes | Time | Space |
|---|---|---|---|---|---|
| Single Number (LC 136) | XOR all; pairs cancel to 0 | None — straightforward | Using hash set (wastes O(n) space) | O(n) | O(1) |
| Number of 1 Bits (LC 191) | `n &= n-1` clears LSB; count until 0 | Java: use `>>>` not `>>` for sign safety | Signed shift extends sign bit on negative input | O(k) k=set bits | O(1) |
| Counting Bits (LC 338) | `dp[i] = dp[i >> 1] + (i & 1)` | dp[0]=0 base case required | Calling popcount per number: O(n log n) vs O(n) | O(n) | O(n) |
| Add Binary (LC 67) | Simulate right-to-left with carry | Carry past the longer string ("1"+"1"="10") | Converting to int — overflows on long strings | O(max(m,n)) | O(max(m,n)) |
| Reverse Bits (LC 190) | Extract LSB, shift into result from MSB | Must do exactly 32 iterations (leading zeros matter) | Using `>>` instead of `>>>` on negative n | O(1) | O(1) |
| Missing Number (LC 268) | XOR indices 0..n with array elements | Missing 0 or missing n are valid cases | Sorting: O(n log n) when O(n) suffices | O(n) | O(1) |
| Sum of Two Integers (LC 371) | `a^b` = sum bits; `(a&b)<<1` = carry | Python: mask with `0xFFFFFFFF` to prevent infinite loop | Forgetting sign extension in Python | O(1) max 32 iters | O(1) |
| Reverse Integer (LC 7) | Extract digits with `% 10`; rebuild with `* 10` | Check overflow BEFORE multiplying, not after | Reversing as string then converting — misses overflow | O(log n) | O(1) |
| Bitwise AND of Range (LC 201) | AND of range = common bit prefix of a and b | Right-shift until equal, then shift result back | Iterating all numbers in range — TLE | O(log n) | O(1) |
| Minimum Array End (LC 3133) | Spread bits of (n-1) into zero-bit positions of x | Bit-by-bit construction; n=1 edge case | Incrementing from x naively — too slow for large n | O(log n) | O(1) |

---

## General Edge Cases

1. **`n = 0` and power-of-two check**: `n & (n - 1)` gives 0 for n=0, incorrectly passing the
   test. Always guard with `n > 0 && (n & (n - 1)) == 0`.

2. **`Integer.MIN_VALUE` (0x80000000)**: negating overflows and gives itself back.
   `-Integer.MIN_VALUE == Integer.MIN_VALUE`. Do not assume `-n != n` for all ints.

3. **`>>` vs `>>>` for negatives**: `(-1) >> 1 == -1` (sign-extended), but
   `(-1) >>> 1 == Integer.MAX_VALUE` (zero-filled). Use `>>>` whenever treating int as unsigned.

4. **XOR swap with aliased variables**: `arr[i] ^= arr[i]` zeroes the element before the second
   step. Always check whether the two variables might reference the same memory location.

5. **Counting bits for n = 0**: must return 0. Both the `n &= n-1` loop and `Integer.bitCount`
   handle this correctly; naive string-conversion approaches may not.

6. **32-bit vs 64-bit overflow**: `1 << 31` overflows `int` (becomes `Integer.MIN_VALUE`).
   Use `1L << 31` when you need a long, or work entirely in `long` for 64-bit masks.

7. **Bit DP subset enumeration**: `1 << n` overflows `int` when n >= 32. Use `1L << n` or
   `BigInteger` for larger n. Bit DP is only practical for n ≤ ~20 anyway (memory: 2^20 entries).

8. **Python arbitrary-precision integers in signed arithmetic**: Python ints have no fixed width.
   For problems requiring 32-bit two's complement (e.g., Sum of Two Integers), mask with
   `& 0xFFFFFFFF` after each carry step to prevent infinite loops or wrong sign extension.

9. **Floating-point representation**: Do not apply integer bit tricks directly to `float` or
   `double`. Java's `Float.floatToIntBits` / `Double.doubleToLongBits` give access to the raw
   IEEE 754 bits safely; casting directly via `(int) someFloat` truncates, not reinterprets.

10. **All bits set (0xFFFFFFFF = -1 in Java)**: Bitwise AND of any number with -1 is that number.
    Bitwise AND of a range where a=0 is always 0. Watch for this in range AND problems.
