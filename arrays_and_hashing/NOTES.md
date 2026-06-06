# Arrays & Hashing — Pattern Notes

## Core Intuition

Arrays + hashing problems are about **trading space for time**. A hash map/set turns O(n) lookups into O(1). The core patterns:

- **Frequency map:** Count occurrences, then reason about counts.
- **Complement lookup:** Store what you've seen; check if current element completes a pair/group.
- **Prefix sum:** Precompute cumulative sums for O(1) range queries.
- **Index marking:** Use the array itself as a hash map (mark visited by negating or swapping).
- **Bucketing:** Group elements by a computed key (e.g., sorted tuple for anagrams).

---

## Decision Flowchart

```mermaid
flowchart TD
    A["Array/Hashing Problem"] --> B{Need O(1) range sum?}
    B -- Yes --> C[Prefix Sum / 2D Prefix Sum]
    B -- No --> D{Grouping by equivalence?}
    D -- Yes --> E[HashMap with canonical key\ne.g. sorted string, char count]
    D -- No --> F{Finding pair/complement?}
    F -- Yes --> G[HashMap: store seen values\ncheck complement]
    F -- No --> H{Frequency / count based?}
    H -- Yes --> I[Frequency array or Counter]
    H -- No --> J{In-place, O(1) space?}
    J -- Yes --> K[Index marking / cyclic sort]
    J -- No --> L[HashSet for O(1) lookup]
```

---

## Per-Problem Notes

### 1. Concatenation of Array — LC 1929 | Easy
- **Key insight:** Return `nums + nums`. That's it.
- **Tricky:** Nothing — warm-up problem.
- **Common mistakes:** Overcomplicating it.
- **Time:** O(n) | **Space:** O(n)

### 2. Contains Duplicate — LC 217 | Easy
- **Key insight:** HashSet — if element already in set, return True.
- **Tricky:** Nothing. Alternative: sort and check adjacent.
- **Common mistakes:** Using O(n²) nested loop.
- **Time:** O(n) | **Space:** O(n)

### 3. Valid Anagram — LC 242 | Easy
- **Key insight:** Count character frequencies. Two strings are anagrams if their frequency maps are equal.
- **Tricky:** Unicode follow-up — use a dict instead of fixed-size array.
- **Common mistakes:** Sorting both strings (O(n log n)) when O(n) is possible.
- **Time:** O(n) | **Space:** O(1) (26 chars)

### 4. Two Sum — LC 1 | Easy
- **Key insight:** Store `{value: index}` as you iterate. For each num, check if `target - num` is in map.
- **Tricky:** Check complement before inserting current element (handles same-element pairs correctly).
- **Common mistakes:** Inserting before checking — can use same element twice.
- **Time:** O(n) | **Space:** O(n)

### 5. Longest Common Prefix — LC 14 | Easy
- **Key insight:** Compare character by character across all strings. Stop at first mismatch or shortest string end.
- **Tricky:** Sort strings and only compare first and last — they'll have the smallest common prefix.
- **Common mistakes:** Not handling empty array or empty string inputs.
- **Time:** O(n·m) | **Space:** O(1)

### 6. Group Anagrams — LC 49 | Medium
- **Key insight:** Key = sorted string (or tuple of 26 char counts). Group words by key in a defaultdict.
- **Tricky:** Char count tuple as key avoids O(k log k) sort → O(k) per word.
- **Common mistakes:** Using sorted string key (fine for interviews, but char count is faster).
- **Time:** O(n·k) | **Space:** O(n·k)

### 7. Remove Element — LC 27 | Easy
- **Key insight:** Two-pointer in-place. Write pointer `k` tracks valid elements. Skip elements equal to val.
- **Tricky:** Order doesn't matter — can swap with last element for O(1) deletion.
- **Common mistakes:** Shifting elements (O(n²)). Forgetting to return k.
- **Time:** O(n) | **Space:** O(1)

### 8. Majority Element — LC 169 | Easy
- **Key insight:** Boyer-Moore Voting. Candidate + count. Increment if same, decrement if different. Reset at 0.
- **Tricky:** Works because majority element appears > n/2 times — it always survives.
- **Common mistakes:** Using sort (O(n log n)) or hashmap (O(n) space) when O(1) space is possible.
- **Time:** O(n) | **Space:** O(1)

### 9. Design HashSet — LC 705 | Easy
- **Key insight:** Use array of linked lists (chaining) or open addressing. Or just use a boolean array for small key range.
- **Tricky:** Handle collisions properly if implementing real hashing.
- **Common mistakes:** Using Python's built-in set (defeats the purpose).
- **Time:** O(1) avg | **Space:** O(n)

### 10. Design HashMap — LC 706 | Easy
- **Key insight:** Same as HashSet but store (key, value) pairs. Use chaining for collision resolution.
- **Tricky:** Update existing key vs. insert new key.
- **Common mistakes:** Not handling key updates in chained list.
- **Time:** O(1) avg | **Space:** O(n)

### 11. Sort an Array — LC 912 | Medium
- **Key insight:** Implement merge sort or heap sort. Quick sort has O(n²) worst case.
- **Tricky:** Merge sort: careful with index bounds during merge. In-place merge is complex.
- **Common mistakes:** Using quick sort without randomization → O(n²) on sorted input.
- **Time:** O(n log n) | **Space:** O(n) merge sort

### 12. Sort Colors — LC 75 | Medium
- **Key insight:** Dutch National Flag (3-way partition). Three pointers: low, mid, high. One pass.
- **Tricky:** When swapping mid with high, don't increment mid (new element at mid is unprocessed).
- **Common mistakes:** Incrementing mid after swapping with high — skips unprocessed element.
- **Time:** O(n) | **Space:** O(1)

### 13. Top K Frequent Elements — LC 347 | Medium
- **Key insight:** Bucket sort by frequency. Bucket index = frequency, size = n+1. Collect from high to low.
- **Tricky:** Bucket sort is O(n) vs. heap's O(n log k). Both are valid.
- **Common mistakes:** Using full sort O(n log n). Heap approach: use `heapq.nlargest(k, count, key=count.get)`.
- **Time:** O(n) bucket sort | **Space:** O(n)

### 14. Encode and Decode Strings — LC 271 | Medium
- **Key insight:** Encode as `len#string` for each word. Decoder reads length, skips '#', reads exactly that many chars.
- **Tricky:** Can't use a delimiter like ',' because strings may contain it. Length-prefix is delimiter-free.
- **Common mistakes:** Using a simple delimiter that appears in strings.
- **Time:** O(n) | **Space:** O(n)

### 15. Range Sum Query 2D — LC 304 | Medium
- **Key insight:** 2D prefix sum. `prefix[r][c]` = sum of rectangle from (0,0) to (r,c). Query uses inclusion-exclusion.
- **Tricky:** Formula: `prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]`.
- **Common mistakes:** Off-by-one in prefix array indexing. Forgetting the +1 offset for 1-indexed prefix array.
- **Time:** O(n·m) build, O(1) query | **Space:** O(n·m)

### 16. Product of Array Except Self — LC 238 | Medium
- **Key insight:** Two passes: left products then right products. No division needed.
- **Tricky:** Do it in O(1) extra space by using output array for left pass, then multiply right pass in-place.
- **Common mistakes:** Using division (fails with zeros). Using O(n) extra space for both passes.
- **Time:** O(n) | **Space:** O(1) extra

### 17. Valid Sudoku — LC 36 | Medium
- **Key insight:** Track seen values per row, column, and 3×3 box. Box index = `(r//3)*3 + c//3`.
- **Tricky:** Use sets of sets, or encode as `(val, row)`, `(val, col)`, `(val, box)` in one set.
- **Common mistakes:** Wrong box index formula. Not skipping '.' cells.
- **Time:** O(81) = O(1) | **Space:** O(81) = O(1)

### 18. Longest Consecutive Sequence — LC 128 | Medium
- **Key insight:** HashSet of all numbers. For each number that is a sequence start (num-1 not in set), count streak.
- **Tricky:** Only start counting from sequence beginnings to avoid O(n²).
- **Common mistakes:** Not checking `num-1 not in set` → O(n²) for each element.
- **Time:** O(n) | **Space:** O(n)

### 19. Best Time to Buy/Sell Stock II — LC 122 | Medium
- **Key insight:** Greedy — sum all positive differences between consecutive days. Capture every upward move.
- **Tricky:** You can hold at most one stock, but this greedy is equivalent to buying/selling every day it goes up.
- **Common mistakes:** Trying DP when greedy is O(n) and simpler.
- **Time:** O(n) | **Space:** O(1)

### 20. Majority Element II — LC 229 | Medium
- **Key insight:** Boyer-Moore for 2 candidates (at most 2 elements can appear > n/3 times). Two-pass: find candidates, then verify counts.
- **Tricky:** Must verify candidates in second pass — not all candidates are majority elements.
- **Common mistakes:** Not verifying candidates. Forgetting there can be 0, 1, or 2 results.
- **Time:** O(n) | **Space:** O(1)

### 21. Subarray Sum Equals K — LC 560 | Medium
- **Key insight:** Prefix sum + hashmap. `count[prefix_sum]` tracks how many times each prefix sum occurred. For each index, check `prefix - k` in map.
- **Tricky:** Initialize `count[0] = 1` for subarrays starting at index 0.
- **Common mistakes:** Forgetting `count[0] = 1`. Sliding window doesn't work here (negative numbers).
- **Time:** O(n) | **Space:** O(n)

### 22. First Missing Positive — LC 41 | Hard
- **Key insight:** Index marking. Place each number x in index x-1 (cyclic sort). Then scan for first index where nums[i] != i+1.
- **Tricky:** Answer is always in range [1, n+1]. Ignore numbers outside [1, n].
- **Common mistakes:** Using extra space (O(n) set) when O(1) is required. Not handling duplicates in cyclic sort.
- **Time:** O(n) | **Space:** O(1)

---

## Edge Cases to Watch For

- **Empty array:** Return 0, [], or handle before main logic.
- **Single element:** Many problems have trivial single-element answers.
- **Negative numbers:** Prefix sum, subarray problems — sliding window won't work with negatives.
- **Duplicates:** Two Sum (same element twice), Group Anagrams, Consecutive Sequence.
- **Integer overflow:** Product of array, sum problems — use Python (no overflow) or long in Java.
- **All same elements:** Majority element, sort colors, consecutive sequence.
- **Zeros in array:** Product except self (can't divide by zero), subarray sum.
- **Unicode strings:** Valid anagram follow-up — use dict not fixed array.
