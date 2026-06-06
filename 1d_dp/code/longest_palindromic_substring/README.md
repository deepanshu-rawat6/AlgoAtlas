# LC 5 — Longest Palindromic Substring

Given a string `s`, return the longest palindromic substring in `s`.

## Approaches

### 1. Brute Force
- **Time:** O(n³) | **Space:** O(1)
- Try all O(n²) substrings and check each for palindrome property in O(n). Too slow for large inputs.

### 2. Expand Around Center
- **Time:** O(n²) | **Space:** O(1)
- For each index `i`, expand outward for both odd-length (center at `i`) and even-length (center between `i` and `i+1`) palindromes. Track the longest found. Works because every palindrome has a center.

### 3. DP Table
- **Time:** O(n²) | **Space:** O(n²)
- `dp[i][j] = True` if `s[i..j]` is a palindrome. Build from length 1 upward: `dp[i][j] = (s[i] == s[j]) and (length <= 2 or dp[i+1][j-1])`.

## Key Insight

Every palindrome expands symmetrically from its center. There are `2n - 1` possible centers (n single characters + n-1 gaps between characters). Expanding from each center in O(n) gives O(n²) total — better than brute force and O(1) space unlike the DP table.

## Edge Cases

- Single character: Always a palindrome of length 1.
- All same characters (e.g., `"aaaa"`): The entire string is the answer.
- No palindrome longer than 1 (e.g., `"abcd"`): Return any single character.
- Even-length palindromes (e.g., `"abba"`): Require the two-center expansion.
