// LC 704: Binary Search
// Classic binary search on a sorted array; return index or -1.
// Time: O(log n), Space: O(1)
#include <vector>
#include <cassert>
#include <iostream>
using namespace std;

class Solution {
public:
    // Brute: O(n) linear scan
    int search_brute(vector<int>& nums, int target) {
        for (int i = 0; i < (int)nums.size(); i++)
            if (nums[i] == target) return i;
        return -1;
    }

    // Optimal: O(log n) binary search
    int search(vector<int>& nums, int target) {
        int lo = 0, hi = (int)nums.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }
};

int main() {
    Solution s;
    vector<int> a = {-1, 0, 3, 5, 9, 12};
    assert(s.search(a, 9) == 4);
    assert(s.search(a, 2) == -1);
    vector<int> b = {5};
    assert(s.search(b, 5) == 0);
    assert(s.search(b, -5) == -1);
    vector<int> c = {1, 3, 5, 7, 9, 11};
    assert(s.search(c, 1) == 0);
    assert(s.search(c, 11) == 5);
    cout << "All tests passed." << endl;
    return 0;
}
