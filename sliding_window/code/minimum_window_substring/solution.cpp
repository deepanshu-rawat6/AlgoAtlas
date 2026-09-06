#include <cassert>
#include <climits>
#include <string>
#include <unordered_map>

class Solution {
public:
    std::string minWindow(std::string s, std::string t) {
        if (t.empty()) return "";
        std::unordered_map<char,int> need, have;
        for (char c : t) need[c]++;
        int formed = 0, required = (int)need.size();
        int left = 0, bestLen = INT_MAX, bestL = 0;
        for (int right = 0; right < (int)s.size(); right++) {
            char ch = s[right];
            have[ch]++;
            if (need.count(ch) && have[ch] == need[ch]) formed++;
            while (formed == required) {
                if (right - left + 1 < bestLen) { bestLen = right - left + 1; bestL = left; }
                char lch = s[left];
                have[lch]--;
                if (need.count(lch) && have[lch] < need[lch]) formed--;
                left++;
            }
        }
        return bestLen == INT_MAX ? "" : s.substr(bestL, bestLen);
    }
};

int main() {
    Solution sol;
    assert(sol.minWindow("ADOBECODEBANC", "ABC") == "BANC");
    assert(sol.minWindow("a", "a") == "a");
    assert(sol.minWindow("a", "aa") == "");
    return 0;
}
