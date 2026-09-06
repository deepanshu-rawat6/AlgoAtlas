#include <cassert>
#include <climits>
#include <vector>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int minPrice = INT_MAX, maxP = 0;
        for (int p : prices) {
            minPrice = std::min(minPrice, p);
            maxP = std::max(maxP, p - minPrice);
        }
        return maxP;
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {7,1,5,3,6,4};
    assert(sol.maxProfit(a) == 5);
    std::vector<int> b = {7,6,4,3,1};
    assert(sol.maxProfit(b) == 0);
    std::vector<int> c = {1,2};
    assert(sol.maxProfit(c) == 1);
    return 0;
}
