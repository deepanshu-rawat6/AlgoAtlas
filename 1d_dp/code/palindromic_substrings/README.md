# LC 647 — Palindromic Substrings

Given a string `s`, return the number of palindromic substrings in it. Every single character is a palindrome.

## Approaches

### 1. Expand Around Center
- **Time:** O(n²) | **Space:** O(1)
- For each of the `2n - 1` centers (single chars and gaps), expand outward while characters match. Increment count for each valid palindrome found during expansion.

### 2. DP Table
- **Time:** O(n²) | **Space:** O(n²)
- `dp[i][j] = True` if `s[i..j]` is a palindrome. Count all `True` entries. Build from length 1 upward using `dp[i][j] = (s[i] == s[j]) and (length <= 2 or dp[i+1][j-1])`.

## Key Insight

The expand-around-center approach is optimal: it finds all palindromes in O(n²) time with O(1) space by exploiting the fact that every palindrome has a unique center. Counting during expansion (rather than after) avoids storing the full DP table.

## Edge Cases

- Single character: Always 1 palindrome.
- All same characters (e.g., `"aaa"`): Every substring is a palindrome — count is `n*(n+1)/2`.
- No repeated characters (e.g., `"abc"`): Only the `n` single-character palindromes.
- Even-length palindromes require expanding from the gap between two equal adjacent characters.
