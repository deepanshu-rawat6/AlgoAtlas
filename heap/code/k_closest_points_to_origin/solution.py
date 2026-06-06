import heapq
import random
from typing import List


class Solution:
    """
    ## 973. K Closest Points to Origin

    Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane
    and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

    The distance between two points on the X-Y plane is the Euclidean distance:
    `sqrt((x1 - x2)^2 + (y1 - y2)^2)`.

    You may return the answer in **any order**. The answer is **guaranteed** to be unique
    (except for the order that it is in).

    ### Examples

    ```text
    Input: points = [[1, 3], [-2, 2]], k = 1
    Output: [[-2, 2]]

    Explanation:
        Distance of [1,3] from origin = sqrt(10) ≈ 3.16
        Distance of [-2,2] from origin = sqrt(8) ≈ 2.83
        [-2,2] is closer, so return [[-2,2]].
    ```

    ```text
    Input: points = [[3, 3], [5, -1], [-2, 4]], k = 2
    Output: [[3, 3], [-2, 4]]
    ```

    ### Constraints
    - `1 <= k <= points.length <= 10^4`
    - `-10^4 <= xi, yi <= 10^4`
    """

    def kClosest_sort(self, points: List[List[int]], k: int) -> List[List[int]]:
        # O(n log n) — sort all points by squared distance
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:k]

    def kClosest_heap(self, points: List[List[int]], k: int) -> List[List[int]]:
        # O(n log k) — max-heap of size k using negated distances
        heap: List = []
        for x, y in points:
            dist = -(x * x + y * y)
            heapq.heappush(heap, (dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for _, x, y in heap]

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use max-heap of size k; evict farthest point when heap exceeds k
        # No need to sort — heap maintains k closest points
        # O(n) average — quickselect partitioning by squared distance
        def dist(p):
            return p[0] ** 2 + p[1] ** 2

        def partition(lo, hi):
            pivot = dist(points[hi])
            i = lo
            for j in range(lo, hi):
                if dist(points[j]) <= pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[hi] = points[hi], points[i]
            return i

        lo, hi = 0, len(points) - 1
        while lo < hi:
            mid = partition(lo, hi)
            if mid == k - 1:
                break
            elif mid < k - 1:
                lo = mid + 1
            else:
                hi = mid - 1
        return points[:k]


if __name__ == '__main__':
    s = Solution()

    res = s.kClosest_sort([[1, 3], [-2, 2]], 1)
    assert res == [[-2, 2]]

    res = s.kClosest_heap([[1, 3], [-2, 2]], 1)
    assert sorted(res) == [[-2, 2]]

    res = s.kClosest([[1, 3], [-2, 2]], 1)
    assert res == [[-2, 2]]

    res = s.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
    assert sorted(res) == [[-2, 4], [3, 3]]

    print("All tests passed.")
