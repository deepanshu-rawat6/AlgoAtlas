"""
# 84. Largest Rectangle in Histogram

## Problem
Given an array of integers `heights` representing the histogram's bar heights
where the width of each bar is `1`, return the area of the largest rectangle
in the histogram.

## Examples
```text
Input:  heights = [2,1,5,6,2,3]
Output: 10
Explanation: The largest rectangle has area 10 (bars of height 5 and 6,
             width 2).

Input:  heights = [2,4]
Output: 4
```

## Constraints
- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`
"""

from typing import List


class Solution:
    def largestRectangleArea_brute(self, heights: List[int]) -> int:
        # For each starting bar, extend right tracking minimum height — O(n^2)
        # O(n^2) time, O(1) extra space — expand each bar left and right
        n = len(heights)
        max_area = 0
        for i in range(n):
            min_h = heights[i]
            for j in range(i, n):
                min_h = min(min_h, heights[j])
                max_area = max(max_area, min_h * (j - i + 1))
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic increasing stack: when a shorter bar is found, pop taller bars
        # Each popped bar's rectangle extends from its stored start index to current i
        # 'start' tracks how far left the current bar can extend
        # O(n) time, O(n) space — increasing monotonic stack with sentinel
        stack = []  # (index, height) — index = leftmost extent of current bar
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
        return max_area


if __name__ == "__main__":
    s = Solution()
    assert s.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert s.largestRectangleArea([2, 4]) == 4
    assert s.largestRectangleArea([1]) == 1
    assert s.largestRectangleArea([6, 2, 5, 4, 5, 1, 6]) == 12
    assert s.largestRectangleArea_brute([2, 1, 5, 6, 2, 3]) == 10
    assert s.largestRectangleArea_brute([2, 4]) == 4
    print("All tests passed.")
