import heapq
from typing import List


class Solution:
    """
    ## 1834. Single-Threaded CPU

    You are given `n` tasks labeled from `0` to `n - 1` represented by a 2D integer array `tasks`,
    where `tasks[i] = [enqueueTimei, processingTimei]` represents the time at which the `i`th task
    will be available for processing and the time it takes to finish processing.

    Return the **order** in which the CPU will process the tasks.

    Rules:
    - If the CPU is idle and there are no available tasks, the CPU waits until the next available task.
    - If the CPU is idle and there are available tasks, the CPU picks the task with the **shortest
      processing time**. If multiple tasks have the same processing time, it picks the task with the
      **smallest index**.
    - Once a task is started, the CPU runs it to completion.

    ### Examples

    ```text
    Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
    Output: [0, 2, 3, 1]

    Explanation:
        t=1: task 0 available, CPU picks task 0 (proc=2), finishes at t=3
        t=3: tasks 1,2 available; pick task 2 (proc=2, shorter than 4), finishes at t=5
        t=5: tasks 1,3 available; pick task 3 (proc=1), finishes at t=6
        t=6: task 1 available; pick task 1, finishes at t=10
    ```

    ```text
    Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
    Output: [4, 3, 2, 0, 1]
    ```

    ### Constraints
    - `1 <= tasks.length <= 10^5`
    - `1 <= enqueueTimei, processingTimei <= 10^9`
    """

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Sort tasks by enqueue time; simulate CPU with a min-heap of (processing_time, index)
        # At each step, advance time to next available task if CPU is idle
        # Always process the shortest available task (min-heap by processing time, then index)
        # O(n log n) — sort by enqueue time, simulate with min-heap on (proc_time, index)
        indexed = sorted(enumerate(tasks), key=lambda x: x[1][0])
        heap: List = []  # (processing_time, original_index)
        result = []
        time = 0
        i = 0
        n = len(tasks)

        while len(result) < n:
            # Push all tasks available at current time
            while i < n and indexed[i][1][0] <= time:
                orig_idx, task = indexed[i]
                heapq.heappush(heap, (task[1], orig_idx))
                i += 1

            if heap:
                proc_time, orig_idx = heapq.heappop(heap)
                result.append(orig_idx)
                time += proc_time
            else:
                # CPU idle — jump to next task's enqueue time
                time = indexed[i][1][0]

        return result


if __name__ == '__main__':
    s = Solution()
    assert s.getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]) == [0, 2, 3, 1]
    assert s.getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]) == [4, 3, 2, 0, 1]
    assert s.getOrder([[1, 1], [1, 1]]) == [0, 1]
    print("All tests passed.")
