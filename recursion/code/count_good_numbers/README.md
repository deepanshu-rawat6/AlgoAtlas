# LC 1922 — Count Good Numbers

A digit string of length `n` is "good" if even-indexed positions (0, 2, 4, ...) contain even digits {0,2,4,6,8} and odd-indexed positions contain prime digits {2,3,5,7}. Return the count modulo 10⁹+7.

## Approaches

### 1. Fast Modular Exponentiation
- **Time:** O(log n) | **Space:** O(1)
- Even positions: `ceil(n/2)` positions × 5 choices each = `5^ceil(n/2)`.
- Odd positions: `floor(n/2)` positions × 4 choices each = `4^floor(n/2)`.
- Use Python's built-in `pow(base, exp, mod)` for fast modular exponentiation.

## Key Insight

Each position is independent — the choice at one position doesn't affect others. The total count is the product of choices at each position. Since even and odd positions have different choice counts, we compute them separately and multiply. Fast modular exponentiation is essential because `n` can be up to 10¹⁵.

## Edge Cases

- `n = 1`: Only one even position, 5 choices. Return 5.
- `n = 2`: 5 × 4 = 20.
- `n = 4`: 5² × 4² = 400.
- Large `n` (up to 10¹⁵): The `pow(base, exp, mod)` built-in handles this in O(log n).
