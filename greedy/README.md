# Greedy

```mermaid
mindmap
  root((Greedy))
    Kadane's Subarray
      Maximum Subarray LC53
      Maximum Sum Circular Subarray LC918
      Longest Turbulent Subarray LC978
    Jump Games
      Jump Game LC55
      Jump Game II LC45
      Jump Game VII LC1871
    Scheduling
      Gas Station LC134
      Hand of Straights LC846
      Dota2 Senate LC649
      Candy LC135
    Partitioning
      Merge Triplets LC1899
      Partition Labels LC763
      Valid Parenthesis String LC678
    Simulation
      Lemonade Change LC860
```

## Problem List

| # | Problem | LC # | Difficulty | Key Technique |
|---|---------|------|------------|---------------|
| 1 | Lemonade Change | 860 | Easy | Greedy simulation |
| 2 | Maximum Subarray | 53 | Medium | Kadane's algorithm |
| 3 | Maximum Sum Circular Subarray | 918 | Medium | Kadane's + total - min subarray |
| 4 | Longest Turbulent Subarray | 978 | Medium | Kadane's variant |
| 5 | Jump Game | 55 | Medium | Greedy farthest reach |
| 6 | Jump Game II | 45 | Medium | Greedy BFS levels |
| 7 | Jump Game VII | 1871 | Medium | Sliding window + greedy |
| 8 | Gas Station | 134 | Medium | Single-pass greedy |
| 9 | Hand of Straights | 846 | Medium | Greedy + sorted map |
| 10 | Dota2 Senate | 649 | Medium | Greedy queue |
| 11 | Merge Triplets | 1899 | Medium | Greedy filtering |
| 12 | Partition Labels | 763 | Medium | Last occurrence greedy |
| 13 | Valid Parenthesis String | 678 | Medium | Greedy range tracking |
| 14 | Candy | 135 | Hard | Two-pass greedy |

---

## Greedy Problem Categories

```mermaid
graph TD
    G[Greedy Problems] --> SA[Subarray]
    G --> JMP[Jump Games]
    G --> SCH[Scheduling / Simulation]
    G --> PART[Partitioning]

    SA --> S1[Maximum Subarray #53]
    SA --> S2[Max Sum Circular #918]
    SA --> S3[Longest Turbulent #978]

    JMP --> J1[Jump Game #55]
    JMP --> J2[Jump Game II #45]
    JMP --> J3[Jump Game VII #1871]

    SCH --> SC1[Lemonade Change #860]
    SCH --> SC2[Gas Station #134]
    SCH --> SC3[Hand of Straights #846]
    SCH --> SC4[Dota2 Senate #649]
    SCH --> SC5[Candy #135]

    PART --> P1[Merge Triplets #1899]
    PART --> P2[Partition Labels #763]
    PART --> P3[Valid Parenthesis String #678]
```

---

## Kadane's Algorithm Flow

```mermaid
flowchart TD
    A["Start: maxSum = nums[0], cur = nums[0]"] --> B[For each num in nums from index 1]
    B --> C{"cur < 0?"}
    C -- Yes --> D[cur = num]
    C -- No --> E[cur = cur + num]
    D --> F[maxSum = max of maxSum and cur]
    E --> F
    F --> G{"More elements?"}
    G -- Yes --> B
    G -- No --> H[Return maxSum]

    style A fill:#2d6a4f,color:#fff
    style H fill:#1b4332,color:#fff
```

**Circular variant (LC 918):** `answer = max(maxSubarray, totalSum - minSubarray)`

---

## Jump Game Greedy Flow

```mermaid
flowchart TD
    A[Start: farthest = 0] --> B[For i = 0 to n-1]
    B --> C{"i > farthest?"}
    C -- Yes --> D[Return False — can't reach i]
    C -- No --> E[farthest = max of farthest and i + nums_i]
    E --> F{"i == n-1?"}
    F -- Yes --> G[Return True]
    F -- No --> B

    style D fill:#9b2226,color:#fff
    style G fill:#2d6a4f,color:#fff
```

**Jump Game II (LC 45):** Track current window end; when `i == windowEnd`, increment jumps and extend window to `farthest`.

---

## Gas Station Single-Pass Logic

```mermaid
flowchart TD
    A[total = 0, tank = 0, start = 0] --> B[For i = 0 to n-1]
    B --> C[gain = gas_i - cost_i]
    C --> D[total += gain, tank += gain]
    D --> E{"tank < 0?"}
    E -- Yes --> F[start = i + 1, tank = 0]
    E -- No --> G{"More stations?"}
    F --> G
    G -- Yes --> B
    G -- No --> H{"total >= 0?"}
    H -- Yes --> I[Return start]
    H -- No --> J[Return -1 — impossible]

    style I fill:#2d6a4f,color:#fff
    style J fill:#9b2226,color:#fff
```

---

## Partition Labels Algorithm Flow

```mermaid
flowchart TD
    A[Build last occurrence map for each char] --> B[size = 0, end = 0, result = empty]
    B --> C[For i, char in enumerate s]
    C --> D[end = max of end and last_char]
    D --> E[size += 1]
    E --> F{"i == end?"}
    F -- Yes --> G[Append size to result, size = 0]
    F -- No --> H{"More chars?"}
    G --> H
    H -- Yes --> C
    H -- No --> I[Return result]

    style A fill:#2d6a4f,color:#fff
    style I fill:#1b4332,color:#fff
```

---

## Complexity Summary

| Problem | Time | Space |
|---------|------|-------|
| Lemonade Change | O(n) | O(1) |
| Maximum Subarray | O(n) | O(1) |
| Max Sum Circular | O(n) | O(1) |
| Longest Turbulent | O(n) | O(1) |
| Jump Game | O(n) | O(1) |
| Jump Game II | O(n) | O(1) |
| Jump Game VII | O(n) | O(n) |
| Gas Station | O(n) | O(1) |
| Hand of Straights | O(n log n) | O(n) |
| Dota2 Senate | O(n) | O(n) |
| Merge Triplets | O(n) | O(1) |
| Partition Labels | O(n) | O(1) |
| Valid Parenthesis String | O(n) | O(1) |
| Candy | O(n) | O(n) |

---

## Study Order

1. **Lemonade Change** — warm-up greedy simulation
2. **Maximum Subarray** — master Kadane's
3. **Max Sum Circular Subarray** — Kadane's variant
4. **Longest Turbulent Subarray** — Kadane's with conditions
5. **Jump Game** — greedy farthest reach
6. **Jump Game II** — greedy BFS levels
7. **Jump Game VII** — sliding window + greedy
8. **Gas Station** — single-pass invariant
9. **Partition Labels** — last occurrence greedy
10. **Valid Parenthesis String** — greedy range
11. **Merge Triplets** — greedy filtering
12. **Hand of Straights** — sorted map greedy
13. **Dota2 Senate** — queue-based greedy
14. **Candy** — two-pass hard greedy
