"""
## LC 11 — Container With Most Water

You are given an integer array `height` of length `n`. There are `n` vertical lines
drawn such that the two endpoints of the `i`-th line are `(i, 0)` and `(i, height[i])`.
Find two lines that together with the x-axis form a container that holds the most water.
Return the maximum amount of water a container can store.

### Examples

```text
Input:  height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49

Input:  height = [1, 1]
Output: 1
```

### Constraints

- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
"""
from typing import List


class Solution:
    def method_brute_force(self, height: List[int]) -> int:
        """O(n^2) time | O(1) space"""
        # Try all pairs of lines — O(n^2)
        max_water = 0
        n = len(height)
        for i in range(n):
            for j in range(i + 1, n):
                max_water = max(max_water, min(height[i], height[j]) * (j - i))
        return max_water

    def maxArea(self, height: List[int]) -> int:
        """O(n) time | O(1) space"""
        # Start with widest container; move the shorter wall inward
        # Moving the taller wall can only decrease area, so always move shorter
        lo, hi = 0, len(height) - 1
        max_water = 0
        while lo < hi:
            max_water = max(max_water, min(height[lo], height[hi]) * (hi - lo))
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return max_water


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(sol.maxArea([1, 1]))                         # 1
