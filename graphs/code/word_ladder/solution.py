from typing import List
from collections import deque, defaultdict


class Solution:
    """
    ## 127. Word Ladder

    A transformation sequence from word `beginWord` to word `endWord` using a dictionary
    `wordList` is a sequence `beginWord -> s1 -> s2 -> ... -> sk` such that:

    - Every adjacent pair of words differs by exactly one letter.
    - Every `si` for `1 <= i <= k` is in `wordList`.
    - `sk == endWord`

    Given `beginWord`, `endWord`, and `wordList`, return the number of words in the
    shortest transformation sequence, or `0` if no such sequence exists.

    ### Examples

    ```text
    Input:  beginWord = "hit", endWord = "cog",
            wordList = ["hot","dot","dog","lot","log","cog"]
    Output: 5
    Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog"

    Input:  beginWord = "hit", endWord = "cog",
            wordList = ["hot","dot","dog","lot","log"]
    Output: 0
    ```

    ### Constraints

    - `1 <= beginWord.length <= 10`
    - `endWord.length == beginWord.length`
    - `1 <= wordList.length <= 5000`
    - `wordList[i].length == beginWord.length`
    - All words consist of lowercase English letters.
    - `beginWord != endWord`
    - All words in `wordList` are unique.
    """

    def ladderLength_bfs(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # O(m^2 * n) time, O(m^2 * n) space — standard BFS
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            word, length = queue.popleft()
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word == endWord:
                        return length + 1
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, length + 1))
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS from beginWord; each level = one transformation step
        # For each word, try changing each character to find valid neighbors in wordSet
        # O(m^2 * n) time, O(m^2 * n) space — bidirectional BFS
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        front, back = {beginWord}, {endWord}
        visited = {beginWord, endWord}
        length = 1

        while front:
            length += 1
            next_front = set()
            for word in front:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in back:
                            return length
                        if next_word in word_set and next_word not in visited:
                            visited.add(next_word)
                            next_front.add(next_word)
            front = next_front
            if len(front) > len(back):
                front, back = back, front
        return 0


if __name__ == '__main__':
    s = Solution()
    wl = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert s.ladderLength_bfs("hit", "cog", wl) == 5
    assert s.ladderLength_bfs("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0

    assert s.ladderLength("hit", "cog", wl) == 5
    assert s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    print("All tests passed.")
