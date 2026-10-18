# Heap — Pattern Notes

## Core Intuition

A heap gives you O(log n) insert and O(1) peek at the min (or max). Use it whenever you need to **repeatedly extract the current best** from a dynamic set. Python only has `heapq` (min-heap) — negate values for max-heap.

Sub-patterns:

- **Top-K** — maintain a heap of size K; push and pop to keep only K best
  - K-th largest → min-heap of size K (heap top is the answer; smallest of the K largest)
  - K-th smallest → max-heap of size K (negate in Python)
  - Rule: use the *opposite* heap type — it evicts the worst of the K candidates on overflow
- **Two Heaps** — max-heap (lower half) + min-heap (upper half) → O(1) median
  - Always push to max-heap first, then rebalance toward min-heap if needed
  - Invariant: `len(lo) == len(hi)` (even total) or `len(lo) == len(hi) + 1` (odd total)
  - Median: odd → `-lo[0]`; even → `(-lo[0] + hi[0]) / 2.0`
- **Greedy + Heap** — sort by one dimension, use heap to greedily pick best on another
  - Always process the best available option at each step (IPO: max profit among affordable projects)
  - Task Scheduler: always schedule the most frequent task that isn't on cooldown
- **Event Simulation / Merge-K** — push all starting events/heads; pop by priority; push successors
  - Start with one element per list; after each pop push the next element from that list

---

## Java Idioms

```java
// Min-heap (default) — smallest element at head
PriorityQueue<Integer> minHeap = new PriorityQueue<>();

// Max-heap — largest element at head
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

// Pairs sorted by first element ascending (e.g., [distance, index])
PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);

// Pairs sorted by second element descending (e.g., [index, profit])
PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[1] - a[1]);

// Safe comparator for large values — avoids integer overflow
PriorityQueue<Integer> safe = new PriorityQueue<>((a, b) -> Integer.compare(a, b));

// Core operations
pq.offer(x);   // add element — O(log n)
pq.poll();     // remove and return head — O(log n); throws NoSuchElementException if empty
pq.peek();     // view head without removing — O(1); returns null if empty
pq.size();     // current element count

// K-largest with min-heap of size k
for (int x : nums) {
    minHeap.offer(x);
    if (minHeap.size() > k) minHeap.poll();  // evict smallest, keeping k largest
}
int kthLargest = minHeap.peek();

// Two-heap median (Java)
PriorityQueue<Integer> lo = new PriorityQueue<>(Collections.reverseOrder()); // max-heap, lower half
PriorityQueue<Integer> hi = new PriorityQueue<>();                            // min-heap, upper half

void addNum(int num) {
    lo.offer(num);
    hi.offer(lo.poll());          // always route through lo first
    if (lo.size() < hi.size())    // rebalance: lo must not be smaller
        lo.offer(hi.poll());
}

double findMedian() {
    return lo.size() > hi.size() ? lo.peek() : (lo.peek() + hi.peek()) / 2.0;
}
```

---

## Decision Diagram

```
Heap Problem
  |
  +-- K largest / K smallest?
  |     --> min-heap size K (for K largest) | max-heap size K (for K smallest)
  |
  +-- Running / dynamic median?
  |     --> Two heaps: max-heap left half, min-heap right half, balance on insert
  |
  +-- Schedule / assign tasks greedily?
  |     --> Sort input by one key; heap tracks best available on other key
  |
  +-- Simulate events / merge sorted lists?
        --> Push heads/events; pop smallest; push successor
```

---

## Per-Problem Notes

| Problem | Key Insight | Tricky Part | Common Mistakes | Time | Space |
|---------|-------------|-------------|-----------------|------|-------|
| Kth Largest in Stream (703) | Min-heap of size K; `heap[0]` is always the K-th largest | Pop when `size > K`, not `size >= K` | Popping too early or too late; forgetting to maintain size K | O(log k) add / O(k) init | O(k) |
| Last Stone Weight (1046) | Max-heap (negate); pop two heaviest, push difference if nonzero | Must check heap has >= 2 stones before popping pair | Forgetting to push back when stones aren't equal | O(n log n) | O(n) |
| K Closest Points (973) | Min-heap by squared distance; pop K times. Or max-heap of size K | Squared distance avoids float sqrt; still correct for comparison | Using `sqrt` (unnecessary); building full heap then popping n-k | O(n log k) | O(k) |
| Kth Largest in Array (215) | Min-heap of size K; `heap[0]` after all inserts. Quickselect for O(n) avg | Quickselect target index = `len - k` in sorted-ascending array | Using max-heap and popping n-k times (correct but O(n log n)) | O(n log k) heap / O(n) avg quickselect | O(k) |
| Task Scheduler (621) | Greedy: schedule most-frequent available task; cooldown queue by (available_time, -count) | Idle time: jump to earliest available task when CPU is free | Not handling CPU idle; forgetting to put tasks back after cooldown | O(n log n) | O(n) |
| Design Twitter (355) | Per-user tweet list; `getNewsFeed` merges followee lists with max-heap of (timestamp, user, idx) | Limit to 10 tweets; use negative timestamp for max-heap via negation | Not limiting to 10; heap comparison failing on equal timestamps without tiebreaker | O(f log f) per getNewsFeed | O(n) total tweets |
| Single-Threaded CPU (1834) | Sort tasks by enqueue time; min-heap of (processing_time, idx); simulate time jumps | When CPU is idle, jump `time` to next task's enqueue time | Not jumping time forward when no task is ready | O(n log n) | O(n) |
| Reorganize String (767) | Max-heap by frequency; place most frequent, hold previous char one step then re-add | Re-add previous char only after placing the current one | Placing same char twice; not re-adding char with remaining count > 0 | O(n log k) k=26 | O(k) |
| Longest Happy String (1405) | Same greedy as Reorganize String but allow up to 2 consecutive; switch to 2nd-most-frequent when top would make 3 | Track last two chars placed; fallback to second-most-frequent | Not switching when top would violate constraint; off-by-one on run length | O(n log k) | O(k) |
| Car Pooling (1094) | Event simulation: (time, delta_passengers) pairs; sort by time; drop-off before pick-up at same stop | At same timestamp, process drop-offs (negative delta) before pick-ups | Handling drop-off/pick-up at same stop in wrong order | O(n log n) | O(n) |
| Find Median from Stream (295) | Two heaps: max-heap `lo` (lower half) + min-heap `hi` (upper half); always push to `lo` first | Rebalance: cross-heap if `lo` top > `hi` top; then size-balance | Not rebalancing after each insert; wrong median formula for even/odd sizes | O(log n) add / O(1) median | O(n) |
| IPO (502) | Sort projects by capital; greedily unlock affordable projects into max-heap by profit; pick top K times | Re-scan newly affordable projects after each pick by advancing sorted pointer | Not re-checking newly affordable projects; sorting by wrong key | O(n log n) | O(n) |

---

## Algorithm Skeletons

**Top-K (Python)**
```python
import heapq

def top_k_largest(nums, k):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)   # evict smallest; heap stays size k
    return heap[0]               # k-th largest
```

**Two Heaps — Running Median (Python)**
```python
import heapq

lo, hi = [], []   # lo: max-heap (negated), hi: min-heap

def add_num(num):
    heapq.heappush(lo, -num)
    if lo and hi and -lo[0] > hi[0]:
        heapq.heappush(hi, -heapq.heappop(lo))
    if len(lo) > len(hi) + 1:
        heapq.heappush(hi, -heapq.heappop(lo))
    elif len(hi) > len(lo):
        heapq.heappush(lo, -heapq.heappop(hi))

def find_median():
    if len(lo) > len(hi):
        return float(-lo[0])
    return (-lo[0] + hi[0]) / 2.0
```

**Greedy + Heap — IPO pattern (Python)**
```python
import heapq

def greedy_pick(projects, k, w):
    # projects: list of (capital, profit)
    projects.sort()               # sort by capital ascending
    available = []                # max-heap of profits (negated)
    i = 0
    for _ in range(k):
        while i < len(projects) and projects[i][0] <= w:
            heapq.heappush(available, -projects[i][1])
            i += 1
        if not available:
            break
        w += -heapq.heappop(available)
    return w
```

**Merge-K Sorted Lists pattern (Python)**
```python
import heapq

def merge_k(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # (value, list_idx, elem_idx)
    result = []
    while heap:
        val, li, ei = heapq.heappop(heap)
        result.append(val)
        if ei + 1 < len(lists[li]):
            heapq.heappush(heap, (lists[li][ei + 1], li, ei + 1))
    return result
```

---

## Edge Cases to Watch

- Empty heap — `heapq.heappop([])` raises `IndexError`; Java `pq.poll()` returns `null`, `pq.remove()` throws `NoSuchElementException`. Always guard with `if heap:` or check size.
- Heap of size K — pop when `size > k`, not `>= k`. Off-by-one here changes which element is evicted.
- Two-heap balance off-by-one — when total count is odd, `lo` must have exactly one more element than `hi`; forgetting the size-balance step after the cross-heap swap causes wrong medians.
- Ties in priority — if two elements compare equal on the first key, Python will compare the second key automatically (tuples); Java comparators must include a tiebreaker or the heap is inconsistent.
- Integer overflow in comparator — `(a, b) -> a - b` overflows when `a` is large positive and `b` is large negative. Use `Integer.compare(a, b)` always for safety.
- Negative frequencies or counts — when negating for max-heap, `cnt + 1` (not `cnt - 1`) decrements the negated count. Getting the sign wrong silently corrupts heap order.
- Reorganize / Longest Happy impossible — when `max_freq > (n + 1) // 2`, no valid arrangement exists; detect before running the greedy loop.
- Car Pooling same-stop order — at the same timestamp, process drop-offs before pick-ups; failing to do so can make passenger count exceed capacity momentarily even when the trip is valid.
