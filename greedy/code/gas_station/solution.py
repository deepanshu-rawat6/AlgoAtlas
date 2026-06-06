from typing import List


class Solution:
    """
    ## 134. Gas Station

    There are n gas stations in a circle. You are given two integer arrays gas and cost.
    Return the starting station's index if you can travel around the circuit once in the
    clockwise direction, otherwise return -1. If a solution exists, it is guaranteed to be unique.

    ### Example
    ```text
    Input:  gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]
    Output: 3

    Input:  gas = [2, 3, 4], cost = [3, 4, 3]
    Output: -1
    ```

    ### Constraints
    - n == gas.length == cost.length
    - 1 <= n <= 10^5
    - 0 <= gas[i], cost[i] <= 10^4
    """

    def canCompleteCircuit_brute(self, gas: List[int], cost: List[int]) -> int:
        # O(n^2) time, O(1) space
        n = len(gas)
        for start in range(n):
            tank = 0
            for i in range(n):
                idx = (start + i) % n
                tank += gas[idx] - cost[idx]
                if tank < 0:
                    break
            else:
                return start
        return -1

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas >= total cost, a solution exists
        # Start from the index after any point where running sum goes negative
        # O(n) time, O(1) space — single pass
        total = tank = start = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            diff = g - c
            total += diff
            tank += diff
            if tank < 0:
                start = i + 1
                tank = 0
        return start if total >= 0 else -1


if __name__ == '__main__':
    s = Solution()
    assert s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert s.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
    assert s.canCompleteCircuit_brute([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    print("All tests passed.")
