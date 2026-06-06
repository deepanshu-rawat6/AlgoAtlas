"""
KMP (Knuth-Morris-Pratt) Pattern Matching
==========================================
Finds all occurrences of a pattern in a text in O(n + m) time,
where n = len(text), m = len(pattern).

Key insight:
  When a mismatch occurs after matching k characters, we don't restart
  from scratch. The failure function (lps array) tells us the longest
  proper prefix of pattern[0..k-1] that is also a suffix — we jump
  to that position instead of 0.

Why O(n + m)?
  - Building lps: O(m). The pointer `len` never decreases below 0 and
    increases at most m times total, so the while loop runs ≤ 2m times.
  - Matching: O(n). The text pointer `i` only moves forward. The pattern
    pointer `j` can decrease via lps, but since `i` advances each step
    and j ≤ i, total decreases ≤ total increases ≤ n.
  Combined: O(n + m), no worst-case O(nm) like naive search.

Use cases:
  - Substring search in editors
  - DNA sequence matching
  - Network intrusion detection (pattern in packet stream)
"""

from typing import List


def build_lps(pattern: str) -> List[int]:
    """
    Build the Longest Proper Prefix which is also Suffix (lps) array.

    lps[i] = length of the longest proper prefix of pattern[0..i]
             that is also a suffix of pattern[0..i].

    Example: pattern = "AABAAB"
      lps = [0, 1, 0, 1, 2, 3]
      lps[4]=2 means "AA" is both a prefix and suffix of "AABAA"
    """
    m = len(pattern)
    lps = [0] * m
    length = 0   # length of previous longest prefix-suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # don't increment i; try shorter prefix
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text: str, pattern: str) -> List[int]:
    """
    Returns list of all starting indices where pattern occurs in text.
    O(n + m) time, O(m) space for lps array.
    """
    if not pattern:
        return list(range(len(text) + 1))

    n, m = len(text), len(pattern)
    lps = build_lps(pattern)
    matches = []

    i = j = 0   # i = text index, j = pattern index
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            matches.append(i - j)   # found match ending at i-1
            j = lps[j - 1]          # look for next match using lps
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]      # skip already-matched prefix
            else:
                i += 1

    return matches


def kmp_count(text: str, pattern: str) -> int:
    """Count non-overlapping occurrences."""
    return len(kmp_search(text, pattern))


def kmp_contains(text: str, pattern: str) -> bool:
    """Check if pattern exists anywhere in text."""
    if not pattern:
        return True
    n, m = len(text), len(pattern)
    lps = build_lps(pattern)
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1; j += 1
        if j == m:
            return True
        elif i < n and text[i] != pattern[j]:
            j = lps[j - 1] if j else (i := i + 1) and 0
    return False


if __name__ == "__main__":
    # Basic search
    text    = "AABAACAADAABAABA"
    pattern = "AABA"
    print(f"Text:    {text}")
    print(f"Pattern: {pattern}")
    print(f"LPS:     {build_lps(pattern)}")          # [0,1,0,1]
    print(f"Matches at indices: {kmp_search(text, pattern)}")  # [0, 9, 12]

    # Overlapping matches
    text2    = "AAAAAA"
    pattern2 = "AAA"
    print(f"\nOverlapping — '{pattern2}' in '{text2}':")
    print(f"Matches: {kmp_search(text2, pattern2)}")  # [0, 1, 2, 3]

    # DNA example
    dna     = "ACGTACGTACGT"
    motif   = "ACGT"
    print(f"\nDNA motif '{motif}' positions: {kmp_search(dna, motif)}")  # [0,4,8]

    # Edge cases
    print("\nEmpty pattern:", kmp_search("hello", ""))
    print("Pattern longer than text:", kmp_search("ab", "abc"))  # []
    print("No match:", kmp_search("abcdef", "xyz"))              # []
