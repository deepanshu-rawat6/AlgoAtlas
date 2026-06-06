# Rabin-Karp String Matching — LC 28 variant

## Problem

Find the first occurrence of `needle` in `haystack`. Return -1 if not found.

**Example:** `haystack="hello"`, `needle="ll"` → 2

## Approach: Rolling Hash

**Why rolling hash?** Naively recomputing the hash of each window is O(m) per window → O(nm) total. Rolling hash updates in O(1) by removing the leftmost character and adding the new rightmost character.

**Hash formula (polynomial):**
```
hash(s[i..i+m-1]) = s[i]*B^(m-1) + s[i+1]*B^(m-2) + ... + s[i+m-1]*B^0
```

**Rolling update:**
```
hash_new = (hash_old - s[i] * B^(m-1)) * B + s[i+m]
```

**Collision handling:** When hashes match, verify with actual string comparison. Use large prime modulus to minimize collisions.

**Complexity:** O(n+m) average, O(nm) worst case (many hash collisions)

## Key Insight

Precompute `B^(m-1) mod MOD` once. The rolling step is then 2 multiplications and 2 additions — O(1).

## Edge Cases

- Empty needle → return 0
- needle longer than haystack → return -1
- All same characters → worst case O(nm) due to collisions; use double hashing to mitigate
