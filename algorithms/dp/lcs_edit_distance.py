"""
LCS (Longest Common Subsequence) & Edit Distance
=================================================

LCS:
  Find the longest subsequence common to both strings (not necessarily contiguous).
  dp[i][j] = LCS length of s1[:i] and s2[:j]
  Recurrence:
    if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
    else:                   dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  Time: O(mn), Space: O(mn) → O(min(m,n)) with rolling rows

Edit Distance (Levenshtein):
  Minimum operations (insert, delete, replace) to transform s1 into s2.
  dp[i][j] = edit distance between s1[:i] and s2[:j]
  Recurrence:
    if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1]
    else: dp[i][j] = 1 + min(dp[i-1][j],    # delete from s1
                              dp[i][j-1],    # insert into s1
                              dp[i-1][j-1])  # replace
  Time: O(mn), Space: O(mn) → O(min(m,n)) with rolling rows
"""

from typing import List, Tuple


# ─── LCS ──────────────────────────────────────────────────────────────────────

def lcs_length(s1: str, s2: str) -> int:
    """Space-optimized LCS using two rows."""
    m, n = len(s1), len(s2)
    # ensure s2 is the shorter string for space optimization
    if m < n:
        s1, s2 = s2, s1
        m, n = n, m

    prev = [0] * (n + 1)
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr
    return prev[n]


def lcs_string(s1: str, s2: str) -> str:
    """Reconstruct the actual LCS string using full 2D table."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # backtrack
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1])
            i -= 1; j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(result))


def shortest_common_supersequence(s1: str, s2: str) -> str:
    """
    Shortest string containing both s1 and s2 as subsequences.
    Length = len(s1) + len(s2) - lcs_length(s1, s2).
    Reconstruct by merging along LCS path.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1]); i -= 1; j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            result.append(s1[i - 1]); i -= 1
        else:
            result.append(s2[j - 1]); j -= 1
    while i > 0:
        result.append(s1[i - 1]); i -= 1
    while j > 0:
        result.append(s2[j - 1]); j -= 1

    return "".join(reversed(result))


# ─── Edit Distance ────────────────────────────────────────────────────────────

def edit_distance(s1: str, s2: str) -> int:
    """Space-optimized edit distance using single row."""
    m, n = len(s1), len(s2)
    # dp[j] = edit distance between s1[:i] and s2[:j]
    dp = list(range(n + 1))   # base case: transform "" to s2[:j] = j insertions

    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = i   # transform s1[:i] to "" = i deletions
        for j in range(1, n + 1):
            temp = dp[j]
            if s1[i - 1] == s2[j - 1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(prev,    # replace
                                dp[j],   # delete from s1
                                dp[j-1]) # insert into s1
            prev = temp

    return dp[n]


def edit_distance_with_ops(s1: str, s2: str) -> Tuple[int, List[str]]:
    """Returns (distance, list_of_operations) for path reconstruction."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1],  # replace
                                   dp[i - 1][j],        # delete
                                   dp[i][j - 1])        # insert

    # backtrack
    ops = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s1[i-1] == s2[j-1]:
            i -= 1; j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + 1:
            ops.append(f"Replace s1[{i-1}]='{s1[i-1]}' with '{s2[j-1]}'")
            i -= 1; j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + 1:
            ops.append(f"Delete s1[{i-1}]='{s1[i-1]}'")
            i -= 1
        else:
            ops.append(f"Insert '{s2[j-1]}' at position {i}")
            j -= 1

    return dp[m][n], ops[::-1]


if __name__ == "__main__":
    # LCS
    s1, s2 = "ABCBDAB", "BDCAB"
    print(f"LCS('{s1}', '{s2}'):")
    print(f"  Length: {lcs_length(s1, s2)}")   # 4
    print(f"  String: '{lcs_string(s1, s2)}'") # BCAB or BDAB

    s1, s2 = "abcde", "ace"
    print(f"\nLCS('{s1}', '{s2}'): {lcs_length(s1, s2)}")  # 3

    # Shortest Common Supersequence
    s1, s2 = "abac", "cab"
    scs = shortest_common_supersequence(s1, s2)
    print(f"\nSCS('{s1}', '{s2}'): '{scs}' (len={len(scs)})")  # cabac or similar

    # Edit Distance
    pairs = [
        ("horse", "ros",    3),
        ("intention", "execution", 5),
        ("",      "abc",   3),
        ("abc",   "abc",   0),
    ]
    print("\nEdit Distance:")
    for a, b, expected in pairs:
        d = edit_distance(a, b)
        print(f"  '{a}' → '{b}': {d} (expected {expected})")

    # With operations
    dist, ops = edit_distance_with_ops("horse", "ros")
    print(f"\nOperations 'horse' → 'ros' (dist={dist}):")
    for op in ops:
        print(f"  {op}")
