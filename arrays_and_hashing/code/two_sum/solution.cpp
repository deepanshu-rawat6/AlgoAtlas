// LC 1: Two Sum
// Return indices of two numbers that add up to target.
// Time: O(n), Space: O(n)
#include <vector>
#include <unordered_map>
#include <cassert>
#include <iostream>
using namespace std;

class Solution {
public:
    // Brute: O(n^2) time | O(1) space
    vector<int> twoSum_brute(vector<int>& nums, int target) {
        for (int i = 0; i < (int)nums.size(); i++)
            for (int j = i + 1; j < (int)nums.size(); j++)
                if (nums[i] + nums[j] == target)
                    return {i, j};
        return {};
    }

    // Optimal: O(n) time | O(n) space
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < (int)nums.size(); i++) {
            int diff = target - nums[i];
            if (seen.count(diff))
                return {seen[diff], i};
            seen[nums[i]] = i;
        }
        return {};
    }
};

int main() {
    Solution s;
    vector<int> a = {2, 7, 11, 15};
    assert((s.twoSum(a, 9) == vector<int>{0, 1}));
    vector<int> b = {3, 2, 4};
    assert((s.twoSum(b, 6) == vector<int>{1, 2}));
    vector<int> c = {3, 3};
    assert((s.twoSum(c, 6) == vector<int>{0, 1}));
    // brute force same results
    vector<int> d = {2, 7, 11, 15};
    assert((s.twoSum_brute(d, 9) == vector<int>{0, 1}));
    cout << "All tests passed." << endl;
    return 0;
}
