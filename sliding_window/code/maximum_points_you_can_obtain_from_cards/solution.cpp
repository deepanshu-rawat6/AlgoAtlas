#include <cassert>
#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int maxScore(std::vector<int>& cardPoints, int k) {
        int n = cardPoints.size();
        int total = std::accumulate(cardPoints.begin(), cardPoints.end(), 0);
        int window = n - k;
        if (window == 0) return total;
        int curr = std::accumulate(cardPoints.begin(), cardPoints.begin() + window, 0);
        int minMid = curr;
        for (int i = window; i < n; i++) {
            curr += cardPoints[i] - cardPoints[i - window];
            minMid = std::min(minMid, curr);
        }
        return total - minMid;
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {1,2,3,4,5,6,1};
    assert(sol.maxScore(a, 3) == 12);
    std::vector<int> b = {2,2,2};
    assert(sol.maxScore(b, 2) == 4);
    std::vector<int> c = {9,7,7,9,7,7,9};
    assert(sol.maxScore(c, 7) == 55);
    return 0;
}
