# Two Pointers

```mermaid
mindmap
  root((Two Pointers))
    Opposite-End
      Reverse String LC344
      Valid Palindrome LC125
      Valid Palindrome II LC680
      Two Sum II LC167
      Container With Most Water LC11
      Trapping Rain Water LC42
    Slow/Fast
      Remove Duplicates from Sorted Array LC26
    Sort + Two Pointers
      3Sum LC15
      4Sum LC18
      Boats to Save People LC881
    Reverse Trick
      Rotate Array LC189
    Parallel Pointers
      Merge Strings Alternately LC1768
      Merge Sorted Array LC88
```

## Overview

This section covers 13 problems focusing on the two-pointer technique — using two indices to traverse data structures efficiently, often reducing O(n²) brute force to O(n).

## Problem List

| # | Problem | LC # | Difficulty | Key Techniques |
|---|---------|------|-----------|----------------|
| 1 | Reverse String | 344 | Easy | Opposite-end pointers |
| 2 | Valid Palindrome | 125 | Easy | Opposite-end pointers |
| 3 | Valid Palindrome II | 680 | Easy | Greedy skip |
| 4 | Merge Strings Alternately | 1768 | Easy | Parallel pointers |
| 5 | Merge Sorted Array | 88 | Easy | Three pointers (from end) |
| 6 | Remove Duplicates from Sorted Array | 26 | Easy | Slow/fast pointers |
| 7 | Two Sum II | 167 | Medium | Opposite-end pointers |
| 8 | 3Sum | 15 | Medium | Sort + two pointers |
| 9 | 4Sum | 18 | Medium | Sort + nested two pointers |
| 10 | Rotate Array | 189 | Medium | Reverse trick |
| 11 | Container With Most Water | 11 | Medium | Opposite-end pointers |
| 12 | Boats to Save People | 881 | Medium | Sort + opposite-end |
| 13 | Trapping Rain Water | 42 | Hard | Opposite-end pointers |

---

## Approach Flow Diagrams

### Two Pointer Categories

```mermaid
flowchart TD
    A[Two Pointer Problem] --> B{Pointer placement?}
    
    B -->|Start & End| C[Opposite-End Pointers]
    B -->|Both at start| D[Slow & Fast Pointers]
    B -->|Separate arrays| E[Parallel Pointers]
    
    C --> C1[Valid Palindrome]
    C --> C2[Two Sum II]
    C --> C3[Container With Most Water]
    C --> C4[Trapping Rain Water]
    C --> C5[3Sum / 4Sum]
    
    D --> D1[Remove Duplicates]
    D --> D2[Remove Element]
    
    E --> E1[Merge Sorted Array]
    E --> E2[Merge Strings Alternately]
```

### Opposite-End Pointer Pattern

```mermaid
flowchart TD
    A["Array/String with left=0, right=n-1"] --> B{Move which pointer?}
    
    B -->|Always both| C[Palindrome Check]
    B -->|Smaller value side| D[Maximize area/sum]
    B -->|Based on target| E[Find target sum]
    
    C --> C1[Reverse String]
    C --> C2[Valid Palindrome]
    C --> C3[Valid Palindrome II]
    
    D --> D1[Container With Most Water]
    D --> D2[Trapping Rain Water]
    D --> D3[Boats to Save People]
    
    E --> E1[Two Sum II]
    E --> E2[3Sum inner loop]
    E --> E3[4Sum inner loop]
    
    subgraph "Decision Logic"
        F["sum < target → left++"]
        G["sum > target → right--"]
        H["sum == target → found!"]
    end
```

### Palindrome Verification Flow

```mermaid
flowchart TD
    A[String Input] --> B[Set left=0, right=len-1]
    B --> C{left < right?}
    
    C -->|No| D[✓ Is Palindrome]
    C -->|Yes| E{Characters match?}
    
    E -->|Yes| F[left++, right--]
    F --> C
    
    E -->|No - LC 125| G[Skip non-alphanumeric]
    G --> C
    
    E -->|No - LC 680| H{Can delete one?}
    H -->|Try skip left| I["Check s[left+1:right+1]"]
    H -->|Try skip right| J["Check s[left:right]"]
    I --> K{Either palindrome?}
    J --> K
    K -->|Yes| L[✓ Valid with one deletion]
    K -->|No| M[✗ Not valid]
```

### Sort + Two Pointers (kSum Pattern)

```mermaid
flowchart TD
    A[Unsorted Array] --> B[Sort Array]
    B --> C{k-Sum variant?}
    
    C -->|2Sum II| D["left=0, right=n-1, find target"]
    C -->|3Sum| E["Fix i, two-pointer on i+1..n-1"]
    C -->|4Sum| F["Fix i,j, two-pointer on j+1..n-1"]
    
    E --> G[Skip duplicate i values]
    G --> H["For each i: left=i+1, right=n-1"]
    H --> I{"nums[i] + nums[left] + nums[right]"}
    I -->|< 0| J[left++]
    I -->|> 0| K[right--]
    I -->|== 0| L[Record triplet, skip duplicates]
    
    F --> M[Skip duplicate i,j values]
    M --> N["Same two-pointer logic inside"]
    
    style G fill:#FFD700
    style L fill:#90EE90
```

### Merge Pattern (From End)

```mermaid
flowchart TD
    A["nums1 = [1,2,3,0,0,0], nums2 = [2,5,6]"] --> B["p1=m-1, p2=n-1, write=m+n-1"]
    
    B --> C{p1 >= 0 AND p2 >= 0?}
    C -->|Yes| D{"nums1[p1] > nums2[p2]?"}
    
    D -->|Yes| E["nums1[write] = nums1[p1], p1--, write--"]
    D -->|No| F["nums1[write] = nums2[p2], p2--, write--"]
    
    E --> C
    F --> C
    
    C -->|No| G{p2 >= 0?}
    G -->|Yes| H["Copy remaining nums2 elements"]
    G -->|No| I[Done - nums1 already in place]
    
    style B fill:#87CEEB
```

### Rotate Array — Reverse Trick

```mermaid
flowchart TD
    A["nums = [1,2,3,4,5,6,7], k=3"] --> B["k = k % n = 3"]
    
    B --> C["Step 1: Reverse entire array"]
    C --> D["[7,6,5,4,3,2,1]"]
    
    D --> E["Step 2: Reverse first k elements"]
    E --> F["[5,6,7,4,3,2,1]"]
    
    F --> G["Step 3: Reverse remaining n-k elements"]
    G --> H["[5,6,7,1,2,3,4] ✓"]
    
    style C fill:#FFB6C1
    style E fill:#98FB98
    style G fill:#87CEEB
```

### Container With Most Water — Greedy Narrowing

```mermaid
flowchart TD
    A["height array, left=0, right=n-1"] --> B["area = min(h[l], h[r]) × (r-l)"]
    B --> C["max_area = max(max_area, area)"]
    
    C --> D{"h[left] < h[right]?"}
    D -->|Yes| E["left++ (move shorter side)"]
    D -->|No| F["right-- (move shorter side)"]
    
    E --> G{left < right?}
    F --> G
    G -->|Yes| B
    G -->|No| H["Return max_area"]
    
    subgraph "Why move shorter side?"
        I["Moving taller side can only decrease area"]
        J["Moving shorter side might find taller bar"]
    end
```

### Trapping Rain Water — Two Pointer Approach

```mermaid
flowchart TD
    A["height array"] --> B["left=0, right=n-1"]
    B --> C["left_max=0, right_max=0"]
    
    C --> D{left < right?}
    D -->|No| E["Return total water"]
    
    D -->|Yes| F{"h[left] < h[right]?"}
    
    F -->|Yes| G{"h[left] >= left_max?"}
    G -->|Yes| H["left_max = h[left]"]
    G -->|No| I["water += left_max - h[left]"]
    H --> J["left++"]
    I --> J
    J --> D
    
    F -->|No| K{"h[right] >= right_max?"}
    K -->|Yes| L["right_max = h[right]"]
    K -->|No| M["water += right_max - h[right]"]
    L --> N["right--"]
    M --> N
    N --> D
    
    style I fill:#87CEEB
    style M fill:#87CEEB
```

### Slow/Fast Pointer — Remove Duplicates

```mermaid
flowchart TD
    A["Sorted array: [1,1,2,2,3]"] --> B["slow=0 (write position)"]
    B --> C["fast=1 (scan position)"]
    
    C --> D{fast < n?}
    D -->|No| E["Return slow+1 (new length)"]
    
    D -->|Yes| F{"nums[fast] != nums[slow]?"}
    F -->|Yes| G["slow++, nums[slow] = nums[fast]"]
    F -->|No| H["Skip duplicate"]
    
    G --> I["fast++"]
    H --> I
    I --> D
    
    subgraph "Result"
        J["[1,2,3,_,_] → length 3"]
    end
```

---

## Complexity Summary

| Problem | Time | Space | Pattern |
|---------|------|-------|---------|
| reverse_string | O(n) | O(1) | Opposite-end pointers |
| valid_palindrome | O(n) | O(1) | Opposite-end pointers |
| valid_palindrome_ii | O(n) | O(1) | Greedy skip |
| merge_strings_alternately | O(n) | O(n) | Parallel pointers |
| merge_sorted_array | O(m+n) | O(1) | Three pointers from end |
| remove_duplicates_from_sorted_array | O(n) | O(1) | Slow/fast pointers |
| two_sum_ii | O(n) | O(1) | Opposite-end pointers |
| 3sum | O(n²) | O(1) | Sort + two pointers |
| 4sum | O(n³) | O(1) | Sort + nested two pointers |
| rotate_array | O(n) | O(1) | Reverse trick |
| container_with_most_water | O(n) | O(1) | Opposite-end pointers |
| boats_to_save_people | O(n log n) | O(1) | Sort + opposite-end |
| trapping_rain_water | O(n) | O(1) | Opposite-end pointers |

---

## Study Order (Recommended)

```mermaid
flowchart LR
    subgraph W1["Week 1: Basics"]
        A1["reverse_string LC344"] --> A2["valid_palindrome LC125"]
        A2 --> A3["valid_palindrome_ii LC680"]
        A3 --> A4["merge_strings_alternately LC1768"]
    end

    subgraph W2["Week 2: Array Ops"]
        B1["remove_duplicates LC26"] --> B2["merge_sorted_array LC88"]
        B2 --> B3["rotate_array LC189"]
    end

    subgraph W3["Week 3: Target Sum"]
        C1["two_sum_ii LC167"] --> C2["three_sum LC15"]
        C2 --> C3["four_sum LC18"]
    end

    subgraph W4["Week 4: Advanced"]
        D1["container_most_water LC11"] --> D2["boats_to_save_people LC881"]
        D2 --> D3["trapping_rain_water LC42"]
    end

    A4 --> B1
    B3 --> C1
    C3 --> D1
```

---

## When to Use Two Pointers

```mermaid
flowchart TD
    A[Problem Input] --> B{Sorted array/string?}
    
    B -->|Yes| C{Find pair with target?}
    C -->|Yes| D[Opposite-end pointers]
    
    B -->|Yes| E{Remove/deduplicate in-place?}
    E -->|Yes| F[Slow/fast pointers]
    
    B -->|No| G{Can sort first?}
    G -->|Yes| H[Sort + two pointers]
    G -->|No| I[Consider hash map instead]
    
    A --> J{Palindrome/symmetry?}
    J -->|Yes| K[Opposite-end pointers]
    
    A --> L{Merge two sorted inputs?}
    L -->|Yes| M[Parallel pointers]
```
