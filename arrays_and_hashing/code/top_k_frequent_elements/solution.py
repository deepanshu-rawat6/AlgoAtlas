"""
# LC 347: Top K Frequent Elements

Given an integer array `nums` and an integer `k`, return the `k` most frequent
elements. You may return the answer in any order.

## Examples

```text
Input:  nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input:  nums = [1], k = 1
Output: [1]
```

## Constraints
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array]
- The answer is guaranteed to be unique
"""
from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent_sort(self, nums: List[int], k: int) -> List[int]:
        """Sort by frequency — O(n log n) time, O(n) space."""
        # Count frequencies, then sort by descending frequency and take top k
        count = Counter(nums)
        return sorted(count, key=lambda x: -count[x])[:k]

    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        """Min-heap of size k — O(n log k) time, O(n) space."""
        # heapq.nlargest keeps a min-heap of size k — O(n log k)
        count = Counter(nums)
        return heapq.nlargest(k, count, key=count.get)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Bucket sort — O(n) time, O(n) space."""
        # Bucket sort: index = frequency, so we can iterate buckets in reverse
        # Collect elements from highest-frequency bucket down until we have k
        count = Counter(nums)
        buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        result: List[int] = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result


if __name__ == "__main__":
    s = Solution()

    assert sorted(s.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert s.topKFrequent([1], 1) == [1]
    assert sorted(s.topKFrequent([1, 2], 2)) == [1, 2]

    print("All tests passed.")
