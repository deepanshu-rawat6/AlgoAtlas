import heapq
from typing import List


class Solution:
    """
    ## 1046. Last Stone Weight

    You are given an array of integers `stones` where `stones[i]` is the weight of the `i`th stone.

    We are playing a game with the stones. On each turn, we choose the **two heaviest** stones and
    smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`:
    - If `x == y`, both stones are destroyed.
    - If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

    At the end of the game, there is **at most one** stone left. Return the weight of the last remaining
    stone. If there are no stones left, return `0`.

    ### Examples

    ```text
    Input: stones = [2, 7, 4, 1, 8, 1]
    Output: 1

    Explanation:
        Smash 8 and 7 → 1. Stones: [2, 4, 1, 1, 1]
        Smash 4 and 2 → 2. Stones: [2, 1, 1, 1]
        Smash 2 and 1 → 1. Stones: [1, 1, 1]
        Smash 1 and 1 → 0. Stones: [1]
        Result: 1
    ```

    ```text
    Input: stones = [1]
    Output: 1
    ```

    ### Constraints
    - `1 <= stones.length <= 30`
    - `1 <= stones[i] <= 1000`
    """

    def lastStoneWeight_sort(self, stones: List[int]) -> int:
        # O(n^2 log n) — sort on every iteration
        stones = sorted(stones)
        while len(stones) > 1:
            y, x = stones.pop(), stones.pop()
            if x != y:
                import bisect
                bisect.insort(stones, y - x)
        return stones[0] if stones else 0

    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use max-heap (negate for Python's min-heap)
        # Repeatedly smash two heaviest; push remainder if non-zero
        # O(n log n) — max-heap via negation
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -(y - x))
        return -heap[0] if heap else 0


if __name__ == '__main__':
    s = Solution()
    assert s.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert s.lastStoneWeight([1]) == 1
    assert s.lastStoneWeight([2, 2]) == 0
    assert s.lastStoneWeight_sort([2, 7, 4, 1, 8, 1]) == 1
    assert s.lastStoneWeight_sort([1]) == 1
    print("All tests passed.")
