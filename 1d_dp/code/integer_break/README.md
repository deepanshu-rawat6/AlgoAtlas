# LC 343 — Integer Break

Given an integer `n`, break it into the sum of at least 2 positive integers and maximize their product. Return the maximum product.

## Approaches

### 1. DP
- **Time:** O(n²) | **Space:** O(n)
- `dp[i] = max over j in [1, i-1] of: j*(i-j)` (keep both as-is) or `j*dp[i-j]` (break the second part further). The max of these two options at each split gives the best product.

### 2. Math / Greedy with 3s
- **Time:** O(n) | **Space:** O(1)
- Greedily break into 3s as much as possible. 3s maximize the product per unit (e^(1/e) ≈ 1/e is maximized at e ≈ 2.718, so 3 is the best integer). Handle remainders: if remainder is 1, use 4 (= 2×2) instead of 3+1; if remainder is 2, keep it.

## Key Insight

Among all integers, 3 gives the best product-per-unit ratio. Breaking a 6 into 3+3 (product 9) beats 2+2+2 (product 8) or 6 itself. The DP approach discovers this empirically; the math approach exploits it directly. Never keep a factor of 1 (it doesn't help the product).

## Edge Cases

- `n = 2`: Must split into 1+1, product = 1.
- `n = 3`: Must split into 1+2 or 1+1+1, best product = 2.
- `n = 4`: Split into 2+2, product = 4 (better than 1+3 = 3).
- The math approach handles `n <= 4` as special cases before the greedy loop.
