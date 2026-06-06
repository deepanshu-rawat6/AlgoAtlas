"""
LC 904 - Fruit Into Baskets

You have two baskets, and each basket can carry any quantity of fruit, but
you want each basket to only carry one type of fruit. Given an integer array
fruits where fruits[i] is the type of fruit the ith tree produces, return the
maximum number of fruits you can pick (must pick from a contiguous subarray).

Equivalent to: longest subarray with at most 2 distinct values.

Examples:
```text
Input: fruits = [1,2,1]
Output: 3

Input: fruits = [0,1,2,2]
Output: 3

Input: fruits = [1,2,3,2,2]
Output: 4
```

Constraints:
- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length
"""

from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Sliding window with freq map — at most 2 distinct fruit types
        count = defaultdict(int)
        left = 0
        result = 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1

            # More than 2 distinct types — shrink window from left
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            result = max(result, right - left + 1)

        return result


if __name__ == '__main__':
    s = Solution()
    assert s.totalFruit([1,2,1]) == 3
    assert s.totalFruit([0,1,2,2]) == 3
    assert s.totalFruit([1,2,3,2,2]) == 4
    assert s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]) == 5
    print("All tests passed.")
