"""
LC 981 - Time Based Key-Value Store
=====================================

Design a time-based key-value data structure that can store multiple values
for the same key at different time stamps and retrieve the key's value at a
certain timestamp.

Implement the TimeMap class:
  - TimeMap() Initializes the object of the data structure.
  - void set(String key, String value, int timestamp) Stores the key with the
    value at the given time timestamp.
  - String get(String key, int timestamp) Returns a value such that set was
    called previously with timestamp_prev <= timestamp. If there are multiple
    such values, it returns the value associated with the largest
    timestamp_prev. If there are no values, it returns "".

Examples
--------
```text
Input:
  ["TimeMap","set","get","get","set","get","get"]
  [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output:
  [null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation:
  set("foo","bar",1)  -> stores foo=bar at t=1
  get("foo",1)        -> "bar"
  get("foo",3)        -> "bar"  (largest ts <= 3 is 1)
  set("foo","bar2",4) -> stores foo=bar2 at t=4
  get("foo",4)        -> "bar2"
  get("foo",5)        -> "bar2" (largest ts <= 5 is 4)
```

Constraints
-----------
- 1 <= key.length, value.length <= 100
- key and value consist of lowercase English letters and digits
- 1 <= timestamp <= 10^7
- All calls to set will have strictly increasing timestamp values
- At most 2 * 10^5 calls will be made to set and get
"""

import bisect
from collections import defaultdict


class TimeMapLinear:
    """Approach 1: linear scan — O(n) per get."""

    def __init__(self):
        self.store: dict = defaultdict(list)  # key -> [(ts, val)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append (timestamp, value) to the list for this key — timestamps are increasing
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Binary search for the largest timestamp <= given timestamp
        # bisect_right finds insertion point; step back one to get the floor
        # O(n) time | O(1) space per call
        result = ""
        for ts, val in self.store[key]:
            if ts <= timestamp:
                result = val
        return result


class TimeMap:
    """Approach 2: binary search — O(log n) per get."""

    def __init__(self):
        self.store: dict = defaultdict(list)  # key -> [(ts, val)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append (timestamp, value) to the list for this key — timestamps are increasing
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Binary search for the largest timestamp <= given timestamp
        # bisect_right finds insertion point; step back one to get the floor
        # O(log n) time | O(1) space per call
        entries = self.store[key]
        idx = bisect.bisect_right(entries, (timestamp, chr(127))) - 1
        return entries[idx][1] if idx >= 0 else ""


if __name__ == "__main__":
    for Cls in (TimeMapLinear, TimeMap):
        tm = Cls()
        tm.set("foo", "bar", 1)
        assert tm.get("foo", 1) == "bar"
        assert tm.get("foo", 3) == "bar"
        tm.set("foo", "bar2", 4)
        assert tm.get("foo", 4) == "bar2"
        assert tm.get("foo", 5) == "bar2"
        assert tm.get("foo", 0) == ""

    print("All tests passed.")
