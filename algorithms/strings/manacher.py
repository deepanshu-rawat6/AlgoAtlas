"""
Manacher's Algorithm — Longest Palindromic Substring in O(n)
=============================================================
Finds the longest palindromic substring (and all palindrome radii) in O(n).

The transform trick:
  Insert '#' between every character (and at boundaries) to unify odd/even
  palindromes into a single odd-length case.
  "abc"  →  "^#a#b#c#$"
  Now every palindrome in the original string maps to an odd palindrome
  in the transformed string.

Why it's O(n):
  We maintain a "rightmost palindrome" window [l, r] centered at c.
  For a new center i:
    - If i < r, we can mirror from the known palindrome at mirror = 2*c - i.
      p[i] ≥ min(p[mirror], r - i)  — free information, no re-checking.
    - We then try to expand beyond what we already know.
  Each character is "visited" at most twice (once when expanding, once when
  used as a mirror), giving O(n) total.

Use cases:
  - Longest palindromic substring (LeetCode 5)
  - Count palindromic substrings (LeetCode 647)
  - Palindrome partitioning
"""

from typing import List, Tuple


def _transform(s: str) -> str:
    """
    Insert '#' separators and sentinel characters.
    '^' and '$' prevent boundary checks inside the loop.
    "abc" → "^#a#b#c#$"
    """
    return "^#" + "#".join(s) + "#$"


def manacher(s: str) -> List[int]:
    """
    Returns array p where p[i] = radius of longest palindrome centered at i
    in the TRANSFORMED string (including '#' characters).

    For original string positions, use manacher_original().
    """
    t = _transform(s)
    n = len(t)
    p = [0] * n
    c = r = 0   # center and right boundary of rightmost palindrome

    for i in range(1, n - 1):
        mirror = 2 * c - i

        if i < r:
            # use mirror's palindrome, but don't exceed current right boundary
            p[i] = min(r - i, p[mirror])

        # attempt to expand beyond known boundary
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        # update rightmost palindrome if we expanded past r
        if i + p[i] > r:
            c, r = i, i + p[i]

    return p


def longest_palindrome(s: str) -> str:
    """Return the longest palindromic substring of s."""
    if not s:
        return ""
    t = _transform(s)
    p = manacher(s)

    # find center with maximum radius in transformed string
    # skip sentinel positions (0 and len-1)
    max_len, center = max((p[i], i) for i in range(1, len(t) - 1))

    # map back to original string
    # center in t corresponds to (center - 1) // 2 in s (roughly)
    start = (center - max_len) // 2
    return s[start: start + max_len]


def count_palindromic_substrings(s: str) -> int:
    """
    Count all palindromic substrings.
    Each palindrome of radius r in transformed string contributes
    ceil(r/2) palindromes in original (alternating real chars and '#').
    Simpler: p[i] // 2 + (1 if t[i] != '#' else 0) ... but easiest:
    sum((p[i] + 1) // 2) over all centers.
    """
    p = manacher(s)
    t = _transform(s)
    total = 0
    for i in range(1, len(t) - 1):
        # each unit of radius in transformed = one palindrome in original
        total += (p[i] + 1) // 2
    return total


def all_palindromes(s: str) -> List[Tuple[int, int]]:
    """
    Return all (start, end) pairs (0-indexed, inclusive) of palindromic substrings.
    """
    p = manacher(s)
    t = _transform(s)
    result = []
    for i in range(1, len(t) - 1):
        # radius r in transformed → palindromes of length 1..r in original
        for r in range(1, p[i] + 1, 2):   # step 2: only real-char radii
            start = (i - r) // 2
            end   = (i + r) // 2 - 1
            if 0 <= start <= end < len(s):
                result.append((start, end))
    return result


if __name__ == "__main__":
    tests = [
        ("babad",    "bab"),      # or "aba"
        ("cbbd",     "bb"),
        ("racecar",  "racecar"),
        ("abacaba",  "abacaba"),
        ("a",        "a"),
        ("",         ""),
    ]

    print("=== Longest Palindromic Substring ===")
    for s, expected in tests:
        result = longest_palindrome(s)
        status = "✓" if len(result) == len(expected) else "✗"
        print(f"  {status} '{s}' → '{result}' (expected len {len(expected)})")

    print("\n=== Count Palindromic Substrings ===")
    # "abc" → a, b, c = 3
    # "aaa" → a,a,a, aa,aa, aaa = 6
    for s, expected_count in [("abc", 3), ("aaa", 6), ("abba", 6)]:
        count = count_palindromic_substrings(s)
        print(f"  '{s}': {count} palindromes")

    print("\n=== Transformed string demo ===")
    s = "abba"
    t = _transform(s)
    p = manacher(s)
    print(f"  Original:    {s}")
    print(f"  Transformed: {t}")
    print(f"  Radii p:     {p}")
    # center at '#' between b's has radius 4 → "abba" is palindrome
