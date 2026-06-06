from typing import List


class Solution:
    """
    ## 435. Non-overlapping Intervals

    Given an array of intervals, return the minimum number of intervals you need to remove
    to make the rest of the intervals non-overlapping.

    ### Example
    ```text
    Input:  intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output: 1  (remove [1,3])

    Input:  intervals = [[1,2],[1,2],[1,2]]
    Output: 2

    Input:  intervals = [[1,2],[2,3]]
    Output: 0
    ```

    ### Constraints
    - 1 <= intervals.length <= 10^5
    - intervals[i].length == 2
    - -5 * 10^4 <= intervals[i][0] < intervals[i][1] <= 5 * 10^4
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by end time; greedily keep intervals with earliest end
        # Count intervals that must be removed (overlap with last kept)
        # O(n log n) time, O(1) space — sort by end, greedily keep non-overlapping
        intervals.sort(key=lambda x: x[1])
        removed = 0
        prev_end = float('-inf')
        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                removed += 1
        return removed


if __name__ == '__main__':
    s = Solution()
    assert s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert s.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
    print("All tests passed.")
