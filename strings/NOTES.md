# Strings — Learning Notes

## Decision Guide: Which Algorithm to Use?

```
String Problem
├── Pattern Matching
│   ├── Single pattern, worst-case guarantee → KMP O(n+m)
│   ├── Single pattern, simple code + rolling hash → Rabin-Karp O(n+m) avg
│   ├── Also need prefix info / Z-array → Z-Function O(n)
│   └── Multiple patterns → Aho-Corasick
├── Palindrome
│   ├── Longest palindromic prefix → KMP on s + '#' + rev(s)
│   ├── Count palindromic subsequences → Interval DP O(n²)
│   └── Longest palindromic substring → Manacher / Expand Center
├── Bracket Balancing
│   └── Stack: remove matched pairs → ceil(open/2) + ceil(close/2)
├── Sliding Window (substring with constraint)
│   └── Char frequency map + window validity counter
└── Sequence Generation
    └── Simulate iteratively, group consecutive chars
```

---

## Core Intuition

Strings problems reduce to a small set of primitives. Identify which one applies first.

- **Sliding window on strings**: maintain a char frequency map and a `valid` counter that tracks how many chars satisfy the window condition. Expand right freely; shrink left when the window violates the constraint. Classic: minimum window substring, count substrings with exactly k distinct.

- **Two-pointer on strings**: palindrome check (left/right converge), reverse words (split on whitespace, reverse list). Python `s.split()` handles multiple spaces; in Java use `s.trim().split("\\s+")`.

- **Pattern matching — KMP vs naive**: naive O(n*m) is fine for short patterns or one-off checks. KMP O(n+m) is required when pattern length is non-trivial or you need all occurrences. Build the LPS (failure function) once, then search in a single pass.

- **Hashing for anagram/palindrome**: frequency array `int[26]` is faster than HashMap for lowercase-only input. Canonical form for anagram grouping: sort the char array and use the sorted string as the map key.

- **String building**: never use `+=` on String inside a loop — each concatenation copies the whole string, giving O(n²). Always use StringBuilder in Java. In Python, collect into a list and `''.join(parts)` at the end.

- **Trie for prefix problems**: when the problem involves many prefix lookups or prefix groupings, a trie beats repeated substring hashing. See the `tries` pattern for details.

---

## Java Idioms

### Char arrays and StringBuilder

```java
// Char array for in-place manipulation
char[] arr = s.toCharArray();
arr[i] = Character.toLowerCase(arr[i]);
String result = new String(arr);

// StringBuilder — O(1) amortized append; NEVER use += in a loop
StringBuilder sb = new StringBuilder();
sb.append(c);           // append char or string
sb.insert(0, c);        // prepend (shifts array — avoid in tight loops)
sb.deleteCharAt(i);     // remove char at index
sb.reverse();           // in-place reversal
String out = sb.toString();
```

### Common String methods

```java
s.indexOf(sub)          // -1 if not found
s.contains(sub)         // boolean
s.startsWith(prefix)
s.endsWith(suffix)
s.replace("old", "new") // replaces all occurrences (not regex)
s.trim()                // strips leading/trailing whitespace
s.split("\\s+")         // split on any whitespace run; "\\." for literal dot
String.join(", ", list) // join with delimiter
String.format("%s-%d", str, num)
```

### Char frequency (lowercase only)

```java
int[] freq = new int[26];
for (char c : s.toCharArray()) freq[c - 'a']++;
// ponytail: ASCII trick only works for 'a'-'z'; use HashMap for arbitrary chars
```

### Anagram canonical form

```java
char[] sorted = s.toCharArray();
Arrays.sort(sorted);
String key = new String(sorted);  // use as HashMap key
```

### KMP in Java

```java
int[] buildLPS(char[] p) {
    int m = p.length, len = 0, i = 1;
    int[] lps = new int[m];
    while (i < m) {
        if (p[i] == p[len]) { lps[i++] = ++len; }
        else if (len != 0)  { len = lps[len - 1]; }
        else                { lps[i++] = 0; }
    }
    return lps;
}

int kmpSearch(char[] t, char[] p, int[] lps) {
    int n = t.length, m = p.length, i = 0, j = 0;
    while (i < n) {
        if (t[i] == p[j]) { i++; j++; }
        if (j == m) return i - j;          // found
        else if (i < n && t[i] != p[j]) {
            if (j != 0) j = lps[j - 1];
            else i++;
        }
    }
    return -1;
}
```

### Rabin-Karp rolling hash in Java

```java
long BASE = 31, MOD = 1_000_000_007L;
// hash = (hash * BASE + (c - 'a' + 1)) % MOD
// Remove leading char: hash = (hash - leading * power % MOD + MOD) % MOD
// ponytail: single hash has collision risk; use double hash if correctness critical
```

---

## Algorithm Skeletons (Python)

### KMP failure function + search

```python
def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length, i = 0, 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length:
            length = lps[length - 1]  # key: don't reset length to 0
        else:
            i += 1
    return lps

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    if not pattern: return 0
    lps = build_lps(pattern)
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1; j += 1
        if j == m:
            return i - j          # found; use lps[j-1] then continue for all
        elif i < n and text[i] != pattern[j]:
            if j: j = lps[j - 1]
            else: i += 1
    return -1
```

### Rolling hash (Rabin-Karp)

```python
def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n: return -1
    BASE, MOD = 31, 10**9 + 7
    power = pow(BASE, m - 1, MOD)

    def char_val(c): return ord(c) - ord('a') + 1

    ph = th = 0
    for i in range(m):
        ph = (ph * BASE + char_val(pattern[i])) % MOD
        th = (th * BASE + char_val(text[i])) % MOD

    if ph == th and text[:m] == pattern: return 0

    for i in range(1, n - m + 1):
        th = (th - char_val(text[i - 1]) * power) % MOD
        th = (th * BASE + char_val(text[i + m - 1])) % MOD
        if th == ph and text[i:i + m] == pattern:  # verify on hash hit
            return i
    return -1
```

### Sliding window for minimum window substring

```python
def min_window(s, t):
    from collections import Counter
    need = Counter(t)
    missing = len(t)          # total chars still needed
    best = ""
    left = 0
    for right, c in enumerate(s):
        if need[c] > 0: missing -= 1
        need[c] -= 1
        if missing == 0:      # window covers t
            while need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if not best or right - left + 1 < len(best):
                best = s[left:right + 1]
            need[s[left]] += 1
            missing += 1
            left += 1
    return best
```

---

## Per-Problem Notes

| Problem | Key Insight | Tricky Part | Common Mistakes | Time | Space |
|---|---|---|---|---|---|
| **Minimum Bracket Reversals** | After stack-removing matched `{}`, remaining is `}}}...{{{`; each adjacent pair needs 1 reversal | Odd length → impossible (-1) | Forgetting odd-length check | O(n) | O(n) |
| **Count and Say** | Read previous term aloud; group consecutive identical digits | n=1 returns "1" with no iteration | Off-by-one on iteration count | O(n * len) | O(len) |
| **Rabin-Karp** | Rolling hash in O(1) per window; verify on hash collision | Modular subtraction can go negative; add MOD before `% MOD` | No collision check → wrong answer | O(n+m) avg | O(m) |
| **Z-Function** | Z[i] = length matching prefix starting at i; use Z-box [l,r] to skip recomputation | Updating [l,r] only when Z[i]+i-1 > r | Confusing Z[0] (undefined; set 0 or n) | O(n) | O(n) |
| **KMP Algorithm** | LPS[i] = longest proper prefix of pattern[0..i] = suffix; on mismatch jump to LPS[j-1] | When j==0 and mismatch, just advance i | Resetting j to 0 on every mismatch (naive) | O(n+m) | O(m) |
| **Shortest Palindrome** | Find longest palindromic prefix via KMP on `s + '#' + rev(s)` | '#' separator prevents LPS spanning the boundary | Using Z-function without separator | O(n) | O(n) |
| **Longest Happy Prefix** | Direct KMP: answer is `s[:LPS[n-1]]` | "Proper" excludes s itself — LPS handles this by definition | Returning the whole string | O(n) | O(n) |
| **Count Palindromic Subsequences** | Interval DP; for each char c find lo/hi, add dp[lo+1][hi-1]+2 | Precompute next/prev arrays for O(1) lo/hi lookup | O(n) lookup per cell → O(n³) total | O(n²) | O(n²) |
| **Count Substrings with K Distinct** | exactly(k) = atMost(k) - atMost(k-1); sliding window for atMost | Deleting from freq map when count hits 0 | Using O(n²) naive enumeration | O(n) | O(k) |
| **Isomorphic Strings** | Bijection: each char in s maps to exactly one char in t, and vice versa | Need two maps (s→t and t→s); one map misses many-to-one collisions | Only checking one direction | O(n) | O(1) |
| **Largest Odd Number in String** | Scan from right; first odd digit is the end of the answer; return prefix | The digit itself determines odd parity; leading zeros fine | Checking even/odd on the full number | O(n) | O(1) |
| **Maximum Nesting Depth of Parentheses** | Track open-paren depth with a counter; max depth seen is the answer | No stack needed — just a counter | Using a stack when a counter suffices | O(n) | O(1) |
| **Remove Outermost Parentheses** | Depth counter: output char only when depth > 0 (open) or depth > 1 (close) before decrement | Order of increment/decrement relative to append | Appending the outermost pair | O(n) | O(n) |
| **Reverse Words in a String** | `' '.join(s.split()[::-1])`; `split()` collapses spaces | Java: `s.trim().split("\\s+")` then reverse array | `s.split(" ")` creates empty strings on multiple spaces | O(n) | O(n) |
| **Rotate String** | s rotated = some rotation of goal; check if goal is substring of s+s | len(s) != len(goal) → False early exit | Checking every rotation in O(n²) | O(n) | O(n) |
| **Sort Characters by Frequency** | Count freq, sort by freq descending, build result string | Tie-breaking (any order valid) | Using sorted() on dict items without reversing | O(n log n) | O(n) |
| **String to Integer (atoi)** | Skip whitespace → sign → digits → clamp to INT_MIN/INT_MAX | Overflow before clamp; check digit by digit | Reading past non-digit chars; ignoring leading spaces | O(n) | O(1) |
| **Sum of Beauty of All Substrings** | For each substring, compute freq then count chars with freq = max_freq | Naive O(n³); optimize to O(n²) by extending substring incrementally | Recomputing freq from scratch for each substring | O(n²) | O(26) |

---

## Edge Cases

1. **Empty string**: most algorithms return 0 or `""` immediately; always guard `if not s` / `if (s.isEmpty())` before indexing.

2. **Single character string**: palindrome check trivially true; KMP with `m=1` works but also catches this; anagram of length-1 strings requires frequency match.

3. **All same characters**: anagram check passes (same freq array); KMP LPS is `[0,1,2,...,m-1]`; sliding window shrinks maximally; palindrome is trivially true.

4. **String with spaces**: `s.split()` (Python, no arg) collapses multiple spaces and strips edges. `s.split(" ")` produces empty strings. In Java, `s.split("\\s+")` on a leading-space string produces an empty first element — use `s.trim().split("\\s+")`.

5. **Unicode vs ASCII**: Java `char` is UTF-16 (16-bit). The `c - 'a'` trick is only valid for lowercase a-z ASCII. For arbitrary characters use `HashMap<Character, Integer>`. Be careful with `Character.isLetter` vs `Character.isAlphabetic` for Unicode.

6. **KMP: pattern longer than text**: return -1 immediately; the while loop would never enter since `j` can never reach `m`.

7. **Overlapping matches**: KMP handles this correctly — after finding a match at index `i-j`, set `j = lps[j-1]` (not 0) and continue. Naive search misses overlapping occurrences.

8. **`String.split(".")` splits on nothing**: `.` is a regex metacharacter matching any char. Use `"\\."` for a literal dot, `"\\s+"` for whitespace, `"\\|"` for pipe. When in doubt, use `Pattern.quote(delim)`.

9. **Modular arithmetic with subtraction**: in rolling hash, `(hash - val) % MOD` can be negative in Java (unlike Python). Always write `(hash - val % MOD + MOD) % MOD`.

10. **StringBuilder `insert(0, c)` is O(n)**: prepending to a StringBuilder shifts all chars. If building a string in reverse, append then call `sb.reverse()` at the end, or use a deque.
