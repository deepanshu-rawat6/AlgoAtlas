# Greatest Common Divisor Traversal (LC 2709)

Given an integer array `nums`, there is an edge between indices `i` and `j` if
`gcd(nums[i], nums[j]) > 1`. Return `true` if all indices are connected (the graph
is connected).

## Approaches

### 1. Union-Find via Shared Prime Factors
**Complexity:** O(n · √max_val) time, O(n + max_val) space

For each number, factorize it. For each prime factor, union the current index with the
first index that had that prime factor. After processing all numbers, check if all
indices share the same root.

**Why it works:** Two numbers share a common factor iff they share a prime factor.
Instead of checking all pairs (O(n²)), we use prime factors as intermediaries: any two
numbers sharing a prime are connected through it. Union-Find merges components efficiently.

## Key Insight

Direct pairwise GCD checking is O(n²). The key insight: two numbers are connected iff
they share a **prime factor**. Use prime factors as "bridge" nodes in Union-Find —
union each number with the first number seen with each of its prime factors. This
reduces the problem to O(n · √max_val).

## Edge Cases

- Single element — trivially connected, return `true`.
- Any element is `1` — `gcd(1, x) = 1` for all `x`, so `1` is isolated. If `n > 1`,
  return `false`.
- All elements are prime and distinct — no two share a factor, return `false` if `n > 1`.
- All elements share a common prime — all connected, return `true`.
