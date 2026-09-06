#include <cassert>
#include <vector>

class Solution {
public:
    std::vector<int> findClosestElements(std::vector<int>& arr, int k, int x) {
        int lo = 0, hi = (int)arr.size() - k;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (x - arr[mid] > arr[mid + k] - x) lo = mid + 1;
            else hi = mid;
        }
        return std::vector<int>(arr.begin() + lo, arr.begin() + lo + k);
    }
};

int main() {
    Solution sol;
    std::vector<int> a = {1,2,3,4,5};
    assert((sol.findClosestElements(a, 4, 3) == std::vector<int>{1,2,3,4}));
    assert((sol.findClosestElements(a, 4, -1) == std::vector<int>{1,2,3,4}));
    assert((sol.findClosestElements(a, 4, 10) == std::vector<int>{2,3,4,5}));
    return 0;
}
