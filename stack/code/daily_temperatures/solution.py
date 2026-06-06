"""
# 739. Daily Temperatures

## Problem
Given an array of integers `temperatures` representing daily temperatures,
return an array `answer` such that `answer[i]` is the number of days you have
to wait after the `i`-th day to get a warmer temperature. If there is no
future day with a warmer temperature, `answer[i] == 0`.

## Examples
```text
Input:  temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Input:  temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input:  temperatures = [30,60,90]
Output: [1,1,0]
```

## Constraints
- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`
"""

from typing import List


class Solution:
    def dailyTemperatures_brute(self, temperatures: List[int]) -> List[int]:
        # For each day, scan forward until a warmer day is found — O(n^2)
        # O(n^2) time, O(1) extra space — check every future day
        n = len(temperatures)
        answer = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    answer[i] = j - i
                    break
        return answer

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic decreasing stack stores indices of unresolved days
        # When a warmer day arrives, resolve all cooler days on the stack
        # O(n) time, O(n) space — decreasing monotonic stack of indices
        n = len(temperatures)
        answer = [0] * n
        stack = []  # indices with unresolved warmer day
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert s.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert s.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
    assert s.dailyTemperatures_brute([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    print("All tests passed.")
