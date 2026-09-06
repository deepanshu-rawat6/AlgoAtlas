#include <cassert>
#include <string>
#include <vector>

class Solution {
public:
    bool checkInclusion(std::string s1, std::string s2) {
        if (s1.size() > s2.size()) return false;
        std::vector<int> need(26, 0), have(26, 0);
        for (char c : s1) need[c - 'a']++;
        int m = s1.size();
        for (int i = 0; i < (int)s2.size(); i++) {
            have[s2[i] - 'a']++;
            if (i >= m) have[s2[i - m] - 'a']--;
            if (have == need) return true;
        }
        return false;
    }
};

int main() {
    Solution sol;
    assert(sol.checkInclusion("ab", "eidbaooo") == true);
    assert(sol.checkInclusion("ab", "eidboaoo") == false);
    assert(sol.checkInclusion("a", "a") == true);
    return 0;
}
