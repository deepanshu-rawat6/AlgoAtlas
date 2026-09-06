#include <cassert>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int numSubarraysWithSum(std::vector<int>& nums, int goal) {
        std::unordered_map<int,int> count;
        count[0] = 1;
        int prefix = 0, result = 0;
        for (int n : nums) {
            prefix += n;
            if (count.count(prefix - goal)) result += count[prefix - goal];
            count[prefix]++;
        }
        return result;
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {1,0,1,0,1};
    assert(sol.numSubarraysWithSum(a, 2) == 4);
    std::vector<int> b = {0,0,0,0,0};
    assert(sol.numSubarraysWithSum(b, 0) == 15);
    std::vector<int> c = {1,0,1};
    assert(sol.numSubarraysWithSum(c, 1) == 4);
    return 0;
}
