# Strings — Pattern Study

## Mindmap

```
Strings
├── Bracket Problems
│   └── Minimum Bracket Reversals (stack)
├── Sequence Generation
│   └── Count and Say (simulation)
├── Pattern Matching
│   ├── Rabin-Karp (rolling hash)
│   ├── Z-Function (Z-array)
│   └── KMP Algorithm (LPS array)
├── Palindrome Problems
│   ├── Shortest Palindrome (KMP + reverse)
│   └── Count Palindromic Subsequences (interval DP)
└── Prefix = Suffix
    └── Longest Happy Prefix (KMP LPS)
```

## Problem Table

| # | Problem | LC | Difficulty | Approach | Time | Space |
|---|---------|-----|------------|----------|------|-------|
| 1 | Minimum Bracket Reversals | - | Medium | Stack | O(n) | O(n) |
| 2 | Count and Say | 38 | Medium | Simulation | O(n·L) | O(L) |
| 3 | Rabin-Karp | 28 | Medium | Rolling Hash | O(n+m) avg | O(1) |
| 4 | Z-Function | - | Medium | Z-Array | O(n) | O(n) |
| 5 | KMP Algorithm | 28 | Medium | LPS Array | O(n+m) | O(m) |
| 6 | Shortest Palindrome | 214 | Hard | KMP / Hash | O(n) | O(n) |
| 7 | Longest Happy Prefix | 1392 | Medium | KMP LPS | O(n) | O(n) |
| 8 | Count Palindromic Subsequences | 730 | Hard | Interval DP | O(n²) | O(n²) |

## Study Order

1. **Count and Say** — warm up with string simulation
2. **Minimum Bracket Reversals** — stack-based string processing
3. **Rabin-Karp** — introduce rolling hash concept
4. **Z-Function** — Z-array pattern matching
5. **KMP Algorithm** — LPS array, the core of prefix matching
6. **Longest Happy Prefix** — direct application of KMP LPS
7. **Shortest Palindrome** — KMP applied to palindrome detection
8. **Count Palindromic Subsequences** — interval DP on strings

## Key Themes

- **Rolling hash**: O(1) hash update by removing leading char, adding trailing char
- **LPS / failure function**: backbone of KMP; reuse prefix info on mismatch
- **Z-array**: alternative to LPS; Z[i] = length of match between s[i:] and s[0:]
- **Interval DP**: dp[i][j] depends on dp[i+1][j-1] and sub-intervals
