"""
Rabin-Karp Rolling Hash Pattern Matching
=========================================
Uses polynomial rolling hash to find pattern(s) in text.

Single pattern:
  Average: O(n + m)  — hash comparison is O(1), string verify only on match
  Worst:   O(nm)     — all hashes collide (e.g., "aaa...a" pattern "aaa")

Multiple patterns:
  Average: O(n + k*m) where k = number of patterns
  Using a hash set of pattern hashes: O(n + sum(m_i))

Rolling hash formula:
  hash(s[i..i+m-1]) = (s[i]*BASE^(m-1) + s[i+1]*BASE^(m-2) + ... + s[i+m-1]) % MOD
  Slide: hash_new = (hash_old - s[i]*BASE^(m-1)) * BASE + s[i+m]

Use cases:
  - Plagiarism detection (multiple pattern search)
  - Longest common substring
  - 2D pattern matching
"""

from typing import List, Set

BASE = 31          # prime close to lowercase alphabet size
MOD  = 10**9 + 7   # large prime to reduce collisions


def _hash(s: str, start: int, length: int, power: int) -> int:
    """Compute polynomial hash of s[start:start+length]. power = BASE^(length-1) % MOD."""
    h = 0
    for i in range(start, start + length):
        h = (h * BASE + ord(s[i]) - ord('a') + 1) % MOD
    return h


def rabin_karp(text: str, pattern: str) -> List[int]:
    """
    Single pattern search. Returns all starting indices.
    Verify on hash match to handle collisions.
    """
    n, m = len(text), len(pattern)
    if m > n:
        return []

    # precompute BASE^(m-1) % MOD for rolling
    power = pow(BASE, m - 1, MOD)

    pat_hash  = _hash(pattern, 0, m, power)
    curr_hash = _hash(text, 0, m, power)
    matches   = []

    if curr_hash == pat_hash and text[:m] == pattern:
        matches.append(0)

    for i in range(1, n - m + 1):
        # roll: remove leftmost char, add new rightmost char
        curr_hash = (curr_hash - (ord(text[i - 1]) - ord('a') + 1) * power) % MOD
        curr_hash = (curr_hash * BASE + ord(text[i + m - 1]) - ord('a') + 1) % MOD
        curr_hash %= MOD

        if curr_hash == pat_hash and text[i:i + m] == pattern:
            matches.append(i)

    return matches


def rabin_karp_multi(text: str, patterns: List[str]) -> dict:
    """
    Search for multiple patterns simultaneously.
    Groups patterns by length, builds hash sets per length.
    Returns dict: pattern -> list of start indices.
    """
    from collections import defaultdict

    # group patterns by length
    by_len: dict[int, List[str]] = defaultdict(list)
    for p in patterns:
        by_len[len(p)].append(p)

    results = {p: [] for p in patterns}
    n = len(text)

    for m, pats in by_len.items():
        if m > n:
            continue
        power = pow(BASE, m - 1, MOD)
        # build hash → pattern mapping (handle collisions with list)
        pat_hashes: dict[int, List[str]] = defaultdict(list)
        for p in pats:
            pat_hashes[_hash(p, 0, m, power)].append(p)

        curr_hash = _hash(text, 0, m, power)
        # check position 0
        for p in pat_hashes.get(curr_hash, []):
            if text[:m] == p:
                results[p].append(0)

        for i in range(1, n - m + 1):
            curr_hash = (curr_hash - (ord(text[i - 1]) - ord('a') + 1) * power) % MOD
            curr_hash = (curr_hash * BASE + ord(text[i + m - 1]) - ord('a') + 1) % MOD
            curr_hash %= MOD
            for p in pat_hashes.get(curr_hash, []):
                if text[i:i + m] == p:
                    results[p].append(i)

    return results


def longest_common_substring(s1: str, s2: str) -> str:
    """
    Binary search on length + rolling hash to find LCS in O(n log n).
    Uses a set of hashes from s1 to check against s2.
    """
    def has_common(length: int) -> str:
        if length == 0:
            return ""
        power = pow(BASE, length - 1, MOD)
        seen: Set[int] = set()

        # hash all substrings of s1 with given length
        h = _hash(s1, 0, length, power)
        seen.add(h)
        for i in range(1, len(s1) - length + 1):
            h = (h - (ord(s1[i - 1]) - ord('a') + 1) * power) % MOD
            h = (h * BASE + ord(s1[i + length - 1]) - ord('a') + 1) % MOD
            h %= MOD
            seen.add(h)

        # check substrings of s2
        h = _hash(s2, 0, length, power)
        if h in seen and s2[:length] in s1:
            return s2[:length]
        for i in range(1, len(s2) - length + 1):
            h = (h - (ord(s2[i - 1]) - ord('a') + 1) * power) % MOD
            h = (h * BASE + ord(s2[i + length - 1]) - ord('a') + 1) % MOD
            h %= MOD
            sub = s2[i:i + length]
            if h in seen and sub in s1:
                return sub
        return ""

    lo, hi, result = 0, min(len(s1), len(s2)), ""
    while lo <= hi:
        mid = (lo + hi) // 2
        candidate = has_common(mid)
        if candidate:
            result = candidate
            lo = mid + 1
        else:
            hi = mid - 1
    return result


if __name__ == "__main__":
    text    = "abcabcabc"
    pattern = "abc"
    print(f"'{pattern}' in '{text}':", rabin_karp(text, pattern))  # [0,3,6]

    # multiple patterns
    patterns = ["ab", "bc", "abc", "xyz"]
    print("\nMulti-pattern search:")
    for p, idxs in rabin_karp_multi(text, patterns).items():
        print(f"  '{p}': {idxs}")

    # longest common substring
    s1, s2 = "abcdefgh", "bcdfgh"
    print(f"\nLCS of '{s1}' and '{s2}': '{longest_common_substring(s1, s2)}'")  # 'fgh' or 'bcd'
