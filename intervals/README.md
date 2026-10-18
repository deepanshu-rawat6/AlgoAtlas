# Intervals

```mermaid
mindmap
  root((Intervals))
    Merge/Insert
      Merge Intervals LC56
      Insert Interval LC57
    Scheduling Rooms
      Meeting Rooms LC252
      Meeting Rooms II LC253
      Meeting Rooms III LC2402
    Sweep Line
      Non-Overlapping Intervals LC435
    Query-Based
      Minimum Interval to Include Each Query LC1851
```

## Problem List

| # | Problem | LC # | Difficulty | Key Technique |
|---|---------|------|------------|---------------|
| 1 | Insert Interval | 57 | Medium | Linear scan + merge |
| 2 | Merge Intervals | 56 | Medium | Sort + merge |
| 3 | Non-Overlapping Intervals | 435 | Medium | Greedy scheduling |
| 4 | Meeting Rooms | 252 | Easy | Sort + check overlap |
| 5 | Meeting Rooms II | 253 | Medium | Min-heap |
| 6 | Meeting Rooms III | 2402 | Hard | Two heaps |
| 7 | Minimum Interval to Include Each Query | 1851 | Hard | Sort + heap + offline queries |

---

## Interval Problem Decision Tree

```mermaid
flowchart TD
    A[Interval Problem] --> B{"What is asked?"}
    B --> C[Merge / Insert]
    B --> D[Count rooms / resources]
    B --> E[Remove minimum intervals]
    B --> F[Answer queries]

    C --> C1[Sort by start, linear merge]
    C --> C2[Insert Interval #57 — binary search + merge]

    D --> D1[Sort by start, min-heap on end times]
    D1 --> D2[Meeting Rooms II #253]
    D1 --> D3[Meeting Rooms III #2402 — two heaps]

    E --> E1[Sort by end, greedy keep earliest end]
    E1 --> E2[Non-Overlapping Intervals #435]

    F --> F1[Offline: sort queries + sweep with heap]
    F1 --> F2[Min Interval per Query #1851]
```

---

## Merge Intervals Algorithm Flow

```mermaid
flowchart TD
    A[Sort intervals by start time] --> B[result = first interval]
    B --> C[For each remaining interval]
    C --> D{"current.start <= last.end?"}
    D -- Yes --> E[Merge: last.end = max of last.end and current.end]
    D -- No --> F[Append current to result as new interval]
    E --> G{"More intervals?"}
    F --> G
    G -- Yes --> C
    G -- No --> H[Return result]

    style A fill:#2d6a4f,color:#fff
    style H fill:#1b4332,color:#fff
```

---

## Sweep Line / Event-Based Approach

```mermaid
flowchart TD
    A[For each interval, emit start +1 and end -1 events] --> B[Sort all events by time]
    B --> C[active = 0, maxActive = 0]
    C --> D[For each event in order]
    D --> E[active += event.delta]
    E --> F[maxActive = max of maxActive and active]
    F --> G{"More events?"}
    G -- Yes --> D
    G -- No --> H[Return maxActive]

    style A fill:#2d6a4f,color:#fff
    style H fill:#1b4332,color:#fff
```

*Used for: counting max concurrent meetings (Meeting Rooms II alternative)*

---

## Meeting Rooms Heap Approach

```mermaid
flowchart TD
    A[Sort meetings by start time] --> B[min-heap = empty, rooms = 0]
    B --> C[For each meeting start, end]
    C --> D{"heap not empty AND heap.top <= start?"}
    D -- Yes --> E[Pop earliest ending room — reuse it]
    D -- No --> F[No room free — allocate new room]
    E --> G[Push end time to heap]
    F --> G
    G --> H{"More meetings?"}
    H -- Yes --> C
    H -- No --> I[Return heap size = rooms needed]

    style A fill:#2d6a4f,color:#fff
    style I fill:#1b4332,color:#fff
```

---

## Interval Overlap Detection Logic

```mermaid
flowchart TD
    A[Two intervals A = a1,a2 and B = b1,b2] --> B{"Do they overlap?"}
    B --> C["Overlap condition: a1 <= b2 AND b1 <= a2"]
    C --> D{"True?"}
    D -- Yes --> E[Overlapping — merged = min a1 b1, max a2 b2]
    D -- No --> F[Non-overlapping — keep separate]

    E --> G[Use for: Merge Intervals, Insert Interval]
    F --> H[Use for: Non-Overlapping — count removals]

    style E fill:#2d6a4f,color:#fff
    style F fill:#9b2226,color:#fff
```

---

## Complexity Summary

| Problem | Time | Space |
|---------|------|-------|
| Insert Interval | O(n) | O(n) |
| Merge Intervals | O(n log n) | O(n) |
| Non-Overlapping Intervals | O(n log n) | O(1) |
| Meeting Rooms | O(n log n) | O(1) |
| Meeting Rooms II | O(n log n) | O(n) |
| Meeting Rooms III | O(n log n) | O(n) |
| Min Interval per Query | O((n+q) log n) | O(n+q) |

---

## Study Order

1. **Meeting Rooms** — basic overlap check
2. **Merge Intervals** — core merge pattern
3. **Insert Interval** — merge with binary search
4. **Non-Overlapping Intervals** — greedy scheduling
5. **Meeting Rooms II** — heap for resource counting
6. **Meeting Rooms III** — two-heap advanced
7. **Minimum Interval per Query** — offline + heap
