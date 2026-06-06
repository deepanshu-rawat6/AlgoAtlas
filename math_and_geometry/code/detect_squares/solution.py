"""
# 2013. Detect Squares

You are given a stream of points on the X-Y plane. Design an algorithm that:
- **Adds** new points from the stream into a data structure.
- **Counts** the number of ways to choose three points from the data structure such that the
  three points and a given query point form an **axis-aligned square** with **positive area**.

An axis-aligned square has all four sides parallel to the axes and all four sides equal in length.

Implement the `DetectSquares` class:
- `DetectSquares()` Initializes the object with an empty data structure.
- `void add(int[] point)` Adds a new point `point = [x, y]` to the data structure.
- `int count(int[] point)` Counts the number of ways to form axis-aligned squares with `point`.

## Examples

```text
Input:
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3,10]], [[11,2]], [[3,2]], [[11,10]], [[14,8]], [[11,2]], [[11,10]]]
Output:
[null, null, null, null, 1, 0, null, 2]
```

## Constraints
- point.length == 2
- 0 <= point[x], point[y] <= 1000
- At most 3000 calls will be made to add and count.
"""

from collections import defaultdict
from typing import List


class DetectSquares:
    def __init__(self):
        self.pt_count = defaultdict(int)   # (x,y) -> count
        self.x_to_ys = defaultdict(set)    # x -> set of y values

    def add(self, point: List[int]) -> None:
        # Increment count of this point in the frequency map
        # O(1) time — update frequency map and x->y index
        x, y = point
        self.pt_count[(x, y)] += 1
        self.x_to_ys[x].add(y)

    def count(self, point: List[int]) -> int:
        # For each point sharing the same x as query, try it as diagonal corner
        # The other two corners are determined; check if they exist in the map
        # O(n) time — for each diagonal point, check if square can be completed
        qx, qy = point
        result = 0
        for y in self.x_to_ys[qx]:
            if y == qy:
                continue
            side = abs(y - qy)
            for dx in (qx + side, qx - side):
                result += self.pt_count[(qx, y)] * self.pt_count[(dx, qy)] * self.pt_count[(dx, y)]
        return result


if __name__ == '__main__':
    ds = DetectSquares()
    ds.add([3, 10]); ds.add([11, 2]); ds.add([3, 2])
    assert ds.count([11, 10]) == 1
    assert ds.count([14, 8]) == 0
    ds.add([11, 2])
    assert ds.count([11, 10]) == 2
    print("All tests passed.")
