"""
## LC 167: Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers `numbers` that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
`target` number. Return the indices of the two numbers as an integer array
`[index1, index2]` where `1 <= index1 < index2 <= numbers.length`.

The solution must use only constant extra space.

### Examples

```text
Input:  numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: 2 + 7 = 9.

Input:  numbers = [2,3,4], target = 6
Output: [1,3]

Input:  numbers = [-1,0], target = -1
Output: [1,2]
```

### Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order.
- The tests are generated such that there is exactly one solution.
- You may not use the same element twice.
"""
from typing import List
import bisect


class Solution:
    def method_brute_force(self, numbers: List[int], target: int) -> List[int]:
        """O(n^2) time, O(1) space."""
        # Check all pairs — O(n^2); array is sorted but we ignore that here
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []

    def method_binary_search(self, numbers: List[int], target: int) -> List[int]:
        """O(n log n) time, O(1) space."""
        # For each element, binary search for its complement in the rest
        for i in range(len(numbers)):
            complement = target - numbers[i]
            j = bisect.bisect_left(numbers, complement, i + 1)
            if j < len(numbers) and numbers[j] == complement:
                return [i + 1, j + 1]
        return []

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """O(n) time, O(1) space."""
        # Sorted array: if sum too small move left pointer right, if too large move right left
        # Converge until the exact target sum is found
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1
        return []


if __name__ == "__main__":
    sol = Solution()

    assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert sol.twoSum([2, 3, 4], 6) == [1, 3]
    assert sol.twoSum([-1, 0], -1) == [1, 2]
    assert sol.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5]

    print("All tests passed.")
