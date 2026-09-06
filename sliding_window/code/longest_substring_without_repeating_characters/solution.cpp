#include <cassert>
#include <algorithm>
#include <string>
#include <unordered_map>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        std::unordered_map<char,int> charIdx;
        int left = 0, best = 0;
        for (int right = 0; right < (int)s.size(); right++) {
            char ch = s[right];
            if (charIdx.count(ch) && charIdx[ch] >= left) left = charIdx[ch] + 1;
            charIdx[ch] = right;
            best = std::max(best, right - left + 1);
        }
        return best;
    }
};

int main() {
    Solution sol;
    assert(sol.lengthOfLongestSubstring("abcabcbb") == 3);
    assert(sol.lengthOfLongestSubstring("bbbbb") == 1);
    assert(sol.lengthOfLongestSubstring("pwwkew") == 3);
    return 0;
}
