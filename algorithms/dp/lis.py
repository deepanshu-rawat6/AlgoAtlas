"""
Longest Increasing Subsequence (LIS)
=====================================

O(n²) DP:
  dp[i] = length of LIS ending at index i
  dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]
  Time: O(n²), Space: O(n)

O(n log n) Patience Sorting:
  Maintain a 'tails' array where tails[i] = smallest tail element of all
  increasing subsequences of length i+1.
  For each num: binary search for leftmost position in tails where tails[pos] >= num,
  replace tails[pos] with num (or append if num > all tails).
  tails is always sorted → binary search works.
  Time: O(n log n), Space: O(n)

Why tails works:
  tails[i] is the minimum possible ending value for an IS of length i+1.
  Replacing tails[pos] with a smaller value gives more room for future extensions.
  len(tails) at the end = LIS length.

Variants:
  - Longest Non-Decreasing Subsequence: use bisect_right instead of bisect_left
  - Number of LIS: track count array alongside dp
  - LIS with path reconstruction
"""

from typing import List, Tuple
import bisect


# ─── O(n²) DP ─────────────────────────────────────────────────────────────────

def lis_dp(nums: List[int]) -> int:
    """O(n²) DP. Returns LIS length."""
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n   # every element is an IS of length 1

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def lis_dp_with_path(nums: List[int]) -> Tuple[int, List[int]]:
    """O(n²) DP with path reconstruction. Returns (length, subsequence)."""
    if not nums:
        return 0, []
    n = len(nums)
    dp     = [1] * n
    parent = [-1] * n   # parent[i] = index of previous element in LIS ending at i

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    # find end of best LIS
    best_len = max(dp)
    end_idx  = dp.index(best_len)

    # reconstruct
    path = []
    idx  = end_idx
    while idx != -1:
        path.append(nums[idx])
        idx = parent[idx]

    return best_len, path[::-1]


# ─── O(n log n) Patience Sorting ──────────────────────────────────────────────

def lis_fast(nums: List[int]) -> int:
    """O(n log n) using binary search on tails array."""
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)   # find leftmost pos where tails[pos] >= num
        if pos == len(tails):
            tails.append(num)   # num extends the longest IS
        else:
            tails[pos] = num    # replace with smaller tail for future extensions
    return len(tails)


def lis_fast_with_path(nums: List[int]) -> Tuple[int, List[int]]:
    """
    O(n log n) with path reconstruction.
    Track 'tails' indices and a parent array.
    """
    if not nums:
        return 0, []
    n      = len(nums)
    tails  = []          # tails[i] = index in nums of smallest tail for IS of length i+1
    parent = [-1] * n

    for i, num in enumerate(nums):
        pos = bisect.bisect_left([nums[t] for t in tails], num)
        if pos == len(tails):
            tails.append(i)
        else:
            tails[pos] = i
        parent[i] = tails[pos - 1] if pos > 0 else -1

    # reconstruct from last element of tails
    path = []
    idx  = tails[-1]
    while idx != -1:
        path.append(nums[idx])
        idx = parent[idx]

    return len(tails), path[::-1]


# ─── Longest Non-Decreasing Subsequence ───────────────────────────────────────

def lnds(nums: List[int]) -> int:
    """Allow equal elements: use bisect_right instead of bisect_left."""
    tails = []
    for num in nums:
        pos = bisect.bisect_right(tails, num)   # allow equal
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)


# ─── Number of LIS ────────────────────────────────────────────────────────────

def count_lis(nums: List[int]) -> int:
    """
    Count the number of distinct LIS.
    dp[i]    = length of LIS ending at i
    count[i] = number of LIS of that length ending at i
    """
    if not nums:
        return 0
    n = len(nums)
    dp    = [1] * n
    count = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i]    = dp[j] + 1
                    count[i] = count[j]
                elif dp[j] + 1 == dp[i]:
                    count[i] += count[j]

    best = max(dp)
    return sum(c for l, c in zip(dp, count) if l == best)


if __name__ == "__main__":
    tests = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),   # [2,3,7,101]
        ([0, 1, 0, 3, 2, 3],           4),   # [0,1,2,3]
        ([7, 7, 7, 7],                 1),
        ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
    ]

    print("=== LIS Length ===")
    for nums, expected in tests:
        dp_res   = lis_dp(nums)
        fast_res = lis_fast(nums)
        status   = "✓" if dp_res == fast_res == expected else "✗"
        print(f"  {status} {nums}: dp={dp_res}, fast={fast_res} (expected {expected})")

    print("\n=== LIS with Path ===")
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    length, path = lis_dp_with_path(nums)
    print(f"  O(n²)    : length={length}, path={path}")
    length, path = lis_fast_with_path(nums)
    print(f"  O(nlogn) : length={length}, path={path}")

    print("\n=== Longest Non-Decreasing ===")
    print("  [1,3,3,5,5,7]:", lnds([1, 3, 3, 5, 5, 7]))  # 6

    print("\n=== Count LIS ===")
    print("  [1,3,5,4,7]:", count_lis([1, 3, 5, 4, 7]))   # 2: [1,3,5,7] and [1,3,4,7]
    print("  [2,2,2,2]:",   count_lis([2, 2, 2, 2]))       # 4
