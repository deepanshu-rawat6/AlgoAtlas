from typing import List


class Solution:
    """
    ## 57. Insert Interval

    Given a list of non-overlapping intervals sorted by start time, insert a new interval
    and merge if necessary. Return the resulting list of non-overlapping intervals.

    ### Example
    ```text
    Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

    Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    ```

    ### Constraints
    - 0 <= intervals.length <= 10^4
    - intervals is sorted in ascending order by start
    - intervals[i].length == newInterval.length == 2
    - 0 <= intervals[i][0] <= intervals[i][1] <= 10^5
    """

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Add all intervals ending before new interval starts
        # Merge all overlapping intervals with the new one
        # Add remaining intervals that start after the merged interval ends
        # O(n) time, O(n) space — linear scan and merge
        result = []
        i, n = 0, len(intervals)
        # Add all intervals that end before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        # Merge all overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        # Add remaining intervals
        result.extend(intervals[i:])
        return result


if __name__ == '__main__':
    s = Solution()
    assert s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert s.insert([], [5, 7]) == [[5, 7]]
    assert s.insert([[1, 5]], [2, 3]) == [[1, 5]]
    print("All tests passed.")
