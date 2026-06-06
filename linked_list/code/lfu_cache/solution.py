"""
# 460. LFU Cache

## Problem
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:
- LFUCache(int capacity): Initializes the object with the capacity of the data structure.
- int get(int key): Gets the value of the key if it exists in the cache. Otherwise, returns -1.
- void put(int key, int value): Update the value of the key if present, or inserts the key
  if not already present. When the cache reaches its capacity, it should invalidate and remove
  the least frequently used key before inserting a new item. For ties, the least recently used
  key among the least frequently used keys is removed.

Both get and put must run in O(1) average time complexity.

## Examples

```text
Input:
  LFUCache(2)
  put(1, 1)       freq: {1:1}
  put(2, 2)       freq: {1:1, 2:1}
  get(1)   -> 1   freq: {1:2, 2:1}
  put(3, 3)       evicts key 2, freq: {1:2, 3:1}
  get(2)   -> -1
  get(3)   -> 3   freq: {1:2, 3:2}
  put(4, 4)       evicts key 3 (or 1, both freq=2; 3 is LRU), freq: {1:2, 4:1}
  get(1)   -> 1
  get(3)   -> -1
  get(4)   -> 4
```

## Constraints
- 0 <= capacity <= 10^4
- 0 <= key <= 10^5
- 0 <= value <= 10^9
- At most 2 * 10^5 calls will be made to get and put.
"""
from collections import defaultdict, OrderedDict


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


class LFUCache:
    # O(1) time per get/put — hash maps + OrderedDict per frequency bucket

    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_freq = 0
        self.key_val = {}                          # key -> value
        self.key_freq = {}                         # key -> frequency
        self.freq_keys = defaultdict(OrderedDict)  # freq -> OrderedDict of keys (LRU order)

    def _update(self, key: int) -> None:
        freq = self.key_freq[key]
        del self.freq_keys[freq][key]
        if not self.freq_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        self.key_freq[key] = freq + 1
        self.freq_keys[freq + 1][key] = None

    def get(self, key: int) -> int:
        # Increment frequency of key, move to higher-freq bucket, return value
        if key not in self.key_val:
            return -1
        self._update(key)
        return self.key_val[key]

    def put(self, key: int, value: int) -> None:
        # If key exists, update value and increment frequency
        # If at capacity, evict the LFU key (least frequent, then least recent)
        # Insert new key with frequency 1; update min_freq to 1
        if self.cap == 0:
            return
        if key in self.key_val:
            self.key_val[key] = value
            self._update(key)
        else:
            if len(self.key_val) >= self.cap:
                evict_key, _ = self.freq_keys[self.min_freq].popitem(last=False)
                del self.key_val[evict_key]
                del self.key_freq[evict_key]
            self.key_val[key] = value
            self.key_freq[key] = 1
            self.freq_keys[1][key] = None
            self.min_freq = 1


if __name__ == '__main__':
    # Trace: cap=2
    # put(1,1): {1:v1,f1}  min=1
    # put(2,2): {1:v1,f1, 2:v2,f1}  min=1
    # get(1)->1: {1:v1,f2, 2:v2,f1}  min=1
    # put(3,3): evict LRU at min_freq=1 -> evict key 2; {1:v1,f2, 3:v3,f1}  min=1
    # get(2)->-1
    # get(3)->3: {1:v1,f2, 3:v3,f2}  min=2
    # put(4,4): evict LRU at min_freq=2 -> evict key 1 (inserted before 3 reached f2)
    #           {3:v3,f2, 4:v4,f1}  min=1
    # get(1)->-1, get(3)->3, get(4)->4
    c = LFUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1
    assert c.get(3) == 3
    c.put(4, 4)
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4

    c2 = LFUCache(0)
    c2.put(0, 0)
    assert c2.get(0) == -1

    print("All tests passed.")
