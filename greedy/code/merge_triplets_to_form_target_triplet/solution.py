from typing import List


class Solution:
    """
    ## 1899. Merge Triplets to Form Target Triplet

    A triplet is an array of three integers. You are given a 2D array triplets and a target triplet.
    You may choose any two triplets and update one of them to [max(a,x), max(b,y), max(c,z)].
    Return true if it is possible to obtain the target triplet as an element of triplets.

    ### Example
    ```text
    Input:  triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
    Output: true  (merge [2,5,3] and [1,7,5] -> [2,7,5])

    Input:  triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
    Output: false
    ```

    ### Constraints
    - 1 <= triplets.length <= 10^5
    - triplets[i].length == target.length == 3
    - 1 <= triplets[i][j], target[j] <= 1000
    """

    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Only consider triplets where no element exceeds the target
        # Check if the union (element-wise max) of valid triplets equals target
        # O(n) time, O(1) space — filter valid triplets and accumulate max
        result = [0, 0, 0]
        for t in triplets:
            # Skip triplets that exceed any target component
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                result = [max(result[i], t[i]) for i in range(3)]
        return result == target


if __name__ == '__main__':
    s = Solution()
    assert s.mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]) == True
    assert s.mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]) == False
    assert s.mergeTriplets([[2, 5, 3], [2, 3, 4], [1, 2, 5]], [2, 5, 5]) == True
    print("All tests passed.")
