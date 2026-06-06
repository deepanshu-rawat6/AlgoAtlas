"""
# LC 706: Design HashMap

Design a HashMap without using any built-in hash table libraries.

Implement `MyHashMap`:
- `put(key, value)` — Inserts a `(key, value)` pair. Updates value if key exists.
- `get(key)` — Returns the value mapped to `key`, or `-1` if not present.
- `remove(key)` — Removes the `key` and its value if present.

## Examples

```text
Input:
  ["MyHashMap","put","put","get","get","put","get","remove","get"]
  [[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]
Output:
  [null,null,null,1,-1,null,1,null,-1]
```

## Constraints
- 0 <= key, value <= 10^6
- At most 10^4 calls will be made to put, get, and remove.
"""


# Approach 1: Array-based — O(1) time | O(10^6) space
class MyHashMap:
    def __init__(self):
        self.data = [-1] * (10**6 + 1)

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key]

    def remove(self, key: int) -> None:
        self.data[key] = -1


# Approach 2: Chaining with lists of (key, value) pairs — O(1) avg time | O(n) space
class MyHashMapChaining:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        h = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[h]):
            if k == key:
                self.buckets[h][i] = (key, value)
                return
        self.buckets[h].append((key, value))

    def get(self, key: int) -> int:
        for k, v in self.buckets[self._hash(key)]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        h = self._hash(key)
        self.buckets[h] = [(k, v) for k, v in self.buckets[h] if k != key]


if __name__ == "__main__":
    hm = MyHashMap()
    hm.put(1, 1)
    hm.put(2, 2)
    assert hm.get(1) == 1
    assert hm.get(3) == -1
    hm.put(2, 1)
    assert hm.get(2) == 1
    hm.remove(2)
    assert hm.get(2) == -1
    print("All tests passed.")
