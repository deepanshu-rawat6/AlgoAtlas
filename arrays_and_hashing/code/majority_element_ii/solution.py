"""
# LC 229: Majority Element II

Given an integer array of size `n`, find all elements that appear more than
⌊n/3⌋ times.

## Examples

```text
Input:  nums = [3,2,3]
Output: [3]

Input:  nums = [1]
Output: [1]

Input:  nums = [1,2]
Output: [1,2]
```

## Constraints
- 1 <= nums.length <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9
"""
from typing import List
from collections import Counter


class Solution:
    def majorityElement_hashmap(self, nums: List[int]) -> List[int]:
        """Hash map counting — O(n) time, O(n) space."""
        # Count all elements; return those appearing more than n//3 times
        threshold = len(nums) // 3
        return [num for num, cnt in Counter(nums).items() if cnt > threshold]

    def majorityElement(self, nums: List[int]) -> List[int]:
        """Boyer-Moore extended (at most 2 candidates) — O(n) time, O(1) space."""
        # At most 2 elements can appear more than n/3 times
        # Maintain two candidates with vote counts; cancel out different pairs
        # Final verification pass confirms candidates actually exceed threshold
        cand1, cand2, cnt1, cnt2 = 0, 1, 0, 0
        for n in nums:
            if n == cand1:
                cnt1 += 1
            elif n == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1, cnt1 = n, 1
            elif cnt2 == 0:
                cand2, cnt2 = n, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        threshold = len(nums) // 3
        return [c for c in (cand1, cand2) if nums.count(c) > threshold]


if __name__ == "__main__":
    s = Solution()

    assert sorted(s.majorityElement([3, 2, 3])) == [3]
    assert sorted(s.majorityElement([1])) == [1]
    assert sorted(s.majorityElement([1, 2])) == [1, 2]
    assert sorted(s.majorityElement([1, 1, 1, 3, 3, 2, 2, 2])) == [1, 2]

    print("All tests passed.")
