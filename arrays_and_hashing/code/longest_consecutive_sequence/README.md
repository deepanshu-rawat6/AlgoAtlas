# LC 128: Longest Consecutive Sequence — O(n) Proof

## Problem
Find the length of the longest consecutive elements sequence. Must run in O(n).

---

## The Algorithm

```python
num_set = set(nums)
longest = 0
for num in num_set:
    if num - 1 not in num_set:  # Only start from sequence beginning
        length = 1
        while num + length in num_set:
            length += 1
        longest = max(longest, length)
return longest
```

---

## 🧮 Proof That This is O(n)

### The "Nested Loop" Concern

At first glance: outer `for` loop is O(n), inner `while` loop could be O(n) → O(n²)?

**NO.** Here's why:

```mermaid
flowchart TD
    A["Array: [100, 4, 200, 1, 3, 2]"] --> B["Set: {"100, 4, 200, 1, 3, 2"}"]
    B --> C["Iterate over set:"]
    C --> D["100: is 99 in set? NO → start sequence<br>  100+1=101 in set? NO → length=1"]
    C --> E["4: is 3 in set? YES → SKIP (not a start)"]
    C --> F["200: is 199 in set? NO → start sequence<br>  200+1=201 in set? NO → length=1"]
    C --> G["1: is 0 in set? NO → start sequence<br>  2 in set? YES, 3? YES, 4? YES, 5? NO → length=4"]
    C --> H["3: is 2 in set? YES → SKIP"]
    C --> I["2: is 1 in set? YES → SKIP"]
    
    J["Key Insight:"] --> K["Each element is visited by the while loop<br>AT MOST ONCE across all iterations"]
```

### Formal Proof

**Claim:** Total work across all iterations of the outer loop is O(n).

**Proof:**
1. The `if num - 1 not in num_set` check ensures we only enter the `while` loop for **sequence starting points**.
2. Each element belongs to exactly ONE sequence.
3. The `while` loop for a sequence of length `k` does `k` iterations.
4. Sum of all sequence lengths = n (every element is in exactly one sequence).
5. Therefore: total `while` loop iterations across ALL outer loop iterations = n.
6. Total work = n (outer loop checks) + n (total while iterations) = **O(n)**. ∎

### Amortized Analysis

| Element | Outer loop check | While loop visits |
|---------|-----------------|-------------------|
| 1 | ✓ (start) | visits 1,2,3,4 |
| 2 | ✓ (skip, 1 exists) | 0 |
| 3 | ✓ (skip, 2 exists) | 0 |
| 4 | ✓ (skip, 3 exists) | 0 |
| 100 | ✓ (start) | visits 100 |
| 200 | ✓ (start) | visits 200 |

**Total while visits:** 4 + 1 + 1 = 6 = n ✓

### Why Sorting Doesn't Work for O(n)
Sorting is O(n log n). The hash set approach achieves true O(n) by trading space for time.

### Complexity
- **Time:** O(n) — proven above
- **Space:** O(n) — hash set
