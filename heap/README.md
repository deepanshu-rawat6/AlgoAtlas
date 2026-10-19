# Heap / Priority Queue

```mermaid
mindmap
  root((Heap))
    Top-K
      Kth Largest Element In a Stream LC703
      K Closest Points to Origin LC973
      Kth Largest Element In An Array LC215
    Two Heaps
      Find Median From Data Stream LC295
      IPO LC502
    Greedy + Heap
      Reorganize String LC767
      Longest Happy String LC1405
      Task Scheduler LC621
    Event Simulation
      Single Threaded CPU LC1834
      Car Pooling LC1094
    Design
      Design Twitter LC355
```

## Problem List

| # | Problem | LC | Difficulty |
|---|---------|-----|------------|
| 1 | Kth Largest Element In a Stream | [703](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | 🟢 Easy |
| 2 | Last Stone Weight | [1046](https://leetcode.com/problems/last-stone-weight/) | 🟢 Easy |
| 3 | K Closest Points to Origin | [973](https://leetcode.com/problems/k-closest-points-to-origin/) | 🟡 Medium |
| 4 | Kth Largest Element In An Array | [215](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 🟡 Medium |
| 5 | Task Scheduler | [621](https://leetcode.com/problems/task-scheduler/) | 🟡 Medium |
| 6 | Design Twitter | [355](https://leetcode.com/problems/design-twitter/) | 🟡 Medium |
| 7 | Single Threaded CPU | [1834](https://leetcode.com/problems/single-threaded-cpu/) | 🟡 Medium |
| 8 | Reorganize String | [767](https://leetcode.com/problems/reorganize-string/) | 🟡 Medium |
| 9 | Longest Happy String | [1405](https://leetcode.com/problems/longest-happy-string/) | 🟡 Medium |
| 10 | Car Pooling | [1094](https://leetcode.com/problems/car-pooling/) | 🟡 Medium |
| 11 | Find Median From Data Stream | [295](https://leetcode.com/problems/find-median-from-data-stream/) | 🔴 Hard |
| 12 | IPO | [502](https://leetcode.com/problems/ipo/) | 🔴 Hard |

---

## Approach Diagrams

### Min Heap vs Max Heap Decision

```mermaid
flowchart TD
    A[Heap Problem] --> B{"What do you need?"}
    B -- Kth largest or top-K smallest --> C[Min Heap of size K heapq in Python]
    B -- Kth smallest or top-K largest --> D[Max Heap of size K negate values in Python]
    B -- Always need smallest next --> E[Min Heap LC 1834 CPU, 1094 Car Pooling]
    B -- Always need largest next --> F[Max Heap LC 1046 Last Stone, 767 Reorganize]
    B -- Need both halves --> G[Two Heaps LC 295 Median]
```

### Top-K Pattern Flow

```mermaid
flowchart TD
    A[Find Top-K elements] --> B[Use Min Heap of size K]
    B --> C[For each element x]
    C --> D{"heap size < K?"}
    D -- Yes --> E[Push x]
    D -- No --> F{"x > heap top?"}
    F -- Yes --> G[Pop min, push x]
    F -- No --> H[Skip]
    E --> C
    G --> C
    H --> C
    C --> I[Heap contains K largest]
    I --> J[LC 703, 215, 973]
```

### Two Heaps Pattern — Median Finding

```mermaid
flowchart TD
    A[Add number n] --> B{"n <= max_heap top?"}
    B -- Yes --> C[Push to max_heap lower half]
    B -- No --> D[Push to min_heap upper half]
    C --> E{"Balance heaps size diff > 1?"}
    D --> E
    E -- max_heap bigger --> F[Move top of max_heap to min_heap]
    E -- min_heap bigger --> G[Move top of min_heap to max_heap]
    E -- balanced --> H[Done]
    F --> I[Get Median]
    G --> I
    H --> I
    I --> J{"Equal sizes?"}
    J -- Yes --> K[avg of both tops]
    J -- No --> L[top of larger heap]
```

### Greedy + Heap Pattern

```mermaid
flowchart TD
    A[Greedy + Heap Problems] --> B{"Pattern type"}
    B -- Always pick most frequent --> C[Max Heap by frequency LC 767 Reorganize, 1405 Happy String]
    C --> D[Pop max freq char append to result decrement and re-push]
    B -- Unlock tasks by capital --> E[Two heaps: available vs locked LC 502 IPO]
    E --> F[Min heap on cost Max heap on profit Unlock affordable, pick best profit]
    B -- Cooldown scheduling --> G[Max heap + cooldown queue LC 621 Task Scheduler]
    G --> H[Pop most frequent wait cooldown re-add to heap]
```

### Event-Driven Simulation with Heap

```mermaid
flowchart TD
    A[Event Simulation] --> B[Sort events by start time]
    B --> C[Min heap tracks active events by end time or priority]
    C --> D[Process next event]
    D --> E{"Any events ended before current start?"}
    E -- Yes --> F[Pop from heap free resources]
    E -- No --> G[All slots busy]
    F --> H[Assign to freed slot]
    G --> I[Wait / queue]
    H --> J[Push new end time to heap]
    I --> J
    J --> D
    D --> K[LC 1834 CPU, 1094 Car Pooling]
```

---

## Complexity Summary

| Problem | Time | Space | Pattern |
|---------|------|-------|---------|
| Kth Largest in Stream (703) | O(log k) per add | O(k) | Min heap size k |
| Last Stone Weight (1046) | O(n log n) | O(n) | Max heap |
| K Closest Points (973) | O(n log k) | O(k) | Min heap size k |
| Kth Largest in Array (215) | O(n log k) | O(k) | Min heap size k |
| Task Scheduler (621) | O(n log n) | O(n) | Max heap + cooldown |
| Design Twitter (355) | O(k log n) per feed | O(n) | Min heap merge |
| Single Threaded CPU (1834) | O(n log n) | O(n) | Min heap by duration |
| Reorganize String (767) | O(n log k) | O(k) | Max heap by freq |
| Longest Happy String (1405) | O(n log k) | O(k) | Max heap by freq |
| Car Pooling (1094) | O(n log n) | O(n) | Min heap by dropoff |
| Find Median (295) | O(log n) add, O(1) query | O(n) | Two heaps |
| IPO (502) | O(n log n) | O(n) | Two heaps |

---

## Study Order

```mermaid
flowchart LR
    W1["Week 1: Heap Basics 703 → 1046 → 215 → 973"]
    W2["Week 2: Greedy + Heap 767 → 1405 → 621 → 502"]
    W3["Week 3: Simulation 355 → 1834 → 1094"]
    W4["Week 4: Hard 295"]
    W1 --> W2 --> W3 --> W4
```

**Key insight:** Python only has `heapq` (min heap). For max heap, negate values. For top-K largest, maintain a min heap of size K — if new element beats the min, swap it in.
