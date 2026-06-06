"""
Interval DP
===========
Problems where the answer for interval [i,j] depends on answers for
sub-intervals. Always iterate by increasing interval length.

Template:
  for length in range(2, n+1):          # interval length
      for i in range(n - length + 1):   # start
          j = i + length - 1            # end
          for k in range(i, j):         # split point
              dp[i][j] = combine(dp[i][k], dp[k+1][j], cost(i,j,k))

Problems covered:
  1. Matrix Chain Multiplication — minimize scalar multiplications
  2. Burst Balloons — maximize coins collected
  3. Palindrome Partitioning — minimum cuts to make all parts palindromes
  4. Minimum Cost to Merge Stones

Time: O(n³) for all problems below
Space: O(n²)
"""

from typing import List, Tuple
import sys


# ─── Matrix Chain Multiplication ──────────────────────────────────────────────

def matrix_chain(dims: List[int]) -> Tuple[int, List[List[int]]]:
    """
    dims[i-1] x dims[i] = dimensions of matrix i (1-indexed).
    Returns (min_cost, split_table) where split[i][j] = optimal split point.

    dp[i][j] = min multiplications to compute product of matrices i..j
    dp[i][j] = min over k in [i,j-1] of dp[i][k] + dp[k+1][j] + dims[i-1]*dims[k]*dims[j]
    """
    n = len(dims) - 1   # number of matrices
    dp    = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                if cost < dp[i][j]:
                    dp[i][j]    = cost
                    split[i][j] = k

    return dp[1][n], split


def matrix_chain_order(split: List[List[int]], i: int, j: int) -> str:
    """Reconstruct optimal parenthesization from split table."""
    if i == j:
        return f"M{i}"
    k = split[i][j]
    left  = matrix_chain_order(split, i, k)
    right = matrix_chain_order(split, k + 1, j)
    return f"({left} x {right})"


# ─── Burst Balloons ───────────────────────────────────────────────────────────

def burst_balloons(nums: List[int]) -> int:
    """
    LeetCode 312. Add sentinel 1s at both ends.
    dp[i][j] = max coins from bursting all balloons between i and j (exclusive).
    Key insight: think of k as the LAST balloon burst in [i+1, j-1].
    When k is last, its neighbors are i and j (already burst).
    dp[i][j] = max over k of dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j]
    """
    nums = [1] + nums + [1]
    n    = len(nums)
    dp   = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            for k in range(i + 1, j):
                coins = nums[i] * nums[k] * nums[j]
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + coins)

    return dp[0][n - 1]


# ─── Palindrome Partitioning (min cuts) ───────────────────────────────────────

def min_palindrome_cuts(s: str) -> int:
    """
    Minimum cuts to partition s into palindromic substrings.
    Precompute is_palindrome[i][j] using DP, then:
    cuts[i] = min cuts for s[:i+1]
    cuts[i] = 0 if s[:i+1] is palindrome
    cuts[i] = min(cuts[j] + 1) for j < i where s[j+1:i+1] is palindrome
    Time: O(n²)
    """
    n = len(s)
    # precompute palindrome table
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True
    for i in range(n - 1):
        is_pal[i][i + 1] = (s[i] == s[i + 1])
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            is_pal[i][j] = (s[i] == s[j]) and is_pal[i + 1][j - 1]

    cuts = list(range(-1, n))   # cuts[i+1] = min cuts for s[:i+1]; cuts[0]=−1 (base)
    for i in range(n):
        if is_pal[0][i]:
            cuts[i + 1] = 0
            continue
        cuts[i + 1] = min(cuts[j + 1] + 1 for j in range(i) if is_pal[j + 1][i])

    return cuts[n]


# ─── Minimum Cost to Merge Stones ─────────────────────────────────────────────

def merge_stones(stones: List[int], k: int) -> int:
    """
    LeetCode 1000. Merge k consecutive piles into one, cost = sum of merged.
    Returns -1 if impossible.
    Possible iff (n-1) % (k-1) == 0.
    dp[i][j] = min cost to merge stones[i..j] into as few piles as possible.
    """
    n = len(stones)
    if (n - 1) % (k - 1) != 0:
        return -1

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + stones[i]

    dp = [[0] * n for _ in range(n)]

    for length in range(k, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            for m in range(i, j, k - 1):   # split into [i,m] and [m+1,j]
                dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j])
            if (j - i) % (k - 1) == 0:    # can merge into one pile
                dp[i][j] += prefix[j + 1] - prefix[i]

    return dp[0][n - 1]


if __name__ == "__main__":
    # Matrix Chain
    dims = [10, 30, 5, 60]   # M1:10x30, M2:30x5, M3:5x60
    cost, split = matrix_chain(dims)
    print(f"Matrix chain min cost: {cost}")          # 4500
    print(f"Optimal order: {matrix_chain_order(split, 1, 3)}")  # (M1 x M2) x M3

    # Burst Balloons
    print(f"\nBurst balloons [3,1,5,8]: {burst_balloons([3,1,5,8])}")  # 167

    # Palindrome Partitioning
    tests = [("aab", 1), ("a", 0), ("ab", 1), ("aaabaa", 1)]
    print("\nMin palindrome cuts:")
    for s, expected in tests:
        result = min_palindrome_cuts(s)
        status = "✓" if result == expected else "✗"
        print(f"  {status} '{s}': {result} (expected {expected})")

    # Merge Stones
    print(f"\nMerge stones [3,2,4,1] k=2: {merge_stones([3,2,4,1], 2)}")  # 20
    print(f"Merge stones [3,2,4,1] k=3: {merge_stones([3,2,4,1], 3)}")  # -1
    print(f"Merge stones [3,5,1,2,6] k=3: {merge_stones([3,5,1,2,6], 3)}")  # 25
