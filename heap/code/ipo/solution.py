import heapq
from typing import List


class Solution:
    """
    ## 502. IPO

    Suppose LeetCode will start its **IPO** soon. In order to sell a good price of its shares to
    Venture Capital, LeetCode would like to work on some projects to increase its capital before
    the IPO. Since it has limited resources, it can only finish at most `k` distinct projects
    before the IPO. Help LeetCode design the best way to maximize its total capital after finishing
    at most `k` distinct projects.

    You are given `n` projects where the `i`th project has a pure profit `profits[i]` and a minimum
    capital of `capital[i]` is needed to start it.

    Initially, you have `w` capital. When you finish a project, you will obtain its pure profit and
    the profit will be added to your total capital.

    Return the **maximized total capital** after finishing at most `k` distinct projects.

    ### Examples

    ```text
    Input: k = 2, w = 0, profits = [1, 2, 3], capital = [0, 1, 1]
    Output: 4

    Explanation:
        Start with w=0. Available: project 0 (capital=0). Pick it → profit=1, w=1.
        Now w=1. Available: projects 1,2 (capital=1). Pick project 2 (profit=3) → w=4.
        Result: 4
    ```

    ```text
    Input: k = 3, w = 0, profits = [1, 2, 3], capital = [0, 1, 2]
    Output: 6
    ```

    ### Constraints
    - `1 <= k <= 10^5`
    - `0 <= w <= 10^9`
    - `n == profits.length == capital.length`
    - `1 <= n <= 10^5`
    - `0 <= profits[i] <= 10^4`
    - `0 <= capital[i] <= 10^9`
    """

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Greedily pick the most profitable available project at each step
        # Use min-heap on capital to unlock projects as capital grows
        # Use max-heap on profit to always pick the best available project
        # O(n log n) — sort by capital, greedily pick max profit available project
        projects = sorted(zip(capital, profits))
        available: List[int] = []  # max-heap (negated profits)
        i = 0
        n = len(projects)

        for _ in range(k):
            # Unlock all projects we can now afford
            while i < n and projects[i][0] <= w:
                heapq.heappush(available, -projects[i][1])
                i += 1
            if not available:
                break
            w += -heapq.heappop(available)

        return w


if __name__ == '__main__':
    s = Solution()
    assert s.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]) == 4
    assert s.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]) == 6
    assert s.findMaximizedCapital(1, 0, [1, 2, 3], [1, 1, 2]) == 0  # can't afford any
    assert s.findMaximizedCapital(2, 1, [1, 2, 3], [1, 1, 2]) == 6
    print("All tests passed.")
