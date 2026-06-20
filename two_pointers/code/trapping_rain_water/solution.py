"""
## LC 42 — Trapping Rain Water

Given `n` non-negative integers representing an elevation map where the width of each
bar is 1, compute how much water it can trap after raining.

### Examples

```text
Input:  height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6

Input:  height = [4, 2, 0, 3, 2, 5]
Output: 9
```

### Constraints

- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
"""
from typing import List


class Solution:
    def method_brute_force(self, height: List[int]) -> int:
        """O(n^2) time | O(1) space — for each bar scan left and right max"""
        # For each bar, scan left and right to find max heights — O(n^2)
        n = len(height)
        water = 0
        for i in range(n):
            left_max = max(height[:i + 1])
            right_max = max(height[i:])
            water += min(left_max, right_max) - height[i]
        return water

    def method_prefix_arrays(self, height: List[int]) -> int:
        """O(n) time | O(n) space"""
        # Precompute left_max[i] and right_max[i] in two passes
        # Water at i = min(left_max[i], right_max[i]) - height[i]
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        return sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))

    def trap(self, height: List[int]) -> int:
        """O(n) time | O(1) space"""
        # Two-pointer: process the side with the smaller max height
        # The shorter side's water level is fully determined by its own max
        # If current bar >= its side's max, update max; else accumulate water
        lo, hi = 0, len(height) - 1
        left_max = right_max = water = 0
        while lo <= hi:
            if height[lo] <= height[hi]:
                if height[lo] >= left_max:
                    left_max = height[lo]
                else:
                    water += left_max - height[lo]
                lo += 1
            else:
                if height[hi] >= right_max:
                    right_max = height[hi]
                else:
                    water += right_max - height[hi]
                hi -= 1
        return water


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(sol.trap([4, 2, 0, 3, 2, 5]))                      # 9
