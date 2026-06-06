import heapq
from typing import List


class MedianFinder:
    """
    ## 295. Find Median from Data Stream

    The **median** is the middle value in an ordered integer list. If the size of the list is even,
    there is no middle value, and the median is the mean of the two middle values.

    Implement the `MedianFinder` class:
    - `MedianFinder()` — initializes the `MedianFinder` object.
    - `void addNum(int num)` — adds the integer `num` from the data stream to the data structure.
    - `double findMedian()` — returns the median of all elements so far. Answers within `10^-5`
      of the actual answer will be accepted.

    ### Examples

    ```text
    Input:
        MedianFinder mf = new MedianFinder();
        mf.addNum(1);
        mf.addNum(2);
        mf.findMedian(); // 1.5
        mf.addNum(3);
        mf.findMedian(); // 2.0
    ```

    ### Constraints
    - `-10^5 <= num <= 10^5`
    - There will be at least one element in the data structure before calling `findMedian`.
    - At most `5 * 10^4` calls will be made to `addNum` and `findMedian`.
    """

    # --- Approach 1: Sort on every findMedian ---

    class _SortApproach:
        def __init__(self):
            self.data: List[int] = []

        def addNum(self, num: int) -> None:
            # Push to max-heap (lower half); rebalance if max of lower > min of upper
            # Keep sizes balanced: small can have at most 1 more element than large
            # O(1) amortized append
            import bisect
            bisect.insort(self.data, num)

        def findMedian(self) -> float:
            # Odd total: median is top of larger heap; even: average of both tops
            # O(1) — data kept sorted via insort
            n = len(self.data)
            return self.data[n // 2] if n % 2 else (self.data[n // 2 - 1] + self.data[n // 2]) / 2.0

    # --- Approach 2: Two heaps ---

    def __init__(self):
        # O(1) init
        self.small: List[int] = []  # max-heap (negated) — lower half
        self.large: List[int] = []  # min-heap — upper half

    def addNum(self, num: int) -> None:
        # Push to max-heap (lower half); rebalance if max of lower > min of upper
        # Keep sizes balanced: small can have at most 1 more element than large
        # O(log n) — push to max-heap, rebalance
        heapq.heappush(self.small, -num)
        # Ensure every element in small <= every element in large
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        # Balance sizes: small can have at most 1 more than large
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # Odd total: median is top of larger heap; even: average of both tops
        # O(1) — peek tops of both heaps
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0

    mf2 = MedianFinder()
    mf2.addNum(-1)
    assert mf2.findMedian() == -1.0
    mf2.addNum(-2)
    assert mf2.findMedian() == -1.5
    mf2.addNum(-3)
    assert mf2.findMedian() == -2.0
    mf2.addNum(-4)
    assert mf2.findMedian() == -2.5
    mf2.addNum(-5)
    assert mf2.findMedian() == -3.0

    print("All tests passed.")
