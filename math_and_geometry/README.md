# Math & Geometry

```mermaid
mindmap
  root((Math & Geometry))
    Matrix Operations
      Transpose Matrix LC867
      Rotate Image LC48
      Spiral Matrix LC54
      Set Matrix Zeroes LC73
    Number Theory
      GCD of Strings LC1071
      Insert GCD in Linked List LC2807
      Happy Number LC202
      Pow x n LC50
      Detect Squares LC2013
    Simulation
      Plus One LC66
      Roman to Integer LC13
      Excel Sheet Column Title LC168
    String Math
      Multiply Strings LC43
      Add Binary LC67
```

## Problem List

| # | Problem | LC # | Difficulty | Key Technique |
|---|---------|------|------------|---------------|
| 1 | Excel Sheet Column Title | 168 | Easy | Base-26 encoding |
| 2 | GCD of Strings | 1071 | Easy | GCD + string divisibility |
| 3 | Insert GCD in Linked List | 2807 | Medium | GCD + list manipulation |
| 4 | Transpose Matrix | 867 | Easy | Index swap |
| 5 | Rotate Image | 48 | Medium | Transpose + reverse |
| 6 | Spiral Matrix | 54 | Medium | Boundary simulation |
| 7 | Set Matrix Zeroes | 73 | Medium | In-place marking |
| 8 | Happy Number | 202 | Easy | Cycle detection (Floyd's) |
| 9 | Plus One | 66 | Easy | Carry propagation |
| 10 | Roman to Integer | 13 | Easy | Symbol map + lookahead |
| 11 | Pow(x, n) | 50 | Medium | Fast exponentiation |
| 12 | Multiply Strings | 43 | Medium | Grade-school multiplication |
| 13 | Detect Squares | 2013 | Medium | Point counting + geometry |

---

## Matrix Operation Patterns

```mermaid
graph TD
    M[Matrix Operations] --> T[Transpose]
    M --> R[Rotate]
    M --> S[Spiral]
    M --> Z[Zero-marking]

    T --> T1["swap matrix[i][j] and matrix[j][i]"]
    T1 --> T2[Transpose Matrix #867]

    R --> R1[Transpose then reverse each row]
    R1 --> R2[Rotate Image #48 — 90° clockwise]

    S --> S1[Shrink boundaries: top, bottom, left, right]
    S1 --> S2[Spiral Matrix #54]

    Z --> Z1[Use first row/col as markers]
    Z1 --> Z2[Set Matrix Zeroes #73]
```

---

## Spiral Matrix Traversal Flow

```mermaid
flowchart TD
    A[top=0, bottom=n-1, left=0, right=m-1] --> B{top <= bottom AND left <= right?}
    B -- No --> Z[Return result]
    B -- Yes --> C[Traverse top row left to right, top++]
    C --> D[Traverse right col top to bottom, right--]
    D --> E{top <= bottom?}
    E -- Yes --> F[Traverse bottom row right to left, bottom--]
    E -- No --> B
    F --> G{left <= right?}
    G -- Yes --> H[Traverse left col bottom to top, left++]
    G -- No --> B
    H --> B

    style A fill:#2d6a4f,color:#fff
    style Z fill:#1b4332,color:#fff
```

---

## Fast Exponentiation Flow

```mermaid
flowchart TD
    A[pow x, n] --> B{n < 0?}
    B -- Yes --> C[x = 1/x, n = -n]
    B -- No --> D[result = 1]
    C --> D
    D --> E{n > 0?}
    E -- No --> K[Return result]
    E -- Yes --> F{n is odd?}
    F -- Yes --> G[result *= x]
    F -- No --> H[skip]
    G --> I[x = x * x, n = n // 2]
    H --> I
    I --> E

    style A fill:#2d6a4f,color:#fff
    style K fill:#1b4332,color:#fff
```

*Time: O(log n) — halve the exponent each iteration*

---

## Cycle Detection — Happy Number Flow

```mermaid
flowchart TD
    A[slow = n, fast = n] --> B[Compute next: sum of squares of digits]
    B --> C[slow = next of slow]
    C --> D[fast = next of next of fast]
    D --> E{slow == fast?}
    E -- No --> C
    E -- Yes --> F{slow == 1?}
    F -- Yes --> G[Return True — Happy Number]
    F -- No --> H[Return False — cycle, not happy]

    style G fill:#2d6a4f,color:#fff
    style H fill:#9b2226,color:#fff
```

*Alternative: use a seen set; stop when 1 or repeated*

---

## GCD / Number Theory Decision Tree

```mermaid
flowchart TD
    A[Number Theory Problem] --> B{Involves strings?}
    B -- Yes --> C[GCD of Strings #1071]
    C --> D["Check s+t == t+s, then return s[:gcd(len s, len t)]"]

    B -- No --> E{Involves linked list?}
    E -- Yes --> F[Insert GCD in Linked List #2807]
    F --> G[Between each pair, insert node with gcd of values]

    E -- No --> H{Involves exponentiation?}
    H -- Yes --> I[Pow x,n #50 — fast exponentiation]

    H -- No --> J{Involves digit sum cycle?}
    J -- Yes --> K[Happy Number #202 — Floyd's cycle detection]

    J -- No --> L[Excel Column #168 — base-26 with offset]
```

---

## Complexity Summary

| Problem | Time | Space |
|---------|------|-------|
| Excel Sheet Column Title | O(log n) | O(log n) |
| GCD of Strings | O(n + m) | O(n + m) |
| Insert GCD in Linked List | O(n log v) | O(1) |
| Transpose Matrix | O(n²) | O(1) |
| Rotate Image | O(n²) | O(1) |
| Spiral Matrix | O(n·m) | O(1) |
| Set Matrix Zeroes | O(n·m) | O(1) |
| Happy Number | O(log n) | O(1) |
| Plus One | O(n) | O(1) |
| Roman to Integer | O(n) | O(1) |
| Pow(x, n) | O(log n) | O(1) |
| Multiply Strings | O(n·m) | O(n+m) |
| Detect Squares | O(n) per query | O(n) |

---

## Study Order

1. **Plus One** — carry propagation warm-up
2. **Roman to Integer** — symbol map
3. **Excel Sheet Column Title** — base conversion
4. **Happy Number** — cycle detection
5. **GCD of Strings** — number theory + strings
6. **Transpose Matrix** — matrix basics
7. **Rotate Image** — transpose + reverse
8. **Spiral Matrix** — boundary simulation
9. **Set Matrix Zeroes** — in-place marking
10. **Pow(x, n)** — fast exponentiation
11. **Multiply Strings** — grade-school algorithm
12. **Insert GCD in Linked List** — GCD + list
13. **Detect Squares** — geometry + counting
