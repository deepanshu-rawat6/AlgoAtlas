import heapq
from typing import List


class Solution:
    """
    ## 1094. Car Pooling

    There is a car with `capacity` empty seats. The vehicle only drives east (i.e., it cannot turn
    around and drive west).

    You are given the integer `capacity` and an array `trips` where `trips[i] = [numPassengersi,
    fromi, toi]` indicates that the `i`th trip has `numPassengersi` passengers and the route goes
    from `fromi` to `toi`. The locations are given as the number of kilometers due east from the
    car's initial location.

    Return `true` if it is possible to pick up and drop off all passengers for all the given trips,
    or `false` otherwise.

    ### Examples

    ```text
    Input: trips = [[2,1,5],[3,3,7]], capacity = 4
    Output: false

    Explanation:
        At stop 1: pick up 2 → current = 2
        At stop 3: pick up 3 → current = 5 > 4 → impossible
    ```

    ```text
    Input: trips = [[2,1,5],[3,3,7]], capacity = 5
    Output: true
    ```

    ```text
    Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
    Output: true
    ```

    ### Constraints
    - `1 <= trips.length <= 1000`
    - `trips[i].length == 3`
    - `1 <= numPassengersi <= 100`
    - `0 <= fromi < toi <= 1000`
    - `1 <= capacity <= 10^5`
    """

    def carPooling_events(self, trips: List[List[int]], capacity: int) -> bool:
        # O(n log n) — sort pickup/dropoff events, simulate
        events = []
        for num, start, end in trips:
            events.append((start, num))   # pickup
            events.append((end, -num))    # dropoff
        events.sort()
        current = 0
        for _, delta in events:
            current += delta
            if current > capacity:
                return False
        return True

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Sort trips by start; use min-heap of (end, passengers) for active trips
        # At each trip start, drop off passengers from trips that have ended
        # If current passengers exceed capacity, return False
        # O(n + max_stop) — difference array over stop positions
        diff = [0] * 1001
        for num, start, end in trips:
            diff[start] += num
            diff[end] -= num
        current = 0
        for delta in diff:
            current += delta
            if current > capacity:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.carPooling_events([[2, 1, 5], [3, 3, 7]], 4) == False
    assert s.carPooling([[2, 1, 5], [3, 3, 7]], 4) == False

    assert s.carPooling_events([[2, 1, 5], [3, 3, 7]], 5) == True
    assert s.carPooling([[2, 1, 5], [3, 3, 7]], 5) == True

    assert s.carPooling([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11) == True
    assert s.carPooling_events([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11) == True

    print("All tests passed.")
