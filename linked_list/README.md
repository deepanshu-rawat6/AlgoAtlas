# Linked List

## Problem List

| # | Problem | Difficulty | Technique |
|---|---------|------------|-----------|
| 1 | [Reverse Linked List (LC 206)](https://leetcode.com/problems/reverse-linked-list/) | Easy | Iterative/Recursive |
| 2 | [Merge Two Sorted Lists (LC 21)](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Two Pointer Merge |
| 3 | [Linked List Cycle (LC 141)](https://leetcode.com/problems/linked-list-cycle/) | Easy | Fast/Slow Pointer |
| 4 | [Reorder List (LC 143)](https://leetcode.com/problems/reorder-list/) | Medium | Find Mid + Reverse + Merge |
| 5 | [Remove Nth Node From End (LC 19)](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | Fast/Slow Pointer |
| 6 | [Copy List With Random Pointer (LC 138)](https://leetcode.com/problems/copy-list-with-random-pointer/) | Medium | HashMap |
| 7 | [Add Two Numbers (LC 2)](https://leetcode.com/problems/add-two-numbers/) | Medium | Carry Simulation |
| 8 | [Find The Duplicate Number (LC 287)](https://leetcode.com/problems/find-the-duplicate-number/) | Medium | Floyd's Cycle Detection |
| 9 | [Reverse Linked List II (LC 92)](https://leetcode.com/problems/reverse-linked-list-ii/) | Medium | In-place Reversal |
| 10 | [Design Circular Queue (LC 622)](https://leetcode.com/problems/design-circular-queue/) | Medium | Array + Pointers |
| 11 | [LRU Cache (LC 146)](https://leetcode.com/problems/lru-cache/) | Medium | DLL + HashMap |
| 12 | [LFU Cache (LC 460)](https://leetcode.com/problems/lfu-cache/) | Hard | Freq Map + DLL |
| 13 | [Merge K Sorted Lists (LC 23)](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | Min Heap |
| 14 | [Reverse Nodes In K Group (LC 25)](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Hard | In-place Group Reversal |

---

## Mermaid Diagrams

### 1. Linked List Operation Categories

```mermaid
mindmap
  root((Linked List))
    Traversal & Pointers
      Fast/Slow Pointer
        Cycle Detection LC141
        Remove Nth LC19
        Find Duplicate LC287
      Two Pointer Merge
        Merge Two Lists LC21
        Merge K Lists LC23
    Reversal
      Full Reverse LC206
      Partial Reverse LC92
      K-Group Reverse LC25
      Reorder List LC143
    Design
      Circular Queue LC622
      LRU Cache LC146
      LFU Cache LC460
    Misc
      Copy with Random LC138
      Add Two Numbers LC2
```

### 2. Fast/Slow Pointer Pattern

```mermaid
flowchart TD
    A([slow=head fast=head]) --> B{"fast and fast.next exist?"}
    B -->|Yes| C[slow = slow.next fast = fast.next.next]
    C --> D{"Cycle detection? slow == fast?"}
    D -->|Yes - cycle found| E[Floyd's: reset one to head move both by 1 to find entry]
    D -->|No| B
    B -->|No - fast reached end| F[slow = middle node Use for: find mid, remove nth]
    F --> G[LC 141 Cycle LC 19 Remove Nth LC 143 Reorder LC 287 Duplicate]
```

### 3. Reverse Linked List Iterative Flow (LC 206)

```mermaid
flowchart LR
    A([prev=None curr=head]) --> B{"curr != None?"}
    B -->|Yes| C[next_node = curr.next]
    C --> D[curr.next = prev]
    D --> E[prev = curr]
    E --> F[curr = next_node]
    F --> B
    B -->|No| G[Return prev new head]
```

### 4. Merge Pattern (LC 21 / LC 23)

```mermaid
flowchart TD
    A[Two sorted lists L1, L2] --> B{"L1.val <= L2.val?"}
    B -->|Yes| C[Append L1.val L1 = L1.next]
    B -->|No| D[Append L2.val L2 = L2.next]
    C --> E{"Both lists have nodes?"}
    D --> E
    E -->|Yes| B
    E -->|No| F[Append remaining list]
    F --> G[Return merged]

    H[K sorted lists] --> I[Use Min Heap push head of each list]
    I --> J[Pop min node push node.next if exists]
    J --> K{"Heap empty?"}
    K -->|No| J
    K -->|Yes| L[Return merged]
```

### 5. LRU Cache Architecture (DLL + HashMap)

```mermaid
flowchart TD
    subgraph HashMap
        M[key → node reference]
    end
    subgraph DLL [Doubly Linked List - MRU to LRU]
        H2[HEAD dummy] <-->|most recent| N1[node1]
        N1 <--> N2[node2]
        N2 <-->|least recent| T[TAIL dummy]
    end
    A[get-key] --> B{"key in map?"}
    B -->|Yes| C[Move node to HEAD Return val]
    B -->|No| D[Return -1]
    E[put-key,val] --> F{"key in map?"}
    F -->|Yes| G[Update val Move to HEAD]
    F -->|No| H[Create node Insert at HEAD Add to map]
    H --> I{"capacity exceeded?"}
    I -->|Yes| J[Remove TAIL.prev Delete from map]
```

---

## Complexity Summary

| Problem | Time | Space | Key Insight |
|---------|------|-------|-------------|
| LC 206 | O(n) | O(1) | Three pointer reversal |
| LC 21 | O(m+n) | O(1) | Dummy head simplifies |
| LC 141 | O(n) | O(1) | Floyd's tortoise & hare |
| LC 143 | O(n) | O(1) | Find mid → reverse → merge |
| LC 19 | O(n) | O(1) | Fast n+1 ahead of slow |
| LC 138 | O(n) | O(n) | Map old→new, then set random |
| LC 2 | O(max(m,n)) | O(1) | Carry through iteration |
| LC 287 | O(n) | O(1) | Array as linked list, Floyd's |
| LC 92 | O(n) | O(1) | Track prev of sublist start |
| LC 622 | O(1) all | O(k) | Circular index with modulo |
| LC 146 | O(1) all | O(n) | DLL + HashMap |
| LC 460 | O(1) all | O(n) | freq map + per-freq DLL |
| LC 23 | O(n log k) | O(k) | Min heap of k heads |
| LC 25 | O(n) | O(1) | Count k, reverse in-place |

---

## Study Order

```mermaid
flowchart LR
    A[LC 206 Reverse] --> B[LC 21 Merge Two]
    B --> C[LC 141 Cycle]
    C --> D[LC 19 Remove Nth]
    D --> E[LC 143 Reorder]
    E --> F[LC 92 Reverse II]
    F --> G[LC 2 Add Numbers]
    G --> H[LC 138 Copy Random]
    H --> I[LC 287 Duplicate]
    I --> J[LC 622 Circular Q]
    J --> K[LC 146 LRU Cache]
    K --> L[LC 23 Merge K]
    L --> M[LC 25 K-Group]
    M --> N[LC 460 LFU Cache]
```

**Recommended order:** Basic ops → Fast/slow pointer → In-place reversal → Design → Hard
