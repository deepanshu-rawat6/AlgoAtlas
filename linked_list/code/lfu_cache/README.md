# LFU Cache (LC 460)

Design a Least Frequently Used cache with O(1) average `get` and `put`. On eviction, remove the least frequently used key; break ties by least recently used.

## Approaches

### 1. Three Hash Maps + OrderedDict per Frequency
- **Time:** O(1) average | **Space:** O(capacity)
- `key_val`: maps key → value.
- `key_freq`: maps key → current frequency.
- `freq_keys`: maps frequency → `OrderedDict` of keys in insertion order (LRU within same frequency).
- `min_freq`: tracks the current minimum frequency.
- **get**: call `_update(key)` to increment frequency, return value.
- **put**: if key exists, update value and frequency. If at capacity, evict `freq_keys[min_freq].popitem(last=False)` (oldest at min frequency). Insert new key with freq=1, set `min_freq = 1`.

## Key Insight

`OrderedDict` per frequency bucket gives O(1) LRU eviction within a frequency group (`popitem(last=False)` removes the oldest). `min_freq` is maintained by: incrementing when a key's frequency increases (if that was the only key at `min_freq`), and resetting to 1 on any new insertion. `min_freq` can only increase by 1 at a time (via `_update`) or reset to 1 (via new insert).

## Edge Cases

- `capacity = 0`: all `put` calls are no-ops; `get` always returns -1.
- `get` on non-existent key → return -1.
- Eviction tie-breaking: `OrderedDict` preserves insertion order; `popitem(last=False)` removes the LRU key at `min_freq`.
- Updating an existing key's value: frequency still increments (it's an access).
