# Design HashMap (LC 706)

Implement a HashMap without built-in hash table libraries, supporting `put(key, value)`,
`get(key)` (returns -1 if absent), and `remove(key)`.

## Approaches

### 1. Direct Array — O(1) time, O(10⁶) space
Allocate an array of size 10⁶+1 initialized to -1. Use the key directly as the index.

**Why it works:** Keys are bounded integers (0 to 10⁶), so the key itself is a perfect index. All operations are O(1) with no collisions, at the cost of large fixed memory.

### 2. Chaining — O(1) average time, O(n) space
Hash key to a bucket index (`key % size`). Each bucket holds a list of `(key, value)` pairs. Scan the list on collision.

**Why it works:** Distributes keys across buckets to reduce memory. Collisions are resolved by linear scan within the bucket — O(1) average when load factor is low.

## Key Insight
Direct array is the simplest O(1) solution when key range is small and bounded. Chaining is the real-world approach that scales to arbitrary key types.

## Edge Cases
- `get` on a key that was never inserted → return -1
- `put` on an existing key → update value, don't duplicate
- `remove` on a non-existent key → no-op
- Key = 0 (valid, must be handled)
