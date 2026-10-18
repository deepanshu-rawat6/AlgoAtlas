# Sliding Window — Pattern Notes

## Core Intuition

Sliding window converts O(n²) brute force (check every subarray) into O(n) by maintaining a window that expands and contracts. The key question: **when do I shrink the window?**

- **Fixed window:** Size is given. Slide by adding the right element and removing the left element at each step. No shrink decision needed.
- **Variable window (find max):** Expand right freely, shrink left when constraint is violated. Track best valid window seen.
- **Variable window (find min):** Expand right until constraint is met, then shrink left as much as possible while constraint still holds. Track best valid window seen.
- **Window validity:** Track via a counter (e.g., number of distinct chars, number of satisfied conditions) rather than iterating the window on every step. Recomputing from scratch costs O(window size) per step; a counter update costs O(1).
- **Monotonic deque:** For window maximum/minimum — maintain a deque of useful candidates in O(1) per element. The front of the deque is always the current window's max.
- **When NOT to use sliding window:** When the optimal subarray is not contiguous, when elements can be negative in a sum-maximization problem (use Kadane's or prefix sum + hashmap), or when window validity does not monotonically depend on window size.

---

## Java Idioms

### Char frequency map

For lowercase-only problems, an `int[26]` array is faster than `HashMap` (no boxing, no hash):

```java
int[] freq = new int[26];
freq[c - 'a']++;          // add
freq[c - 'a']--;          // remove
```

For general characters, use `merge` to avoid explicit null checks:

```java
Map<Character, Integer> freq = new HashMap<>();
freq.merge(c, 1, Integer::sum);   // add
freq.merge(c, -1, Integer::sum);  // remove
freq.remove(c, 0);                // delete key when value reaches 0
```

`freq.remove(c, 0)` is key: without it, a zero-count key still looks like a "present" key if you check `freq.containsKey(c)`, giving wrong window validity counts.

### Monotonic deque for sliding window maximum

Store indices, not values, so you can check whether the front has left the window:

```java
Deque<Integer> dq = new ArrayDeque<>();
for (int i = 0; i < n; i++) {
    // evict stale front
    while (!dq.isEmpty() && dq.peekFirst() <= i - k) dq.pollFirst();
    // maintain decreasing order: evict smaller candidates from back
    while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();
    dq.offerLast(i);
    if (i >= k - 1) result[i - k + 1] = nums[dq.peekFirst()];
}
```

### Fixed window template

```java
int sum = 0, maxSum = 0;
for (int i = 0; i < k; i++) sum += nums[i];
maxSum = sum;
for (int i = k; i < n; i++) {
    sum += nums[i] - nums[i - k];
    maxSum = Math.max(maxSum, sum);
}
```

### Variable window expand-right / shrink-left template

```java
int left = 0;
for (int right = 0; right < n; right++) {
    // add nums[right] to window state
    while (/* window is invalid */) {
        // remove nums[left] from window state
        left++;
    }
    // record answer using (right - left + 1) or similar
}
```

### Validity tracking with a counter

Avoid recomputing window validity from scratch each step. Use a `have` / `formed` counter:

```java
int formed = 0, required = need.size();
// increment formed only when a char's window count exactly meets its required count
if (freq.get(ch).equals(need.get(ch))) formed++;
// decrement formed only when a char's window count falls below its required count
if (need.containsKey(lch) && freq.get(lch) < need.get(lch)) formed--;
```

---

## Decision Flowchart

```
Sliding Window Problem
        |
  Window size fixed?
   /            \
 Yes             No
  |               |
Fixed window   Minimize or Maximize?
               /              \
          Maximize           Minimize
              |                  |
  Expand right freely    Expand until valid
  Shrink left when       Shrink left while still valid
  invalid                Track min window size
  Track max window
        |
  Need element ordering in window?
   /          \
 Yes           No
  |             |
Monotonic    HashMap /
Deque        frequency array
```

---

## Algorithm Skeletons (Python)

### Fixed window

```python
def fixed_window(nums, k):
    n = len(nums)
    if k > n:
        return 0  # or handle gracefully
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, n):
        window_sum += nums[i] - nums[i - k]
        best = max(best, window_sum)
    return best
```

### Variable window — at most k distinct characters

```python
def at_most_k_distinct(s, k):
    freq = {}
    left = best = 0
    for right, ch in enumerate(s):
        freq[ch] = freq.get(ch, 0) + 1
        while len(freq) > k:
            lch = s[left]
            freq[lch] -= 1
            if freq[lch] == 0:
                del freq[lch]
            left += 1
        best = max(best, right - left + 1)
    return best
```

### Sliding window maximum — monotonic deque

```python
from collections import deque

def sliding_window_max(nums, k):
    dq = deque()  # stores indices, decreasing by value
    result = []
    for i, num in enumerate(nums):
        # remove back candidates smaller than current
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        dq.append(i)
        # evict front if it has left the window
        if dq[0] < i - k + 1:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

---

## Per-Problem Notes

| Problem | Key Insight | Tricky Part | Common Mistakes | Time | Space |
|---|---|---|---|---|---|
| Contains Duplicate II (LC 219) | Fixed window of size k; HashSet membership check | Remove `nums[i-k]` not `nums[i-k-1]` | Off-by-one in removal; using HashMap when HashSet suffices | O(n) | O(k) |
| Best Time to Buy/Sell Stock (LC 121) | Track running min (buy price); profit = price - min\_so\_far | Left pointer = min price day, not shrunk by invalid constraint | Updating max profit before updating min; allowing sell before buy | O(n) | O(1) |
| Longest Substring Without Repeating Chars (LC 3) | Variable window; HashMap of last-seen index; move left to `max(left, last_seen[c]+1)` | Must take `max` to avoid moving left backward | Moving left to `last_seen[c]+1` without the max | O(n) | O(min(n,128)) |
| Longest Repeating Character Replacement (LC 424) | Window valid if `(size - max_freq) <= k`; max\_freq never decreases | max\_freq stays monotone — only grow when new char beats it; we only care about larger windows | Decrementing max\_freq when shrinking (unnecessary); shrinking by more than 1 | O(n) | O(26) |
| Permutation in String (LC 567) | Fixed window of `len(s1)`; compare freq arrays; track `matches` counter | matches counter: increment when counts equalize, decrement when they diverge | Sorting window each step O(n·k log k); wrong window size | O(n) | O(26) |
| Minimum Size Subarray Sum (LC 209) | Variable window (minimize); shrink left while `sum >= target` | Shrink as much as possible each iteration, not just once | Shrinking only once; returning 0 vs no-answer ambiguity | O(n) | O(1) |
| Find K Closest Elements (LC 658) | Binary search on the left index of the window of size k | Condition `x - arr[mid] > arr[mid+k] - x` decides direction | Binary searching on value; wrong comparison direction | O(log(n-k)+k) | O(1) |
| Minimum Window Substring (LC 76) | Variable window (minimize); `formed`/`required` counters; expand then shrink | `formed` increments only when count matches exactly, not every occurrence | Incrementing `formed` for every occurrence; not handling chars absent from t | O(n+m) | O(n+m) |
| Sliding Window Maximum (LC 239) | Monotonic decreasing deque of indices; front is always current max | Store indices not values to check window boundary; evict stale front | Storing values instead of indices; not evicting stale front | O(n) | O(k) |
| Binary Subarrays with Sum (LC 930) | `count(goal) = atMost(goal) - atMost(goal-1)` decomposition | atMost with negative goal returns 0 | Trying to directly count with a single window | O(n) | O(1) |
| Count Number of Nice Subarrays (LC 1248) | Same decomposition: `atMost(k) - atMost(k-1)` where window tracks odd-count | Map odds to 1, evens to 0, then exact-k subarray count | Direct count without decomposition; wrong parity mapping | O(n) | O(1) |
| Fruit Into Baskets (LC 904) | At most 2 distinct types in window; longest such subarray | When third type enters, shrink until one type is gone | Tracking basket counts wrong; forgetting to delete key at 0 | O(n) | O(1) |
| Longest Substring with At Most K Distinct Chars (LC 340) | Variable window; shrink when `len(freq) > k` | Remove key from freq when its count hits 0 to keep len(freq) accurate | Leaving zero-count keys in map; shrinking more than needed | O(n) | O(k) |
| Max Consecutive Ones III (LC 1004) | Variable window; allow at most k zeros; window valid if `zeros <= k` | Count zeros in window; shrink left only when zero-count exceeds k | Recounting zeros in window; not tracking zero count separately | O(n) | O(1) |
| Maximum Points from Cards (LC 1423) | Take k cards from either end; equivalent to finding minimum subarray of size `n-k` in the middle | Complement: min window of size `n-k` → total - min = max points | Trying to simulate card-picking directly; off-by-one in complement size | O(n) | O(1) |
| Minimum Window Subsequence (LC 727) | Variable window; find s1 in s2 as subsequence, then shrink from left | After finding subsequence right-to-left from right end, recompute left boundary | Using substring instead of subsequence matching; not shrinking left optimally | O(n·m) | O(1) |
| Number of Substrings Containing All Three Chars (LC 1358) | For each right, find leftmost position where a,b,c all appear; all windows ending at right and starting at ≤ that left are valid | Count = `left + 1` contribution per right pointer | Counting each valid window individually instead of using the complement | O(n) | O(1) |
| Subarrays with K Different Integers (LC 992) | `exactly(k) = atMost(k) - atMost(k-1)` | atMost shrinks left when distinct count exceeds k | Direct exact-k with one window (doesn't generalize cleanly) | O(n) | O(n) |

---

## Edge Cases to Watch For

- **k > array length (fixed window):** Guard `if k > n: return 0` before building the initial window. Without this, `sum(nums[:k])` silently returns a partial sum and the loop never runs.
- **Empty string/array:** Return 0 or `""` immediately. The `for` loop body never executes, but return values and initial best values must be meaningful.
- **All characters the same (permutation in string):** The entire window matches trivially; ensure freq comparison handles this without off-by-one in the `matches` counter.
- **Window of size 1:** Every single-element window is its own valid window. Make sure best is initialized and updated from the first iteration, not only after a shrink event.
- **Negative numbers in sum problems:** Sliding window breaks for max-subarray with negatives because adding more elements can decrease the sum. Use Kadane's algorithm or prefix sum + hashmap (e.g., subarray sum equals k) instead.
- **Deque front out of window (sliding window max):** Check `dq[0] < i - k + 1` (or `dq.peekFirst() <= i - k` in Java) before reading the front as the window max. The off-by-one between `<` and `<=` matters.
- **HashMap key at zero count:** In variable-window problems tracking distinct counts, deleting the key when count reaches 0 is mandatory. Leaving a zero-count key makes `len(freq)` (or `freq.size()` in Java) report more distinct elements than actually present, causing the window to shrink unnecessarily.
- **Character frequency array indexing:** Use `c - 'a'` for lowercase only (array size 26). For mixed case (LC 76), use `ord(c)` (Python) or cast to `int` (Java) with array size 128, or just use a HashMap.
- **`formed` counter in minimum window substring:** Increment `formed` only when `have[ch] == need[ch]`, not every time `have[ch] > 0`. Otherwise the window validates before all required chars are covered.
- **k = 0 edge case (contains duplicate II):** No two distinct indices can satisfy `|i - j| <= 0` (indices are distinct by definition), so the answer is always False. Similarly, `atMost(-1)` in decomposition problems must return 0, not a negative count.
