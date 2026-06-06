from typing import List


class Solution:
    """
    ## 135. Candy

    There are n children standing in a line. Each child is assigned a rating value.
    You must give each child at least one candy. Children with a higher rating than
    their adjacent neighbor must receive more candies. Return the minimum total candies.

    ### Example
    ```text
    Input:  ratings = [1, 0, 2]
    Output: 5  (give [2, 1, 2] candies)

    Input:  ratings = [1, 2, 2]
    Output: 4  (give [1, 2, 1] candies)
    ```

    ### Constraints
    - 1 <= ratings.length <= 2 * 10^4
    - 0 <= ratings[i] <= 2 * 10^4
    """

    def candy(self, ratings: List[int]) -> int:
        # Two passes: left-to-right ensures higher-rated child gets more than left neighbor
        # Right-to-left ensures higher-rated child gets more than right neighbor
        # Take max of both passes at each position
        # O(n) time, O(n) space — two-pass left-right then right-left
        n = len(ratings)
        candies = [1] * n
        # Left pass: ensure right neighbor with higher rating gets more
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        # Right pass: ensure left neighbor with higher rating gets more
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)


if __name__ == '__main__':
    s = Solution()
    assert s.candy([1, 0, 2]) == 5
    assert s.candy([1, 2, 2]) == 4
    assert s.candy([1]) == 1
    assert s.candy([1, 3, 2, 2, 1]) == 7
    print("All tests passed.")
