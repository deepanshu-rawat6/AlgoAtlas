# Arrays & Hashing

```mermaid
mindmap
  root((Arrays & Hashing))
    Hash Map Lookup
      Two Sum LC1
      Group Anagrams LC49
      Valid Sudoku LC36
      Longest Consecutive Sequence LC128
      Subarray Sum Equals K LC560
    Frequency Counting
      Valid Anagram LC242
      Top K Frequent Elements LC347
      Majority Element LC169
      Majority Element II LC229
    Prefix Sum
      Product of Array Except Self LC238
      Range Sum Query 2D LC304
      Subarray Sum Equals K LC560
    Sorting
      Sort an Array LC912
      Sort Colors LC75
      Longest Common Prefix LC14
    Index Marking
      First Missing Positive LC41
    Design
      Design HashSet LC705
      Design HashMap LC706
    Encoding
      Encode and Decode Strings LC271
```

## Overview

This section covers 22 problems focusing on array manipulation, hashing techniques, and frequency counting.

## Problem List

| # | Problem | LC # | Difficulty | Key Techniques |
|---|---------|------|-----------|----------------|
| 1 | Concatenation of Array | 1929 | Easy | Array |
| 2 | Contains Duplicate | 217 | Easy | Hash Set |
| 3 | Valid Anagram | 242 | Easy | Char Counting |
| 4 | Two Sum | 1 | Easy | Hash Map |
| 5 | Longest Common Prefix | 14 | Easy | String Scan |
| 6 | Group Anagrams | 49 | Medium | Hash Map + Sort |
| 7 | Remove Element | 27 | Easy | Two Pointers |
| 8 | Majority Element | 169 | Easy | Boyer-Moore |
| 9 | Design HashSet | 705 | Easy | Design |
| 10 | Design HashMap | 706 | Easy | Design |
| 11 | Sort an Array | 912 | Medium | Merge/Quick Sort |
| 12 | Sort Colors | 75 | Medium | Dutch National Flag |
| 13 | Top K Frequent Elements | 347 | Medium | Bucket Sort |
| 14 | Encode and Decode Strings | 271 | Medium | Length Prefix |
| 15 | Range Sum Query 2D | 304 | Medium | Prefix Sum 2D |
| 16 | Product of Array Except Self | 238 | Medium | Prefix/Suffix |
| 17 | Valid Sudoku | 36 | Medium | Hash Sets |
| 18 | Longest Consecutive Sequence | 128 | Medium | Hash Set |
| 19 | Best Time to Buy/Sell Stock II | 122 | Medium | Greedy |
| 20 | Majority Element II | 229 | Medium | Boyer-Moore Extended |
| 21 | Subarray Sum Equals K | 560 | Medium | Prefix Sum + Map |
| 22 | First Missing Positive | 41 | Hard | Index Marking |

---

## Approach Flow Diagrams

### Hash Map / Hash Set Pattern

```mermaid
flowchart TD
    A[Input Array] --> B{"Need to track seen elements?"}
    B -->|Yes| C[Use Hash Set]
    B -->|No| D{"Need key-value mapping?"}
    D -->|Yes| E[Use Hash Map]
    D -->|No| F[Array manipulation]
    
    C --> G[Contains Duplicate]
    C --> H[Longest Consecutive Sequence]
    C --> I[Valid Sudoku]
    
    E --> J[Two Sum]
    E --> K[Group Anagrams]
    E --> L[Subarray Sum Equals K]
    
    F --> M[Concatenation of Array]
    F --> N[Remove Element]
```

### Frequency Counting Pattern

```mermaid
flowchart TD
    A[Input Data] --> B{"Count frequencies"}
    B --> C[Hash Map / Counter]
    
    C --> D{"What to find?"}
    D -->|Top K elements| E[Top K Frequent Elements]
    D -->|Majority > n/2| F[Majority Element]
    D -->|Majority > n/3| G[Majority Element II]
    D -->|Anagram check| H[Valid Anagram]
    
    E --> E1[Approach 1: Sort by freq O-n log n-]
    E --> E2[Approach 2: Heap O-n log k-]
    E --> E3[Approach 3: Bucket Sort O-n-]
    
    F --> F1[Approach 1: Hash Map O-n-]
    F --> F2[Approach 2: Sort O-n log n-]
    F --> F3[Approach 3: Boyer-Moore O-n- O-1-]
```

### Prefix Sum Pattern

```mermaid
flowchart TD
    A["Array/Matrix"] --> B{"Repeated range queries?"}
    B -->|1D Array| C[Prefix Sum Array]
    B -->|2D Matrix| D[2D Prefix Sum]
    B -->|Product queries| E[Prefix & Suffix Products]
    
    C --> C1[Subarray Sum Equals K]
    C1 --> C2[prefix_sum + hash_map = O-n-]
    
    D --> D1[Range Sum Query 2D]
    D1 --> D2[Precompute: O-mn-, Query: O-1-]
    
    E --> E1[Product of Array Except Self]
    E1 --> E2[Left pass × Right pass = O-n- O-1- space]
```

### Sorting-Based Pattern

```mermaid
flowchart TD
    A[Unsorted Array] --> B{"Which sort?"}
    
    B -->|Divide & Conquer| C[Merge Sort O-n log n-]
    B -->|Partition| D[Quick Sort O-n log n- avg]
    B -->|Limited range 0,1,2| E[Dutch National Flag O-n-]
    B -->|Count occurrences| F[Counting/Bucket Sort O-n-]
    
    C --> C1[Sort an Array - stable]
    D --> D1[Sort an Array - in-place]
    E --> E1[Sort Colors - one pass]
    F --> F1[Top K Frequent Elements]
    
    E1 --> G[Three pointers: low, mid, high]
    G --> G1["low: boundary of 0s"]
    G --> G2["mid: current element"]
    G --> G3["high: boundary of 2s"]
```

### Design Pattern (HashSet / HashMap)

```mermaid
flowchart TD
    A[Design Problem] --> B{"Data Structure"}
    
    B -->|HashSet| C[MyHashSet]
    B -->|HashMap| D[MyHashMap]
    
    C --> C1[Approach 1: Boolean Array]
    C --> C2[Approach 2: Chaining - Linked List]
    
    D --> D1[Approach 1: Direct Array]
    D --> D2[Approach 2: Chaining - Linked List]
    
    C1 --> E["arr[key] = True/False"]
    C2 --> F["hash(key) % size -> bucket -> linked list"]
    
    D1 --> G["arr[key] = value"]
    D2 --> H["hash(key) % size -> bucket -> (key,val) pairs"]
```

### Index Marking / Cyclic Sort Pattern

```mermaid
flowchart TD
    A["Array with values in [1, n]"] --> B{"Find missing/duplicate?"}
    
    B -->|Missing positive| C[First Missing Positive]
    
    C --> D[Approach 1: Hash Set O-n- space]
    C --> E[Approach 2: Index Marking O-1- space]
    
    E --> F["For each num, mark nums[num-1] as negative"]
    F --> G["First positive index i → answer is i+1"]
    
    style E fill:#90EE90
```

### Encode/Decode Pattern

```mermaid
flowchart TD
    A["List of Strings"] --> B{"Encode to single string"}
    
    B --> C[Approach 1: Delimiter with Escaping]
    B --> D[Approach 2: Length Prefix]
    
    C --> C1["Join with special delimiter"]
    C --> C2["Must handle delimiter in strings"]
    
    D --> D1["For each str: len + '#' + str"]
    D --> D2["'5#Hello5#World'"]
    
    D2 --> E{"Decode"}
    E --> F["Read length → read that many chars → repeat"]
    
    style D fill:#90EE90
```

### Greedy Pattern (Stock Problems)

```mermaid
flowchart TD
    A[Price Array] --> B{"Multiple transactions allowed?"}
    
    B -->|Yes - LC 122| C[Best Time to Buy/Sell Stock II]
    
    C --> D[Approach 1: Recursion O-2^n-]
    C --> E[Approach 2: Greedy O-n-]
    
    E --> F["Sum all positive differences"]
    F --> G["if prices[i] > prices[i-1]: profit += diff"]
    
    style E fill:#90EE90
```

---

## Complexity Summary

| Problem | Time | Space | Pattern |
|---------|------|-------|---------|
| concatenation_of_array | O(n) | O(n) | Array copy |
| contains_duplicate | O(n) | O(n) | Hash set |
| valid_anagram | O(n) | O(1) | Char counting |
| two_sum | O(n) | O(n) | Hash map |
| longest_common_prefix | O(n·k) | O(1) | String scan |
| group_anagrams | O(n·k log k) | O(n·k) | Hash map + sort |
| remove_element | O(n) | O(1) | Two pointers |
| majority_element | O(n) | O(1) | Boyer-Moore |
| design_hashset | O(1) avg | O(n) | Chaining |
| design_hashmap | O(1) avg | O(n) | Chaining |
| sort_an_array | O(n log n) | O(n) | Merge/Quick sort |
| sort_colors | O(n) | O(1) | Dutch national flag |
| top_k_frequent_elements | O(n) | O(n) | Bucket sort |
| encode_and_decode_strings | O(n) | O(n) | Length prefix |
| range_sum_query_2d | O(mn) pre / O(1) query | O(mn) | 2D prefix sum |
| product_of_array_except_self | O(n) | O(1) | Prefix/suffix products |
| valid_sudoku | O(1) | O(1) | Hash sets (fixed 9×9) |
| longest_consecutive_sequence | O(n) | O(n) | Hash set |
| best_time_to_buy_sell_stock_ii | O(n) | O(1) | Greedy |
| majority_element_ii | O(n) | O(1) | Boyer-Moore extended |
| subarray_sum_equals_k | O(n) | O(n) | Prefix sum + map |
| first_missing_positive | O(n) | O(1) | Index marking |

---

## Study Order (Recommended)

```mermaid
flowchart LR
    A[Easy] --> B[Medium] --> C[Hard]
    
    A --> A1[Concatenation]
    A --> A2[Contains Duplicate]
    A --> A3[Valid Anagram]
    A --> A4[Two Sum]
    A --> A5[Remove Element]
    A --> A6[Majority Element]
    
    B --> B1[Group Anagrams]
    B --> B2[Top K Frequent]
    B --> B3[Product Except Self]
    B --> B4[Longest Consecutive]
    B --> B5[Subarray Sum K]
    B --> B6[Sort Colors]
    
    C --> C1[First Missing Positive]
```
