// LC 217: Contains Duplicate
// Return true if any value appears at least twice in the array.
// Time: O(n), Space: O(n)
#include <vector>
#include <unordered_set>
#include <cassert>
#include <iostream>
using namespace std;

class Solution {
public:
    // Brute: O(n^2) time | O(1) space
    bool containsDuplicate_brute(vector<int>& nums) {
        for (int i = 0; i < (int)nums.size(); i++)
            for (int j = i + 1; j < (int)nums.size(); j++)
                if (nums[i] == nums[j]) return true;
        return false;
    }

    // Optimal: O(n) time | O(n) space
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int n : nums) {
            if (seen.count(n)) return true;
            seen.insert(n);
        }
        return false;
    }
};

int main() {
    Solution s;
    vector<int> a = {1, 2, 3, 1};
    assert(s.containsDuplicate(a) == true);
    vector<int> b = {1, 2, 3, 4};
    assert(s.containsDuplicate(b) == false);
    vector<int> c = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
    assert(s.containsDuplicate(c) == true);
    vector<int> d = {1};
    assert(s.containsDuplicate(d) == false);
    cout << "All tests passed." << endl;
    return 0;
}
