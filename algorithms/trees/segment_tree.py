"""
Segment Tree
============
A segment tree stores aggregate values (sum/min/max) over array intervals,
enabling both point updates and range queries in O(log n).

Use cases:
  - Range sum / min / max queries with point updates
  - Range updates with lazy propagation (e.g., add k to all elements in [l,r])

Complexity:
  Build:        O(n)
  Point update: O(log n)
  Range query:  O(log n)
  Range update (lazy): O(log n)
Space: O(4n) for the tree array
"""

from typing import List


class SegmentTree:
    """
    Generic segment tree supporting sum, min, max queries.
    Uses 1-indexed internal array of size 4*n.
    """

    def __init__(self, data: List[int], mode: str = "sum"):
        """
        mode: 'sum' | 'min' | 'max'
        """
        assert mode in ("sum", "min", "max")
        self.n = len(data)
        self.mode = mode
        self.tree = [0] * (4 * self.n)
        if data:
            self._build(data, 1, 0, self.n - 1)

    def _combine(self, a, b):
        if self.mode == "sum":
            return a + b
        if self.mode == "min":
            return min(a, b)
        return max(a, b)

    def _identity(self):
        if self.mode == "sum":
            return 0
        if self.mode == "min":
            return float('inf')
        return float('-inf')

    def _build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
            return
        mid = (start + end) // 2
        self._build(data, 2 * node, start, mid)
        self._build(data, 2 * node + 1, mid + 1, end)
        self.tree[node] = self._combine(self.tree[2 * node], self.tree[2 * node + 1])

    def update(self, idx: int, val: int):
        """Point update: set arr[idx] = val."""
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self._update(2 * node, start, mid, idx, val)
        else:
            self._update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = self._combine(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, l: int, r: int) -> int:
        """Range query over [l, r] (0-indexed, inclusive)."""
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:          # completely outside
            return self._identity()
        if l <= start and end <= r:       # completely inside
            return self.tree[node]
        mid = (start + end) // 2
        left  = self._query(2 * node, start, mid, l, r)
        right = self._query(2 * node + 1, mid + 1, end, l, r)
        return self._combine(left, right)


# ─── Lazy Propagation (range add + range sum) ─────────────────────────────────

class LazySegmentTree:
    """
    Supports range add updates and range sum queries in O(log n).

    Lazy array defers propagation: when we update a range, we store the
    pending addition in lazy[node] and only push it down when we need to
    access children.
    """

    def __init__(self, data: List[int]):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        if data:
            self._build(data, 1, 0, self.n - 1)

    def _build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
            return
        mid = (start + end) // 2
        self._build(data, 2 * node, start, mid)
        self._build(data, 2 * node + 1, mid + 1, end)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def _push_down(self, node, start, end):
        """Propagate pending lazy value to children."""
        if self.lazy[node] != 0:
            mid = (start + end) // 2
            left_len  = mid - start + 1
            right_len = end - mid
            self.tree[2 * node]     += self.lazy[node] * left_len
            self.tree[2 * node + 1] += self.lazy[node] * right_len
            self.lazy[2 * node]     += self.lazy[node]
            self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

    def range_add(self, l: int, r: int, val: int):
        """Add val to every element in [l, r]."""
        self._range_add(1, 0, self.n - 1, l, r, val)

    def _range_add(self, node, start, end, l, r, val):
        if r < start or end < l:
            return
        if l <= start and end <= r:
            self.tree[node] += val * (end - start + 1)
            self.lazy[node] += val
            return
        self._push_down(node, start, end)
        mid = (start + end) // 2
        self._range_add(2 * node, start, mid, l, r, val)
        self._range_add(2 * node + 1, mid + 1, end, l, r, val)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, l: int, r: int) -> int:
        """Range sum query over [l, r]."""
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        self._push_down(node, start, end)
        mid = (start + end) // 2
        return (self._query(2 * node, start, mid, l, r) +
                self._query(2 * node + 1, mid + 1, end, l, r))


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]

    # --- Sum segment tree ---
    st = SegmentTree(arr, mode="sum")
    print("Sum [1,3]:", st.query(1, 3))   # 3+5+7 = 15
    st.update(2, 10)                       # arr[2] = 10
    print("Sum [1,3] after update:", st.query(1, 3))  # 3+10+7 = 20

    # --- Min segment tree ---
    mn = SegmentTree(arr, mode="min")
    print("Min [0,4]:", mn.query(0, 4))   # 1

    # --- Max segment tree ---
    mx = SegmentTree(arr, mode="max")
    print("Max [2,5]:", mx.query(2, 5))   # 11

    # --- Lazy propagation ---
    lazy = LazySegmentTree([1, 2, 3, 4, 5])
    print("Sum [0,4]:", lazy.query(0, 4))  # 15
    lazy.range_add(1, 3, 10)              # add 10 to indices 1,2,3
    print("Sum [0,4] after range add:", lazy.query(0, 4))  # 15+30 = 45
    print("Sum [1,3]:", lazy.query(1, 3))  # 12+13+14 = 39
