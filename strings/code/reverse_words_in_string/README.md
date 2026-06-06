# LC 151 — Reverse Words in a String

## Problem
Given a string `s`, reverse the order of words. Words are separated by spaces.
The result must not have leading/trailing spaces or multiple spaces between words.

**Example:**
- `s = "  hello world  "` → `"world hello"`
- `s = "a good   example"` → `"example good a"`

**Constraints:** `1 <= s.length <= 10^4`, `s` contains English letters, digits, spaces.

---

## Approach 1 — Split + Reverse  `O(n)` time · `O(n)` space

`s.split()` handles all whitespace (leading, trailing, multiple spaces) and
returns a clean list of words. Reverse the list and join with a single space.

```
"  hello world  " → ["hello","world"] → ["world","hello"] → "world hello"
```

Simple and idiomatic Python. The only downside is O(n) extra space for the list.

---

## Approach 2 — Reverse Entire String then Reverse Each Word  `O(n)` time · `O(1)` space

1. Strip and convert to char array.
2. Reverse the entire array → words are in correct order but each word is reversed.
3. Reverse each individual word → words restored to correct spelling.
4. Collapse any remaining multiple spaces.

**Why it works:** Reversing twice at different granularities (whole → per-word)
achieves the net effect of reversing word order while keeping word content intact.

---

## Key Insight
`s.split()` (no argument) is the cleanest way to tokenize with arbitrary whitespace.
For the in-place approach, double-reverse is the classic O(1)-space trick.

---

## Edge Cases
| Input | Output | Reason |
|-------|--------|--------|
| `"  spaces  "` | `"spaces"` | Leading/trailing stripped |
| `"a"` | `"a"` | Single word unchanged |
| `"a   b   c"` | `"c b a"` | Multiple spaces collapsed |
| All spaces | `""` | split() returns empty list |

---

## Complexity
- **Approach 1 — Time:** O(n) · **Space:** O(n)
- **Approach 2 — Time:** O(n) · **Space:** O(1) (excluding output)
