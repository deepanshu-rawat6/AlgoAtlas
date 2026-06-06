from typing import List


class Solution:
    """
    ## 252. Meeting Rooms

    Given an array of meeting time intervals where intervals[i] = [start_i, end_i],
    return true if a person could attend all meetings (no two meetings overlap).

    ### Example
    ```text
    Input:  intervals = [[0,30],[5,10],[15,20]]
    Output: false

    Input:  intervals = [[7,10],[2,4]]
    Output: true
    ```

    ### Constraints
    - 0 <= intervals.length <= 10^4
    - intervals[i].length == 2
    - 0 <= start_i < end_i <= 10^6
    """

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort by start; if any meeting starts before previous ends, conflict
        # O(n log n) time, O(1) space — sort by start and check adjacent overlap
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.canAttendMeetings([[0, 30], [5, 10], [15, 20]]) == False
    assert s.canAttendMeetings([[7, 10], [2, 4]]) == True
    assert s.canAttendMeetings([]) == True
    assert s.canAttendMeetings([[1, 5], [5, 10]]) == True
    print("All tests passed.")
