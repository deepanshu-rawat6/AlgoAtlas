# Bit Manipulation

```mermaid
mindmap
  root((Bit Manipulation))
    XOR Tricks
      Single Number LC136
      Missing Number LC268
      Sum of Two Integers LC371
    Bit Counting
      Number of 1 Bits LC191
      Counting Bits LC338
      Bitwise AND of Numbers Range LC201
    Bit Construction
      Reverse Bits LC190
      Minimum Array End LC3133
    Arithmetic
      Add Binary LC67
      Reverse Integer LC7
```

## Problem List

| # | Problem | LC # | Difficulty | Key Technique |
|---|---------|------|------------|---------------|
| 1 | Single Number | 136 | Easy | XOR all elements |
| 2 | Number of 1 Bits | 191 | Easy | Brian Kernighan's |
| 3 | Counting Bits | 338 | Easy | DP with bit shift |
| 4 | Add Binary | 67 | Easy | Bit-by-bit addition |
| 5 | Reverse Bits | 190 | Easy | Shift and OR |
| 6 | Missing Number | 268 | Easy | XOR or Gauss sum |
| 7 | Sum of Two Integers | 371 | Medium | XOR + AND carry |
| 8 | Reverse Integer | 7 | Medium | Mod + overflow check |
| 9 | Bitwise AND of Numbers Range | 201 | Medium | Common prefix |
| 10 | Minimum Array End | 3133 | Medium | Bit construction |

---

## Bit Manipulation Tricks Cheat Sheet

```mermaid
graph TD
    B[Bit Tricks] --> X[XOR]
    B --> A[AND]
    B --> S[Shifts]
    B --> O[OR]

    X --> X1["a XOR a = 0"]
    X --> X2["a XOR 0 = a"]
    X --> X3["XOR all → find unique"]

    A --> A1["n AND n-1 → clear lowest set bit"]
    A --> A2["n AND 1 → check odd/even"]
    A --> A3["range AND → common prefix"]

    S --> S1["n >> 1 → divide by 2"]
    S --> S2["n << 1 → multiply by 2"]
    S --> S3["dp[i] = dp[i>>1] + (i&1)"]

    O --> O1["a OR b → set bits from both"]
    O --> O2["used in bit-by-bit addition carry"]
```

---

## XOR Properties and Applications

```mermaid
flowchart TD
    A[XOR Properties] --> B["Identity: a XOR 0 = a"]
    A --> C["Self-inverse: a XOR a = 0"]
    A --> D["Commutative & Associative"]

    B --> E[Single Number #136]
    E --> F["XOR all nums → pairs cancel → unique remains"]

    C --> G[Missing Number #268]
    G --> H["XOR 0..n XOR all nums → missing remains"]

    D --> I[Sum of Two Integers #371]
    I --> J["sum = a XOR b, carry = a AND b shifted left, repeat"]

    style F fill:#2d6a4f,color:#fff
    style H fill:#2d6a4f,color:#fff
    style J fill:#2d6a4f,color:#fff
```

---

## Brian Kernighan's Algorithm Flow

```mermaid
flowchart TD
    A[count = 0, n = input] --> B{n != 0?}
    B -- No --> E[Return count]
    B -- Yes --> C["n = n AND n-1  ← clears lowest set bit"]
    C --> D[count += 1]
    D --> B

    style A fill:#2d6a4f,color:#fff
    style E fill:#1b4332,color:#fff
```

*Each iteration removes exactly one set bit → O(number of set bits)*

**Counting Bits (LC 338) DP shortcut:** `dp[i] = dp[i >> 1] + (i & 1)`

---

## Bit-by-Bit Addition Flow (No + Operator)

```mermaid
flowchart TD
    A["a = x, b = y"] --> B{b != 0?}
    B -- No --> F[Return a]
    B -- Yes --> C["sum_bits = a XOR b  ← add without carry"]
    C --> D["carry = a AND b shifted left 1  ← carry positions"]
    D --> E["a = sum_bits, b = carry"]
    E --> B

    style A fill:#2d6a4f,color:#fff
    style F fill:#1b4332,color:#fff
```

*Terminates when no carry remains. Used in: Sum of Two Integers #371*

---

## Common Prefix — Range AND Flow

```mermaid
flowchart TD
    A["left, right"] --> B{left != right?}
    B -- No --> E["Return left  ← common prefix"]
    B -- Yes --> C["left = left >> 1"]
    C --> D["right = right >> 1, shift_count++"]
    D --> B
    E --> F["Return left << shift_count"]

    style A fill:#2d6a4f,color:#fff
    style F fill:#1b4332,color:#fff
```

*All bits that differ between left and right become 0 in the AND of the range.*

---

## Complexity Summary

| Problem | Time | Space |
|---------|------|-------|
| Single Number | O(n) | O(1) |
| Number of 1 Bits | O(log n) | O(1) |
| Counting Bits | O(n) | O(n) |
| Add Binary | O(n) | O(n) |
| Reverse Bits | O(1) — 32 iters | O(1) |
| Missing Number | O(n) | O(1) |
| Sum of Two Integers | O(1) — 32 iters | O(1) |
| Reverse Integer | O(log n) | O(1) |
| Bitwise AND of Range | O(log n) | O(1) |
| Minimum Array End | O(log n) | O(1) |

---

## Study Order

1. **Single Number** — XOR identity
2. **Missing Number** — XOR or Gauss
3. **Number of 1 Bits** — Brian Kernighan's
4. **Counting Bits** — DP with right shift
5. **Reverse Bits** — shift and OR
6. **Add Binary** — string bit addition
7. **Sum of Two Integers** — XOR + carry loop
8. **Reverse Integer** — overflow handling
9. **Bitwise AND of Numbers Range** — common prefix
10. **Minimum Array End** — bit construction
