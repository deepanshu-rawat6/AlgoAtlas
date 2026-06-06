"""
# 146. LRU Cache

## Problem
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity): Initialize the LRU cache with positive size capacity.
- int get(int key): Return the value of the key if it exists, otherwise return -1.
- void put(int key, int value): Update the value of the key if it exists. Otherwise,
  add the key-value pair to the cache. If the number of keys exceeds the capacity,
  evict the least recently used key.

Both get and put must run in O(1) average time complexity.

## Examples

```text
Input:
  LRUCache(2)
  put(1, 1)       cache: {1=1}
  put(2, 2)       cache: {1=1, 2=2}
  get(1)   -> 1   cache: {2=2, 1=1}
  put(3, 3)       evicts key 2, cache: {1=1, 3=3}
  get(2)   -> -1
  put(4, 4)       evicts key 1, cache: {3=3, 4=4}
  get(1)   -> -1
  get(3)   -> 3
  get(4)   -> 4
```

## Constraints
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.
"""
from collections import OrderedDict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(vals):
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def list_to_arr(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


# ── Approach 1: OrderedDict ──────────────────────────────────────────────────

class LRUCache_OrderedDict:
    # O(1) time per get/put, O(capacity) space
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        # Move accessed node to tail (most recently used), return its value
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # If key exists, remove old node; insert new node at tail
        # If over capacity, evict the LRU node at head.next
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)


# ── Approach 2: Doubly linked list + hash map ────────────────────────────────

class _DNode:
    __slots__ = ('key', 'val', 'prev', 'next')
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    # O(1) time per get/put, O(capacity) space
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head = _DNode()   # dummy head (LRU end)
        self.tail = _DNode()   # dummy tail (MRU end)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: _DNode) -> None:
        # Unlink node from doubly linked list by connecting its neighbors
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_tail(self, node: _DNode) -> None:
        # Insert node just before the dummy tail (most recently used position)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        # Move accessed node to tail (most recently used), return its value
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._insert_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # If key exists, remove old node; insert new node at tail
        # If over capacity, evict the LRU node at head.next
        if key in self.map:
            self._remove(self.map[key])
        node = _DNode(key, value)
        self.map[key] = node
        self._insert_tail(node)
        if len(self.map) > self.cap:
            lru = self.head.next
            self._remove(lru)
            del self.map[lru.key]


if __name__ == '__main__':
    for Cache in (LRUCache_OrderedDict, LRUCache):
        c = Cache(2)
        c.put(1, 1)
        c.put(2, 2)
        assert c.get(1) == 1
        c.put(3, 3)
        assert c.get(2) == -1
        c.put(4, 4)
        assert c.get(1) == -1
        assert c.get(3) == 3
        assert c.get(4) == 4

    print("All tests passed.")
