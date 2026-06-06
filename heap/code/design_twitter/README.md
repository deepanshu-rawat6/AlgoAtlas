# Design Twitter (LC 355)

Design a simplified Twitter: users can post tweets, follow/unfollow others, and retrieve the 10 most recent tweets from their feed (own + followed users).

## Approaches

### Heap-Merge of Per-User Tweet Lists
- **Time:** O(f * 10 * log f) per `getNewsFeed` where f = number of followed users; O(1) for other ops
- **Space:** O(total tweets + follow relationships)
- Store each user's tweets as a list with a global timestamp. Store follow relationships in a set per user.
- `getNewsFeed`: initialize a max-heap with the most recent tweet from each followed user (and self). Repeatedly pop the most recent tweet, add to result, and push the next tweet from that same user. Stop after 10 tweets.

## Key Insight

This is a k-way merge problem. Each user's tweet list is already in chronological order. Instead of merging all tweets and sorting, we use a heap to lazily fetch only the 10 needed tweets. The heap always contains at most one tweet per followed user, so it stays small regardless of total tweet count.

## Edge Cases

- User follows themselves — the solution adds `{userId}` to the followed set, so self-tweets always appear.
- User with no tweets contributes nothing to the heap.
- Unfollow a user not being followed → `discard` (not `remove`) avoids KeyError.
- Feed capped at 10 even if the user follows many active users.
