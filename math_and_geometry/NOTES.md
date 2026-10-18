# Math & Geometry

## Core Intuition

These problems rely on mathematical properties or careful simulation. Key skills: modular arithmetic, GCD/LCM, number base conversion, matrix traversal patterns, and detecting cycles.

- **Number theory**: GCD/LCM via Euclidean algorithm; prime factorization; modular arithmetic for remainders that must stay non-negative
  - GCD is the foundation: LCM, GCD strings, linked-list insertions all reduce here
  - Modular arithmetic: `((n % m) + m) % m` for true non-negative result in Java
- **Geometry**: Direction arrays replace if-else chains for grid traversal; cross product detects collinearity; coordinate encoding packs 2D into a single int for hash lookups
- **Simulation**: Follow the spec exactly — spiral matrix, robot movement, game rules. Use direction arrays (`dr`, `dc`) and rotate direction with `d = (d + 1) % 4` to avoid branching
- **Math shortcuts**: Closed-form sum `n*(n+1)/2`, parity via `(n & 1) == 0`, base-k encoding via repeated division/modulo
- **Matrix ops**: In-place rotation uses transpose + reverse; spiral uses boundary shrink; set-zeroes uses first row/col as flags
- **When to use `long`**: Any multiplication of two `int` values where either could exceed ~46,340 (sqrt of `Integer.MAX_VALUE`). Cast one operand before the multiply: `(long)a * b`.

## Java Idioms

### Math class (no import needed)

```java
Math.abs(n)          // absolute value
Math.max(a, b)       // larger of two
Math.min(a, b)       // smaller of two
Math.sqrt(n)         // returns double — use (int)Math.sqrt(n) carefully (see edge cases)
Math.pow(base, exp)  // returns double — cast to int only when sure result fits
Math.floor(d)        // round down (returns double)
Math.ceil(d)         // round up (returns double)
Math.PI              // 3.141592653589793
Math.E               // 2.718281828459045
```

### GCD and LCM — no stdlib, implement manually

```java
// Euclid's algorithm — O(log(min(a,b)))
int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

// Divide BEFORE multiply to avoid overflow
long lcm(long a, long b) {
    return a / gcd((int)a, (int)b) * b;
}
```

Java's standard library has no `Math.gcd()`. The `BigInteger.gcd()` exists but costs an object allocation per call — use the one-liner above instead.

### Modulo that stays non-negative

```java
// Java % is remainder, not modulo: -7 % 3 == -1, not 2
int mod(int n, int m) {
    return ((n % m) + m) % m;
}
```

### Overflow-safe multiplication

```java
// WRONG: (long)(a * b)  — overflow already happened inside the cast
// RIGHT: cast one operand first
long product = (long) a * b;
```

### Prime check

```java
boolean isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; (long) i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}
```

Note `(long) i * i` — when `n` is near `Integer.MAX_VALUE`, `i * i` overflows without the cast.

### Sieve of Eratosthenes

```java
boolean[] sieve(int n) {
    boolean[] isPrime = new boolean[n + 1];
    Arrays.fill(isPrime, true);
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; (long) i * i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    return isPrime;
}
```

### Direction arrays for grid traversal

```java
int[] dr = {0, 1, 0, -1};   // right, down, left, up
int[] dc = {1, 0, -1,  0};

// move in direction d
int nr = r + dr[d], nc = c + dc[d];

// rotate clockwise
d = (d + 1) % 4;
```

### Coordinate encoding (2D → 1D key)

```java
// For small grids where r < rows and c < cols
int key = r * cols + c;

// For large grids (r or c up to 10^5+)
long key = (long) r * cols + c;
```

### Math.sqrt floating-point trap

`(int) Math.sqrt(n)` may return `k-1` for a perfect square `k²` due to floating-point rounding. Safe check:

```java
int s = (int) Math.sqrt(n);
while ((long)(s+1)*(s+1) <= n) s++;  // nudge up if needed
// or just use: for (int i = 1; (long)i*i <= n; i++)
```

## Decision Flowchart

```
Math/Geometry Problem
├── Matrix traversal?
│   ├── Layer-by-layer rotation   → Rotate Image (transpose + reverse rows)
│   ├── Boundary-shrink traversal → Spiral Matrix (four pointers / direction array)
│   ├── Row/col zeroing           → Set Matrix Zeroes (flag first row/col)
│   └── Simple transpose          → Transpose Matrix (result[j][i] = matrix[i][j])
├── Number properties?
│   ├── Digit manipulation        → Plus One (carry from right)
│   ├── Cycle detection           → Happy Number (Floyd's or set)
│   ├── GCD-based                 → GCD Strings, Insert GCD LL (Euclidean)
│   └── Fast exponentiation       → Pow (binary exponentiation / squaring)
├── String arithmetic             → Multiply Strings (grade-school)
├── Numeral systems               → Excel Column, Roman to Integer (mapping + iteration)
└── Geometry / counting           → Detect Squares (coordinate count map)
```

## Algorithm Skeletons

### Sieve of Eratosthenes (Python)

```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime
```

### Fast power / modular exponentiation (Python)

```python
def fast_pow(base, exp, mod=None):
    result = 1
    while exp > 0:
        if exp & 1:
            result = result * base if mod is None else result * base % mod
        base = base * base if mod is None else base * base % mod
        exp >>= 1
    return result
```

### Spiral matrix traversal with direction array (Python)

```python
def spiral_order(matrix):
    m, n = len(matrix), len(matrix[0])
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    d = r = c = 0
    result = []
    for _ in range(m * n):
        result.append(matrix[r][c])
        matrix[r][c] = None          # mark visited
        nr, nc = r + dirs[d][0], c + dirs[d][1]
        if not (0 <= nr < m and 0 <= nc < n and matrix[nr][nc] is not None):
            d = (d + 1) % 4
            nr, nc = r + dirs[d][0], c + dirs[d][1]
        r, c = nr, nc
    return result
```

## Problems

| Problem | Key Insight | Tricky Part | Common Mistakes | Time | Space |
|---------|-------------|-------------|-----------------|------|-------|
| **Excel Sheet Column Title** LC 168 Easy | Base-26 but 1-indexed; subtract 1 before each modulo to shift A=1→0 | Off-by-one in the shift; `n=26` must give "Z" not "Z\0" | Treating as standard base-26 (breaks at Z, AZ, …) | O(log n) | O(log n) |
| **GCD of Strings** LC 1071 Easy | GCD string divides both; `s+t == t+s` is the necessary/sufficient check; answer is `s[:gcd(len(s), len(t))]` | Verifying divisibility without the concatenation trick | Manually checking every prefix | O(m+n) | O(m+n) |
| **Insert GCD in Linked List** LC 2807 Medium | Traverse adjacent pairs; insert node with `gcd(a.val, b.val)` between them | Saving `next` reference before inserting the new node | Losing pointer to rest of list | O(n·log V) | O(1) |
| **Transpose Matrix** LC 867 Easy | `result[j][i] = matrix[i][j]`; rows and cols swap for non-square | In-place transpose only works for square matrices | Trying to transpose in-place on a non-square matrix | O(m·n) | O(m·n) |
| **Rotate Image** LC 48 Medium | Transpose then reverse each row = 90° clockwise; all in-place | Order matters: reverse then transpose = counter-clockwise | Using extra space; wrong operation order | O(n²) | O(1) |
| **Spiral Matrix** LC 54 Medium | Four boundary pointers (top/bottom/left/right); shrink after each side | Must check `top <= bottom` and `left <= right` before inner passes to avoid duplicates on single row/col | Not guarding inner passes; direction array alternative marks visited with `None` | O(m·n) | O(1) |
| **Set Matrix Zeroes** LC 73 Medium | Use first row and first column as flags; handle them last with two booleans | If `matrix[0][0]` is zero it belongs to both; need separate `row0` and `col0` flags | Zeroing rows/cols immediately (corrupts flags); using O(m+n) space | O(m·n) | O(1) |
| **Happy Number** LC 202 Easy | Sum of squares of digits; unhappy numbers cycle back to 4 | Cycle detection: Floyd's two-pointer (O(1) space) or seen set (O(log n)) | Infinite loop without cycle detection | O(log n)/step | O(log n) or O(1) |
| **Plus One** LC 66 Easy | Traverse from right; propagate carry; if carry exits front, prepend 1 | All-9s input needs array expansion | Not handling `[9,9,9]` → `[1,0,0,0]` | O(n) | O(n) worst |
| **Roman to Integer** LC 13 Easy | If current symbol value < next symbol value, subtract; else add | Subtractive cases: IV, IX, XL, XC, CD, CM | Processing left-to-right without lookahead | O(n) | O(1) |
| **Pow(x, n)** LC 50 Medium | Binary exponentiation: `x^n = (x²)^(n/2)`; halve `n` each step | Negative `n`: invert `x` and use `abs(n)`; `n = INT_MIN` overflows on negation → use `long` | Linear recursion O(n); not handling `n < 0` | O(log n) | O(1) iterative |
| **Multiply Strings** LC 43 Medium | Grade-school multiplication; `result[i+j+1] += d1 * d2`; carry in second pass | Result array size is `m+n`; strip leading zeros at end | Converting to `int`/`long` (overflow for large inputs) | O(m·n) | O(m+n) |
| **Detect Squares** LC 2013 Medium | Store point counts in a dict; for each query point + each point sharing x-coord, the diagonal determines the square's other two corners | Count duplicates separately; query point may already be in the set | Checking all pairs O(n²) per query; forgetting to multiply by count of diagonal point | O(1) add, O(n) query | O(n) |

## General Edge Cases

1. **`gcd(0, n) = n`** — valid by Euclid's algorithm; `gcd(0, 6) = 6`. Don't special-case zero unnecessarily, but also don't call `gcd(0, 0)` without a guard if your downstream uses division.
2. **`sqrt` float imprecision** — `Math.sqrt(4)` returns `2.0` but `Math.sqrt(3)` is `1.7320508...`. Never compare `Math.sqrt(n) == k` directly for integers; use `(long)k*k == n` or a loop `i*i <= n`.
3. **`int` overflow on multiplication** — two `int` values each around 10⁵ multiply to ~10¹⁰, which overflows. Cast one operand to `long` before the `*` operator, not after.
4. **`Math.pow(2, 31)` is not `Integer.MAX_VALUE + 1`** — `Math.pow` returns a `double`; `2^31` as double is `2147483648.0` but comparing it with `Integer.MAX_VALUE` via `==` is fragile. Use `1L << 31` or explicit `long` arithmetic.
5. **`n % 2` for odd negative numbers in Java** — `(-7) % 2 == -1`, not `1`. Use `(n & 1) == 0` to test even/odd; it works correctly for all signs.
6. **Division by zero** — before calling `gcd(a, b)` in a loop or inside LCM, confirm `b != 0`; before any `a / b` expression, guard with `b != 0`.
7. **Spiral matrix with 1×n or m×1** — the boundary pointer approach must check `top < bottom` before the bottom-to-left pass and `left < right` before the right-to-top pass; skipping these checks duplicates the single row or column.
8. **`Integer.MIN_VALUE` negation overflow** — `-Integer.MIN_VALUE == Integer.MIN_VALUE` in Java (two's complement). In `Pow(x, n)` when `n = Integer.MIN_VALUE`, cast to `long` before negating: `long exp = Math.abs((long) n)`.
9. **`Math.pow` for integer exponentiation** — `Math.pow` operates on `double`, which has only 53 bits of mantissa. For large integer exponents where exact integer results matter, use binary exponentiation in `long` or `BigInteger` instead.
10. **Negative modulo for true modular arithmetic** — anywhere you need a non-negative remainder (e.g., wrapping a direction index), use `((n % m) + m) % m` rather than `n % m`.
