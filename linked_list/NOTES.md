# Linked List — Pattern Notes

## Core Intuition

Linked list problems reduce to a small set of pointer manipulation techniques. The key is **drawing pointer state before and after** each operation. Most bugs come from losing a reference before saving it.

### Dummy Head Pattern
Use a sentinel node (`dummy = ListNode(0)`) whenever you are building or merging a list. It eliminates the special case of inserting at the head and lets you return `dummy.next` cleanly. Always pair with a `cur` pointer that walks forward while `dummy` stays fixed.

```python
dummy = ListNode(0)
cur = dummy
# ... attach nodes to cur.next, then cur = cur.next
return dummy.next
```

### Fast / Slow Pointer
Two pointers at different speeds reveal structural properties without a second pass:
- **Cycle detection**: if `fast` and `slow` meet, a cycle exists; if `fast` reaches `None`, no cycle.
- **Middle finding**: when `fast` reaches the end, `slow` is at the middle. For even-length lists, slow lands on the first of the two middle nodes.
- **Nth from end**: advance `fast` by n first, then move both at the same speed; when `fast` hits `None`, `slow.next` is the target (use a dummy to handle head removal).

```python
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### Reversal
In-place iterative reversal is O(n) time, O(1) space. Track three pointers: `prev`, `cur`, and the saved `next`.

```python
prev, cur = None, head
while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
# prev is the new head
```

Using a stack is O(n) space — reach for it only when the reversal logic is recursive (e.g., reverse-k-group recursion) or when you need a copy. Partial reversal (Reverse II, K-Group) requires finding the left boundary first, then reversing a segment, then reconnecting both ends.

### Design Problems (LRU, LFU, Circular Queue)
These separate two concerns: the data structure invariant (ordering, frequency tracking) and the linked list wiring (O(1) insert/delete). LRU uses a doubly-linked list ordered by recency plus a hashmap from key to node. LFU adds a second layer: a hashmap from frequency to a doubly-linked list of nodes at that frequency, plus a `min_freq` tracker. The DLL always gets sentinel head and tail nodes.

### Merge Patterns
- **Two lists**: single dummy head, compare front nodes, attach the smaller, advance. Attach any remaining tail with `cur.next = l1 or l2`.
- **K lists**: min-heap of `(val, tiebreaker_idx, node)` gives O(N log k). Divide-and-conquer (pair-wise merge rounds) also achieves O(N log k) with O(log k) stack space instead of O(k) heap space.

---

## Java Idioms

### ListNode definition
Define package-private in the same file — no need for `public`:

```java
class ListNode { int val; ListNode next; ListNode(int v) { val = v; } }
```

### Dummy head for build / merge
```java
ListNode dummy = new ListNode(0);
ListNode cur = dummy;
// attach nodes; return dummy.next
```

### Fast / slow pointers
```java
ListNode slow = head, fast = head;
while (fast != null && fast.next != null) {
    slow = slow.next;
    fast = fast.next.next;
}
```

### Floyd's cycle detection guard
Always check both before advancing:
```java
if (fast == null || fast.next == null) return false; // no cycle
```

### LRU with LinkedHashMap (access-ordered)
```java
LinkedHashMap<Integer, Integer> cache = new LinkedHashMap<>(capacity, 0.75f, true) {
    protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
        return size() > capacity;
    }
};
```
The third constructor argument `true` enables access-order (get moves the entry to the tail). `removeEldestEntry` fires on every `put`.

### Merge-K heap (Java)
```java
PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
```
Add the head of each non-null list; pop, attach, push `node.next` if non-null.

### In-place reversal (Java)
```java
ListNode prev = null, cur = head;
while (cur != null) {
    ListNode next = cur.next;
    cur.next = prev;
    prev = cur;
    cur = next;
}
// prev is new head
```

### Copy list with random pointer
HashMap approach is cleaner (two passes: create all copies, then wire `.next` and `.random`). The interleave approach (`A → A' → B → B' → ...`) avoids the HashMap but is harder to follow — use HashMap unless space is the explicit constraint.

---

## Decision Guide

```
Linked List Problem
│
├─ Reverse or rearrange?
│   ├─ Full reversal → iterative prev/cur/next, O(1) space
│   ├─ Partial reversal → advance to left boundary, reverse segment, reconnect
│   └─ K-group → check k nodes remain first; recurse or iterate
│
├─ Detect cycle / find position?
│   └─ Fast/slow: cycle → do they meet?
│                 middle → slow at n//2 when fast ends
│                 nth from end → gap-of-n trick with dummy
│
├─ Merge sorted lists?
│   ├─ Two lists → dummy head + merge loop
│   └─ K lists → min-heap (O(N log k), O(k)) or divide-and-conquer (O(log k) stack)
│
└─ Design cache / queue?
    ├─ LRU → HashMap + DLL (or OrderedDict / LinkedHashMap)
    ├─ LFU → HashMap + freq buckets each a DLL + min_freq tracker
    └─ Circular Queue → array + head/tail indices + size counter
```

---

## Per-Problem Notes

| Problem | LC | Key Insight | Tricky Part | Common Mistakes | Time | Space |
|---------|-----|-------------|-------------|-----------------|------|-------|
| Reverse Linked List | 206 | `prev=None, cur=head`; save next, flip, advance | None — straightforward | Losing `cur.next` before reassigning | O(n) | O(1) |
| Merge Two Sorted Lists | 21 | Dummy head; compare heads, attach smaller, advance | Attach remaining non-null tail with `cur.next = l1 or l2` | Forgetting to attach remaining tail | O(m+n) | O(1) |
| Linked List Cycle | 141 | Floyd's: fast=2x, slow=1x; meet → cycle; fast=null → no cycle | Guard `fast and fast.next` before each advance | Checking equality before first advance | O(n) | O(1) |
| Add Two Numbers | 2 | Simulate addition digit by digit with carry; both lists treated as 0 when exhausted | Emit a final carry node after both lists end | Forgetting the last carry; misaligned list lengths | O(max(m,n)) | O(max(m,n)) |
| Remove Nth From End | 19 | Gap of n between fast and slow (dummy enables head removal); remove `slow.next` | Dummy head makes the "remove head" case uniform | Removing `slow` instead of `slow.next`; forgetting dummy for head | O(n) | O(1) |
| Reorder List | 143 | (1) find middle via slow/fast, (2) reverse second half, (3) interleave | Sever the first half from second before reversing or you get a cycle | Not cutting the link between halves; off-by-one on middle | O(n) | O(1) |
| Copy List with Random Pointer | 138 | HashMap `{original: copy}`; pass 1 creates all nodes, pass 2 wires `.next`/`.random` | One-pass fails because `.random` target may not exist yet | Trying to wire in one pass; forgetting `.random = None` case | O(n) | O(n) |
| Find the Duplicate Number | 287 | Treat array values as next-pointers; Floyd's cycle entrance = duplicate | Phase 2: reset one pointer to index 0, both move 1x until meeting | Confusing it with sort/set approach (need O(1) space) | O(n) | O(1) |
| Reverse Linked List II | 92 | Advance to node before `left`; reverse the segment; reconnect both ends | Save the node just before `left` and the `left` node itself (becomes new tail) | Losing the node after `right`; not saving `prev_left` | O(n) | O(1) |
| Design Circular Queue | 622 | Array + `head`, `tail`, `size`; `tail = (tail+1) % cap` on enqueue | Use a `size` counter for full/empty; avoids off-by-one with indices alone | Off-by-one full/empty; not handling wrap-around | O(1) all ops | O(n) |
| LRU Cache | 146 | HashMap + DLL (or OrderedDict); `get` moves node to MRU end; `put` evicts LRU on overflow | DLL needs sentinel head and tail to avoid null checks | Not moving existing key on `get`; not updating value on `put` before checking capacity | O(1) get/put | O(cap) |
| LFU Cache | 460 | `key→val`, `key→freq`, `freq→OrderedDict`; track `min_freq` | `min_freq` resets to 1 only on a new key insert, not on updates | `min_freq` not reset; forgetting to delete old freq bucket | O(1) get/put | O(cap) |
| Merge K Sorted Lists | 23 | Min-heap `(val, idx, node)`; pop min, push `node.next` | Heap breaks on equal vals without `idx` tiebreaker | Heap comparison error on equal vals; pushing null nodes | O(N log k) | O(k) |
| Reverse Nodes in K-Group | 25 | Check k nodes remain first; reverse k; connect tail to recursive/iterative result | In iterative form, track `group_prev` and `group_next` across iterations | Not checking k nodes remain; losing the tail of the reversed segment | O(n) | O(n/k) recursion, O(1) iterative |

---

## Edge Cases to Watch

- **Empty list (`head == null`)**: most operations should return early; heap-based merge must skip null list heads.
- **Single-node list**: cycle detection still works; reversal is a no-op; middle-finding returns the only node.
- **Cycle back to head**: Floyd's still detects it; phase 2 (finding entrance) works correctly because the math holds regardless of where the cycle starts.
- **Even vs. odd length for middle-finding**: with `while fast and fast.next`, slow lands on the first middle for even-length lists. If you need the second middle (for Reorder List), step slow one more time or change the condition.
- **k > remaining nodes in Reverse K-Group**: the k-node check must fail gracefully and leave the remainder untouched — this is the termination condition, not an error.
- **Random pointer pointing to null or to the node itself**: handle `None` case explicitly when copying; `node.random = map[node.random]` works only after a null-guard.
- **`left == right` in Reverse II**: the segment is one node — no pointer changes needed; ensure the code does not corrupt the list.
- **All lists empty in Merge K**: input may be `[]` or `[None, None]`; skip null heads when pushing to the heap.
