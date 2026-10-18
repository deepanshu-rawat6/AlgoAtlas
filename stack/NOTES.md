# Stack — Pattern Notes

## Core Intuition
A stack is the right tool when you need to **defer a decision** until you see a future element, or when you need to **undo/match** the most recent thing seen. LIFO naturally models nested structure and "nearest previous element" queries.

Sub-patterns:

- **Matching/Balancing** — push open bracket; on close, pop and validate compatibility. End check: stack must be empty. Applies to valid parentheses, decode string (push entire state on `[`).

- **Monotonic Stack** — maintain a stack whose elements stay in increasing or decreasing order by popping whenever the invariant breaks. Each pop resolves one "nearest" query in O(1) amortized.
  - Use a *decreasing* stack (pop when current > top) to find the **next greater element** — daily temperatures, online stock span.
  - Use an *increasing* stack (pop when current < top) to find the **next smaller element** or compute areas bounded below — largest rectangle in histogram.
  - Store **indices**, not values, whenever you need distance or width. The value is `arr[index]`.

- **Simulation** — stack as scratch space for stateful, ordered operations: baseball game (undo with `C`), simplify path (navigate with `..`), asteroid collision (resolve destruction left-to-right).

- **Expression Evaluation** — RPN uses a single operand stack (pop two, apply operator, push result). Infix needs a separate operator stack (or convert to postfix first).

- **Design** — augment a plain stack with extra state:
  - Min stack: track running minimum alongside each pushed value.
  - Frequency stack: `freq` map + `group` map indexed by frequency; pop always targets `max_freq` group.
  - Queue using stacks: two stacks (inbox / outbox); lazy transfer only when outbox drains.

---

## Decision Guide

Ask these questions in order:

1. Does the problem ask for the **nearest greater/smaller** element to the left or right? → Monotonic stack. Decreasing for next-greater, increasing for next-smaller.
2. Does the problem involve **matching open/close pairs** or **nested structure**? → Push on open, pop and validate on close.
3. Does the problem need to **undo or revisit** the last operation? → Plain stack as scratch.
4. Does the problem need **O(1) min/max alongside push/pop**? → Augmented stack storing running extremum per frame.
5. Does the problem need **O(1) push/pop by frequency rank**? → Frequency stack (freq map + group map).
6. Does the problem need a **queue but only stacks are allowed**? → Two stacks, lazy transfer.

---

## Python Skeletons

**Monotonic decreasing (next greater element):**

```python
stack = []  # indices
result = [0] * n
for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        idx = stack.pop()
        result[idx] = i - idx  # or arr[i] for value
    stack.append(i)
```

**Matching/balancing:**

```python
pairs = {')': '(', ']': '[', '}': '{'}
stack = []
for ch in s:
    if ch in '([{':
        stack.append(ch)
    elif not stack or stack[-1] != pairs[ch]:
        return False
    else:
        stack.pop()
return len(stack) == 0
```

**Min stack (pair approach):**

```python
stack = []  # [(val, current_min)]
def push(val):
    cur_min = min(val, stack[-1][1]) if stack else val
    stack.append((val, cur_min))
def get_min():
    return stack[-1][1]
```

---

## Java Idioms

**Never use `Stack<T>`.** It extends `Vector`, is synchronized on every operation, and has the wrong performance profile. Use `ArrayDeque` instead.

```java
// Stack semantics
Deque<Integer> stack = new ArrayDeque<>();
stack.push(x);      // addFirst — O(1)
stack.pop();        // removeFirst — O(1)
stack.peek();       // peekFirst — O(1)

// Queue semantics (same class, different end)
Deque<Integer> queue = new ArrayDeque<>();
queue.offerLast(x); // enqueue — O(1)
queue.pollFirst();  // dequeue — O(1)
```

`ArrayDeque` is the right default for both stacks and queues. Pick the end you use; the class handles both.

**Monotonic stack skeleton (Java):**

```java
Deque<Integer> mono = new ArrayDeque<>();
for (int i = 0; i < n; i++) {
    // Decreasing: pop while top is smaller than current (next-greater pattern)
    while (!mono.isEmpty() && arr[mono.peek()] < arr[i]) {
        int idx = mono.pop();
        // arr[idx]'s next greater element is at i; distance = i - idx
    }
    mono.push(i);  // always store index, not value
}
```

Swap `<` for `>` to get a next-smaller / increasing-stack variant.

**Store indices, not values**, whenever you need distance or width. `arr[mono.peek()]` gives the value; the index gives span or gap.

**Min stack (Java pair approach):**

```java
Deque<int[]> stack = new ArrayDeque<>();
// push: [val, currentMin]
int newMin = stack.isEmpty() ? val : Math.min(val, stack.peek()[1]);
stack.push(new int[]{val, newMin});
// getMin: stack.peek()[1]
```

**Frequency stack (Java):**

```java
Map<Integer, Integer> freq = new HashMap<>();
Map<Integer, Deque<Integer>> group = new HashMap<>();
int maxFreq = 0;

// push
freq.merge(val, 1, Integer::sum);
int f = freq.get(val);
maxFreq = Math.max(maxFreq, f);
group.computeIfAbsent(f, k -> new ArrayDeque<>()).push(val);

// pop
int val = group.get(maxFreq).pop();
freq.merge(val, -1, Integer::sum);
if (group.get(maxFreq).isEmpty()) maxFreq--;
```

---

## Per-Problem Notes

| Problem | Key Insight | Tricky Part | Common Mistakes | Time | Space |
|---------|-------------|-------------|-----------------|------|-------|
| Baseball Game (682) | Simulation: `C`=pop, `D`=double top, `+`=sum top two, else push int | `+` does NOT pop the two values it reads | Treating `+` as destructive | O(n) | O(n) |
| Valid Parentheses (20) | Push open; on close pop and check match against closer map | Stack may be empty when a close arrives; stack may be non-empty at end | Forgetting end-of-string empty check | O(n) | O(n) |
| Implement Stack Using Queues (225) | Costly-push: rotate entire queue after each push so front = top | Single queue is sufficient; no need for two | Using two queues unnecessarily | O(n) push, O(1) pop | O(n) |
| Implement Queue Using Stacks (232) | Inbox/outbox; transfer only when outbox is empty (lazy) | Transfer is O(n) worst case but each element moves at most once | Transferring on every dequeue | O(1) amortized | O(n) |
| Min Stack (155) | Each stack frame stores `[val, currentMin]`; min is always at peek | Single global `min` variable breaks when the minimum is popped | Using a separate unsynced min variable | O(1) all ops | O(n) |
| Evaluate RPN (150) | Single operand stack; pop two on operator; push result | Operand order matters: `b op a` where `a = stack.pop()` first, `b = stack.pop()` second | Reversed operand order for `-` and `/`; Python `//` rounds toward −∞, use `int(a/b)` | O(n) | O(n) |
| Asteroid Collision (735) | Positive → push; negative → destroy positives on top in a loop; equal-size → both gone | Negative asteroid survives only after destroying everything on stack; still push if stack empty or top is negative | Missing inner loop; equal-size explosion | O(n) | O(n) |
| Daily Temperatures (739) | Monotonic decreasing stack of **indices**; pop when current temp > stack top | Distance = `i - popped_index`; only possible if indices are stored | Storing temperatures instead of indices | O(n) | O(n) |
| Online Stock Span (901) | Stack of `(price, span)`; when top price ≤ current, absorb its span and pop | Accumulated span, not just count of pops | Counting pops instead of summing spans | O(1) amortized | O(n) |
| Car Fleet (853) | Sort by position descending; compute `time = (target - pos) / speed`; if time ≤ top of stack it merges, else push | Equal times also merge (same fleet) | Sorting ascending; missing the equal-time merge | O(n log n) | O(n) |
| Simplify Path (71) | Split on `/`; skip empty strings and `.`; pop on `..`; push everything else | Multiple consecutive slashes produce empty tokens (skip them); leading `/` must be re-added | Not handling `..` at root; missing leading slash in output | O(n) | O(n) |
| Decode String (394) | Two stacks: one for repeat counts, one for string prefixes; on `[` push state; on `]` pop and repeat | Multi-digit numbers require accumulating digits before pushing | Treating multi-digit numbers as single digits; off-by-one on bracket matching | O(n·k) | O(n) |
| Maximum Frequency Stack (895) | `freq` map + `group` map (freq → stack of vals); `maxFreq` tracks current peak | `maxFreq` decrements only when its group becomes empty after a pop | Forgetting to decrement `maxFreq`; not handling tie-breaking (recency already handled by stack order within group) | O(1) push/pop | O(n) |
| Largest Rectangle in Histogram (84) | Monotonic increasing stack of `(start_index, height)`; when shorter bar arrives, pop and compute area = `height × (i - start_index)`; `start` carried back to leftmost extent | Width calculation: popped bar extends left to wherever it could have started, not just its original index | Not flushing remaining stack after loop; width off-by-one | O(n) | O(n) |

---

## Edge Cases to Watch

- **Empty stack pop** — always check `if stack` (Python) or `!stack.isEmpty()` (Java) before `pop()` / `peek()`. Applies everywhere: asteroid collision inner loop, RPN operators, close-bracket in valid parentheses.

- **All same elements in monotonic stack** — invariant never breaks during the loop, so the stack accumulates every element. These must be processed in a final flush pass after the loop (as in largest rectangle).

- **Nested brackets in decode_string** — each `[` must push the *entire current string* and the current count onto their respective stacks, not just a reference. Restoring state on `]` means popping both stacks and concatenating.

- **Negative numbers in asteroid_collision** — a right-moving (positive) asteroid followed by a left-moving (negative) one of the same magnitude: both are destroyed. A negative asteroid moving left when the stack is empty or the top is also negative: it survives and is pushed as-is.

- **Stack not empty at end means invalid** — for valid_parentheses, any unmatched open bracket left on the stack at the end of the string is an error. Return `len(stack) == 0`, not just whether a close mismatched.

- **Stack-as-queue amortized vs worst case** — implement_queue_using_stacks is O(1) *amortized* per dequeue, but a single dequeue after n pushes costs O(n). This is fine for interviews but matters for latency-sensitive code where worst-case matters more than average.

- **Path traversal past root** — in simplify_path, `..` on an empty stack should be a no-op, not an error. The result is still `/`.

- **Sentinel trick in histogram** — appending a `0` height sentinel to `heights` before iterating lets you flush the stack in one pass without a separate post-loop sweep. The trade-off: slightly less obvious code for simpler loop structure.
