"""
# LC 169: Majority Element

Given an array `nums` of size `n`, return the majority element — the element that
appears more than `⌊n / 2⌋` times. The majority element always exists.

## Examples

```text
Input:  nums = [3,2,3]
Output: 3

Input:  nums = [2,2,1,1,1,2,2]
Output: 2
```

## Constraints
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9
- The majority element always exists.
"""
from typing import List
from collections import Counter


class Solution:
    def majorityElement_map(self, nums: List[int]) -> int:
        # Count occurrences and return the element with the highest count
        # O(n) time | O(n) space
        count = Counter(nums)
        return max(count, key=count.get)

    def majorityElement_sort(self, nums: List[int]) -> int:
        # The majority element always occupies the middle index after sorting
        # O(n log n) time | O(1) space
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore: maintain a candidate and a net vote count
        # When count hits 0, the current element becomes the new candidate
        # Majority element's votes always outlast all opposition combined
        # O(n) time | O(1) space — Boyer-Moore Voting
        candidate, count = None, 0
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n == candidate else -1
        return candidate


if __name__ == "__main__":
    s = Solution()
    assert s.majorityElement([3, 2, 3]) == 3
    assert s.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert s.majorityElement([1]) == 1
    print("All tests passed.")
