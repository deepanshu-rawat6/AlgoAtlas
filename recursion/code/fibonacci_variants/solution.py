"""
# Fibonacci Variants

1. Compute the nth Fibonacci number (0-indexed: fib(0)=0, fib(1)=1).
2. Count the number of ways to climb n stairs taking 1 or 2 steps at a time.

## Examples
```text
Input:  fib(10)
Output: 55

Input:  climbStairs(5)
Output: 8
```

## Constraints
- fib(0) = 0, fib(1) = 1; fib(n) = fib(n-1) + fib(n-2).
- climbStairs(n) = climbStairs(n-1) + climbStairs(n-2).
- For large n, prefer the memoized or iterative approach to avoid recursion limits.
"""
class Solution:
    def fib_naive(self, n: int) -> int:
        # Approach 1: Naive recursion O(2^n) — recomputes same subproblems repeatedly
        if n <= 1:
            return n
        return self.fib_naive(n - 1) + self.fib_naive(n - 2)

    def fib(self, n: int) -> int:
        # Approach 2: Memoized recursion O(n) — cache results to avoid recomputation
        memo = {}

        def dp(n):
            if n <= 1:
                return n
            if n in memo:
                return memo[n]
            memo[n] = dp(n - 1) + dp(n - 2)
            return memo[n]

        return dp(n)

    def fib_iterative(self, n: int) -> int:
        # Approach 3: Iterative O(n) time, O(1) space — no recursion overhead
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def climbStairs(self, n: int) -> int:
        # Count ways to climb n stairs (1 or 2 steps at a time) — same recurrence as fib
        # climbStairs(n) = climbStairs(n-1) + climbStairs(n-2)
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    sol = Solution()
    assert sol.fib(10) == 55
    assert sol.fib_naive(10) == 55
    assert sol.fib_iterative(10) == 55
    assert sol.climbStairs(5) == 8
    assert sol.climbStairs(1) == 1
    assert sol.climbStairs(2) == 2
    print("All tests passed.")
