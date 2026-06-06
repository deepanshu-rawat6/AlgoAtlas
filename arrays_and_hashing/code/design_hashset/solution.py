"""
# LC 705: Design HashSet

Design a HashSet without using any built-in hash table libraries.

Implement `MyHashSet`:
- `add(key)` — Inserts the value `key` into the HashSet.
- `remove(key)` — Removes the value `key` in the HashSet. If `key` does not exist, do nothing.
- `contains(key)` — Returns whether the value `key` exists in the HashSet or not.

## Examples

```text
Input:
  ["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]
  [[],[1],[2],[1],[3],[2],[2],[2],[2]]
Output:
  [null,null,null,true,false,null,true,null,false]
```

## Constraints
- 0 <= key <= 10^6
- At most 10^4 calls will be made to add, remove, and contains.
"""


# Approach 1: Boolean array — O(1) time | O(10^6) space
class MyHashSet:
    def __init__(self):
        self.data = [False] * (10**6 + 1)

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]


# Approach 2: Chaining with lists — O(1) avg time | O(n) space
class MyHashSetChaining:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        h = self._hash(key)
        if key not in self.buckets[h]:
            self.buckets[h].append(key)

    def remove(self, key: int) -> None:
        h = self._hash(key)
        if key in self.buckets[h]:
            self.buckets[h].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets[self._hash(key)]


if __name__ == "__main__":
    hs = MyHashSet()
    hs.add(1)
    hs.add(2)
    assert hs.contains(1) == True
    assert hs.contains(3) == False
    hs.add(2)
    assert hs.contains(2) == True
    hs.remove(2)
    assert hs.contains(2) == False
    print("All tests passed.")
