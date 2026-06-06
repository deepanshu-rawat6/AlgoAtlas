from typing import List


class Solution:
    """
    ## 56. Merge Intervals

    Given an array of intervals, merge all overlapping intervals and return an array
    of the non-overlapping intervals that cover all the intervals in the input.

    ### Example
    ```text
    Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]

    Input:  intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    ```

    ### Constraints
    - 1 <= intervals.length <= 10^4
    - intervals[i].length == 2
    - 0 <= intervals[i][0] <= intervals[i][1] <= 10^4
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort by start time; merge current with next if they overlap
        # Two intervals overlap if next.start <= current.end
        # O(n log n) time, O(n) space — sort by start then merge
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        return result


if __name__ == '__main__':
    s = Solution()
    assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert s.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert s.merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert s.merge([[1, 4], [2, 3]]) == [[1, 4]]
    print("All tests passed.")
