import java.util.*;

public class Solution {
    static class Twitter {
        private int timestamp = 0;
        private Map<Integer, List<int[]>> tweets = new HashMap<>();  // userId -> [(time, tweetId)]
        private Map<Integer, Set<Integer>> following = new HashMap<>(); // userId -> {followeeId}

        public void postTweet(int userId, int tweetId) {
            tweets.computeIfAbsent(userId, k -> new ArrayList<>()).add(new int[]{timestamp++, tweetId});
        }

        public List<Integer> getNewsFeed(int userId) {
            // Max-heap by timestamp; merge latest tweets from self + followees
            PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> b[0] - a[0]); // [time, tweetId, userId, idx]
            Set<Integer> users = new HashSet<>(following.getOrDefault(userId, Collections.emptySet()));
            users.add(userId);
            for (int uid : users) {
                List<int[]> list = tweets.get(uid);
                if (list != null && !list.isEmpty()) {
                    int idx = list.size() - 1;
                    heap.offer(new int[]{list.get(idx)[0], list.get(idx)[1], uid, idx});
                }
            }
            List<Integer> result = new ArrayList<>();
            while (!heap.isEmpty() && result.size() < 10) {
                int[] top = heap.poll();
                result.add(top[1]);
                int nextIdx = top[3] - 1;
                if (nextIdx >= 0) {
                    List<int[]> list = tweets.get(top[2]);
                    heap.offer(new int[]{list.get(nextIdx)[0], list.get(nextIdx)[1], top[2], nextIdx});
                }
            }
            return result;
        }

        public void follow(int followerId, int followeeId) {
            following.computeIfAbsent(followerId, k -> new HashSet<>()).add(followeeId);
        }

        public void unfollow(int followerId, int followeeId) {
            following.getOrDefault(followerId, Collections.emptySet()).remove(followeeId);
        }
    }

    public static void main(String[] args) {
        Twitter t = new Twitter();
        t.postTweet(1, 5);
        assert t.getNewsFeed(1).equals(List.of(5));
        t.follow(1, 2);
        t.postTweet(2, 6);
        assert t.getNewsFeed(1).equals(List.of(6, 5));
        t.unfollow(1, 2);
        assert t.getNewsFeed(1).equals(List.of(5));

        // Top-10 cap
        Twitter t2 = new Twitter();
        for (int i = 0; i < 11; i++) t2.postTweet(1, i);
        List<Integer> feed = t2.getNewsFeed(1);
        assert feed.size() == 10;
        assert feed.equals(List.of(10, 9, 8, 7, 6, 5, 4, 3, 2, 1));

        System.out.println("All tests passed.");
    }
}
