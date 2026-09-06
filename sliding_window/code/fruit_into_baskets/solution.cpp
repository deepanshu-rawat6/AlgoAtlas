#include <cassert>
#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int totalFruit(std::vector<int>& fruits) {
        std::unordered_map<int,int> count;
        int left = 0, result = 0;
        for (int right = 0; right < (int)fruits.size(); right++) {
            count[fruits[right]]++;
            while ((int)count.size() > 2) {
                if (--count[fruits[left]] == 0) count.erase(fruits[left]);
                left++;
            }
            result = std::max(result, right - left + 1);
        }
        return result;
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {1,2,1};
    assert(sol.totalFruit(a) == 3);
    std::vector<int> b = {0,1,2,2};
    assert(sol.totalFruit(b) == 3);
    std::vector<int> c = {1,2,3,2,2};
    assert(sol.totalFruit(c) == 4);
    return 0;
}
