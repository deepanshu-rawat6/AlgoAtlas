#include <cassert>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int numberOfSubarrays(std::vector<int>& nums, int k) {
        std::unordered_map<int,int> count;
        count[0] = 1;
        int prefix = 0, result = 0;
        for (int n : nums) {
            prefix += n % 2;
            if (count.count(prefix - k)) result += count[prefix - k];
            count[prefix]++;
        }
        return result;
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {1,1,2,1,1};
    assert(sol.numberOfSubarrays(a, 3) == 2);
    std::vector<int> b = {2,4,6};
    assert(sol.numberOfSubarrays(b, 1) == 0);
    std::vector<int> c = {2,2,2,1,2,2,1,2,2,2};
    assert(sol.numberOfSubarrays(c, 2) == 16);
    return 0;
}
