import heapq
from typing import List


class KthLargest:
    """
    ## 703. Kth Largest Element in a Stream

    Design a class to find the `k`th largest element in a stream.
    Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

    Implement the `KthLargest` class:
    - `KthLargest(int k, int[] nums)` — initializes the object with `k` and the stream `nums`.
    - `int add(int val)` — appends `val` to the stream and returns the element representing
      the `k`th largest element in the stream.

    ### Examples

    ```text
    Input:
        KthLargest(3, [4, 5, 8, 2])
        add(3) -> 4
        add(5) -> 5
        add(10) -> 8
        add(9) -> 8
        add(4) -> 8

    Explanation:
        After init: stream = [2, 4, 5, 8], k=3 → 3rd largest = 4
        add(3): stream = [2, 3, 4, 5, 8] → 3rd largest = 4
        add(5): stream = [2, 3, 4, 5, 5, 8] → 3rd largest = 5
    ```

    ### Constraints
    - `1 <= k <= 10^4`
    - `0 <= nums.length <= 10^4`
    - `-10^4 <= nums[i] <= 10^4`
    - `-10^4 <= val <= 10^4`
    - At most `10^4` calls to `add`
    - It is guaranteed that there will be at least `k` elements in the array when `add` is called.
    """

    # --- Approach 1: Sort on every add ---

    def __init__sort(self, k: int, nums: List[int]):
        # O(n log n) init
        self.k = k
        self.nums = sorted(nums)

    def add_sort(self, val: int) -> int:
        # O(n log n) per add — insert and re-sort
        import bisect
        bisect.insort(self.nums, val)
        return self.nums[-self.k]

    # --- Approach 2: Min-heap of size k ---

    def __init__(self, k: int, nums: List[int]):
        # Maintain a min-heap of size k; top is always the k-th largest
        # O(n log k) init
        self.k = k
        self.heap: List[int] = []
        for n in nums:
            heapq.heappush(self.heap, n)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Push new val; if heap exceeds k, pop the smallest (not in top-k)
        # Top of min-heap is the k-th largest element
        # O(log k) per add — maintain min-heap of size k
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == '__main__':
    # stream after init: [2,4,5,8], k=3 → 3rd largest = 4
    obj = KthLargest(3, [4, 5, 8, 2])
    assert obj.add(3) == 4   # [2,3,4,5,8] → 3rd largest = 4
    assert obj.add(5) == 5   # [2,3,4,5,5,8] → 3rd largest = 5
    assert obj.add(10) == 5  # [2,3,4,5,5,8,10] → 3rd largest = 5
    assert obj.add(9) == 8   # [2,3,4,5,5,8,9,10] → 3rd largest = 8
    assert obj.add(4) == 8   # [2,3,4,4,5,5,8,9,10] → 3rd largest = 8

    obj2 = KthLargest(1, [])
    assert obj2.add(-3) == -3
    assert obj2.add(-2) == -2
    assert obj2.add(-4) == -2

    print("All tests passed.")
