# Stack

## Problem List

| # | Problem | Difficulty | Category |
|---|---------|------------|----------|
| 1 | [Baseball Game (LC 682)](https://leetcode.com/problems/baseball-game/) | Easy | Simulation |
| 2 | [Valid Parentheses (LC 20)](https://leetcode.com/problems/valid-parentheses/) | Easy | Matching |
| 3 | [Implement Stack Using Queues (LC 225)](https://leetcode.com/problems/implement-stack-using-queues/) | Easy | Design |
| 4 | [Implement Queue using Stacks (LC 232)](https://leetcode.com/problems/implement-queue-using-stacks/) | Easy | Design |
| 5 | [Min Stack (LC 155)](https://leetcode.com/problems/min-stack/) | Medium | Design |
| 6 | [Evaluate Reverse Polish Notation (LC 150)](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | Simulation |
| 7 | [Asteroid Collision (LC 735)](https://leetcode.com/problems/asteroid-collision/) | Medium | Simulation |
| 8 | [Daily Temperatures (LC 739)](https://leetcode.com/problems/daily-temperatures/) | Medium | Monotonic |
| 9 | [Online Stock Span (LC 901)](https://leetcode.com/problems/online-stock-span/) | Medium | Monotonic |
| 10 | [Car Fleet (LC 853)](https://leetcode.com/problems/car-fleet/) | Medium | Monotonic |
| 11 | [Simplify Path (LC 71)](https://leetcode.com/problems/simplify-path/) | Medium | Simulation |
| 12 | [Decode String (LC 394)](https://leetcode.com/problems/decode-string/) | Medium | Simulation |
| 13 | [Maximum Frequency Stack (LC 895)](https://leetcode.com/problems/maximum-frequency-stack/) | Hard | Design |
| 14 | [Largest Rectangle In Histogram (LC 84)](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | Monotonic |

---

## Mermaid Diagrams

### 1. Stack Problem Categories

```mermaid
mindmap
  root((Stack))
    Matching
      Valid Parentheses LC20
    Monotonic
      Daily Temperatures LC739
      Online Stock Span LC901
      Car Fleet LC853
      Largest Rectangle LC84
    Simulation
      Baseball Game LC682
      Evaluate RPN LC150
      Asteroid Collision LC735
      Simplify Path LC71
      Decode String LC394
    Design
      Implement Stack LC225
      Implement Queue LC232
      Min Stack LC155
      Max Freq Stack LC895
```

### 2. Monotonic Stack Pattern (Next Greater/Smaller)

```mermaid
flowchart TD
    A[For each element arr-i] --> B{"Stack not empty AND condition met?"}
    B -->|Next Greater: arr-i > stack.top| C[Pop top<br>result-top = i]
    B -->|Next Smaller: arr-i < stack.top| C
    C --> B
    B -->|Condition not met| D[Push i onto stack]
    D --> E[Next element]
    E --> A
    D --> F{"End of array?"}
    F -->|Yes, remaining in stack| G[No next greater/smaller<br>result = -1 or 0]
```

### 3. Parentheses Matching Flow (LC 20)

```mermaid
flowchart TD
    A[Read char c] --> B{"c is opening bracket?"}
    B -->|Yes| C[Push c onto stack]
    B -->|No - closing bracket| D{"Stack empty?"}
    D -->|Yes| E[Return False]
    D -->|No| F{"stack.top matches c?"}
    F -->|Yes| G[Pop stack]
    F -->|No| E
    G --> H[Next char]
    C --> H
    H --> I{"More chars?"}
    I -->|Yes| A
    I -->|No| J{"Stack empty?"}
    J -->|Yes| K[Return True]
    J -->|No| E
```

### 4. Stack vs Queue Decision

```mermaid
flowchart TD
    A[Need temporary storage?] --> B{"Access order?"}
    B -->|Last In First Out<br>Undo, backtrack, nested| C[Stack]
    B -->|First In First Out<br>BFS, scheduling, order| D[Queue]
    C --> C1[Monotonic problems<br>Matching brackets<br>Expression eval]
    D --> D1[BFS traversal<br>Sliding window<br>Task scheduling]
    C --> C2{"Need O-1 min/max?"}
    C2 -->|Yes| C3[Auxiliary stack<br>Min Stack LC155]
    C2 -->|No| C4[Regular stack]
```

---

## Complexity Summary

| Problem | Time | Space | Key Insight |
|---------|------|-------|-------------|
| LC 682 | O(n) | O(n) | Simulate with stack |
| LC 20 | O(n) | O(n) | Push open, match close |
| LC 225 | O(n) push | O(n) | Rotate queue on push |
| LC 232 | O(1) amortized | O(n) | Two stacks: in/out |
| LC 155 | O(1) all | O(n) | Stack of (val, curMin) pairs |
| LC 150 | O(n) | O(n) | Push nums, pop on operator |
| LC 735 | O(n) | O(n) | Positive right, negative left |
| LC 739 | O(n) | O(n) | Monotonic decreasing stack |
| LC 901 | O(1) amortized | O(n) | Monotonic non-increasing |
| LC 853 | O(n log n) | O(n) | Sort by pos, stack arrival times |
| LC 71 | O(n) | O(n) | Split on `/`, handle `..` |
| LC 394 | O(n) | O(n) | Stack of (string, count) |
| LC 895 | O(1) all | O(n) | freq map + group stacks |
| LC 84 | O(n) | O(n) | Monotonic increasing stack |

---

## Study Order

```mermaid
flowchart LR
    A[LC 20<br>Matching] --> B[LC 682<br>Simulation]
    B --> C[LC 225 / 232<br>Design Basics]
    C --> D[LC 155<br>Min Stack]
    D --> E[LC 150<br>RPN]
    E --> F[LC 739<br>Monotonic]
    F --> G[LC 901<br>Stock Span]
    G --> H[LC 735<br>Collision]
    H --> I[LC 853<br>Car Fleet]
    I --> J[LC 394<br>Decode]
    J --> K[LC 84<br>Histogram]
    K --> L[LC 895<br>Freq Stack]
```

**Recommended order:** Matching → Simulation → Design → Monotonic → Hard
