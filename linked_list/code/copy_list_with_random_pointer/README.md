# Copy List with Random Pointer (LC 138)

Deep copy a linked list where each node has a `next` and a `random` pointer (which can point to any node or null).

## Approaches

### 1. Hash Map
- **Time:** O(n) | **Space:** O(n)
- First pass: create all new nodes and store `old → new` mapping.
- Second pass: wire up `next` and `random` pointers using the map.

### 2. Interleaving (O(1) Space)
- **Time:** O(n) | **Space:** O(1)
- **Step 1:** Interleave clones — insert each clone right after its original: `A → A' → B → B' → ...`
- **Step 2:** Set random pointers: `curr.next.random = curr.random.next` (clone's random = original's random's clone).
- **Step 3:** Separate the two lists, restoring the original and extracting the clone.

## Key Insight

The interleaving trick uses the list structure itself as the mapping: `original.next` is always the clone, so `curr.random.next` gives the clone of the random target — no hash map needed. The three-step process is careful to not break the interleaved structure until Step 3.

## Edge Cases

- `head = None` → return None.
- Node with `random = None` → skip random assignment (guarded by `if curr.random`).
- Node whose `random` points to itself → handled correctly by both approaches.
- All `random` pointers are None → just a standard deep copy.
