#include <algorithm>
#include <cassert>
#include <vector>

class Solution {
public:
    int numRescueBoats(std::vector<int>& people, int limit) {
        std::sort(people.begin(), people.end());
        int lo = 0, hi = (int)people.size() - 1, boats = 0;
        while (lo <= hi) {
            if (people[lo] + people[hi] <= limit) lo++;
            hi--;
            boats++;
        }
        return boats;
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {1, 2};
    assert(sol.numRescueBoats(a, 3) == 1);
    std::vector<int> b = {3, 2, 2, 1};
    assert(sol.numRescueBoats(b, 3) == 3);
    std::vector<int> c = {3, 5, 3, 4};
    assert(sol.numRescueBoats(c, 5) == 4);
    return 0;
}
