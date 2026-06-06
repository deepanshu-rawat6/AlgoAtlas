import heapq
from collections import defaultdict
from typing import List


class Twitter:
    """
    ## 355. Design Twitter

    Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
    and see the 10 most recent tweets in the user's news feed.

    Implement the `Twitter` class:
    - `Twitter()` — initializes the Twitter object.
    - `void postTweet(int userId, int tweetId)` — composes a new tweet with ID `tweetId` by user `userId`.
    - `List<Integer> getNewsFeed(int userId)` — retrieves the 10 most recent tweet IDs in the user's
      news feed. Each item must be posted by users who the user followed or by the user themselves.
      Tweets must be ordered from most recent to least recent.
    - `void follow(int followerId, int followeeId)` — the user with ID `followerId` starts following
      the user with ID `followeeId`.
    - `void unfollow(int followerId, int followeeId)` — the user with ID `followerId` starts unfollowing
      the user with ID `followeeId`.

    ### Examples

    ```text
    Input:
        Twitter twitter = new Twitter();
        twitter.postTweet(1, 5);
        twitter.getNewsFeed(1);   // [5]
        twitter.follow(1, 2);
        twitter.postTweet(2, 6);
        twitter.getNewsFeed(1);   // [6, 5]
        twitter.unfollow(1, 2);
        twitter.getNewsFeed(1);   // [5]
    ```

    ### Constraints
    - `1 <= userId, tweetId <= 500`
    - All the tweets have **unique** IDs.
    - At most `3 * 10^4` calls will be made to `postTweet`, `getNewsFeed`, `follow`, and `unfollow`.
    """

    def __init__(self):
        # O(1) init
        self.timestamp = 0
        self.tweets: dict = defaultdict(list)   # userId -> [(time, tweetId), ...]
        self.following: dict = defaultdict(set)  # userId -> {followeeId}

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Store tweet with a global timestamp for ordering
        # O(1) — append tweet with global timestamp
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Collect recent tweets from user and all followees
        # Use heap or sort to get the 10 most recent
        # O(f * 10 * log f) — heap-merge latest tweets from followed users + self
        heap: List = []
        users = self.following[userId] | {userId}
        for uid in users:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                time, tid = self.tweets[uid][idx]
                heapq.heappush(heap, (-time, tid, uid, idx))

        result = []
        while heap and len(result) < 10:
            neg_time, tid, uid, idx = heapq.heappop(heap)
            result.append(tid)
            if idx > 0:
                time, next_tid = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (-time, next_tid, uid, idx - 1))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add followee to user's follow set
        # O(1)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove followee from user's follow set if present
        # O(1)
        self.following[followerId].discard(followeeId)


if __name__ == '__main__':
    t = Twitter()
    t.postTweet(1, 5)
    assert t.getNewsFeed(1) == [5]
    t.follow(1, 2)
    t.postTweet(2, 6)
    assert t.getNewsFeed(1) == [6, 5]
    t.unfollow(1, 2)
    assert t.getNewsFeed(1) == [5]

    t2 = Twitter()
    for i in range(11):
        t2.postTweet(1, i)
    feed = t2.getNewsFeed(1)
    assert len(feed) == 10
    assert feed == list(range(10, 0, -1))

    print("All tests passed.")
