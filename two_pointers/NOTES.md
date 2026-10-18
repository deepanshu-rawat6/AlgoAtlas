# Two Pointers — Pattern Notes

## Core Intuition

Two pointers eliminate the need for nested loops by maintaining two indices that move toward each other or in the same direction. The key is identifying **what invariant the pointers maintain**.

- **Opposite-end:** Left and right converge on a sorted array. Used when you need pairs or triplets summing to a target. Move the pointer whose side is the bottleneck (smaller value → move that side in).
- **Same direction (slow/fast):** One pointer reads, one writes. The slow pointer tracks the write position. Used for removing duplicates, partitioning, or moving zeros in-place.
- **Two separate arrays:** One pointer per array, advance based on comparison. Used for merging two sorted arrays or comparing two strings character by character.
- **Sort + two pointers (k-sum):** Fix one element with an outer loop, then reduce to a two-pointer subproblem on the rest. Sort first to enable duplicate skipping and the convergence invariant.
- **When to sort vs not:** Sorting changes index positions, so avoid it when the problem cares about original indices (e.g., Two Sum returning indices). If the problem only cares about values (3Sum, 4Sum), sort freely.

---

## Java Idioms

### Sort prerequisite
```java
Arrays.sort(nums); // required before opposite-end two-pointer
```

### In-place mutations
Java arrays are passed by reference — `void` methods can mutate in place. Return the new logical length:
```java
public int removeDuplicates(int[] nums) {
    int k = 1;
    for (int i = 1; i < nums.length; i++)
        if (nums[i] != nums[k - 1]) nums[k++] = nums[i];
    return k;
}
```

### Opposite-end loop
```java
int left = 0, right = n - 1;
while (left < right) {
    // process, then:
    left++;   // or
    right--;  // based on comparison
}
```

### 3Sum duplicate skip (after advancing pointer)
```java
// After finding a valid triplet and advancing left:
while (left < right && nums[left] == nums[left - 1]) left++;
// After advancing right:
while (left < right && nums[right] == nums[right + 1]) right--;
```

### Same-direction: remove duplicates
```java
int k = 1;
for (int i = 1; i < n; i++)
    if (nums[i] != nums[k - 1]) nums[k++] = nums[i];
return k;
```

### Fast/slow pointer
```java
int slow = 0, fast = 0;
while (fast < n) {
    // process nums[fast], conditionally advance slow
    fast++;
}
```

### Two pointers on two separate arrays (merge sorted)
```java
int i = 0, j = 0;
while (i < m && j < n) {
    if (nums1[i] <= nums2[j]) result[k++] = nums1[i++];
    else result[k++] = nums2[j++];
}
// append leftovers
```

### Overflow guard (4Sum in Java)
```java
long sum = (long) nums[a] + nums[b] + nums[c] + nums[d];
```

---

## Algorithm Skeletons

### Two Sum II — opposite ends
```python
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]   # 1-indexed
        elif s < target:
            left += 1
        else:
            right -= 1
```

### Remove Duplicates — same direction
```python
def removeDuplicates(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1
    return k
```

### 3Sum — fix one, two-pointer inner loop
```python
def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:   # skip outer duplicates
            continue
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if s == 0:
                result.append([nums[i], nums[lo], nums[hi]])
                while lo < hi and nums[lo] == nums[lo + 1]: lo += 1
                while lo < hi and nums[hi] == nums[hi - 1]: hi -= 1
                lo += 1; hi -= 1
            elif s < 0:
                lo += 1
            else:
                hi -= 1
    return result
```

---

## Decision Flowchart

```
Two Pointer Problem
├── In-place modification?
│   └── Yes → slow/fast pointers (write + read)
└── No
    ├── Sorted or can sort?
    │   └── Yes
    │       ├── Finding pairs/triplets? → opposite-end pointers after sorting
    │       └── Palindrome/symmetric?  → left/right converge, check equality
    └── No
        ├── Merging two sequences?     → two pointers on two separate arrays
        └── Else                       → sliding window or fast/slow
```

---

## Per-Problem Notes

| Problem | Key Insight | Tricky Part | Common Mistakes | Time | Space |
|---|---|---|---|---|---|
| Reverse String (LC 344) | Swap `s[left]` and `s[right]`, move inward | Nothing — pure warm-up | Using extra space / reversing into new array | O(n) | O(1) |
| Valid Palindrome (LC 125) | Skip non-alphanumeric; compare lowercased chars from both ends | Use `isalnum()` filter; no preprocessing into new string | Missing non-alphanumeric handling; case sensitivity | O(n) | O(1) |
| Valid Palindrome II (LC 680) | On first mismatch, try skipping left OR right; check either remaining substring | Only one deletion allowed; use helper `isPalin(s,l,r)` to avoid slicing | Greedy skip without checking both options; O(n) space from slicing | O(n) | O(1) |
| Merge Strings Alternately (LC 1768) | Two pointers on two strings, append alternately; append remainder of longer | One pointer may exhaust before the other | Forgetting to append remaining chars of longer string | O(n+m) | O(n+m) |
| Merge Sorted Array (LC 88) | Merge from back with three pointers; avoids shifting | Fill right-to-left — no extra space needed | Merging from front (requires shifting); forgetting remaining nums2 | O(n+m) | O(1) |
| Remove Duplicates (LC 26) | Slow pointer `k` marks next write position; write when `nums[fast] != nums[k-1]` | Return `k` (count), not the array | Comparing `nums[fast-1]` instead of `nums[k-1]` — wrong when duplicates skipped | O(n) | O(1) |
| Two Sum II (LC 167) | Sorted → opposite-end; sum too big → move right left; sum too small → move left right | 1-indexed output; exactly one solution guaranteed | Using hashmap (O(n) space) when O(1) is possible | O(n) | O(1) |
| 3Sum (LC 15) | Sort, fix one element, two-pointer on rest; skip duplicates at all three levels | Three places to skip duplicates: outer loop, after left advance, after right advance | Not skipping duplicates → duplicate triplets; not sorting first | O(n²) | O(1) |
| 4Sum (LC 18) | Two nested loops + two-pointer; sort first; skip duplicates at all four levels | Integer overflow for large values — use `long` in Java | Not skipping outer duplicates; overflow with large numbers | O(n³) | O(1) |
| Rotate Array (LC 189) | Three reverses: all → first k → last n-k | `k = k % n` before any reversal | Not taking k mod n; using extra array | O(n) | O(1) |
| Container With Most Water (LC 11) | Opposite-end; always move the shorter wall (shorter side is the bottleneck) | Moving taller side can only decrease area | Moving the taller side; not updating max at each step | O(n) | O(1) |
| Boats to Save People (LC 881) | Sort; pair heaviest with lightest if they fit; else heaviest goes alone | Always advance right; advance left only if paired | Not sorting first; moving both pointers when they don't fit | O(n log n) | O(1) |
| Trapping Rain Water (LC 42) | Maintain `maxLeft` and `maxRight`; water at position = `min(maxLeft, maxRight) - height[i]`; move side with smaller max | The shorter side's water level is fully determined | Using O(n) extra arrays (works but not optimal); moving wrong pointer | O(n) | O(1) |

---

## Edge Cases to Watch For

- **Empty array:** Most problems short-circuit with 0 or trivially true/false before the loop starts.
- **All duplicates in 3Sum:** `[0,0,0]` → one valid triplet `[0,0,0]`. `[2,2,2]` with target 0 → no triplet. Duplicate skipping must still add the first valid triplet before skipping.
- **`left == right` during duplicate skip in 3Sum:** The guard `while left < right && ...` prevents pointers from crossing; skip logic must always include this bound check.
- **Two Sum II with no valid pair:** Problem guarantees exactly one solution, but in a generalized version guard with `left < right` and return empty/sentinel.
- **Container with water — single element:** Constraint says n >= 2, but conceptually one wall cannot form a container; area = 0.
- **Remove duplicates — array of length 1:** `k = 1` from initialization, the loop body never executes; return 1 correctly with no work.
- **Trapping rain water — monotonically decreasing sequence:** `maxLeft` never exceeds current bar from the left, so no water accumulates; total = 0.
- **Fast/slow pointer — fast skips past end:** Always check `fast < n` (or `fast < len(s)`) inside the loop; with same-direction two pointers, `fast` can reach `n` and the loop must terminate cleanly.
- **k > n in Rotate Array:** Always apply `k = k % n` first; if `k == 0` after mod, no rotation needed.
- **Negative numbers in k-sum:** Sorting still works; just be careful with overflow in 4Sum — cast to `long` in Java before summing.
- **Palindrome with all same chars in Palindrome II:** Any single deletion still yields a palindrome; both branches of the helper return true.
