# Design HashSet (LC 705)

Implement a HashSet without built-in hash table libraries, supporting `add(key)`,
`remove(key)`, and `contains(key)`.

## Approaches

### 1. Boolean Array — O(1) time, O(10⁶) space
Allocate a boolean array of size 10⁶+1. `add` sets index to True, `remove` sets to False, `contains` reads the index.

**Why it works:** Keys are bounded integers (0 to 10⁶), so the key is a direct index. All operations are O(1) with zero collision handling.

### 2. Chaining — O(1) average time, O(n) space
Hash key to a bucket (`key % size`). Each bucket holds a list of keys. Scan on collision.

**Why it works:** Distributes keys across buckets. Membership check, add, and remove all scan the small bucket list — O(1) average with a good hash and low load factor.

## Key Insight
Same as HashMap but storing presence/absence instead of a value. Direct array is optimal for bounded integer keys.

## Edge Cases
- `add` the same key twice → idempotent, still contains it once
- `remove` a key not in the set → no-op
- `contains` on never-added key → false
- Key = 0 (valid boundary case)
