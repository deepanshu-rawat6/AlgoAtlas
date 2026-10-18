# Binary Search — Pattern Notes

## Core Intuition

Binary search works on any **monotonic search space**. If you can define a predicate `f(x)` where all values on one side are `True` and the other `False`, you can binary search it. This extends to searching on the *answer itself* rather than an index.

Sub-patterns:
- **Classic BS** — find exact value or insertion point in sorted array
- **BS on Answer** — search space is the range of possible answers; check feasibility with a helper
- **Rotated Arrays** — one half is always sorted; use that to decide which half to search
- **2D / Implicit** — flatten or use row/col properties

### When to use exact search vs search-on-answer

Use **exact search** when the target is a value that already exists in the array and you just need its index — or when you need the insertion point (first position where the predicate flips). The loop terminates when `lo > hi`.

Use **search-on-answer** when the question is "what is the minimum/maximum X such that some condition holds?" The search space is not the array — it is the *range of valid answer values*. The condition must be monotone: once feasible, always feasible as you move in one direction.

### How to identify the search space boundaries

- Exact search: `lo = 0`, `hi = len(arr) - 1`
- Search-on-answer (minimize): `lo = smallest possible answer` (often `max(arr)` or `1`), `hi = largest possible answer` (often `sum(arr)` or `max(arr)`)
- Rotated search: `lo = 0`, `hi = len(arr) - 1`; the pivot is implicit

### Why binary search works: monotone predicate

Binary search is valid whenever you have a **monotone predicate** `f`: a function where the input domain can be split into a contiguous `False` region followed by a contiguous `True` region (or vice versa). Each step eliminates half the remaining space because `f(mid)` tells you which half the boundary is in. If the predicate is not monotone — values oscillate — binary search gives wrong results.

---

## Java Idioms

### Avoid integer overflow in mid calculation

```java
// WRONG — can overflow when lo + hi > Integer.MAX_VALUE
int mid = (lo + hi) / 2;

// CORRECT — equivalent but overflow-safe
int mid = lo + (hi - lo) / 2;
```

### `Arrays.binarySearch` — rarely used in interviews

```java
int idx = Arrays.binarySearch(arr, target);
// Returns index if found; returns -(insertion_point) - 1 if missing
// Avoid in interviews: awkward return value, no custom comparator needed here
```

### Template 1: Classic (exact match)

```java
int lo = 0, hi = arr.length - 1;
while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) lo = mid + 1;
    else hi = mid - 1;
}
return -1; // not found
```

### Template 2: Search-on-answer (minimize feasible value)

```java
// lo converges to the minimum value where feasible(x) is true
int lo = minAnswer, hi = maxAnswer;
while (lo < hi) {
    int mid = lo + (hi - lo) / 2;
    if (feasible(mid)) hi = mid;   // mid works, try smaller
    else lo = mid + 1;             // mid too small, go right
}
return lo; // lo == hi == answer
```

### Template 3: Rotated array

```java
// Find minimum in rotated sorted array
int lo = 0, hi = arr.length - 1;
while (lo < hi) {
    int mid = lo + (hi - lo) / 2;
    if (arr[mid] > arr[hi]) lo = mid + 1; // min is in right half
    else hi = mid;                         // min is at mid or left
}
return arr[lo];
```

### Search-on-answer boundary rule for capacity problems

For problems like Koko and Ship Packages, the answer space is always:
- `lo = max(arr)` — must handle the largest single element
- `hi = sum(arr)` — worst case: move everything in one trip

Setting `lo = 1` is a common mistake; it allows infeasible starting points that inflate the search range needlessly.

---

## Per-Problem Notes

| Problem | LC | Key Insight | Tricky Part | Common Mistakes | Time | Space |
|---------|-----|-------------|-------------|-----------------|------|-------|
| Binary Search | 704 | Classic template; return `mid` on hit | Loop condition `<=`; update both bounds | Using `(lo+hi)/2` overflow; wrong bound update | O(log n) | O(1) |
| Search Insert Position | 35 | After loop, `lo` is the insertion point | Loop ends at `lo > hi`; `lo` is correct | Returning `mid` when element absent | O(log n) | O(1) |
| Guess Number Higher or Lower | 374 | API-based BS; `guess(mid)` returns -1/0/1 | Map return values to lo/hi moves correctly | Confusing -1/1 semantics (too high vs too low) | O(log n) | O(1) |
| Sqrt(x) | 69 | BS on `[0, x]`; find largest `mid` where `mid*mid <= x`; return `hi` | Overflow: use `mid <= x // mid` not `mid*mid <= x` | Integer overflow in `mid*mid`; returning `mid` not `hi` | O(log x) | O(1) |
| Search 2D Matrix | 74 | Flatten: treat as 1D array; `mid // cols`, `mid % cols` | Row-major order must hold (each row starts after last row ends) | Using staircase search (unnecessary); wrong index mapping | O(log mn) | O(1) |
| Koko Eating Bananas | 875 | Search-on-answer; `lo=1`, `hi=max(piles)`; feasible if `sum(ceil(p/k)) <= h` | Ceiling division: `(p + k - 1) // k` or `math.ceil(p/k)` | Using `p // k` (floor) instead of ceiling; `lo=0` start | O(n log M) | O(1) |
| Capacity to Ship Packages | 1011 | Search-on-answer; `lo=max(weights)`, `hi=sum(weights)`; greedy day simulation | Pieces start at 1 in feasibility check, not 0 | Setting `lo=1` instead of `max(weights)` | O(n log S) | O(1) |
| Find Minimum in Rotated Sorted Array | 153 | Compare `nums[mid]` with `nums[hi]`; if greater, min is in right half | Always compare with `hi`, not `lo` | Comparing with `nums[lo]` instead of `nums[hi]`; using `<=` | O(log n) | O(1) |
| Search in Rotated Sorted Array | 33 | Identify which half is sorted first, then check if target lies in that half | Two conditions: which half sorted AND target in that half | Skipping the "which half sorted" check; going directly to target comparison | O(log n) | O(1) |
| Search in Rotated Sorted Array II | 81 | Same as LC 33 but add: when `nums[lo]==nums[mid]==nums[hi]`, shrink both ends | The equal case breaks the sorted-half identification — must shrink | Not handling equal case → infinite loop; O(n) worst case is expected | O(log n) avg, O(n) worst | O(1) |
| Time Based Key-Value Store | 981 | Store `(timestamp, value)` list per key; `bisect_right` on timestamps then subtract 1 | `bisect_right` gives insertion point after equal timestamps; subtract 1 for floor | Off-by-one with `bisect_left` vs `bisect_right`; not checking index > 0 | O(log n) get, O(1) set | O(n) |
| Split Array Largest Sum | 410 | Search-on-answer; `lo=max(nums)`, `hi=sum(nums)`; count pieces greedily | Pieces counter starts at 1 (first piece always exists) | Feasibility off-by-one: starting pieces=0; `lo=0` | O(n log S) | O(1) |
| Median of Two Sorted Arrays | 4 | BS on partition of smaller array; derive partition of larger automatically | Use `float('-inf')`/`float('inf')` as sentinels at boundaries | Not BS-ing on smaller array; wrong odd/even total handling; sentinel values | O(log min(m,n)) | O(1) |
| Find in Mountain Array | 1095 | Three phases: find peak index, BS ascending left side, BS descending right side | Right side is descending — flip comparison direction | Forgetting to search right side; not inverting comparison for descending BS | O(log n) | O(1) |

---

## Templates (Python)

### Classic binary search

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

### Search-on-answer (minimize)

```python
def search_on_answer(arr, limit):
    lo, hi = max(arr), sum(arr)   # bounds for capacity-style problems
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if feasible(arr, mid, limit):
            hi = mid      # mid works, try smaller
        else:
            lo = mid + 1  # mid too small
    return lo             # lo == hi == minimum feasible answer
```

### Rotated array search

```python
def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        # Left half is sorted
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
```

---

## Edge Cases to Watch

- **Off-by-one in loop condition**: `while lo <= hi` for exact match (loop exits when `lo > hi`); `while lo < hi` for search-on-answer (loop exits when `lo == hi == answer`). Mixing these causes either an infinite loop or a missed answer.
- **Mid calculation overflow**: Always use `lo + (hi - lo) // 2`, not `(lo + hi) // 2`. Critical in Java/C++; Python arbitrary-precision ints are immune but write it correctly anyway for interview portability.
- **Empty array**: Classic BS returns -1 immediately (`lo > hi`); search-on-answer will have an empty `arr` making `max(arr)` crash — guard with an early return if input can be empty.
- **All-same elements**: Classic BS works fine. Rotated BS (LC 81) breaks because `nums[lo]==nums[mid]==nums[hi]` prevents identifying the sorted half — must shrink both ends (`lo++`, `hi--`) at the cost of O(n) worst case.
- **Target smaller than all / larger than all**: Classic BS ends with `lo = 0` or `lo = n`; both are valid insertion points (LC 35 returns `lo`). For search-on-answer this cannot happen because `hi = sum(arr)` is always feasible.
- **Duplicates in rotated array (LC 81)**: The only binary search problem where worst-case degrades to O(n). When all three of `nums[lo]`, `nums[mid]`, `nums[hi]` are equal you cannot tell which half is sorted. The fix is to shrink: `lo += 1; hi -= 1`. This is the intended trade-off.
- **Sentinel values in partition problems**: LC 4 (Median) needs `float('-inf')` and `float('inf')` when a partition is at index 0 or end; forgetting them causes index-out-of-bounds or wrong comparisons at the array boundaries.
